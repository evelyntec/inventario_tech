# Sistema de Gestión de Inventario Tecnológico

Este proyecto es una aplicación de consola escrita completamente en Python que ayuda a llevar el control de los equipos tecnológicos de una empresa: notebooks, monitores, teclados, impresoras y todo lo que suele perderse de vista cuando nadie lo administra.

Soy Evelyn Álvarez y este es mi primer sistema completo construido desde cero.

## ¿Qué hace el sistema?

Al ejecutarlo aparece un menú que acompaña en todo momento. Desde ahí puedes registrar equipos nuevos con su código, nombre, marca, categoría y valor; ver todo el inventario ordenado en una tabla; buscar un equipo puntual por su código o eliminarlo si ya no existe; y consultar cuáles marcas tienes registradas sin repeticiones.

Mi parte favorita es la opción de depreciación: le indicas un equipo y cuántos años quieres proyectar, y el sistema calcula cuánto valdrá en ese tiempo, asumiendo que los equipos tecnológicos pierden un 20% de su valor cada año. Ese cálculo lo hace una función recursiva, es decir, una función que se llama a sí misma año tras año hasta llegar al presente, algo así como pelar una cebolla capa por capa hasta llegar al centro.

También puedes generar un reporte en formato CSV con un solo clic en el menú. Ese archivo se puede abrir en Excel y trae todos los equipos registrados, cuánto valdrá cada uno en tres años, el valor total del inventario y la fecha en que se generó el reporte.

## ¿Cómo se usa?

Solo necesitas tener Python instalado en tu computador (versión 3.10 o superior). No hay que instalar nada adicional, porque el sistema usa únicamente herramientas que ya vienen con Python.

Para ejecutarlo, abre una terminal en la carpeta del proyecto y escribe:
python main.py
Si estás en Windows, también funciona con `py main.py`.

## ¿Cómo está construido por dentro?

En lugar de escribir todo el código en un solo archivo gigante, el proyecto está separado en módulos, donde cada uno tiene una responsabilidad clara: uno se encarga de conversar con el usuario y mostrar el menú, otro valida que los datos ingresados sean correctos, otro administra las operaciones del inventario, otro hace los cálculos y el último genera los reportes. Los módulos se comunican entre sí importando las funciones que necesitan, igual que compañeros de equipo que se piden ayuda.

Una de las cosas que más cuidé fue que el programa no se caiga nunca, sin importar lo que escriba el usuario. Si el sistema espera un número y alguien escribe letras, o deja un campo vacío, o elige una opción que no existe, el programa lo explica con un mensaje claro y vuelve a preguntar.

También me preocupé de usar la herramienta correcta para cada tipo de dato: las categorías de equipos viven en una estructura que no se puede modificar por accidente porque son fijas, el inventario está en una lista que crece y se achica según lo que pase, cada equipo guarda sus datos con nombres claros para que el código se lea casi como español, y las marcas únicas se obtienen con una estructura que elimina los duplicados por sí sola.

## Lo que aprendí

Este proyecto me permitió aplicar todo lo del bootcamp en algo concreto: capturar y validar datos, tomar decisiones con condicionales, repetir tareas con bucles, crear funciones reutilizables incluyendo una recursiva, elegir estructuras de datos con criterio, dividir un programa en módulos y generar archivos como resultado del trabajo del sistema. Pero sobre todo aprendí que un buen programa no es el que funciona cuando todo sale bien, sino el que sigue en pie cuando las cosas salen mal.