window.addEventListener('DOMContentLoaded', function(){
  $('INPUT#btn_translate').click(function () {
    let lang = $('INPUT#language_code').val()
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (x) {
      $('DIV#hello').text(x.hello);
    });
  });
});
