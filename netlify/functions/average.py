import json

def handler(event, context):
    if event.get("httpMethod") != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method Not Allowed"})
        }

    try:
        data = json.loads(event.get("body", "{}"))
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))

        # Your core logic
        total = num1 + num2
        avg = total / 2

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "num1": num1,
                "num2": num2,
                "total": total,
                "average": avg
            })
        }
    except (ValueError, TypeError):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Please enter valid numbers."})
        }
