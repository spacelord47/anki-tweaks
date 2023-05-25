/**
  * Script with logic related to cloze notes.
  */

window.anki_tweaks.showCloze = ({ isShowAll } = {}) => {
  let clozes = document.querySelectorAll(`.cloze[data-cloze][data-ordinal="1"]:not(.cloze_revealed)`);

  if (clozes.length === 0) {
    pycmd("anki_tweaks:cloze:no_more_hidden");
    return;
  }

  if (isShowAll !== true) {
    clozes = [clozes[0]];
  }

  clozes.forEach(cloze => {
    const answer = cloze.dataset.cloze;

    cloze.textContent = answer;
    cloze.classList.add("cloze_revealed");
  });
};

window.anki_tweaks.handleClozeKeyDown = (event) => {
  switch (event.key) {
    case window.anki_tweaks.next_shortcut:
      window.anki_tweaks.showCloze();
      break;
    case window.anki_tweaks.all_shortcut:
      window.anki_tweaks.showCloze({ isShowAll: true });
      break;
    default:
  }
};

document.removeEventListener("keydown", window.anki_tweaks.handleClozeKeyDown);
document.addEventListener("keydown", window.anki_tweaks.handleClozeKeyDown);
