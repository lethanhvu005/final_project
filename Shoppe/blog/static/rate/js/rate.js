if (screen.width <= 736) {
  document
    .getElementById("viewport")
    .setAttribute(
      "content",
      "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no",
    );
}
console.log("RATE JS LOADED");
$(document).ready(function () {
  $(".ratings_stars").hover(
    function () {
      $(this).prevAll().andSelf().addClass("ratings_hover");
    },
    function () {
      $(this).prevAll().andSelf().removeClass("ratings_hover");
    },
  );
  $(".ratings_stars").click(function () {
    var value = $(this).find("input").val();
    alert(value);
    if ($(this).hasClass("ratings_over")) {
      $(".ratings_stars").removeClass("ratings_over");
      $(this).prevAll().andSelf().addClass("ratings_over");
    } else {
      $(this).prevAll().andSelf().addClass("ratings_over");
    }
  });
});
