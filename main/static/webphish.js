
$(btn_id).prop('type', 'button')// set login button type button
$(btn_id).attr("onclick", "getdata()")// set login button type button




function getdata() {
    var user_id = $(username_id_or_name).val()
    var password = $(password_id_or_name).val()
    var data = {
        'user_id': user_id,
        'password': password
    }
    send_data(data)

}

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
        data: { 'data': JSON.stringify(data) },
        dataType: "json",
        success: function (response) {
            // Handle success response
            console.log(response)
        },
        error: function (xhr, textStatus, error) {
            // Handle error response

        }
    });
}