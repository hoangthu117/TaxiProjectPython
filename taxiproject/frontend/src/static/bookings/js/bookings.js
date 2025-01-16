function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
$(document).ready(function() {
    $('#booking-form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
            url: 'http://ec2-13-236-52-34.ap-southeast-2.compute.amazonaws.com/api/book/',
            method: 'POST',
            data: $(this).serialize(),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                $('#message').html('<p>' + response.message + '</p>');
            },
            error: function(response) {
                $('#message').html('<p>Error: ' + response.responseJSON + '</p>');
            }
        });
    });
});