# La Mole Edilizia su Fune — sito web

Sito di [lamoledilizia.it](https://www.lamoledilizia.it): edilizia su fune a Torino e in tutta Italia, interventi su tetti e facciate senza ponteggi.

Sito statico (HTML + CSS + poco JavaScript), senza framework né dipendenze.

## Struttura

```
*.html          pagine del sito (generate, non modificarle a mano)
sitemap.xml     generata
src/build.py    testi e modello delle pagine: si modifica qui
assets/         css, js, immagini, font
doc/            documentazione del progetto (regole, design, changelog)
vercel.json     configurazione per Vercel
```

## Modificare il sito

1. Cambia testi, menu o footer in `src/build.py` (stile in `assets/css/style.css`).
2. Rigenera le pagine:
   ```bash
   python3 src/build.py
   ```
   Lo script stampa `OK` e controlla che non ci siano link rotti.
3. Guarda il risultato in locale:
   ```bash
   python3 -m http.server 8123
   ```
   e apri http://localhost:8123
4. Registra la modifica in `doc/changelog.md`.

Serve solo Python 3, nessuna installazione.

## Pubblicazione

Il sito è pubblicato su Vercel: ogni push sul ramo `main` avvia un nuovo deploy. Le cartelle `src/` e `doc/` non vengono pubblicate (`.vercelignore`).

## Documentazione

Prima di lavorare sul progetto leggi [`doc/agent.md`](doc/agent.md). Colori, font e componenti sono in [`doc/design.md`](doc/design.md); lo storico delle modifiche in [`doc/changelog.md`](doc/changelog.md).

## Contatti

LA MOLE EDILIZIA SU FUNE SRL · P.IVA 12716000018
Via Camillo Cenni 17, 10095 Grugliasco (TO) · 011 428 7322 · fune@lamoledilizia.com

Testi e immagini sono di proprietà di La Mole Edilizia su Fune SRL. Tutti i diritti riservati.
