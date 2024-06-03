$(document).ready(function () {
  const amsCheck = {};
  $('.amenities INPUT').change(function () {
    const $input = $(this);
    if ($input.is(':checked')) {
      amsCheck[$input.data('id')] = $input.data('name');
    } else {
      delete amsCheck[$input.data('id')];
    }
    const str = Object.values(amsCheck);
    $('.amenities h4').text(str.join(', '));
  });
});

