# Image recognition and data extraction

## Landmarks and Joints
The first thing to do is to create a code that can be used to obtain the information we need. Fortunately we know that the are going to be using MediaPipe since the begining of the project wich made a straight shot for us at the time of developing this simple tool in wich we can iterate the different requirements.

We start off by creating a module that obtains the image information from our camera and then we use mediaPipe to process the information. Using the Vision module we obtain the landmaks @landmarker. Landmarks are the name given to the visual representation of the human body joints that the model is able to track and reproduce.

![Pose landmarks\label{Pose Landmark Numeration}](pose_landmarks_index.png){width=50%}

For clarity, we colored different sections. The head section is colored green and the body is split into two sections, the right and the left hemispheres. Right side is red and the left is blue.

At this point we draw the points that we obtained in the image in the picture frame and the conections between them that mediapipe also provides us. To draw the dots and lines, we have to normalize the data as mediapipe provides us with values in the range [1,-1] therefor we have to translate them into the canvas using the picture resolution as values for normalization.

By doing this we get a simple code that draws in the frame the data that is obtained and processed by mediapipe.

## Human body planes.

@BodyPlanes @humBodPlanes @cardinalPlanesBody

In anatomy, understanding the concept of anatomical planes and axes is fundamental for describing the orientation and movement of the human body. Anatomical planes are imaginary flat surfaces used to divide the body into sections, aiding in the visualization and communication of anatomical relationships. These planes serve as reference points for describing the position of structures and organs relative to each other. The three primary anatomical planes are the sagittal, frontal (coronal), and transverse (horizontal) planes.

The sagittal plane divides the body into left and right halves, running parallel to the midline. It is further subdivided into median (or midsagittal) and parasagittal planes. The median sagittal plane precisely bisects the body into equal left and right halves, passing through the midline, while parasagittal planes are parallel to the median plane but offset to either side.

The frontal plane, also known as the coronal plane, divides the body into anterior (front) and posterior (back) portions. It is perpendicular to the sagittal plane and runs parallel to the coronal suture of the skull. Movement within the frontal plane includes abduction (moving away from the midline) and adduction (moving toward the midline) of limbs.

The transverse plane, often referred to as the horizontal plane, divides the body into superior (upper) and inferior (lower) portions. It is perpendicular to both the sagittal and frontal planes and is typically positioned parallel to the ground when the body is in the standard anatomical position. Rotational movements within the transverse plane include internal rotation (rotation toward the midline) and external rotation (rotation away from the midline) of limbs. Understanding these planes and their associated movements is essential for anatomical studies, medical diagnoses, and surgical procedures.

![Axes of the Human Body\label{Axes of the Human Body}](humanBodyPlanes.jpg){width=50%}

In our research, we are trying to establish a movement within these planes to be able to determine different parameters of the body's behavior and the direction of movement. For this precise reason, we are going to be using the data and we are going to normalize it in one of the different planes that we before mentioned using the angles of the joints for this process. The movement as described is considered to be an extension or a flexion seen by any of the axes of movement, therefore we can try to use this data to determine the direction of movement and the rate of it @Parklandcsit2012Apr. 

The process would be:

- Calculating the vector between joints A, B and C on a certain plane. 
- Calculating the product and the magnitude of the vectors.
- Applying the formula " cos(a) = (AB · BC) / (|AB| * |BC|) "
- The arccos would give us the angle of the B landmark so we can normalize its data.

## Stepping stones

In terms of raw programming, I'm finding an issue with finding the normalization of a joint at a given time with the method previously used due to the fact that I cannot access the coordinates of the previous and next joint. For this precise reason, I proceed to create a new function that returns me a vector of the currently visible landmarks.
This is key as we decided that an important point of reference that we could start measuring is when a step is taken, this is really important because since we don't have depth sensing cameras we cannot distinguish between floor and wall for example, we will have to use other much different approaches to know when a step is taken.

We are going to start trying to evaluate the height of the different landmarks that form a foot. We know as documentation tells us, that landmarks [27,29,31] and [28,30,32] form the left and right foot respectively. As we talked about before, we know that movement is a combination of extension and flexion @Parklandcsit2012Apr, in this case, we assess that in order to take a step, one foot must flex and rise above the other, then proceeding to do the opposite, extending and causing the other foot to flex. This extension and flexion are reflected in our data as a change in the "y" variable of the joints, and normal steps commonly make the whole foot rise over the ankle of the other foot.

During testing, we also noticed and tweaked the variables as we noticed visibility as a parameter part of the landmarker function, which will be very useful for the assessment of false positives in the joint visualization. At this point, we also implemented several different features such as the ability to determine which landmarks are visible at a certain point in time and also the ability to extract the data that we collect to a csv file for future processing and easier visualization.
