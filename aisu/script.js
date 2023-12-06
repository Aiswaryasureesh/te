function myFunction(){
alert("registration successfull");
}

      function ValidateEmail(inputText)
      {
         var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
         if(inputText.value.match(mailformat))
         {
            document.write("Valid email address!");
            document.form1.text1.focus();
            return true;
         }
         else
         {
            document.write("You have entered an invalid email address!");
            document.form1.text1.focus();
            return false;
         }
      }
      function validateForm(){
      var str=document.getElementById("email").value;
      if(name===null||name=='');
      alert("invalid");
      }
   


