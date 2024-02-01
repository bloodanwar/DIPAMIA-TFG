# Methodology

The first thing to do is to create a code that can be used to obtain the information we need. Fortunately we know that the are going to be using MediaPipe since the begining of the project wich made a straight shot for us at the time of developing this simple tool in wich we can iterate the different requirements.

We start off by creating a module that obtains the image information from our camera and then we use mediaPipe to process the information. Using the Vision module we obtain the landmaks @landmarker. Landmarks are the name given to the visual representation of the human body joints that the model is able to track and reproduce.

![Pose landmarks\label{Pose Landmark Numeration}](pose_landmarks_index.png){width=50%}

For clarity, we colored different sections. The head section is colored green and the body is split into two sections, the right and the left hemispheres. Right side is red and the left is blue.

At this point we draw the points that we obtained in the image in the picture frame and the conections between them that mediapipe also provides us. To draw the dots and lines, we have to normalize the data as mediapipe provides us with values in the range [1,-1] therefor we have to translate them into the canvas using the picture resolution as values for normalization.

By doing this we get a simple code that draws in the frame the data that is obtained and processed by mediapipe.

At this point we decide to start the straction of the data so we can start procesing it in our own way. As we have previously mentioned the data is of the range [1,-1] wich we can tecnicaly use but we shouldnt. We are going to normalize the data. In order to normalize the data decided that we are going to use the angles made by the joint conections. 
The process would be:
- Calculating the vector between joints A, B and C. 
- Calculating the product and the magnitude of the vectors.
- Applying the formula " cos(a) = (AB · BC) / (|AB| * |BC|) "
- The arccos would give us the angle of the B landmark so we can normalize its data.




---------------------------------- 
## IGNORAR TODO LO SIGUIENTE SON ANOTACIONES

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