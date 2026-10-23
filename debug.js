
const cols = document.querySelectorAll('.column');
const result = [];
cols.forEach((col, i) => {
  const cards = col.querySelectorAll('.poster-card');
  const cardData = [];
  cards.forEach(c => {
    const cs = window.getComputedStyle(c);
    cardData.push({ title: c.querySelector('.card-title')?.innerText, height: c.offsetHeight, flexGrow: cs.flexGrow, flexBasis: cs.flexBasis });
  });
  result.push({ colIndex: i, colHeight: col.offsetHeight, cards: cardData });
});
console.log(JSON.stringify(result, null, 2));
