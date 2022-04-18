$(document).ready(function(){
    $('#reg').click(function(){
        var name=$('#name')
        if(name.val()=='')
        {
            $('#p1').show()
            $('#name').css({'border':'solid 2px red'})
            return false
        }
        else
        {
          $('#p1').hide()
          $('#name').css({'border':'solid 2px black'})
        }
        var email=$('#email')
        if(email.val()=='')
        {
            $('#p2').show()
            $('#email').css({'border':'solid 2px red'})
            return false
        }
        else
        {
          $('#p2').hide()
          $('#email').css({'border':'solid 2px black'})
        }
        var password=$('#password')
        if(password.val()=='')
        {
            $('#p3').show()
            $('#password').css({'border':'solid 2px red'})
            return false
        }
        else
        {
          $('#p3').hide()
          $('#password').css({'border':'solid 2px black'})
        }
        var cpassword=$('#cpassword')
        if(cpassword.val()=='')
        {
            $('#p4').show()
            $('#cpassword').css({'border':'solid 2px red'})
            return false
        }
        else
        {
          $('#p4').hide()
          $('#cpassword').css({'border':'solid 2px black'})
        }
    })
})