# Eksempel på bruk av PAD-API

## Generer kode via REST

```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Lag en python-funksjon som returnerer summen av to tall"}'
```

Respons:
```json
{
  "code": "# Språk: python\ndef hello():\n    print('Hei fra PAD!')",
  "feedback": "Koden er PEP8-kompatibel."
}
```
