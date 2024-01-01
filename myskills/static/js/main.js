$(document).ready(function () {
  const url = window.location.href;
  const searchForm = $("#search-form");
  const searchInput = $("input[name='query']");
  const resultBox = $("#results-box");
  const csrf = $("input[name='csrfmiddlewaretoken']").val();
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
        var datalistElement = $("#browsers");
        console.log("Received data:", data[0]);
        datalistElement.empty();
        if (Array.isArray(data) && data.length > 0) {
          const datalist = $.map(data, function (item) {
            return item.name;
          });

          $.each(datalist, function (index, option) {
            $("<option>").val(option).appendTo(datalistElement);
          });
        } else {
          $("<option>").val("No courses available").appendTo(datalistElement);
          console.log(datalistElement);
          if (data !== null) {
            console.log("No courses found. Placeholder item:", data[0]);
          } else {
            console.log("No data received from the server.");
            return;
          }
        }
      },
      error: (err) => {
        console.log(err);
      },
    });
  };
  searchInput.on("keyup", function (e) {
    if (
      resultBox.length > 0 &&
      resultBox[0].classList.contains("not-visible")
    ) {
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
