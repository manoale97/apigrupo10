<h1>API para que puedas consultar a las galletas de la fortuna.</h1>
<p>Desarrollada en python con Flask</p>
<p>Autores:<br>
Manolo Revelo<br>
Sebastian Sandoval<br>
Isaac Mora<br>
</p>
<h2 align="center"> Evidencias</h2>

### Uso de Docker
![Docker](evidencias/docker.png)

### Método: GET sin ruta asociada
![Imagen general](evidencias/imagen.png)
<p>Cuando un usuario accede a la raíz del servidor, la función devuelve un mensaje de bienvenida en formato JSON.</p>

### Método: Info
![Info](evidencias/info.png)
<p>Devuelve un objeto JSON con datos como el nombre del proyecto, la versión actual, una breve descripción y los autores.</p>

### Método: Obtener frase invitado
![Obtener frase invitado](evidencias/obtenerFraseInvitado.png)
<p>Permite a un usuario invitado obtener una frase de la fortuna basada en el mes actual.</p>

### Método: Abrir galleta
![Abrir galleta](evidencias/abrirGalleta.png)
<p>Esta ruta permite a un usuario recibir una frase personalizada de la galleta de la fortuna enviando su nombre mediante una solicitud   POST. La frase se selecciona aleatoriamente entre un conjunto de frases específicas del mes actual.</p>

### Método: Obtener frases 
![Obtener frases](evidencias/obtenerFrases.png)
<p>Esta ruta permite obtener todas las frases de la fortuna disponibles, organizadas por mes.</p>

### Método: Actualizar frases
Detalle: Se agrega una frase al mes Agosto.
![Actualizar frases](evidencias/actualizarFrases.png)
<p>Permite actualizar las frases de la fortuna correspondientes a un mes específico.</p>

### Evidencia
Detalle: Frase agregada.
![Obtener frases 2](evidencias/obtenerFrases2.png)


### Método: Borrar frase
Detalle: Se elimina una frase del mes Enero.
![Borrar frase](evidencias/borrarFrase.png)
<p>Permite eliminar las frases de la fortuna correspondientes a un mes específico.</p>

### Evidencia
Detalle: Se evidencia que solo se tiene una frase en el mes de Enero.
![Obtener frases 3](evidencias/obtenerFrases3.png)

### Método: Crear frase
Detalle: Se agrega una nueva frase en el mes Enero.
![Crear frase](evidencias/crearFrase.png)
<p>Permite crear las frases de la fortuna en un mes específico.</p>

### Evidencia
Detalle: Se evidencia que se agrego una nueva frase en el mes Enero.
![Obtener frases 4](evidencias/obtenerFrases4.png)
