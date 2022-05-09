var pos;

var $demo;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(create_post);
    } else {
        $demo.text("Geolocation is not supported by this browser.");
    }
}

$(document).ready(function () {
    $demo = $("#demo");
    $('#btn_submit').on('click', function () {
        var data = pos.coords;
        data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.post("/ajax/", data, function () {
            alert("Saved Data!");
        });
    });
});


$('#post-form').on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    getLocation();
});

function create_post(position) {
    console.log("create post is working!") // sanity check
    console.log($('#id_point').val())
    pos = position
    var {latitude , longitude } = pos.coords;
    $.ajax({
        url : "submit_point/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#id_point').val(),
                 lat : latitude,
                 long : longitude,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), }, // data sent with the post request


        // handle a successful response
        success : function(response) {
            $('#post-text').val('');
            document.getElementsByTagName("html")[0].innerHTML = response;
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}