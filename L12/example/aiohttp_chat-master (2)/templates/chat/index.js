    $(function() {
       var conn = null;
       var name = "UNKNOWN";
       function log(msg) {
         var control = $('#log');
         control.html(control.html() + msg + '<br/>');
         control.scrollTop(control.scrollTop() + 1000);
       }

        login = ""
        password = ""

       function connect() {
         disconnect();
         var wsUri = (window.location.protocol=='https:'&&'wss://'||'ws://')+window.location.host;
         conn = new WebSocket(wsUri);
         //log('Connecting...');
         conn.onopen = function() {
           conn.send("{'user_name': ' " + login + " ','user_password': '"+ password +"'}");
           update_ui();
         };
         conn.onmessage = function(e) {
           var data = JSON.parse(e.data);
           switch (data.action) {
             case  'connect':
               name = data.name;
               log('Connected as ' + name);
               update_ui();
               break;
             case  'disconnect':
               name = data.name;
               log('Disconnected ' + name);
               update_ui();
               break;
             case 'join':
               log('Joined ' + data.name);
               break;
             case 'sent':
               log("(" + data.time + ")" + data.name + ': ' + data.text);
               break;
           }
         };
         conn.onclose = function() {
           log('Disconnected.');
           conn = null;
           update_ui();
         };
       }
       function disconnect() {
         if (conn != null) {
           //log('Disconnecting...');
           conn.close();
           conn = null;
           name = 'UNKNOWN';
           update_ui();
         }
       }
        function showError(error){
            $('#error').html(error);
        }
        $('#send_name').click(function(){

            login = $('#user_name').val();
            password = $('#user_password').val();

                console.log('click')
                if (login && password){
                    $.post('/login', {'user': login, 'password': password}, function(data){
                        console.log(data);
                        console.log('done')
                        if (data.error){
                            console.log(data)
                            showError(data.error)
                        }else{
                         if (conn == null) {
                           connect();

                         } else {
                           disconnect();
                         }
                         update_ui();
                            console.log(data)
                            showError("")
                        }
                    });
                }else{
                    console.log('Please fill all fields')
                }
        });

       function update_ui() {
         if (conn == null) {
           $('#status').text('disconnected');
           $('#connect').html('Connect');
           $('#send').prop("disabled", true);
           $('#send_name').prop("disabled", false);

         } else {
           $('#status').text('connected');
           $('#connect').html('Disconnect');
           $('#send').prop("disabled", false);
           $('#send_name').prop("disabled", true);
         }
         $('#name').text(name);
       }
       $('#connect').on('click', function() {
         if (conn == null) {
           connect();
         } else {
           disconnect();
         }
         update_ui();
         return false;
       });
       $('#send').on('click', function() {
         var text = $('#text').val();
         // log('Sending: ' + text);
         log(text);
         conn.send(text);
         $('#text').val('').focus();
         return false;
       });
//       $('#send_name').on('click', function() {
//         if (conn == null) {
//           connect();
//         }
//
//         var user_name = $('#user_name').val();
//         var user_password = $('#user_password').val();
//
//         // log('Sending: ' + text);
//         log(user_name);
//         conn.send("{'user_name': ' " + user_name + " ','user_password': '"+ user_password +"'}");
//         $('#text').val('').focus();
//         $('#send_name').prop("disabled", true);
//
//         return false;
//       });
       $('#text').on('keyup', function(e) {
         if (e.keyCode === 13) {
           $('#send').click();
           return false;
         }
       });
     });