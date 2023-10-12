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
        var datalist = [];
        var datalistElement = $("#browsers");
        datalistElement.empty();
        if (Array.isArray(data) && data.length > 0) {
          for (let i = 0; i < data.length; i++) {
            datalist.push(data[i].name);
          }
          $.each(datalist, function (index, option) {
            $("<option>").val(option).appendTo(datalistElement);
          });
        } else {
          if (data !== null) {
            datalistElement.empty();
            var newOption = $("<option>").val("No option available")[0];
            datalistElement.append(newOption);
            console.log(newOption, datalistElement[0]);
          }
          //data is null
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
