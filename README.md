🧠 Real-Time Voice AI Assistant (Python + LLaMA 3)

A real-time voice-based AI assistant that listens to your spoken questions, understands them using a local Large Language Model (LLaMA 3), and responds back in natural voice — all in real time.

This project demonstrates the full AI pipeline from voice input → LLM reasoning → voice output.

🎯 Example Interaction

User (voice):

"What is Machine Learning?"

Assistant (voice):

"Machine Learning is a branch of artificial intelligence where systems learn from data and improve performance without being explicitly programmed."

✅ Fully local, no cloud APIs used.
✅ Works entirely through voice.

⚙️ How It Works — Step by Step

🎧 Voice Input
Captures your speech through the microphone.

📝 Speech-to-Text
Converts audio into text using the SpeechRecognition library.

🧠 AI Reasoning (LLM)
Sends the text to LLaMA 3 running locally via Ollama for intelligent response generation.

🔊 Text-to-Speech
Converts the AI-generated response into natural voice using pyttsx3.

🔁 Voice Output
Speaks the response back to the user in real time.

🛠 Technologies Used

🐍 Python

🎤 SpeechRecognition – convert voice → text

🧠 LLaMA 3 (Ollama) – local large language model

🔊 pyttsx3 – text-to-speech engine

💻 Optional: PyCharm IDE

💼 Potential Applications

📞 Voice-based customer support assistants

🏫 AI-powered learning tutors

🏥 Privacy-focused offline AI assistants

🏢 Enterprise internal AI tools

🚀 Installation & Setup

1️⃣ Clone the repo

git clone https://github.com/SwethaSivakumar2590/voice-ai-assistant.git
cd voice-ai-assistant


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Install Ollama & pull LLaMA 3 model

# Install Ollama app from https://ollama.com
ollama pull llama3


4️⃣ Run the assistant

python voice_assistant.py


🎙 Speak into the microphone when prompted.

📌 Notes / Tips

Requires a working microphone

Ensure LLaMA 3 model is pulled locally

.venv or other virtual environment should not be pushed to GitHub

Adjust microphone sensitivity if the assistant doesn’t hear you

🔖 Project Structure
voice-ai-assistant/
│
├── voice_assistant.py        # Main script
├── requirements.txt          # Required Python libraries
├── README.md                 # Project documentation
└── .gitignore                # Ignore virtual environments & cache

🙋 Author

Swetha Sivakumar
Actively seeking AI / Machine Learning internship & entry-level opportunities.
Open to professional connections, mentorship, and collaborative projects.

📚 References / Resources

LLaMA 3 Model

Python SpeechRecognition

pyttsx3 Documentation

🏷 GitHub Topics / Tags

Python AI MachineLearning VoiceAssistant LLM SpeechRecognition TextToSpeech Ollama AppliedAI AIProjects
