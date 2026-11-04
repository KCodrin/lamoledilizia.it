# Changelog

## 2026-11-04 · Barra in alto e header a pillola su tutte le pagine
**Cosa:** la barra blu in alto e l'header bianco a pillola, prima solo in home, ora sono su tutte le pagine. Tolto il vecchio header blu.
**Perché / Dettagli:** richiesto dal cliente. Funzione `header()` in `src/build.py`.
**Verifica:** pagine rigenerate, controllo a schermo su una pagina servizio (desktop e mobile).

## 2026-11-04 · Home: barra in alto, header a pillola, hero a tutto schermo
**Cosa:** solo in home, aggiunta una barra blu arrotondata in alto (senza ponteggi · Torino e tutta Italia · telefono), un header bianco a pillola che resta fisso scorrendo, con logo blu e bottone "Richiedi un preventivo", e una testata a tutto schermo con angoli arrotondati, badge, titolo grande e tre punti di forza. Tolta la fascia dei numeri sotto la testata, perché i punti ora sono dentro la testata. Le altre pagine non cambiano.
**Perché / Dettagli:** richiesto dal cliente su un riferimento grafico. Codice in `src/build.py` (header, home) e in fondo a `assets/css/style.css`. Il logo blu si ottiene colorando con il CSS il logo bianco esistente.
**Verifica:** controllo a schermo su desktop e mobile (375px), nessuno scorrimento orizzontale.

## 2026-11-04 · Colori del marchio
**Cosa:** il colore primario diventa il blu #282e69 (prima antracite #171a1a); il secondario resta l'oro #d39f6f. Adeguati di conseguenza fascia numeri, footer, velature sulle foto e grigio dei testi secondari.
**Perché / Dettagli:** colori indicati dal cliente; token in `assets/css/style.css`, aggiornati `design.md` e `agent.md`.
**Verifica:** controllo a schermo.

## 2026-11-04 · Meta Pixel
**Cosa:** aggiunto il codice Meta Pixel (3593393790961940) in tutte le pagine; aggiornata la pagina privacy.
**Perché / Dettagli:** richiesto dal cliente; inserito in `src/build.py` (funzione `head`).
**Verifica:** rigenerate le pagine, codice presente in tutte e identico all'originale.

## 2026-11-04 · Verifica dominio Facebook
**Cosa:** aggiunto il codice di verifica del dominio di Facebook in tutte le pagine.
**Perché / Dettagli:** richiesto dal cliente; inserito in `src/build.py` (funzione `head`).
**Verifica:** rigenerate le pagine, codice presente in tutte.

## 2026-11-04 · Google Analytics
**Cosa:** aggiunto il codice di Google Analytics (G-29DS1SS66B) in tutte le pagine. Aggiornata la frase della pagina privacy che diceva "nessun tracciamento".
**Perché / Dettagli:** richiesto dal cliente; inserito una volta sola in `src/build.py` (funzione `head`).
**Verifica:** rigenerate le pagine, codice presente in tutte.

## 2026-11-04 · Modulo contatti: resta via email
**Cosa:** deciso con il cliente che il modulo contatti continua ad aprire il programma di posta, senza servizi esterni. Aggiornati wiki, informazioni cliente e roadmap.
**Verifica:** nessuna modifica al sito, solo documentazione.

## 2026-11-04 · Nuovo sito
**Cosa:** rifatto il sito di La Mole Edilizia su Fune da zero, con nuova grafica, riportando tutti i testi, le immagini e i contatti del vecchio sito WordPress. Ogni pagina tiene lo stesso indirizzo di prima.
**Perché / Dettagli:** pagine generate da `src/build.py`; stile in `assets/css/style.css`; immagini ridimensionate in `assets/img/`. Aggiunte: briciole di percorso, link "altri servizi", tabella di confronto leggibile su telefono, bottone WhatsApp, sitemap. Corretti piccoli refusi dei testi (es. "al'edilizia", "piattaforme aree", "incompleta sospensione"). Pagina privacy segnaposto in attesa del testo legale.
**Verifica:** lo script controlla che nessun link sia rotto (OK, 24 pagine); controllo a schermo su desktop e mobile (375px), menu mobile funzionante, nessuno scorrimento orizzontale.
