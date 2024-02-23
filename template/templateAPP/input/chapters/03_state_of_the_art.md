# State of the art

To know what can be done regarding our interests, we must look at what has already been done so far, so we don't waste our time doing something already done by someone else and also so we can use that research as a base to further improve our understanding and our work. 
Because of this, we are going to be looking at the state of the art on camera technologies, methods of extracting the data and different models of artificial intelligence.

## Cameras @galal2016analytical

RGB cameras, short for Red, Green, and Blue cameras, are imaging devices that capture color information by utilizing three primary color channels: red, green, and blue. These cameras mimic the way human vision perceives color by combining these three channels in varying intensities to produce a wide spectrum of colors. Each pixel in the image sensor of an RGB camera contains three sub-pixels, each sensitive to one of the three primary colors. The combination of these sub-pixels allows the camera to capture and reproduce a full range of colors, making RGB cameras essential for applications where color fidelity is crucial.

The popularization of RGB cameras can be attributed to their widespread use in various fields. In consumer electronics, RGB cameras are a key component of smartphones, digital cameras, and webcams, enabling users to capture high-quality and realistic images. In the field of entertainment, RGB cameras play a key role in film and television production, making accurate color representation for a more immersive viewing experience. Even more so, RGB cameras are extensively employed in computer vision applications, such as facial recognition, object detection, and augmented reality, where precise color information is vital for accurate analysis and interpretation. This is the field we are going to be using them in, but as we will see, there are more complications to be dealt with when using RGB cameras in the medical field.

RGB cameras have become necessary in modern society, finding applications in industries ranging from healthcare and automotive to agriculture and surveillance. Their ability to faithfully capture and reproduce color has made them indispensable tools in a wide array of technological advancements, contributing significantly to the way we perceive and interact with the visual world. This is the precise reason we chose to evolve on this type of technology, to make our outcome, the application that relies on the data model, the most accessible possible to all the possible public of our application.


- Infrared (IR) Cameras: Capture infrared light, which is beyond the visible spectrum. Used in night vision applications, thermal imaging, and scientific research @vandersmissen2008night.
- Ultraviolet (UV) Cameras: Detect ultraviolet light, which is also outside the visible spectrum. Applied in scientific research, forensics, and some industrial processes @Fulton1997Mar. 
- Multispectral Cameras: Capture light in multiple bands across the electromagnetic spectrum. Useful in agriculture, environmental monitoring, and medical imaging @honrado2017uav.
- Thermal Infrared Cameras: Detect the heat emitted by objects. Commonly used in night vision, security, and industrial applications @waxman1995color.
- X-ray Cameras: Utilized for medical imaging, security screening, and industrial inspection. Capture X-rays, which have shorter wavelengths than visible light @szot2004diagnostic.
- 3D Cameras: Capture depth information along with color. Used in computer vision, robotics, and augmented reality applications @bleser2005real.
- Depth Cameras: Measure the distance of objects from the camera to create a depth map. Commonly used in computer vision, gesture recognition, and virtual reality @Krishnan2015Feb.


These are just a few examples, and there are many specialized cameras designed for specific applications. Each type of camera serves a particular purpose, depending on the information required for a given task. In particular, we are going to take a look at Depth cameras, in particular Kinect, as it is a well-known and established camera within the medical community for a variety of applications, as we have talked about before.

RGB cameras and depth cameras, such as the Kinect sensor, serve distinct purposes in imaging technology. While RGB cameras focus on capturing color information, depth cameras are designed to measure the distance of objects in a scene, providing a three-dimensional representation of the environment. The Kinect sensor, for instance, utilizes a combination of infrared sensors and a depth-sensing technology called time-of-flight to measure the time it takes for infrared light to travel to an object and back. This information is then used to create a depth map, representing the spatial layout of the scene. @Smisek2013

One significant difference between RGB and depth cameras lies in their respective capabilities. RGB cameras are great at capturing detailed color information, making them suitable for applications like photography, video recording, and image analysis where color fidelity is essential. On the other hand, depth cameras are valuable in scenarios where understanding the spatial relationships and distances between objects is critical. This makes them ideal for applications like gesture recognition, virtual reality, and robotics, where depth perception plays a vital role. 

Even more so, in the medical field, depth cameras have been used for many different purposes for years now. Here are some detailed examples of how depth cameras have been utilized in healthcare @Chiu2019Jun @Bonnechere2014Jan @Dutta2012Jul: 

- Rehabilitation and Physical Therapy: Depth cameras have been employed in rehabilitation settings to monitor and assist patients during physical therapy. Kinect-based systems can track body movements in real-time, providing quantitative data on a patient's range of motion, posture, and joint angles. Physical therapists can use this information to customize rehabilitation exercises and track the progress of patients recovering from injuries or surgeries. In some cases, they can even give output on how a patient is doing a particular exercise and correct them in the case they are doing it wrongly @Omelina2016. 

