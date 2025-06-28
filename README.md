
# 🌱 SmartAgricultiral IoT – Monitoring Roślin

**SmartAgricultiral** to system IoT do automatycznego monitorowania wilgotności gleby i oświetlenia, który:
- Wysyła dane z urządzenia IoT (lub symulatora) do chmury Azure
- Włącza lampę LED, gdy poziom światła jest niski
- Informuje użytkownika, gdy gleba wymaga podlania

---

## 🔧 Technologia

- Python 3
- FastAPI (backend)
- Azure IoT Hub (komunikacja z urządzeniem)
- Azure Blob Storage (przechowywanie danych)
- Azure Device Simulator lub własny symulator
- Postman (testowanie API)

---

## 🚀 Jak uruchomić projekt lokalnie

### ✅ 1. Klonowanie repozytorium
```bash
git clone https://github.com/FDDCDV/cdv-SmartAgricultiral
cd SmartAgricultiral_project
```

### ✅ 2. Instalacja zależności
```bash
pip install -r requirements.txt
```

### ✅ 3. Uruchomienie symulatora (urządzenie IoT)
```bash
python SmartAgricultiral_simulator.py
```

Symulator co 15 sekund wysyła dane `soilMoisture`, `lightLevel` i odbiera komendy LED ON/OFF.

### ✅ 4. Uruchomienie backendu (FastAPI)
```bash
py -m uvicorn main:app --reload 
```

Backend dostępny pod adresem:  
[http://localhost:8000](http://localhost:8000)

---

## 📬 Endpointy REST API

| Endpoint              | Metoda | Opis                                   |
|-----------------------|--------|----------------------------------------|
| `/`                   | GET    | Test działania backendu                |
| `/sensor/latest`      | GET    | Zwraca najnowsze dane z Blob Storage   |
| `/device/led`         | POST   | Wysyła komendę do urządzenia IoT       |

#### 🔸 Przykład `POST /device/led`:
```json
{
  "status": "ON"
}
```

---

## 👤 User Stories

- Jako właściciel rośliny chcę być powiadamiany, gdy gleba jest sucha
- Jako system chcę automatycznie włączać lampę LED, gdy jest ciemno
- Jako użytkownik chcę sprawdzić ostatni odczyt z czujników przez aplikację

---

## 📂 Struktura projektu

```
SmartAgricultiral/
├── backend/
│   ├── main.py
│   ├── auto_control.py
│   ├── blob_utils.py
│   ├── led_control.py
│   ├── notifications.py
│   ├── alerts_email.py
│   ├── sendgrid_notify.py
│   └── __init__.py
├── SmartAgricultiral_simulator.py
├── SmartAgricultiral_API_Final.postman_collection.json
├── README.md
├── Diagram C4 - Poziom 1.pdf
├── Diagram C4 - Poziom 2.pdf
├── Diagram C4 - Poziom 3.pdf
├── Diagram C4 Poziom 4.pdf
└── requirements.txt
```

---

## 💰 Koszty (szacowane)

Koszty: [Azure Pricing Calculator](https://azure.com/e/fbf035af787b457a82e6901defafdf98)

---

## 📦 Testowanie API

Użyj pliku kolekcji Postman:  
`SmartAgricultiral_API.postman_collection.json`  
Importuj do Postmana i testuj lokalnie.

---

## 📸 Diagram architektury (C4)

[Diagram C4 Poziom 1](https://github.com/FDDCDV/cdv-SmartAgricultiral/blob/main/Diagram%20C4%20-%20Poziom%201.pdf)<br>
[Diagram C4 Poziom 2](https://github.com/FDDCDV/cdv-SmartAgricultiral/blob/main/Diagram%20C4%20-%20Poziom%202.pdf)<br>
[Diagram C4 Poziom 3](https://github.com/FDDCDV/cdv-SmartAgricultiral/blob/main/Diagram%20C4%20-%20Poziom%203.pdf)<br>
[Diagram C4 Poziom 4](https://github.com/FDDCDV/cdv-SmartAgricultiral/blob/main/Diagram%20C4%20Poziom%204.pdf)<br>

---

## ✅ Status

- [x] Urządzenie IoT / symulator
- [x] Backend z API
- [x] Przechowywanie danych w chmurze
- [x] Diagram architektury
- [x] Kolekcja Postman
- [x] Kalkulator kosztów (do wypełnienia)

---

## 📧 Kontakt

Projekt stworzony w ramach zaliczenia – 2025.
Wykonany przez : Bartosz Filipiak oraz Filip Dzięcioł
