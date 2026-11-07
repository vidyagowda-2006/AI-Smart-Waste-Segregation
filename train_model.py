import tensorflow as tf
from tensorflow.keras import layers, models
import os

# ==========================================
# AI SMART WASTE SEGREGATION SYSTEM
# IMPROVED TRAINING
# ==========================================

IMAGE_SIZE = (160, 160)
BATCH_SIZE = 8
EPOCHS = 30
DATASET_PATH = "dataset/train"

# Load training data
train_data = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True,
    validation_split=0.2,
    subset="training",
    seed=123
)

# Load validation data
validation_data = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True,
    validation_split=0.2,
    subset="validation",
    seed=123
)

class_names = train_data.class_names

print("\nWaste Categories:")
print(class_names)

# Data augmentation
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.15),
    layers.RandomZoom(0.15)
])

AUTOTUNE = tf.data.AUTOTUNE

train_data = train_data.prefetch(buffer_size=AUTOTUNE)
validation_data = validation_data.prefetch(buffer_size=AUTOTUNE)

# Build model
model = models.Sequential([
    layers.Input(shape=(160, 160, 3)),
    data_augmentation,
    layers.Rescaling(1.0 / 255),

    layers.Conv2D(32, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(128, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),

    layers.Dense(128, activation="relu"),
    layers.Dropout(0.5),

    layers.Dense(len(class_names), activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

print("\nStarting improved AI model training...\n")

history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=EPOCHS
)

os.makedirs("../model", exist_ok=True)

model.save("../model/waste_classifier.keras")

print("\n===================================")
print("IMPROVED AI MODEL TRAINING COMPLETED!")
print("Model saved successfully.")
print("Location: model/waste_classifier.keras")
print("===================================")
