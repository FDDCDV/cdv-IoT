
# 🌱 SmartAgricultiral IoT – System monitorowania roślin

**SmartAgricultiral** to system IoT, który monitoruje wilgotność gleby i poziom światła, wysyła powiadomienia, oraz automatycznie włącza lampę LED dla roślin w warunkach słabego oświetlenia.

---

## 📦 Zawartość projektu

- **Symulator urządzenia IoT** – wysyła dane wilgotności i światła do Azure IoT Hub
- **Azure Blob Storage** – przechowuje dane pomiarowe w formacie JSON
- **Backend (FastAPI)** – udostępnia REST API, wykonuje logikę biznesową i steruje LED
- **Diagram C4 (PNG)** – architektura systemu
- **Kolekcja Postman** – do testowania REST API
- **Azure Pricing Calculator** – oszacowanie kosztów rozwiązania

---

## 🚀 Szybki start

### 🔧 Wymagania

- Python 3.10+
- Azure konto (IoT Hub, Storage Account)
- `pip install -r requirements.txt`

### ⚙️ Uruchom backend

```bash
uvicorn main:app --reload
```

### 🤖 Uruchom symulator

```bash
python plantguardian_simulator.py
```

---

## 🧪 REST API – Endpointy

| Endpoint         | Metoda | Opis                                     |
|------------------|--------|------------------------------------------|
| `/`              | GET    | Sprawdzenie działania API                |
| `/sensor/latest` | GET    | Zwraca ostatnie dane z Blob Storage      |
| `/device/led`    | POST   | Wysyła komendę LED ON/OFF do urządzenia  |

**Przykład body dla /device/led:**
```json
{ "status": "ON" }
```

---

## 📖 User Stories

- Jako użytkownik chcę otrzymać powiadomienie, gdy gleba jest zbyt sucha
- Jako użytkownik chcę, aby lampa LED włączała się, gdy poziom światła jest niski
- Jako użytkownik chcę przeglądać ostatnie dane z sensora

---

## ☁️ Konfiguracja Azure

- **IoT Hub**: do komunikacji z urządzeniem
- **Storage Account + Blob**: do przechowywania danych
- **Device (symulator)**: zarejestrowany w IoT Hub
- **Routing (opcjonalnie)**: z IoT Hub do Blob

---

## 💰 Koszty

Sprawdź kalkulację w pliku `azure-costs.xlsx` wygenerowanym w Azure Pricing Calculator:
- IoT Hub (S1)
- Storage Account
- App Service lub Container App (backend)

---

## 📂 Struktura katalogów

```
plantguardian/
├── main.py
├── led_control.py
├── blob_utils.py
├── plantguardian_simulator.py
├── requirements.txt
├── README.md
├── diagram/ (C4)
├── postman/ (kolekcja API)
└── azure-costs.xlsx
```

---

## 📬 Autorzy

Projekt edukacyjny – inżynieria IoT i chmura Azure.
