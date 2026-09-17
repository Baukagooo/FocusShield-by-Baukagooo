# ==========================================
# FOCUS SHIELD — MAIN TRACKER & MONITOR
# ==========================================

import time
import os
import cv2
import ctypes
import config
from notifier import send_alert, send_stats_summary

def save_stats(duration_dict):
    """Saves final session statistics to a local text file."""
    filename = "focus_stats.txt"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n--- SESSION: {timestamp} ---\n")
        f.write(f"🎯 Present (In Focus): {int(duration_dict.get('PRESENT', 0))} sec\n")
        f.write(f"🏃 Absent (Away): {int(duration_dict.get('ABSENT', 0))} sec\n")
        f.write("="*35 + "\n")

def main():
    cascade_path = 'haarcascade_frontalface_default.xml'
    if not os.path.exists(cascade_path):
        print(f"❌ Error: Could not find '{cascade_path}' in the current directory.")
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Could not access the webcam.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)

    # Window locking settings (Windows API)
    window_name = getattr(config, 'WINDOW_NAME', 'FocusShield Monitor')
    
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, config.FRAME_WIDTH, config.FRAME_HEIGHT)

    cv2.waitKey(1)
    hwnd = ctypes.windll.user32.FindWindowW(None, window_name)
    if hwnd:
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
        style &= ~0x00010000  # Disable maximize button
        style &= ~0x00040000  # Disable window resizing
        ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)

    face_cascade = cv2.CascadeClassifier(cascade_path)

    stats_time = {
        "PRESENT": 0,
        "ABSENT": 0
    }

    state_start_time = time.time()
    last_frame_time = time.time()
    current_state = "PRESENT"
    alert_sent = False

    print("🛡️ FocusShield Monitor started! Press 'Q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        now = time.time()
        delta = now - last_frame_time
        last_frame_time = now

        stats_time[current_state] += delta

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(120, 120))

        if len(faces) > 0:
            detected_state = "PRESENT"
            (fx, fy, fw, fh) = faces[0]
            cv2.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (0, 255, 0), 2)
        else:
            detected_state = "ABSENT"

        if detected_state != current_state:
            current_state = detected_state
            state_start_time = time.time()
            alert_sent = False

        elapsed = time.time() - state_start_time

        timeout = getattr(config, 'TIMEOUT_ABSENT', 5)
        if current_state == "ABSENT" and elapsed >= timeout and not alert_sent:
            send_alert()
            alert_sent = True

        # Visual overlay
        color = (0, 255, 0) if current_state == "PRESENT" else (0, 0, 255)
        cv2.putText(frame, f"Status: {current_state} ({int(elapsed)}s)", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        focus_sec = int(stats_time["PRESENT"])
        cv2.putText(frame, f"Focus Time: {focus_sec}s", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Save stats locally
    save_stats(stats_time)
    print("📊 Statistics saved to 'focus_stats.txt'!")

    # Send summary via Telegram
    send_stats_summary(stats_time["PRESENT"], stats_time["ABSENT"])

if __name__ == "__main__":
    main()