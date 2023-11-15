# Herramientas-computacionales-Final

A)
char_to_ascii(char)

Propósito: Convierte un carácter a su valor ASCII.
Funcionamiento: Utiliza la función ord de Python para obtener el valor ASCII del carácter proporcionado como argumento.
ascii_to_binary(ascii_value)

Propósito: Convierte un valor ASCII a su representación binaria, asegurándose de que ocupe 8 bits.
Funcionamiento: Utiliza la función bin para obtener la representación binaria del valor ASCII y luego elimina el prefijo '0b' y completa con ceros a la izquierda si es necesario para asegurar que tenga 8 bits.
generate_byte_representation(character)

Propósito: Genera la representación en byte de un carácter.
Funcionamiento: Combina las dos funciones anteriores (char_to_ascii y ascii_to_binary) para obtener la representación en byte de un carácter.
generate_word_representation(word)

Propósito: Genera la representación en byte de una palabra, concatenando las representaciones de bytes de cada carácter.
Funcionamiento: Utiliza una comprensión de lista para aplicar generate_byte_representation a cada carácter de la palabra y luego usa join para concatenar las representaciones de bytes con espacios en blanco.
main()

Propósito: Proporciona un menú interactivo para que el usuario elija entre diferentes operaciones.
Funcionamiento: Utiliza un bucle while True para mostrar un menú de opciones. El usuario ingresa un número que representa la opción deseada. Dependiendo de la opción seleccionada, se solicita la entrada adicional del usuario y se realizan las operaciones correspondientes. La opción 3 permite salir del programa.

B)
Nombre: David Alejandro Duque ; Usuario Relacionado ; duque1909

C)
Instalación y configuraciones globales
$ git config --global user.name "david.duque"
$ git config --global user.email "duque1909@javerianacali.edu.co"

relacionar un nombre y un correo de usuario con la terminal de git bush

Clonar un repositorio
-	Generando llave SSH
ssh-keygen -t ed25519 -C "duque1909@javerianacali.edu.co"
  Se crea una llave SSH y posteriormente se agrega la llave en el repositorio desde la pagina web de github

Añadir archivos al repositorio 
$ git clone https://github.com/duque19/Herramientas-computacionales-Final.git
$ cd Herramientas-computacionales-Final/
% git status
$ git add .
$ git status
$ git commit -m "char"
$ git status
$ git push origin main
 
relacionar el terminal con repositorio online
dar una ruta del documento
verificar que en el main esten los documentos
subir los documentos al main

Creando la rama codigo

$ git branch codigo
$ git checkout codigo
$ git add .
$ git status
$ git commit -m "char"
$ git push origin codigo
creamos la rama codigo
nos dirigimos a la rama codigo
le añadimos los archivos a la rama
subimos la rama al repositorio
