import tensorflow as tf
import numpy as np

# Load the trained AI model
model = tf.keras.models.load_model("../model/waste_classifier.keras")

# Waste categories
class_names = ["Glass", "Metal", "Organic", "Paper", "Plastic"]

# Image to predict
image_path = input("Enter the image path: ")

# Load and prepare image
image = tf.keras.utils.load_img(
    image_path,
    target_size=(160, 160)
)

image_array = tf.keras.utils.img_to_array(image)
image_array = np.expand_dims(image_array, axis=0)

# Make prediction
prediction = model.predict(image_array, verbose=0)

# Get result
predicted_index = np.argmax(prediction[0])
predicted_class = class_names[predicted_index]
confidence = prediction[0][predicted_index] * 100

print("\n==============================")
print("AI SMART WASTE SEGREGATION")
print("==============================")
print("Predicted Waste :", predicted_class)
print("Confidence      :", f"{confidence:.2f}%")
print("==============================")