- Surgical Planning and Navigation: Depth cameras have been integrated into surgical planning and navigation systems to enhance the precision of procedures. By capturing detailed 3D models of a patient's anatomy, surgeons can visualize internal structures with greater accuracy. This technology assists in preoperative planning, allowing surgeons to better understand the space between organs and plan the optimal approach for surgeries. This has been used in combination with X-rays and in their replacement in cases where X-rays are not a viable option @LACHER201911. 

- Prosthetics and Orthotics Design: Depth cameras have been applied in the design and fitting of prosthetics and orthotics. By capturing precise measurements of a patient's limbs in three dimensions, doctors can create customized prosthetics that offer a better fit and improved functionality. This personalized approach enhances patient comfort and the overall effectiveness of prosthetic or orthopedic devices @7130596. 


## Tracking

We not only need to talk about the way we are going to obtain the images for the purposes we are aiming at. Tracking is also a very important aspect of the design and the decision that we have to make. Human movement tracking involves capturing and analyzing the motion of the human body, often represented through skeletal models based on joints @huang2002model. 

A skeletal model based on joints is a representation of the human body's underlying skeletal structure, focusing on key points or joints where bones articulate. This model is used in the context of human movement tracking and motion analysis. The skeletal model typically consists of interconnected joints, each associated with specific body parts, such as the head, shoulders, elbows, wrists, hips, knees, and ankles. These joints are crucial for capturing and understanding the intricate motions and positions of the human body during various activities. These joints are not only possible to be captured on a still image, but also on moving images of the body.

In the field of motion capture and tracking technologies, the skeletal model serves as a virtual framework that mirrors the actual movements of a person. The movement of joints is tracked and recorded using sensors or cameras, providing a three-dimensional representation of how the body is positioned and oriented in space over time. The accuracy and completeness of the skeletal model are essential for capturing natural and realistic human movements. The joints serve as key anchor points, enabling the reconstruction of the entire body's pose and facilitating a deeper understanding of biomechanics, kinematics, and human behavior. As technology advances, these skeletal models become increasingly sophisticated, contributing to the development of more immersive virtual environments, precise biomechanical assessments, and innovative applications in fields such as healthcare, sports, and entertainment.

Various technologies are employed for this purpose, each with its strengths and limitations.

- Inertial Sensors @Ponciano2020May: Inertial sensors, such as accelerometers and gyroscopes, are commonly used for motion tracking. These sensors measure acceleration and angular velocity, allowing the calculation of joint angles and movements. Inertial sensors are wearable and portable, making them suitable for applications like fitness tracking and sports analysis, but in our case, also the medical field.

- 2D Cameras @Krishnan2015Feb: 2D cameras or RGB cameras capture images in two dimensions and can be employed for human movement tracking using computer vision techniques. These cameras are cost-effective and versatile, making them widely used in applications like gesture recognition and video surveillance. However, they lack depth information, limiting their ability to capture the full three-dimensional nature of human movement. These are the ones we have been talking about before.

- 3D Cameras @Smisek2013: 3D cameras, such as depth-sensing cameras, provide depth information along with visual data. They use technologies like structured light or time-of-flight to measure distances, enabling more accurate skeletal modeling. 3D cameras are beneficial for applications like virtual reality, gaming, and biomechanical research, as they offer improved depth perception compared to 2D cameras. These cameras are the category that fits the Kinect as we have talked about before.

- Infrared Cameras @zappi2010tracking: Infrared cameras capture infrared radiation, allowing them to work in low-light conditions. They are often used in conjunction with markers or reflective surfaces to track human movement accurately. Infrared cameras are employed in motion capture systems for animation, biomechanics research, and clinical applications. They offer high precision, but the setup can be complex and requires controlled environments.

- Marker-Based Motion Capture @Furtado2019Jun: Marker-based motion capture systems use markers placed on specific body parts. Cameras, often infrared, track the movement of these markers to create a detailed skeletal model. This method provides high accuracy but may be intrusive, as markers must be attached to the subject's body.  For example, Optitrack is a commercial solution for motion tracking using markers, OptiTrack’s motion capture systems are used in the film industry for creating realistic animations, in the gaming industry for creating immersive experiences, in the VR industry for creating low-latency positional tracking, in the robotics industry for 6DoF tracking, and in the movement sciences industry for human movement analysis.  The cameras are placed around the area where the motion capture is taking place, and they capture the movement of reflective markers that are placed on the objects or people being tracked.

- Markerless Motion Capture @mundermann2006evolution: Markerless motion capture relies on computer vision algorithms to track and reconstruct skeletal models without the need for physical markers. This approach offers more natural movement and is less invasive than marker-based systems, making it suitable for applications like entertainment, sports analysis, and healthcare. OpenPose is a 3D markerless motion capture technique that uses multiple synchronized video cameras to track human poses or skeletons from images. It has been shown to have an accuracy of 30 mm or less.

