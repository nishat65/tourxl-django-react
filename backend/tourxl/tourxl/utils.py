def predefinedJsonRes(message, data, code=200):
    status = "success" if str(code).startswith("2") else "error"
    return {"message": message, "data": data, "status": status}
