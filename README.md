

Tony Stark Q&A Session 🦾
An immersive, Streamlit-based chatbot interface that lets you converse with a digital recreation of Tony Stark (Iron Man). This project uses Ollama to run local Large Language Models (LLMs) with a custom system prompt to capture the genius, billionaire, playboy, and philanthropist's unique personality.

🛠️ Features
Stark Nano Theme: A custom-styled UI featuring a "Stark Tech" aesthetic, including radial gradients, arc reactor blue user bubbles, and gold/red assistant bubbles.

Animated UI: Custom CSS animations for "Stark typing dots" to simulate the AI thinking process.

Dynamic Personality: Powered by a system prompt that enforces Tony Stark's witty, sarcastic, and fast-talking persona.

Adjustable Reactor Output: A sidebar slider to control the model's temperature (creativity/randomness).

Local Execution: Uses the ollama Python library to keep conversations private and run models locally.

🚀 Getting Started
Prerequisites
Ollama: Download and install Ollama from ollama.com.

Model: Pull the required model (default is gemma3:latest):

Bash
ollama pull gemma3:latest
Installation
Clone the repository (or save the code to character_bot.py).

Install dependencies:

Bash
pip install streamlit ollama
Running the App
Launch the Stark interface using Streamlit:

Bash
streamlit run character_bot.py
⚙️ Configuration
Setting	Description
Model	Defaulted to gemma3:latest. Can be changed in the code to llama3, mistral, etc.
Reactor Output	Adjusts the temperature (0.0 to 1.5) to change how creative or precise Tony's responses are.
Clear Chat	Wipes the current session memory while maintaining the core Stark personality.
📝 System Persona
The AI is strictly instructed to:

Be concise, sharp, and slightly arrogant.

Use nicknames like "kid," "buddy," or "cap."

Avoid sounding like a generic assistant or Jarvis.

Prioritize technical accuracy while maintaining the "Stark" attitude.

🛡️ Troubleshooting
Connection Error: Ensure the Ollama desktop application is running in the background before starting the Streamlit app.

Missing Assets: The app looks for a local reactor.png in the sidebar. If not found, that specific icon will not render, but the chat will function normally
