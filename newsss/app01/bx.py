import app01.zhenzismsclient as smsclient

api_url = "http://sms_developer.zhenzikj.com"
app_id = 100097
app_secret = "468b085c-24c7-4a25-a138-4e51b50c45ee"

client = smsclient.ZhenziSmsClient(api_url, app_id, app_secret)
result = client.send("13439492124", "你的验证码是1234")
