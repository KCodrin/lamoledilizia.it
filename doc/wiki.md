# wiki.md — Decisioni

## 1. Sito statico generato da uno script Python (scelta 2026-11-04)
**Cosa:** pagine HTML statiche prodotte da `src/build.py`, che contiene testi e modello.
**Perché:** il vecchio WordPress caricava ~2 MB di CSS/JS e plugin. Statico = veloce, sicuro, ospitabile ovunque; lo script evita di ripetere header e footer in 24 file.
**Alternative scartate:** WordPress (pesante, da aggiornare), framework JS come Next/Astro (dipendenze e build per un sito di 24 pagine).

## 2. Stessi indirizzi del vecchio sito (scelta 2026-11-04)
**Cosa:** ogni pagina mantiene il nome file del vecchio sito.
**Perché:** non si perdono posizionamento Google e link esistenti.
**Alternative scartate:** URL nuovi più corti (richiederebbero redirect 301).

## 3. Modulo contatti via email (scelta 2026-11-04, confermata)
**Cosa:** il modulo apre il programma di posta con il messaggio compilato.
**Perché:** senza server non c'è invio diretto; il vecchio WPForms dipendeva da WordPress.
**Alternative scartate:** servizio esterno di form come Formspree (scartato dal cliente il 2026-11-04).
