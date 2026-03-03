import requests
import subprocess

chat_history = []

def response(user_input, api_key="YOUR_API_KEY"):
    global chat_history
    chat_history.append(f"User: {user_input}")

    prompt = (
        "You are an AI that generates command-line instructions based on user queries. "
        "Your responses should be clear and brief, using small words, but cover the answer completely.\n\n"
        + "\n".join(chat_history)
        + "\nAI:"
    )

    payload = {
        "model": "command",
        "prompt": prompt,
        "max_tokens": 500
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    r = requests.post("https://api.cohere.ai/v2/generate", json=payload, headers=headers)

    if r.status_code == 200:
        data = r.json()
        ai_text = data.get("generations", [{}])[0].get("text", "").strip()
        chat_history.append(f"AI: {ai_text}")
        return ai_text
    else:
        return f"Error {r.status_code}: {r.text}"

def main():
    print(" SEA Shell")

    while True:
        cmd = input("<< ")
        if cmd.startswith("~"):
                result = subprocess.run(cmd.replace("~","",1), shell=True,capture_output=True, text=True)
                print("<<")
                print(result.stdout)
        else:
            if cmd.lower() in ["exit", "quit"]:
                print(">> Goodbye.")
                break
            res = response(cmd)
            print(">> " + res)

main()