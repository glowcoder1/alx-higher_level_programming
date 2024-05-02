$('#toggle_header').click((e) => {
  e.preventDefault();
  const header = $('header');
  header.toggleClass('red green');
});
