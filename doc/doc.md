# doc.md — Stato attuale del progetto

> Ultimo aggiornamento: 2026-11-04

## Obiettivo
Rifare il sito di La Mole Edilizia su Fune (Grugliasco, TO): far capire subito i servizi di edilizia su fune senza ponteggi e portare richieste di preventivo da condomini, aziende e privati.

## Stack
| Livello | Scelta | Note |
|---|---|---|
| Markup | HTML statico | generato da `src/build.py` |
| Stile | CSS unico | `assets/css/style.css` |
| Script | JS minimo | `assets/js/main.js`: menu mobile + modulo contatti |
| Font | Montserrat locale | `assets/fonts/` |

## Struttura delle cartelle
```
SITO NUOVO/
  *.html          pagine generate (stessi nomi del vecchio sito)
  sitemap.xml     generata
  src/build.py    testi + modello delle pagine: si modifica qui
  assets/css|js|img|fonts
  doc/            documentazione
```

## Come si lavora
- Rigenerare le pagine: `python3 src/build.py`
- Vedere in locale: `python3 -m http.server 8123 -d "SITO NUOVO"` e aprire http://localhost:8123
- Pubblicazione: da confermare (hosting attuale del vecchio sito WordPress?). Basta caricare la cartella, senza `src/` e `doc/`.
