import requests
    
def sendSms(num:str, message:str) -> requests.Response:
    from api.configs.config import Setting
    data = {
        "urns":
        ["tel:"+num]
        ,
        "text":message
    }
    resp = requests.post(Setting.SMS_SEND_ADDRESS, json=data, headers={
        "Authorization":"Token 5778602bfcb3efc863a33f803da0cee0db7af8b1"
    })
    return resp
