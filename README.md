# Instrucciones

Descargamos el projecto del siguiente Github:

https://github.com/Gokuss7/Projecto-Final

Para poder accesar y correr el Padron Electoral debemos hacer lo siguiente:

Instalar los requerimentos indicados en:

requierments.txt

Para ello abrimos la terminal y vamos a la ruta del projecto, ahi usamos:

pip install -r requirements.txt

Desues de que se termine de instalar todo, debemos configurar el archivo padronapi.ini que se encuentra en la raize del projecto y le pegamos dentro el sigiente texto tal cual como esta aqui:

[DB]
name = padron
user = python
password = greencore
host = hagrid.delhelsa.com
port = 5432

Despues corremos primero el archivo get_api.py y despues el web.py ( ambos se encuentran en raiz del projecto ), verificamos que ambos esten corriendo y mostrando los siguientes enlaces funcionando:

http://127.0.0.1:5000/

http://127.0.0.1:2000/

Si no hay ningun error, podemos ir a consultar el padron electoral a la ruta:

http://127.0.0.1:2000/

Consultas con mucho gusto!
