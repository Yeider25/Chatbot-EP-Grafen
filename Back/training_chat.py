import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
import random

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.optimizers.schedules import ExponentialDecay

# Descargar los recursos necesarios de nltk
nltk.download('punkt')
nltk.download('punkt_tab')

# Cargar los datos
datafile = open('./Dataset.json', 'r', encoding='utf-8').read()
intents = json.loads(datafile)

lemmatizer = WordNetLemmatizer()
words = []
classes = []
documents = []
ignore_words = ['?', '!']

# Procesar los patrones y etiquetas
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lematizar y limpiar palabras
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Guardar palabras y clases
pickle.dump(words, open('./words.pkl', 'wb'))
pickle.dump(classes, open('./classes.pkl', 'wb'))

# Crear entrenamiento
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in doc[0]]
    for word in words:
        bag.append(1) if word in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Mezclar los datos
random.shuffle(training)

# Separar en características (X) y etiquetas (y)
train_x = np.array([row[0] for row in training])
train_y = np.array([row[1] for row in training])

# Crear modelo
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Configurar optimizador
lr_schedule = ExponentialDecay(
    initial_learning_rate=0.01,
    decay_steps=10000,
    decay_rate=0.9
)
sgd = SGD(learning_rate=lr_schedule, momentum=0.9, nesterov=True)

model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Entrenar modelo
hist = model.fit(train_x, train_y, epochs=110, batch_size=5, verbose=1)

# Guardar el modelo
model.save('./chatbotejemplo.h5')

print('Modelo creado exitosamente')