🦖 Chrome Dino AI (NEAT + Python)

A clone of the Google Chrome Dino game powered by artificial intelligence that learns to play automatically using neuroevolution (NEAT).

Un clon del juego del dinosaurio de Google Chrome con inteligencia artificial que aprende automáticamente usando neuroevolución (NEAT).

🚀 Demo / Demo

The AI controls the dinosaur and improves over generations.

La IA controla el dinosaurio y mejora generación tras generación.

🧠 How it works / Cómo funciona

This project uses:

Este proyecto usa:

🧬 NEAT (NeuroEvolution of Augmenting Topologies)
Evolves neural networks without supervised learning.
Evoluciona redes neuronales sin aprendizaje supervisado.
🎮 Pygame
2D game engine for simulation.
Motor 2D para la simulación del juego.
📊 Fitness system
Rewards survival and penalizes crashes.
Recompensa la supervivencia y penaliza choques.
🎯 Goal / Objetivo

Train an AI that can:

Entrenar una IA capaz de:

Learn to jump over obstacles
Aprender a saltar obstáculos
Improve over generations
Mejorar generación tras generación
Survive as long as possible
Sobrevivir el mayor tiempo posible
🕹️ Controls / Controles

In play.py (optional manual mode):

En play.py (modo manual opcional):

SPACE → Jump / Saltar
📦 Installation / Instalación
1. Clone repository / Clonar repositorio
git clone https://github.com/yourusername/chrome-dino-ai.git
cd chrome-dino-ai
2. Install dependencies / Instalar dependencias
pip install pygame neat-python
⚠️ Python version / Versión de Python

Recommended:

Recomendado:

Python 3.10 – 3.12

⚠️ Python 3.13+ may cause issues
⚠️ Python 3.13+ puede dar problemas

▶️ How to run / Cómo ejecutar
🧬 Train AI / Entrenar IA
python train.py
🧠 Run trained AI / Ejecutar IA entrenada
python play.py
💾 Model saving / Guardado del modelo

Best model is saved as:

El mejor modelo se guarda como:

best_dino.pkl

Contains the trained neural network.

Contiene la red neuronal entrenada.

⚙️ Configuration / Configuración

Edit:

Editar:

config-feedforward.txt

You can modify:

Puedes modificar:

population size / tamaño de población
mutation rate / tasa de mutación
activation functions / funciones de activación
evolution speed / velocidad de evolución
📈 How learning works / Cómo aprende

The AI improves through:

La IA mejora mediante:

survival time / tiempo de supervivencia
crash penalties / penalización por choque
genetic evolution / evolución genética
🧱 Project structure / Estructura del proyecto
chrome-dino-ai/
│
├── game.py                 # Game logic / lógica del juego
├── train.py                # Training script / entrenamiento
├── play.py                 # Run AI / ejecutar IA
├── config-feedforward.txt  # NEAT config / configuración NEAT
├── best_dino.pkl          # Trained model / modelo entrenado
└── README.md
🧠 Technologies / Tecnologías
Python 🐍
Pygame 🎮
NEAT-Python 🧬
🚀 Future improvements / Mejoras futuras
Pixel-perfect Chrome Dino sprites
Sprites exactos del Dino de Chrome
CNN vision-based AI
IA basada en visión por píxeles
Day/night cycle
Ciclo día/noche
Clouds and parallax background
Nubes y fondo con parallax
Leaderboards
Rankings de mejores modelos
Faster training mode
Entrenamiento más rápido sin render
⚠️ Known issues / Problemas conocidos
New Python versions may break compatibility
Versiones nuevas de Python pueden dar problemas
High population may reduce performance
Poblaciones altas pueden afectar rendimiento
