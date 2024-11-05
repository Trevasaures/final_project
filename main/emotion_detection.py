import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the request to the server and set a timeout error if no response is received within 10 seconds
    response = requests.post(url, headers=headers, json=input_json, timeout=10)

    # Check for responses from the server 
    if response.status_code == 200:
        return response.json().get("text")
    else:
        print("Error:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    text = "I love this new technology :)"
    result = emotion_detector(text)
    print(result)

