(function () {
    let Message;
    Message = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;
        this.draw = function (_this) {
            return function () {
                let $message;
                $message = $($('.message_template').clone().html());
                $message.addClass(_this.message_side).find('.text').html(_this.text);
                $('.messages').append($message);
                return setTimeout(function () {
                    return $message.addClass('appeared');
                }, 0);
            };
        }(this);
        return this;
    };

    let get_response = async(msg) => {
        const response = await fetch("/chat", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ msg: msg })


            });
        let json = await response.json();
        let message = json.message;
        return message.toString();

    };
    var Response;
    Response = async function(arg) {
        this.msg = arg.msg;
        sendMessage(this.msg, 'right');
        bot_res = await get_response(this.msg);
        sendMessage(bot_res, 'left');
    };

    let sendMessage;
    sendMessage = function (text, side) {
        var $messages, message;
        if (text === '') {
            return;
        }
        $('.message_input').val('');
        $messages = $('.messages');
        let message_side;
        message_side = message_side === 'left' ? 'right' : 'left';
        message = new Message({
            text: text,
            message_side: side
        });
        message.draw();
        return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
    };
    $(function () {
        var getMessageText;
        message_side = 'right';
        getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };
        
        let msg;
        $('.send_message').click(function (e) {
            msg = getMessageText();
            return Response({"msg": msg});
        });
        $('.message_input').keyup(function (e) {
            if (e.which === 13) {
                msg = getMessageText();
                return Response({"msg": msg});
            }
        });
        sendMessage('Hi there, I am your assistant. Describe your favorite items and I will recommend you some products that match your needs', 'left');
    });
}.call(this));