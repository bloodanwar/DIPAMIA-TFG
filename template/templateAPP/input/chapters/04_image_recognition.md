Info recavada de mediapipe y el codigo de david


El dodigo de david usa dos clases, una detecta la pose y la otra dibuja el frame

pose:
    Utiliza 3 modelos que están en una carpeta separados (pregunter por ellos)
    utiliza la task de vision en media pipa para elegir los parametros basicos en el modelo.
    inicializa el objeto con los valores pasados en la creación
    para la detección de imagen usa la libreria de mp con la función image.
    landmarker es la función que usa para la detección de los puntos
        esto es lo que sale en la documentación de mediapipe y por eso lo referencian tanto en el paper.
    devuelve el resultado de la pose del landmarker
draw:
    llama al objeto de la pose
    toma como configuracion los colores para los parametros.
    tiene unos condicionantes que colorean los joints dependiendo de la posición, como se ve en la imagen unos son la cara y otros son el lado izquierdo o derecho del cuerpo. (preguntar los enteros pero supongo que serán los numeros de los landmarks que ya están definidos por mp)
    los dibuja usando cv2
    notar que en este dibujado accede a .poselandmarks, lo cual parece ser la lista de los landmarks que hay en el frame. 
    investigar ka función circle pero parece "simple" en su función
    usa line para las conexiones haciendo referencia a las coords x e y de ambos puntos


en el main solo hace un bucle infinito con las dos funciones
se definen los valores para el objeto de la pose
usa cv2 para la captura del video




-----------


La función de convolución realiza el filtrado de los valores de píxel de una imagen, lo que se puede utilizar para aumentar su nitidez, difuminarla, detectar sus ejes u otros realces basados en el kernel. Los filtros se ut  ilizan para mejorar la calidad de la imagen de ráster al eliminar datos falsos o mejorar las entidades de los datos. Estos filtros de convolución se aplican a un kernel móvil o superpuesto (ventana o vecindad), como 3 x 3. Los filtros de convolución actúan calculando el valor de píxel en función de la ponderación de sus vecinos