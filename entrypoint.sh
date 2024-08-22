#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve llama3-groq-tool-use model..."
ollama pull llama3-groq-tool-use
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid