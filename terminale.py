import openai
import os
import platform

# verifica il sistema operativo
sistemaos = platform.system()

# inserisci la tua chiave API di OpenAI
openai.api_key = "API_KEY"

# funzione per la generazione di testo con GPT-3.5 turbo
def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content

while True:
    
    richiesta = input("Inserisci il comando da richiedere: ")

    # prompt per GPT-3.5 turbo
    prompt = f"Sei un AI che invia comandi su terminale in un sistema operativo {sistemaos}.\
    Visualizzi il comando richiesto come se fossi un terminale rispondendo solamente 'Comando:[COMANDO]'. Non aggiungere altri commenti.\
    Se sono richiesti comandi compatibili con nmap, usalo. Il comando richiesto è: {richiesta}, interpretalo nel modo corretto."

    response = BasicGeneration(prompt)

    # estrazione del comando
    comando = response.split("Comando:")[1]

    print(response)

    # esecuzione del comando
    os.system(comando)
    

