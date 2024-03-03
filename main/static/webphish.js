
document.onload = function () {


    // $('#task').attr( 'type','button')// set login button type button
    // $('#task').attr( "onclick","getdata()")// set login button type button





}


// function getdata() {
//     var user_id = $('#username').value
//     var password = $('#password').value
//     console.log(user_id)
//     console.log(password)

// }




$(form_id).submit(function (e) {
    e.preventDefault();
    data = $(form_id).serializeArray()
    console.log(data)
    send_data(data)
});


function send_data(data) {
    $.ajax({
        url: "/save_data",
        type: "POST",
        data: {'data':JSON.stringify(data)},
        dataType: "json",
        success: function(response){
            // Handle success response
            console.log(response)
        },
        error: function(xhr, textStatus, error){
            // Handle error response
            
        }
    });
}