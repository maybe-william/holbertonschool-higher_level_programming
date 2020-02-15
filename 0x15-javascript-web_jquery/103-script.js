window.addEventListener('DOMContentLoaded', function () {
  function doThing () {
    const lang = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (x) {
      $('DIV#hello').text(x.hello);
    });
  }
  $('INPUT#btn_translate').click(doThing);
  $('INPUT#language_code').keyup(function (e) {
    if (e.keyCode === 13) {
      doThing();
    }
  });
});
