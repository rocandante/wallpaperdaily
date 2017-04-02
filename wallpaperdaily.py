#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wallpaper.py
#  
#  Copyright 2017 Juan David C <rocandante@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import requests
import os
from lxml.html import fromstring
from gi.repository import Gio
from gi.repository import GLib
import subprocess
import datetime

#URL desde donde se va descargar la imagen para el fondo de pantalla
URL = 'http://www.nationalgeographic.com/photography/photo-of-the-day/'
#Nombre de la carpeta donde queremos guardar las imagenes
img_dir = 'wallpapers'

def make_image_dir(img_path):
	try:
		os.makedirs(img_path)
	except OSError:
		pass
	# si no podemos crear la ruta dejamos que pase
	return img_path

def set_image_path():
	
	#Fecha actual
	ahora = datetime.date.today()
	#Se establece el nombre para el archivo
	fname = 'natgeo_'+ahora.strftime("%Y%m%d")+'.jpg'
	
	#Se establece la ruta donde se va guardar el archivo
	cur_path = os.getcwd()+'/'+img_dir
	
	if not os.path.exists(cur_path):
		dir_path = make_image_dir(cur_path)
	else:
		dir_path = cur_path
	img_path = os.path.join(dir_path, fname)
	return img_path

def set_background(afile=None):
	#solamente para escritorios xfce4 con una sola pantalla

	#Establece el fondo de pantalla en el workspace actual
	put_wallpaper = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/workspace0/last-image", "-s", afile]
	subprocess.Popen(put_wallpaper)
	
	#Si se desea establecer un estilo, 5 = ampliada
	style = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-style", "-s", "5"]
	subprocess.Popen(style)
	
	#Recarga la configuracion
	reload_conf = ["xfdesktop","--reload"]
	subprocess.Popen(reload_conf)
            

def main():
	#Solicita la url
	r = requests.get(URL)
	
	if r.status_code == 200:
		#Captura el contenido html
		doc = fromstring(r.text)
		#Busca la propiedad og:image para extraer la url de la imagen
		for meta in doc.cssselect('meta'):
			prop = meta.get('property')
			if prop == 'og:image':
				image_url = meta.get('content')
				r = requests.get(image_url, stream=True)
				if r.status_code == 200:
					photo_path = set_image_path()
					try:
						with open(photo_path, 'wb') as f:
							for chunk in r.iter_content(1024):
								f.write(chunk)
						set_background(photo_path)
					except Exception as e:
						print(e)
                

if __name__ == '__main__':
    main()
    exit(0)
