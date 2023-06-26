import requests

def generate_proxy():
    url = 'https://api.getproxylist.com/proxy'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        proxy = f"{data['ip']}:{data['port']}"
        return proxy
    else:
        return None

proxy = generate_proxy()
if proxy:
    print(f"Generated Proxy: {proxy}")
else:
    print("Failed to generate proxy.")
