$(document).ready(function () {
  const url = window.location.href;
  const searchForm = $("#search-form");
  const searchInput = $("input[name='query']");
  const resultBox = $("#results-box");
  const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  const sendSearchData = (course) => {
    $.ajax({
      type: "POST",
      url: "search_results/",
      data: {
        csrfmiddlewaretoken: csrf,
        course: course,
      },
      success: (res) => {
        const data = res.data;
        console.log(data);
        if (Array.isArray(data)) {
          console.log("We have an array");
        } else {
          console.log(data, searchInput[0]);
          //data is null
        }
      },
      error: (err) => {
        console.log(err);
      },
    });
  };
  searchInput.on("keyup", function (e) {
    if (resultBox[0].classList.contains("not-visible")) {
      resultBox[0].classList.remove("not-visible");
    }
    sendSearchData(e.target.value);
  });
  $("#search-form").on("submit", function (event) {
    var queryValue =
      $("input[name='query']").val() === undefined
        ? ""
        : $("input[name='query']").val().trim();

    if (queryValue === "") {
      event.preventDefault();
    }
  });
  $("input[name='query']").on("input", function () {
    var inputValue = $(this).val().trim();
    if (inputValue.length === 0) {
      $(this).val("");
    }
  });
});
