function onSectionClick(section) {
  window.location.href = '/subsection?section=' + section;
  console.info('section clicked is', section);
}

function onSubSectionClick(section, subsection) {
  window.location.href =
    '/content?subsection=' + subsection + '&section=' + section;
  console.info('section clicked is', section);
}
