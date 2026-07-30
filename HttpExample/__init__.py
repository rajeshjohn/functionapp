import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'world')
    return func.HttpResponse(f"Hello, {name}! This came from Azure Functions.")