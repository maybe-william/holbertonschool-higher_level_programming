$('HEADER').addClass('green');
$('DIV#toggle_header').click(function () {
  let x = $('HEADER');
  let y = 'red';
  let z = 'green';
  if (x.hasClass('green')) {
    let a = y;
    y = z;
    z = a;
  }
  x.removeClass(y);
  x.addClass(z);
});
