$(document).ready(function () {
  $("#search-form").on("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    var query = $("#search-input").val(); // Get the search query from the input field

    // Send an AJAX request to the server
    $.ajax({
      type: "GET",
      url: "/courses/", // URL endpoint for the search view
      data: {
        query: query,
      },
      success: function (data) {
        // Clear the existing course list
        $("#course-list").empty();

        // Process the received data and update the course list dynamically
        for (var i = 0; i < data.length; i++) {
          var course = data[i];

          var courseCard = `
            <div class="col-lg-3 col-md-4 col-sm-2">
              <div class="card courses" style="width: 15rem;">
                <img class="card-img-top course-img" src="${course.image_url}" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">${course.name}</h5>
                  <p class="card-text">
                    ${course.description}
                  </p>
                  <hr class="courseline">
                  <a href="/courses/${course.pk}/" class="btn btn-primary aboutthis">About this</a>
                  <a href="#" class="btn btn-success"><i class="fa-solid fa-indian-rupee-sign cost"></i> ${course.cost}</a>
                  <a href="/courses/${course.pk}/update/" class="btn btn-warning aboutthis">Update</a>
                  <a href="/courses/${course.pk}/delete/" class="btn btn-danger aboutthis">Delete</a>
                </div>
              </div>
            </div>
          `;

          $("#course-list").append(courseCard);
        }
      },
      error: function (xhr, textStatus, errorThrown) {
        console.log("Error:", errorThrown);
      },
    });
  });
});
