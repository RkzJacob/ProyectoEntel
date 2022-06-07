$(document).ready(
    function(){

    $("#EscribirCodigo").blur(
        function(){
          var mensaje="";
          if($("#EscribirCodigo").val().trim().length==0){
            mensaje= "El nombre esta en blanco";
          }
          if(mensaje!=""){
            $("#error1").html(mensaje);
            $("#error1").show();
          }else{
            $("#error1").hide();
          }
           
        }
    )
    $("#error2").hide();    
    $("#EscribirNombre").blur(
        function(){
          var mensaje="";
          if($("#EscribirNombre").val().trim().length==0){
            mensaje= "El nombre del medicamento esta en blanco";
          }
          if(mensaje!=""){
            $("#error2").html(mensaje);
            $("#error2").show();
          }else{
            $("#error2").hide();
          }
           
        }
    )

    $("#error3").hide();    
    $("#EscribirDesc").blur(
        function(){
          var mensaje="";
          if($("#EscribirDesc").val().trim().length==0){
            mensaje= "La descripción está en blanco";
          }
          if(mensaje!=""){
            $("#error3").html(mensaje);
            $("#error3").show();
          }else{
            $("#error3").hide();
          }
           
        }
      
    )
    $("#error4").hide();    
    $("#EscribirFabricante").blur(
        function(){
          var mensaje="";
          if($("#EscribirFabricante").val().trim().length==0){
            mensaje= "El fabricante del medicamento está en blanco";
          }
          if(mensaje!=""){
            $("#error4").html(mensaje);
            $("#error4").show();
          }else{
            $("#error4").hide();
          }
           
        }
      
    )

    $("#error5").hide();    
    $("#EscribirContenido").blur(
        function(){
          var mensaje="";
          if($("#EscribirContenido").val().trim().length==0){
            mensaje= "El contenido del fabricante esta en blanco";
          }
          if(mensaje!=""){
            $("#error5").html(mensaje);
            $("#error5").show();
          }else{
            $("#error5").hide();
          }
           
        }
      
    )
    $("#error6").hide();    
    $("#EscribirCantidad").blur(
        function(){
          var mensaje="";
          if($("#EscribirCantidad").val().trim().length==0){
            mensaje= "La cantidad esta vacio";
          }
          if(mensaje!=""){
            $("#error6").html(mensaje);
            $("#error6").show();
          }else{
            $("#error6").hide();
          }
           
        }
      
    )
    $("#error7").hide();
    $("#EscribirGramaje").blur(
        function(){
          var mensaje="";
          if($("#EscribirGramaje").val().trim().length==0){
            mensaje= "El gramaje esta en blanco";
          }
          if(mensaje!=""){
            $("#error7").html(mensaje);
            $("#error7").show();
          }else{
            $("#error7").hide();
          }
           
        }
      
    )
    
});    