## Machine Learning Algorithms

Machine learning is the practice of instructing machines on how to manage data more effectively. When it becomes challenging to extract information directly from data, machine learning techniques are applied. The increasing availability of datasets has led to a growing demand for machine learning across various industries, where it is used to extract pertinent information. The primary objective of machine learning is to enable machines to learn autonomously from data, a topic that has attracted extensive research from mathematicians and programmers seeking solutions for handling large datasets.

In Azure's words @AzureML: "Machine learning is an application of AI. It’s the process of using mathematical models of data to help a computer learn without direct instruction. This enables a computer system to continue learning and improving on its own, based on experience.
One way to train a computer to mimic human reasoning is to use a neural network, which is a series of algorithms that are modeled after the human brain. The neural network helps the computer system achieve AI through deep learning. This close connection is why the idea of AI vs. machine learning is really about the ways that AI and machine learning work together."

Machine learning employs a variety of algorithms to address data-related challenges. Data scientists emphasize that there isn't a single, universally optimal algorithm for every problem. The choice of algorithm depends on factors such as the problem type, the number of variables, and the most suitable model. Here's a brief overview of some commonly used machine learning algorithms @MLAlg @Bonaccorso_2018: 

- Supervised Learning: Supervised learning involves training a model to map input data to output based on labeled examples. These algorithms require external guidance, and the dataset is typically split into training and test sets. The algorithms learn patterns from the training set and apply them to the test set for prediction or classification.

- Decision Tree: A decision tree is a graphical representation of choices and their outcomes organized in a tree structure. Nodes represent events or decisions, while edges represent decision rules. Each tree comprises nodes and branches, with nodes representing attributes to be classified and branches indicating potential attribute values.

- Naive Bayes: Naive Bayes is a classification technique based on Bayes Theorem, assuming independence among predictors. It assumes that the presence of one feature in a class is unrelated to the presence of any other feature. Naive Bayes is commonly used for text classification and relies on conditional probabilities.

- Support Vector Machine (SVM): SVM is a widely used machine learning technique for classification and regression analysis. It constructs linear or non-linear boundaries, known as margins, between classes. SVMs utilize a technique called the kernel trick to map inputs into higher-dimensional feature spaces, maximizing the margins between classes and minimizing classification errors.

These of course are not all the Machine Learning algorithms, but they are some of the most used. Machine learning is an ever-evolving field and with recent developments in the AI world, there is sure to be a huge influx of new ideas and changes to the field that will surely guide the path to improvements in Machine Learning.

## MediaPipe 

Now that we have established a basis for motion capture through cameras and tracking systems and we talked briefly about what is machine learning, we have arrived at a very important part of the project, MediaPipe. @Lugaresi2019Jun

MediaPipe is an open-source framework developed by Google that provides a comprehensive solution for building real-time multimodal perceptual pipelines. It is designed to simplify the development of applications that involve various forms of sensor inputs, such as cameras and microphones. MediaPipe offers pre-built components and tools for tasks like hand tracking, face detection, pose estimation, and more.

MediaPipe provides a solution for human tracking through its Pose module, which is designed to estimate the poses of multiple people in real-time. This module can be used for applications such as fitness tracking, gesture recognition, and augmented reality experiences. It uses a pre-trained machine learning model for pose estimation. This model is trained on a large dataset of annotated images to learn the key points (joints) of the human body. The model predicts the positions of specific joints on the human body, typically including key points like the nose, shoulders, elbows, wrists, hips, knees, and ankles. These landmarks form a skeletal representation of the human pose.

The detected pose landmarks are then used as input data in a graph-based processing pipeline. Each joint becomes a node in the graph, and the connections between the joints define the edges. This structure enables efficient processing and tracking of human poses. It is optimized for real-time performance, allowing the pose estimation model to process video streams or camera input in real-time. This is crucial for applications where low-latency tracking is required such as ours.

## Data extraction and compilation 

Análisis de movimiento
Lo primero que deberías entender aquí porque te va a ser muy necesario es el ciclo de la marcha humana, junto con sus fases.
Una vez entendido eso verás que hay 2 tipos de parámetros:
    Parámetros espacio-temporales
        Aquí los espacio-temporales que son algunos como longitud de paso, longitud de zancada, tiempo de paso, tiempo de doble apoyo, etc.
    Parámetros cinemáticos
        Para entender estos primero debes entender que el cuerpo está dividido en 3 planos: Sagital, transversal y frontal.
        Con esos planos se pueden obtener los parámetros cinemáticos (ángulos) de las diferentes articulaciones. Por ejemplo:
            - Flexion/extension de la rodilla
            - Abducción/aducción de la rodilla
            - Rotación interna/externa de la rodilla.



