
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from keras.utils import plot_model


import numpy as np
from keras.preprocessing import image

classifier = Sequential()
model = load_model("idalyCatGenerator.h5")

# test_image = image.load_img('training_set/cats/cat.1700.jpg', target_size = (64, 64))
test_image = image.load_img('cats.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)

result = model.predict(test_image)

print result

# if result[0][0] == 1:
#     prediction = 'dog'
#     print("it's a dog!")
# else:
#     prediction = 'cat'
#     print("yup, it's a cat.")
