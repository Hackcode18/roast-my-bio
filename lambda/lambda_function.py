import json
import boto3

def lambda_handler(event, context):
    
    # Handle CORS preflight
    if event.get('requestContext', {}).get('http', {}).get('method') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': ''
        }
    
    try:
        body = json.loads(event['body'])
        bio = body['bio']
        
        if not bio or len(bio.strip()) < 10:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Bio is too short to roast!'})
            }
        
        client = boto3.client('bedrock-runtime', region_name='us-east-1')
        
        prompt = f"""You are a witty stand-up comedian. 
Roast this person's bio in exactly 3 funny sentences.
Be clever and playful, not cruel or offensive.
End with one backhanded compliment.
Bio: {bio}"""
        
        response = client.invoke_model(
            modelId='amazon.nova-lite-v1:0',
            body=json.dumps({
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 300,
                "inferenceConfig": {
                    "temperature": 0.9
                }
            })
        )
        
        result = json.loads(response['body'].read())
        roast = result['output']['message']['content'][0]['text']
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'roast': roast})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
