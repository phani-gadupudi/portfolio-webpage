import json

CONTENT1 = """
<html>
<body>
    <p>IP:
"""

CONTENT2 = """
</p>
</body>
</html>
"""

def lambda_handler(event, context):
    print(event)
    #print(event["Records"][0].get("cf").get("request").get("clientIp"))
    #ip = event[Records[0]].cf.request.clientIp
    ip = event["Records"][0].get("cf").get("request").get("clientIp")
    CONTENT = CONTENT1 + ip + CONTENT2
    # Generate HTTP OK response using 200 status code with HTML body.
    response = {
        'status': '200',
        'statusDescription': 'OK',
        'headers': {
            'cache-control': [
                {
                    'key': 'Cache-Control',
                    'value': 'max-age=100'
                }
            ],
            "content-type": [
                {
                    'key': 'Content-Type',
                    'value': 'text/html'
                }
            ]
        },
        'body': CONTENT
    }
    return response
