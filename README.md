
# **🤖 ChatBot Grafen - Tu Guía Interactiva SENA**
<div align="center"> <img src="https://www.sena.edu.co/es-co/PublishingImages/logo-sena.png" width="200" alt="Logo SENA"> <br> <img src="https://img.shields.io/badge/Estado-En%20Producción-brightgreen" alt="Estado"> <img src="https://img.shields.io/badge/Versión-1.0.0-blue" alt="Versión"> <img src="https://img.shields.io/badge/Licencia-MIT-orange" alt="Licencia"> </div>
✨ ¿Qué ofrece este chatbot?
Función	Descripción	Icono
📋 Guía documental	Te explica paso a paso qué documentos necesitas	📄
⏰ Recordatorios	Alertas para entregas importantes	🔔
❓ FAQ inteligente	Resuelve 80% de dudas frecuentes	💡
👨‍🏫 Conexión humana	Cuando el bot no sabe, te contacta con tu instructor	👥
python
# Ejemplo de interacción
bot.responder("¿Cómo lleno el formato de seguimiento?")
>>> "Te guiaré paso a paso. Primero necesitas descargar el formato de..."
🚀 Tecnologías Clave
<div align="center"> <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" alt="Python"> <img src="https://img.shields.io/badge/FastAPI-0.68-green?logo=fastapi" alt="FastAPI"> <img src="https://img.shields.io/badge/NLTK-3.6.1-lightgrey?logo=nltk" alt="NLTK"> </div>
📂 Estructura del Proyecto
bash
chatbot-grafen/
├── 📁 Back/          # Lógica principal
│   ├── brain.py     # Procesamiento NLP
│   └── api.py       # Endpoints REST
├── 📁 Front/         # Interfaz web
│   ├── index.html   # Chat interactivo
│   └── styles.css   # Diseño responsive
├── 📜 dataset.txt    # 150+ preguntas entrenadas
└── 📄 docs/          # Manuales completos
⚡ ¡Pruébalo ahora!
Bot en Vivo

bash
# Para desarrolladores:
git clone https://github.com/Yelder25/chatbot-grafen
cd chatbot-grafen/Back
pip install -r requirements.txt
python api.py
📊 Evolución del Proyecto
Diagram
Code
gantt
    title Roadmap 2024
    dateFormat  YYYY-MM-DD
    section Fase 1
    Entrenamiento NLP       :done, 2024-01-01, 30d
    Integración con SENA    :active, 2024-02-01, 20d
    section Fase 2
    Módulo de recordatorios :2024-03-01, 15d
    App móvil              :2024-04-01, 30d
💡 ¿Cómo contribuir?
🍴 Haz fork del proyecto

🌿 Crea una rama: git checkout -b mejora/descripcion-breve

💾 Guarda tus cambios: git commit -m "feat: añade X funcionalidad"

🚀 Sube los cambios: git push origin mejora/descripcion-breve

🔄 Abre un Pull Request

<div align="center"> <h3>📬 ¿Necesitas ayuda?</h3> <a href="mailto:contacto@ejemplo.com"> <img src="https://img.shields.io/badge/Contacto-Email-red" alt="Email"> </a> <a href="https://t.me/usuario"> <img src="https://img.shields.io/badge/Soporte-Telegram-blue" alt="Telegram"> </a> </div>
<div align="center"> <sub>Creado con ❤️ por <a href="https://github.com/Yelder25">Yelder25</a></sub> | <sub>Última actualización: <b>6 horas atrás</b> (commit df6a82a)</sub> </div>
