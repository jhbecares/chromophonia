### Chromophonia
Proyecto realizado para la asignatura TMI del Máster en Ingeniería Informática de la Universidad Complutense de Madrid. 

_Autores_

- Jennifer Hernández Bécares

- Viktor Jacynycz García

### Manual de uso

El proyecto se divide en dos partes:

_Primera parte_

Por un lado, la carpeta *spectrogram* contiene el código necesario para pasar de canciones a imágenes. 
Para ello, se proporciona un script denominado generate_images.sh, que se encuentra en spectrogram/generate_images.sh y que lo que hace es
tomar todos los audios que se encuentren en la ruta spectrogram/wavs/audio y generar sus correspondientes imágenes en la carpeta
spectrogram/images. 

_Segunda parte_

Una vez el algoritmo inicial ha convertido a imágenes todas las canciones, podemos comparar dichas imágenes para intentar decidir cuáles
son más parecidas entre ellas. El script de comparación de canciones se encuentra en histogram/compare_histograms_1D_all.sh. Este script
compara los histogramas a color en una dimensión de las imágenes, haciéndolo una a una. También se proporcionan scripts para generar los
histogramas a color en 1, 2 y 3 dimensiones, aunque finalmente no los hemos utilizado todos para la versión final de nuestro proyecto.

_Aplicación_

Hemos decidido utilizar lo anterior para crear una herramienta que, partiendo de ciertas canciones y pasándolas a su correspondiente
imagen generada, podamos elegir una de ellas y mostrar las 6 canciones más parecidas a ella. Esto nos sirve para, cuando nos enfrentamos
a una base de datos con muchísimas canciones y queremos encontrar canciones parecidas a nuestra favorita, podemos seleccionar esa 
canción y el programa nos devolverá los nombres de las 6 canciones que más se parecen junto con su correspondiente imagen. 

Para probar esto, es necesario que las imágenes generadas por el algoritmo de la primera parte estén en la carpeta spectrogram/images y, 
además, lanzar el programa de la siguiente forma:

```
python histogram/compare_histograms_1D_all.py
```
