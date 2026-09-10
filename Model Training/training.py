import tensorflow as tf

train_ds = tf.keras.utils.image_dataset_from_directory(
    "GTSRB/Train",
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(32, 32),
    batch_size=32,
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    "GTSRB/Train",
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(32, 32),
    batch_size=32,
)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(32, 32, 3)),
    tf.keras.layers.Rescaling(1. / 255),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(43, activation="softmax"),
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10,
)

model.save("gtsrb_model.keras")

