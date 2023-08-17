$(document).ready(function () {
  $("#search-form").on("submit", function (event) {
    var queryValue =
      $("input[name='query']").val() === undefined
        ? ""
        : (queryValue = queryValue.trim());

    if (queryValue === "") {
      event.preventDefault();
      alert("Search query cannot be empty.");
    }
  });
  $("input[name='query']").on("input", function () {
    var inputValue = $(this).val().trim();
    if (inputValue.length === 0) {
      $(this).val("");
    }
  });
});

var queryValue = $("input[name='query']").val().trim();

if (queryValue === "") {
  event.preventDefault();
  alert("Search query cannot be empty.");
}
