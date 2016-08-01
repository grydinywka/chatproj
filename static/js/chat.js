function scrollToBottom() {
    var height = $('body').prop('scrollHeight');

    $(window).scrollTop(height);
}

function appendNotice() {
    $("#add_notice").click(function(event) {
        var form = $('form#new-msg-form');

        $.ajax({
            'url': form.attr('action'),
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'add_notice': true,
                'content': $('input#content').val(),
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'beforeSend': function() {
                event.preventDefault();
            },
            'success': function(data, status, xhr) {
                var notice_error = $('#notice-error');

                if ( 'content_error' in data ) {
                    notice_error.text(data.content_error);
                    notice_error.parent().addClass('has-error');
                } else {
                    var list_message = $('#msg-list ul');

                    notice_error.text('');
                    notice_error.parent().removeClass('has-error');
                    $('#content').val('');

                    list_message.append(
                        '<li class="list-group-item">(' +
                             data.created + ') <strong>' + data.username +
                            '</strong><p>' + data.content + '</p>' +
                        '</li>'
                    );
//                    getNotices();
                }
                scrollToBottom();
            },
            'error': function() {
                alert('Error on server');
            }
        });
    });
}

function getNotices() {
    $.get('/chat/', function(html) {
        var html = $(html);
        var messages_from_db = html.find('div#msg-list ul');
        var messages_from_chat = $('div#msg-list ul');

        if ( messages_from_db.children().length > messages_from_chat.children().length ) {
            messages_from_chat.html(messages_from_db.children());
            if ( $('body').prop('scrollHeight') - $(window).scrollTop() < 2000 ) {
                scrollToBottom();
            }
        }
    });

//    scrollToBottom();
}

$(document).ready(function() {
    scrollToBottom();
    appendNotice();
    setInterval(getNotices, 1000);

});