def lambda_handler(event, context):
    for record in event["Records"]:
        print(f"Mensagem recebida: {record['body']}")
    return {"status": "ok"}