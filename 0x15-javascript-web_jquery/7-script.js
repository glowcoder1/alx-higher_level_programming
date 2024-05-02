fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then((resp) => {
    return resp.json();
  })
  .then((val) => $('#character').text(val.name));
