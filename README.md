
---

```markdown
# 🛡️ FocusShield Monitor

**FocusShield** — это лёгкий локальный инструмент на Python для отслеживания фокуса и дисциплины с помощью компьютерного зрения. Приложение определяет присутствие пользователя перед экраном в реальном времени, отправляет мотивирующие уведомления в Telegram при отлучках и формирует итоговый отчёт эффективности по завершении работы.

Проект является фундаментальным модулем-прототипом для системы **ATLAS (Adaptive Technology & Logic Assistant System)**.

---

## 🚀 Возможности

* 🎥 **Детекция присутствия:** Быстрый поиск лица с помощью алгоритмов OpenCV (Haar Cascade).
* ⚡ **Минимальная нагрузка:** Простая бинарная логика состояний (`PRESENT` / `ABSENT`) без тяжёлых нейросетей.
* 📲 **Уведомления в Telegram:** Пул из 20 случайных англоязычных цитат о дисциплине и фокусе без повторов подряд.
* 📊 **Итоговая статистика:** Автоматический расчёт процента эффективности (`Focus Efficiency`) и отправка сводки в Telegram при выходе.
* 🔒 **Локальные логи:** Сохранение истории всех сессий в `focus_stats.txt`.
* 🪟 **Фиксация окна:** Закрепление размера окна монитора (Windows API).

---

## 🛠️ Установка и запуск

### 1. Клонирование репозитория
```bash
git clone [https://github.com/YOUR_USERNAME/FocusShield.git](https://github.com/YOUR_USERNAME/FocusShield.git)
cd FocusShield

```

### 2. Настройка виртуального окружения

```bash
python -m venv .venv
# Для Windows:
.venv\Scripts\activate
# Для Linux/macOS:
source .venv/bin/activate

```

### 3. Установка зависимостей

```bash
pip install opencv-python requests

```

### 4. Конфигурация Telegram

1. Переименуйте `config.example.py` в `config.py`.
2. Получите токен бота у [@BotFather](https://t.me/BotFather) и укажите его в `TELEGRAM_TOKEN`.
3. Узнайте ваш Chat ID с помощью [@userinfobot](https://t.me/userinfobot) и укажите его в `CHAT_ID`.

### 5. Запуск

```bash
python main.py

```

*Для завершения работы и отправки статистики нажмите **`Q`**.*

---

---

# 🛡️ FocusShield Monitor (English Version)

**FocusShield** is a lightweight, local computer-vision tool built with Python to maintain personal focus and productivity. It tracks the user's presence in real-time, sends strict motivational alerts via Telegram upon prolonged absences, and delivers a full session efficiency report upon exiting.

This project serves as a foundational prototype module for **ATLAS (Adaptive Technology & Logic Assistant System)**.

---

## 🚀 Features

* 🎥 **Real-Time Detection:** Fast and precise face detection powered by OpenCV Haar Cascades.
* ⚡ **Performance-Optimized:** Simplified binary state detection (`PRESENT` / `ABSENT`) ensuring zero CPU overhead.
* 📲 **Telegram Discipline Alerts:** A pool of 20 hard-hitting stoic/discipline quotes with a anti-repetition mechanism.
* 📊 **Session Summaries:** Automatic focus efficiency percentage calculation (`Focus Efficiency`) sent straight to Telegram upon exit.
* 🔒 **Local Logging:** Persistent session statistics appended to `focus_stats.txt`.
* 🪟 **Fixed UI Constraint:** Enforced monitor window dimensions using Windows API integration.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/FocusShield.git
cd FocusShield

```

### 2. Configure Virtual Environment

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install opencv-python requests

```

### 4. Telegram Configuration

1. Rename `config.example.py` to `config.py`.
2. Create a bot via [@BotFather](https://t.me/BotFather) and paste the API token into `TELEGRAM_TOKEN`.
3. Retrieve your personal ID using [@userinfobot](https://t.me/userinfobot) and set it in `CHAT_ID`.

### 5. Run FocusShield

```bash
python main.py

```

*Press **`Q`** inside the display window to end the session and generate your summary report.*