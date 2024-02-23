<!-- https://docs.aws.amazon.com/machine-learning/latest/dg/types-of-ml-models.html
https://docs.aws.amazon.com/machine-learning/latest/dg/training-ml-models.html
https://datagen.tech/guides/data-training/model-training/



https://www.youtube.com/playlist?list=PLOU2XLYxmsILr3HQpqjLAUkIPa5EaZiui

https://www.tensorflow.org/guide



redes neuronales trabajan entre 0 y 1 -->

# Data models

After creating our first piece of code that implements the mediapipe model as a way to extract the landmarks from a human body, we knew that we had to do something with that, because there are several different important data points to analyze.

The first step we took was to create some videos for two reasons:

 - first we wanted to know if the data we are obtaining from our analysis was consistent, if we obtained diferent data each time we analyzed the same image, we would not reliably be able to trust the analisis that we would do after obtaining that data.
 - Second, recorfing videos alows us the posibility of analyzing different types of body movements in an isolated manner. We will go more in depth later on, but there are some key factors or key movements that we woud have to look for as a indicative of a certain illness.

## Data Extraction.

After recording the videos we decided that we should split our focus into two sides, the extraction of the data of the videos and the analysis of that data. We created new piece of code based on our previous work where we extract using mediapipe and the csv library the data for it's latter analisis.


## Data analisis.

Once we have the data we need, we can analyze it.

the first step we took is a look on the body planes that we already talked about before. 

https://copyprogramming.com/howto/translate-image-orientation-into-axial-sagittal-or-coronal-plane
https://teachmeanatomy.info/the-basics/anatomical-terminology/planes/
https://dicomiseasy.blogspot.com/2013/06/getting-oriented-using-image-plane.html
https://www.youtube.com/watch?v=TWdN9TTQis4
