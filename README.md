18:18






# CampusHub AI Service

FastAPI ile hazırlanmış deneme sınıflandırma servisi.

## Kurulum — Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Kurulum — macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Çalıştırma — Windows (PowerShell)

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8005
```

## Çalıştırma — macOS/Linux

Sanal ortam aktifken:

```bash
python -m uvicorn app.main:app --reload --port 8005
```

Swagger: http://127.0.0.1:8005/docs

## API

POST /ai/classify

İstek:
```json
{"text": "Python atölyesi"}
```

Yanıt:
```json
{"category": "TECHNOLOGY", "confidence": 0.91}
```

FakeClassifier her geçerli isteğe sabit deneme sonucu döndürür.
Bu sonuç gerçek model tahmini değildir.

Geçersiz isteklerde HTTP 400 ve error/message alanları döner.

## Testler — Windows (PowerShell)

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Testler — macOS/Linux

Sanal ortam aktifken:

```bash
python -m pytest -q
```

## Durum

Gerçek model bağlantısı ve K3'ün hazırlayacağı /health router'ının
uygulamaya bağlanması henüz tamamlanmamıştır.
