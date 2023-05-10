import base64
import json
import requests

def hello_pubsub(event, context):

    # Process pubsub message 
    print("###########################")
    print("# Hello Serverless World")
    print("###########################")
    
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    message_data = json.loads(pubsub_message)
    print(f"message_data: {message_data}")
    
    # Construct public URL 
    bucket_name = message_data.get('bucket', '')
    object_name = message_data.get('name', '')
    public_url = f"https://storage.googleapis.com/{bucket_name}/{object_name}"

    print(f"public_url: {public_url}")

    # Call microservice
    if public_url:
        response = requests.get(
            f"https://sentry-service-eekakz7xnq-as.a.run.app/detect?url={public_url}",
            timeout=10,
        )
        response.raise_for_status()
        print(f"##################################")
        print(f"# Results")
        print(f"##################################")
        print(f"Function called with URL: {public_url}")
        print(f"Microservice response: {response.text}")
    else:
        print("Media link not found in the message")
