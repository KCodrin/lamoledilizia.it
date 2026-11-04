# design.md — Design system

## Colori
| Token | Valore | Uso |
|---|---|---|
| `--ink` | #282e69 | colore primario: header, hero, CTA, testo |
| `--ink-2` | #343b80 | fascia numeri in home |
| `--gold` | #d39f6f | colore secondario: bottoni, accenti su fondo scuro |
| `--gold-dark` | #9a6a3e | accenti e link su fondo chiaro (contrasto leggibile) |
| `--paper` / `--paper-2` | #ffffff / #f5f3f0 | sfondi sezioni alternate |
| `--muted` | #5a5f73 | testi secondari |
| `--line` | #e4e0da | bordi |

## Tipografia, spazi, raggi
Montserrat (variabile, locale). Titoli 700-800, testo 400 a 17px. Raggio `--radius` 20px (come l'header) per riquadri, foto, card e campi; `--radius-sm` 12px per icone piccole dentro i riquadri; bottoni sempre a pillola (999px). Non usare altri valori. Spazio sezioni `--section` (56-104px). Larghezza massima `--wrap` 1180px.

## Componenti (tutti in `src/build.py` + `style.css`)
- `hero()`: testata con foto di sfondo, occhiello, titolo, frase.
- `tiles()`: griglia di riquadri con foto che portano ai servizi.
- `.card`: riquadro con bordo oro per i punti "Perché sceglierci".
- `cta()`: fascia scura "Hai bisogno di interventi in quota…" in fondo a ogni pagina.
- `crumbs()`: percorso (Home / Servizi / …).
- `.btn`, `.btn-ghost`, `.link`: bottoni e link.
- Su tutte le pagine: `.topbar` (barra in alto) e `.site-header.pill` (header a pillola). Solo in home: `.hero-home` (testata a tutto schermo), `.btn-pill` (bottone arrotondato), `.badge`.
