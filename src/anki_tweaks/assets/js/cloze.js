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
  const nextBindingCode = `Key${window.anki_tweaks.next_shortcut.toUpperCase()}`;
  const allBindingCode = `Key${window.anki_tweaks.all_shortcut.toUpperCase()}`;

  const isMatchingNextShortcut = event.code === nextCode
  && ((event.shiftKey === false && window.anki_tweaks.next_shortcut.match(/[a-z]/)) || (event.shiftKey === true && window.anki_tweaks.next_shortcut.match(/[A-Z]/)))
  const isMatchingAllShortcut = event.code === allBindingCode
  && ((event.shiftKey === false && window.anki_tweaks.all_shortcut.match(/[a-z]/)) || (event.shiftKey === true && window.anki_tweaks.all_shortcut.match(/[A-Z]/)))
  console.log(event.code, event.shiftKey)

  if (isMatchingNextShortcut) {
    window.anki_tweaks.showCloze();
  } else if (isMatchingAllShortcut) {
    window.anki_tweaks.showCloze({ isShowAll: true });
  }
};

document.removeEventListener("keydown", window.anki_tweaks.handleClozeKeyDown);
document.addEventListener("keydown", window.anki_tweaks.handleClozeKeyDown);
