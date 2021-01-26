$(window).on('beforeunload', function() {
  $.cookie("input", $("#input-text").val());
  console.log($.cookie("input"));
});
