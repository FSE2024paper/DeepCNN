model = Sequential()
model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), padding="same", activation = 'relu', kernel_initializer='glorot_uniform', input_shape=(28, 28 ,1) ))
model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), padding="same", activation = 'relu', kernel_initializer='glorot_uniform'))
model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), padding="same", activation = 'relu', kernel_initializer='glorot_uniform'))
model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
model.add(Flatten())
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.20))
model.add(Dense(num_classes, activation = 'softmax'))
model.compile(loss = keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])
history = model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs=epochs, batch_size=batch_size)