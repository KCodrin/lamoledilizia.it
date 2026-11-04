// Menu mobile
const btn = document.querySelector(".menu-btn");
const nav = document.getElementById("nav");
btn?.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  btn.setAttribute("aria-expanded", open);
});

// Modulo contatti: apre il programma di posta con i dati compilati.
// shortcut: nessun server, quindi niente invio diretto; quando c'è un hosting con backend (o Formspree/Netlify Forms) sostituire con un POST.
const form = document.getElementById("contact-form");
form?.addEventListener("submit", (e) => {
  e.preventDefault();
  const d = Object.fromEntries(new FormData(form));
  const body = `Nome: ${d.nome} ${d.cognome}\nCellulare: ${d.cellulare}\nEmail: ${d.email}\nServizio: ${d.servizio}\n\n${d.messaggio}`;
  location.href = `mailto:${form.dataset.email}?subject=${encodeURIComponent("Richiesta informazioni - " + d.servizio)}&body=${encodeURIComponent(body)}`;
});
