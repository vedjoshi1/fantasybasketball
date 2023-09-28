import pandas as pd
import tensorflow as tf

def trainPoints(pointsDB, unfilteredData):
    y = pointsDB
    X = unfilteredData



    model = tf.keras.Sequential([
        tf.keras.layers.Dense(15, activation='relu', input_shape=(X.shape[1],)),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(1)  # Output layer for regression
    ])

    # Step 4: Compile the Model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Step 5: Train the Model
    model.fit(X, y, epochs=10, batch_size=32)

    print(model)