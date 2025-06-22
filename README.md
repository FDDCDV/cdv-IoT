
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
git clone <repo-url>
cd plantguardian_project
```

### ✅ 2. Instalacja zależności
```bash
pip install -r requirements.txt
```

### ✅ 3. Uruchomienie symulatora (urządzenie IoT)
```bash
python plantguardian_simulator.py
```

Symulator co 5 sekund wysyła dane `soilMoisture`, `lightLevel` i odbiera komendy LED ON/OFF.

### ✅ 4. Uruchomienie backendu (FastAPI)
```bash
uvicorn main:app --reload
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
cdv-IoT/
├── main.py                 # Backend FastAPI
├── plantguardian_simulator.py  # Symulator urządzenia
├── led_control.py          # Komendy do IoT Hub
├── blob_utils.py           # Dostęp do Blob Storage
├── requirements.txt
├── README.md
```

---

## 💰 Koszty (szacowane)

- Azure IoT Hub (S1): ~0.04 zł/dzień (mały ruch)
- Azure Blob Storage (LRS): ~0.01 zł/GB
- App Service: ~15–30 zł/miesiąc (opcjonalnie)

Więcej: [Azure Pricing Calculator](https://azure.com/pricing/calculator)

---

## 📦 Testowanie API

Użyj pliku kolekcji Postman:  
`PlantGuardian_API.postman_collection.json`  
Importuj do Postmana i testuj lokalnie.

---

## 📸 Diagram architektury (C4)

![Diagram C4](./diagram/c4_level_2.png)

---

## ✅ Status

- [x] Urządzenie IoT / symulator
- [x] Backend z API
- [x] Przechowywanie danych w chmurze
- [x] Diagram architektury
- [x] Kolekcja Postman
- [ ] Kalkulator kosztów (do wypełnienia)

---

## 📧 Kontakt

Projekt stworzony w ramach zaliczenia – 2025.
