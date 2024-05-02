$('#update_header').click((e) => {
  e.preventDefault();
  const header = $('header');
  header.text('New Header!!!');
});
