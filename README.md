# Wallpaperdaily
Es un script en python para descargar la imagen del día publicada en la web de National Geographic y luego establecerla como fondo de escritorio (sólo para escritorios XFCE)

Me he inspirado en el articulo de [El Atareado](https://www.atareao.es/apps/wallpapers-con-national-geographic-en-ubuntu/) que funciona para escritorios Gnome, así que quise intentar hacerlo para xfce que es mi escritorio por defecto en Manjaro Linux.

A diferencia de la app de El Atareado con instalador para los sabores de ubuntu, este es un sencillo script en python que pueden correr desde su sistema siguiendo los siguientes pasos:

## Requisitos
* Python 3.6
* python-lxml
* python-pip
* python-cssselect

## Paso 1
Bueno, no soy programador habitual en Python, por lo general lo hago en PHP o Javascript, pero quise retarme un poco y practicar python, así que los requisitos son porque ninguna de las librerías las tenía instaladas en mi sistema, Si ya eres un programador habitual de python es muy probablemente que no requieres instalar nada.

En Arch Linux o derivados con escritorio xfce:

    sudo pacman -S python-lxml python-pip

    sudo pip install cssselect

En xubuntu

    sudo apt-get install python3-pip python3-lxml python3-cssselect

## Paso 2
Puedes clonar o descargar el repositorio y ponerlo en la ubicación que gustes:

    git clone https://github.com/rocandante/wallpaperdaily.git

## Pase 3
**Ejecutar el script:** 
De momento sólo he probado el script en ejecución manual, no he hecho pruebas con cron (cronie en Arch) para ver si se ejecuta correctamente. Lo pueden correr desde el terminal con la siguiente instrucción:

    python Ruta al script/wallpaperdaily.py

Tengan en cuenta que el script creara una carpeta llamada wallpappers en la ruta de ejecución del script, donde guardara la imagen para poder ser usada como fondo de escritorio.

Disfruten.

## Licencia

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.