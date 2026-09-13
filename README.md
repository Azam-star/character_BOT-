# 🦾 Character BOT — Tony Stark Q&A

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,50:172554,100:7a0000&height=230&section=header&text=TONY%20STARK%20Q%20and%20A&fontSize=46&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=An%20AI%20Character%20Chatbot%20Powered%20by%20Ollama&descAlignY=60"/>

<br>

<img src="https://img.icons8.com/fluency/96/iron-man.png" width="90"/>

### 💬 Talk to Tony Stark. Think like an engineer. Build like a Stark.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge)
![Gemma](https://img.shields.io/badge/Gemma-3-blue?style=for-the-badge)

</div>

---

## ⚡ Overview

**Character BOT** is an interactive AI chatbot that recreates the personality and conversational style of **Tony Stark — Iron Man**.

Built with **Streamlit** and powered by **Ollama**, the application runs a Large Language Model locally while using a custom system prompt to shape the AI into a witty, sarcastic, confident, technically capable character.

The interface is designed around a **Stark-inspired technology aesthetic**, combining dark gradients, reactor-inspired controls, Iron Man avatars, animated typing indicators, and customizable AI creativity.

> **No generic assistant responses. No boring conversations. Just Stark. 🦾**

---

## ✨ Features

### 🦾 Tony Stark Personality

The chatbot is configured with a custom system persona designed to make responses:

* 🧠 Intelligent
* 😏 Witty
* 🗣️ Fast-paced
* 😎 Confident
* 🔥 Slightly sarcastic
* 💻 Technically accurate

The personality is instructed to stay in character while still providing useful technical answers.

---

### 🎨 Stark Nano UI

The application includes a custom interface inspired by Stark technology:

* 🌌 Dark futuristic background
* 🔵 Arc-reactor-inspired user styling
* 🟡 Stark gold accents
* 🔴 Red/gold assistant styling
* ✨ Glowing title effects
* 🎭 Iron Man avatars
* ⚡ Custom animated elements

---

### 💭 Animated Thinking Indicator

Instead of immediately displaying the response, the chatbot shows animated **Stark typing dots** while the model generates its response.

```text
●  ●  ●
```

This creates a more natural conversational experience.

---

### 🎛️ Reactor Output Control

The sidebar contains a **Reactor Output** slider that controls the model's temperature.

```text
0.0 ─────────────── 1.5
        ▲
      0.6
```

Lower values produce more predictable responses, while higher values allow more creativity and variation.

---

### 🧠 Session Memory

The application maintains the current conversation using Streamlit session state.

This allows the chatbot to use previous messages as context during the conversation.

---

### 🧹 Clear Chat

A dedicated **Clear Chat** button resets the conversation while preserving the core Tony Stark personality.

After clearing the conversation, Stark responds:

> "Memory wiped. Try not to break anything this time, kid."

---

### 🔒 Local AI Execution

The application communicates with **Ollama**, allowing the selected language model to run locally.

This means the chatbot can operate without sending conversations to a traditional cloud chatbot service.

---

## 🏗️ Architecture

```text
                    👤 USER
                       │
                       ▼
              ┌─────────────────┐
              │   Streamlit UI  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Chat History   │
              │ Session State   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Tony Stark      │
              │ System Persona  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     Ollama      │
              │  Local LLM      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Gemma 3 Model  │
              └────────┬────────┘
                       │
                       ▼
                🤖 STARK REPLY
```

---

## 🧰 Tech Stack

| Technology           | Purpose                 |
| -------------------- | ------------------------ |
| 🐍 **Python**        | Application development |
| 🎈 **Streamlit**     | Web interface           |
| 🦙 **Ollama**        | Local LLM execution     |
| 🧠 **Gemma 3**       | Language model          |
| 🎨 **Custom CSS**    | Stark-themed UI         |
| 💾 **Session State** | Conversation memory     |

The current implementation imports `streamlit` and `ollama`, uses `gemma3:latest` as the default model, and passes the conversation history plus temperature setting to Ollama.

---

## 📁 Project Structure

```text
character_BOT-/
│
├── 📄 character_bot.py
└── 📄 README.md
```

### `character_bot.py`

The main Streamlit application containing:

* UI styling
* Tony Stark system prompt
* Chat interface
* Session memory
* Ollama integration
* Temperature control
* Clear-chat functionality
* Animated typing indicator

### `reactor.png`

Used as the reactor-themed sidebar asset.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Azam-star/character_BOT-.git
```

```bash
cd character_BOT-
```

---

## 2. Install Python Dependencies

```bash
pip install streamlit ollama
```

---

## 3. Install Ollama

Install Ollama on your system and make sure the Ollama application/service is running.

Then download the model used by the project:

```bash
ollama pull gemma3:latest
```

---

## 4. Run the Application

Start Streamlit:

```bash
streamlit run character_bot.py
```

The application will open in your browser.

---

# 🎛️ Configuration

The default model is:

```python
model = "gemma3:latest"
```

You can change it to another Ollama-supported model installed on your system.

For example:

```python
model = "llama3"
```

or:

```python
model = "mistral"
```

The chatbot temperature can also be adjusted through the **Reactor Output** slider.

---

# 🧠 Character Design

The personality is defined through a custom system prompt.

### Tony Stark is instructed to:

```text
• Be witty and sarcastic
• Maintain billionaire-level confidence
• Give technically accurate answers
• Use punchy responses
• Occasionally call the user "kid", "buddy", or "cap"
• Avoid sounding like a generic AI assistant
• Stay in character
```

This demonstrates how **prompt engineering** can be used to create a specialized AI character on top of a general-purpose language model.

---

# 🔄 Conversation Flow

```text
User enters message
        │
        ▼
Message added to session state
        │
        ▼
Streamlit displays user message
        │
        ▼
Stark typing animation appears
        │
        ▼
Conversation sent to Ollama
        │
        ▼
Gemma 3 generates response
        │
        ▼
Typing animation replaced
        │
        ▼
Tony Stark response displayed
        │
        ▼
Response saved to session memory
```

---

# 🎯 What This Project Demonstrates

This project is more than a chatbot UI.

It demonstrates practical concepts including:

* 🤖 Generative AI
* 🧠 Large Language Models
* ✍️ Prompt Engineering
* 🎭 AI Persona Design
* 🐍 Python development
* 🎈 Streamlit application development
* 🦙 Local LLM deployment with Ollama
* 💾 Conversational state management
* 🎨 Custom frontend styling

---

# 🔮 Future Improvements

Possible upgrades for the next version:

* [ ] 🎭 Multiple AI characters
* [ ] 👤 Character selection screen
* [ ] 🧠 Persistent long-term memory
* [ ] 💾 Save conversation history
* [ ] 🎙️ Voice input
* [ ] 🔊 Text-to-speech responses
* [ ] 🖼️ Custom character avatars
* [ ] 🌐 Multi-language conversations
* [ ] ⚙️ Dynamic model selection
* [ ] 📱 Improved mobile interface
* [ ] 🔐 User authentication
* [ ] 📊 Conversation analytics
* [ ] ✨ Streaming token-by-token responses

---

# 🧪 Example

### 👤 User

```text
Explain artificial intelligence in simple terms.
```

### 🦾 Tony Stark

```text
Think of AI as a really fast intern who never sleeps,
reads way too much, and occasionally needs supervision.

You give it data, it finds patterns, and then it uses
those patterns to make predictions or decisions.

Basically: teach the machine, hope it doesn't become Skynet.
```

---

# 🛡️ Troubleshooting

### ❌ Ollama Connection Error

Make sure Ollama is installed and running before launching Streamlit.

Check whether the model is available:

```bash
ollama list
```

If `gemma3:latest` isn't available:

```bash
ollama pull gemma3:latest
```

---

### ❌ Reactor Image Not Showing

The application expects:

```text
reactor.png
```

in the project directory.

If the image is missing, the chatbot can still function, but the sidebar reactor image will not appear.

---

# 🌟 Why I Built This

I built **Character BOT** as an exploration of how Large Language Models can be combined with **personality, prompt engineering, and interactive interfaces** to create more engaging AI experiences.

The project combines my interest in:

**Artificial Intelligence + Python + UI Design + Generative AI**

into a practical conversational application.

---

# 👨‍💻 Author

<div align="center">

## Shaik Abdullah Azam

**B.Tech Artificial Intelligence Student**

AI • Python • Generative AI • Machine Learning • Development

<br>

<a href="https://github.com/Azam-star">
<img src="https://img.shields.io/badge/GitHub-Azam--star-181717?style=for-the-badge&logo=github"/>
</a>

</div>

---

# ⭐ Support

If you found this project interesting:

⭐ **Star this repository**

🍴 **Fork it**

🐛 **Report issues**

💡 **Suggest improvements**

---

<div align="center">

### 🦾 "Sometimes you gotta run before you can walk."

**Built with Python • Streamlit • Ollama • Gemma 3**

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7a0000,50:b8860b,100:020617&height=120&section=footer"/>

</div>
