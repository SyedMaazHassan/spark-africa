$(function () {
  "use strict";

  // :: 1.0 Preloader Active Code
  $(window).on("load", function () {
    $(".preloader").fadeOut("slow", function () {
      $(this).remove();
    });
  });

  $(window).on("load", function () {
    $(".btn-forget").on("click", function (e) {
      e.preventDefault();
      $(".form-items", ".form-content").addClass("hide-it");
      $(".form-sent", ".form-content").addClass("show-it");
    });
    $(".btn-tab-next").on("click", function (e) {
      e.preventDefault();
      $(".nav-tabs .nav-item > .active")
        .parent()
        .next("li")
        .find("a")
        .trigger("click");
    });
  });
});
