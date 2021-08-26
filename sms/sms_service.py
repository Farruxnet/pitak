from django.conf import settings
import requests
url = "https://notify.eskiz.uz/api/message/sms/send"
def sms_sender(phone_number, text):
    payload={
        'mobile_phone': phone_number,
        'message': text,
        'from': '4546',
        'callback_url': 'http://0000.uz/test.php'
    }
    files=[]
    headers = {
      'Authorization': 'Bearer {0}'.format(settings.SMS_TOKEN)
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    if response.json()['status'] == 'error':
        print('xato')
        print(response.json())
        return False
    else:
        print('okay')
        print(response.json())
        return True
