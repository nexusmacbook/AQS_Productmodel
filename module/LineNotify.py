import requests

line_notify_token = "6t4U06gBrJU8KkPvSZynkXPISsHrpJ6NEHhsaP0InDv"

def LINE(mess):
    # 送信したいメッセージ
    message = mess
    # Line Notifyを使った、送信部分
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'{message}'}
    requests.post(line_notify_api, headers=headers, data=data)