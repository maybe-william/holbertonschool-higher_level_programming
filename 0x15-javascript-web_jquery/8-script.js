$.get('https://swapi.co/api/films/?format=json', function (x) {
  for (film of x.results) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  }
});
