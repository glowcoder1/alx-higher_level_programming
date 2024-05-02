$('#add_item').click((e) => {
  e.preventDefault();
  const list = $('.my_list');
  list.append('<li>Item</li>');
});
