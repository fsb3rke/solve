import requests
web_content = requests.get("https://raw.githubusercontent.com/LuNiZz/davet/main/qrcode.png")
with open("https://raw.githubusercontent.com/LuNiZz/davet/main/qrcode.png".split("/")[-1], "wb") as f:
    f.write(web_content.content)