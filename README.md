# TPO-fundamentos-de-programacion (No se usan returns o breaks en ciclos)

## ABOUT

Resolucion del tpo propuesto, resolucion de problemas de la empresa ficticia "UADEtech corp"
El alcance funcional de nuestro proyecto será orientado a un sistema de gestión de suministros para gaming "Pro-Gamer Logistics"

Interrogantes para resolver a la hora desarrollar la solución de software:
¿Para que se va a usar?
Nuestro programa buscara consultar y actualizar el estado del stock de la empresa.
Dara un informe de productos que esten sin stock. 
Nos hara un calculo de presupuestos para compras de usuarios minoristas o mayoristas.
En base al metodo de pago y el tipo de cliente (mayorista o minorista) se hara promociones

¿Como se va a usar?
A través de un uso claro de menúes podremos ir variando entre las opciones a elegir.Siendo estas:
1- Consultar estado actual del stock y modificarlo
2- Mostrar stock faltante y productos cuya última actualización en su estado haya sido hace mas de un año
3- Actualizar listas de precios 
4- Calculo de presupuestos
5- Salir

Cada item del menu nos podrá generar un sub-menú en el que podremos operar, siendo por ejemplo en el caso de la primer opción "Consultar estado actual del stock y modificarlo" nos entregará un sub menu que nos dara elegir entre:
1. Mostrar inventario actual.
2. Modificar el inventario actual.


## PREREQUISIST DOWNLOAD


Python Lastest recomended


git 

https://git-scm.com/install/

# SETUP


Clone the repository:

Open CMD 

cd desktop (si se quiere guardar en el escritorio la carpeta, en cualquier otro caso hacer cd la carpeta querida)

git clone https://github.com/TOMK358/TPO-fundamentos-de-programacion.git


## Posible forma de tener que abrir el proyecto en VS CODE

Open CMD


cd TU carpeta guardada


cd TPO-fundamentos-de-programacion


code .


## Connect git with Visual studio Code 

Desde la carpeta clonada del repo


Abrir la terminal



git config --global user.name "Tu Nombre"


git config --global user.email "tumail@gmail.com"
(same as github)


## ANTES DEL COMMIT 

HAGAN UN git pull origin main (esto va a copiar el codigo del repo en su IDE)


## Como hacer un commit desde VS Code
Paso a paso


Agregá archivos al commit

A la IZQUIERDA del VISUAL, ir a la opcion "SOURCE CONTROL"

Tocá el + al lado de cada archivo
o arriba donde dice:


Stage All Changes


Escribí el mensaje del commit


Arriba aparece una caja de texto.


## Ejemplo:


Agregué sistema de login


Confirmá el commit


Tocá:


Commit

o el tilde


Subir a GitHub (push)


## Después del commit:


Sync Changes


o:


Push



## Primera vez: branch main

A veces se necesita esto:

git branch -M main
git push -u origin main



