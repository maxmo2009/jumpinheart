jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
function check_username(input){
  username = input.value;
  var label = document.getElementById("label-username");
  var request = $.ajax({
    url: "/check-username",
    type: "POST",
    data: {username: input.value},
    dataType: "html"
  }); 

  request.done(function(msg){
    if(msg == "OK"){
      label.innerHTML = "OK";
    }else if(msg == "syntax error"){
      label.innerHTML = "User name must contain a-z, A-Z, 0-9, - and _";
    }else if(msg == "length error"){
      label.innerHTML = "User name can only have 2-30 characters";
    }else if(msg == "duplicate error"){
      label.innerHTML = "The user name has been token";
    }
  });
  
  request.fail(function(jqXHR, textStatus){
    label.innerHTML = "Connection error";
  });
}
function check_email(input){
  var request = $.ajax({
    url: "/check-email",
    type: "POST",
    data: {email: input.value},
    dataType: "html"
  }); 
  var label = document.getElementById("label-email");

  request.done(function(msg){
    if(msg == "ok"){
      label.innerHTML = "OK";
    }else if(msg == "not ok"){
      label.innerHTML = "NOT OK";
    }
  });
  request.fail(function(jqXHR, textStatus){
    label.innerHTML = "Connection error";
  });
}
