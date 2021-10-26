$(document).ready(function() {
    $(document).on('click','.estudiante-perfil', function (evento) {
        evento.preventDefault();
        let id=document.getElementById('idEstudiante').textContent;
        console.log(id);
        $.post('/estudiante',{id}, function (response) {
            const validacion=JSON.parse(response);
            /*if(validacion.name=='true'){
                alert('El Cliente ya tiene Servicios Registrados');
                return;
            }else{                    
                $('#servicios_frm').submit();                    
            }*/
        });
    }); 
});