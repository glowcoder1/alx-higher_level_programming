fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then((resp) => {
    return resp.json();
  })
  .then((val) => {
    val.results.forEach(data => {
      $('#list_movies').append(`<li>${data.title}</li>`);
    });
  });
