from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import json
import pickle
import numpy as np
import nltk
import nltk
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from keras.models import load_model

app = Flask(__name__)
CORS(app)  # Habilitar CORS para toda la aplicación

# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('wordnet')

# Cargar el lematizador, dataset de intenciones, palabras y clases entrenadas, y el modelo
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('./Back/Dataset.json', 'r', encoding='utf-8').read())
words = pickle.load(open('./Back/words.pkl', 'rb'))
classes = pickle.load(open('./Back/classes.pkl', 'rb'))
model = load_model('./Back/chatbotejemplo.h5')

class ChatbotAgent:
    def __init__(self, name="Bot"):
        self.name = name

    # Preprocesa la entrada del usuario
    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        return [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

    # Convierte una frase en un vector binario (bag of words)
    def bag_of_words(self, sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(words)
        for w in sentence_words:
            for i, word in enumerate(words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)

    # Predice la intención utilizando el modelo entrenado
    def predict_class(self, sentence):
        bow = self.bag_of_words(sentence)
        res = model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.3 # Ajusta este valor para filtrar mejor las intenciones
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
        return return_list

    # Encuentra la intención con la mayor similitud a la entrada del usuario
    def find_best_intent(self, preprocessed_message, intents):
        best_intent = None
        best_similarity = 0
        for intent in intents:
            patterns = intent['patterns']
            for pattern in patterns:
                preprocessed_pattern = self.clean_up_sentence(pattern)
                preprocessed_message_bow = self.bag_of_words(" ".join(preprocessed_message))
                preprocessed_pattern_bow = self.bag_of_words(" ".join(preprocessed_pattern))
                
                # Calcula la similitud de coseno
                similarity = cosine_similarity([preprocessed_message_bow], [preprocessed_pattern_bow])[0][0]
                if similarity > best_similarity:
                    best_intent = intent
                    best_similarity = similarity
        return best_intent

    # Genera una respuesta basándose en la intención con la mayor similitud y un umbral de similitud
    def generate_response(self, preprocessed_message, intents, similarity_threshold=0.3):
        best_intent = self.find_best_intent(preprocessed_message, intents)
        if best_intent and cosine_similarity(
            [self.bag_of_words(" ".join(preprocessed_message))],
            [self.bag_of_words(" ".join(self.clean_up_sentence(best_intent['patterns'][0])))]
        )[0][0] >= similarity_threshold:
            return random.choice(best_intent['responses'])
        else:
            return "Lo siento, no entendí completamente tu pregunta. ¿Podrías reformularla de otra manera?"

# Instancia del agente
chatbot_agent = ChatbotAgent(name="Bot")

@app.route('/chat', methods=['POST'])
def hello():
    user_input = request.json.get('message')
    
    if not user_input:
        return jsonify({'error': 'Mensaje no proporcionado'}), 400
    
    # Preprocesamos el mensaje usando el agente
    preprocessed_message = chatbot_agent.clean_up_sentence(user_input)
    
    # Generamos la respuesta utilizando el agente
    response = chatbot_agent.generate_response(preprocessed_message, intents['intents'])
    
    return jsonify({'response': response}), 200

if __name__ == '__main__':
    app.run(debug=True)


