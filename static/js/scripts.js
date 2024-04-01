$("form[name=signup_form").on("submit",function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/user/signup",
      type: "POST",
      data: data,
      dataType: "json",
      success: function(resp) {
        // redirects to dashboard if success
        window.location.href = "/dashboard/"
      },
      error: function(resp) {
        
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });