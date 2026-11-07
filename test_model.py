import tensorflow as tf
import numpy as np
import os

# Load trained model
model = tf.keras.models.load_model("../model/waste_classifier.keras")

class_names = ["Glass", "Metal", "Organic", "Paper", "Plastic"]

test_path = "dataset/test"

correct = 0
total = 0

print("\n===================================")
print("AI WASTE MODEL ACCURACY TEST")
print("===================================\n")

for actual_class in class_names:

    folder_path = os.path.join(test_path, actual_class)

    class_correct = 0
    class_total = 0

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        try:
            image = tf.keras.utils.load_img(
                file_path,
                target_size=(160, 160)
            )

            image_array = tf.keras.utils.img_to_array(image)
            image_array = np.expand_dims(image_array, axis=0)

            prediction = model.predict(image_array, verbose=0)

            predicted_index = np.argmax(prediction[0])
            predicted_class = class_names[predicted_index]

            total += 1
            class_total += 1

            if predicted_class == actual_class:
                correct += 1
                class_correct += 1
                result = "CORRECT"
            else:
                result = "WRONG"

            print(
                f"{actual_class:8} | "
                f"{file_name:25} | "
                f"Predicted: {predicted_class:8} | "
                f"{result}"
            )

        except Exception as e:
            print(f"Could not process {file_name}: {e}")

    class_accuracy = (class_correct / class_total) * 100

    print(
        f"\n{actual_class} Accuracy: "
        f"{class_correct}/{class_total} = "
        f"{class_accuracy:.2f}%\n"
    )

overall_accuracy = (correct / total) * 100

print("===================================")
print(f"Correct Predictions : {correct}/{total}")
print(f"Overall Accuracy    : {overall_accuracy:.2f}%")
print("===================================")