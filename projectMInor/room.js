$(".input_text").focus(function () {
  $(this).prev(".fa").addclass("glowIcon");
});
$(".input_text").focusout(function () {
  $(this).prev(".fa").removeclass("glowIcon");
});
function replaceContent() {
  document.getElementById("login_form").innerHTML =
    "<h1>Thanks for Booking We wish you amazing Experience and hospitality in our hotel. Keep coming to our amazing hotel Diamond 5STAR</h1>";
}
