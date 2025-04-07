import requests

def ask(prompt: str) -> str:
    url = "https://test1.diecoders.com/get.php"
    payload = {"prompt": prompt}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "No response found.")
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception: {str(e)}"
