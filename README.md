# 🧠 Real-Time Voice AI Assistant (Python + LLaMA 3)

A **real-time voice AI assistant** that listens to your spoken questions, reasons using a **local Large Language Model (LLaMA 3)**, and responds in natural voice — entirely offline and interactive.

---

## 🎯 Example Interaction

**User (voice):**  
> "What is Machine Learning?"

**Assistant (voice):**  
> "Machine Learning is a branch of artificial intelligence where systems learn from data and improve performance without explicit programming."

**✅ Key points:**  
- Fully **local**, no cloud API  
- Works **entirely through voice**

---

## ⚙️ System Workflow (Step by Step)

### 🎧 Voice Input
Captures user speech via microphone.

### 📝 Speech-to-Text
Converts audio into text using **SpeechRecognition**.

### 🧠 AI Reasoning (LLM)
Text is sent to **LLaMA 3 (Ollama)** running locally to generate an intelligent response.

### 🔊 Text-to-Speech
Converts AI text output into natural speech using **pyttsx3**.

### 🔁 Voice Output
Assistant speaks the response back in **real time**.

---

## 🛠 Technologies Used

- 🐍 **Python** – main programming language  
- 🎤 **SpeechRecognition** – voice to text  
- 🧠 **LLaMA 3 (Ollama)** – local large language model  
- 🔊 **pyttsx3** – text-to-speech engine  
- 💻 **PyCharm IDE** – optional  

---

## 💼 Real-World Applications

- 📞 Voice-based customer support  
- 🏫 AI-powered learning tutors  
- 🏥 Offline & privacy-focused AI assistants  
- 🏢 Enterprise internal AI tools  

---

## 🚀 Installation & Setup

### Step 1: Clone the repository
```bash
git clone https://github.com/SwethaSivakumar2590/voice-ai-assistant.git
cd voice-ai-assistant

### Step 2: Install dependencies
pip install -r requirements.txt

### Step 3: Install Ollama & pull LLaMA 3 model
# Install Ollama app from https://ollama.com
ollama pull llama3

### Step 4: Run the assistant
python voice_assistant.py


