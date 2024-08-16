import requests

TOKEN = 'silicek ve değişecek token' 
VANITY_URL = 'URL'
GUILD_ID = 'SW ID'
WEBHOOK_URL = 'WEBHOOK' # CONFİG KISMINI YANLIŞ YAPMA ALLAHINI XD

def main():
    api = DiscordAPI(TOKEN, WEBHOOK_URL)
    
    api.delete_vanity_url(VANITY_URL)
    
    api.update_guild_vanity_url(GUILD_ID, VANITY_URL)

class DiscordAPI:
    BASE_URL = "https://discord.com/api/v10"

    def __init__(self, token, webhook_url):
        self.token = token
        self.webhook_url = webhook_url
        self.headers = {"Authorization": token, "Content-Type": "application/json"}

    def send_webhook_message(self, message):
        response = requests.post(self.webhook_url, json={"content": message})
        if response.status_code != 204:
            print(f"Webhook error: {response.status_code} - {response.text}")

    def delete_vanity_url(self, vanity_url):
        url = f"{self.BASE_URL}/invites/{vanity_url}"
        response = requests.delete(url, headers=self.headers)
        
        if response.status_code == 204:
            log_message = f"Nighthawk URL Deleted : {vanity_url}"
            self.send_webhook_message(log_message)
        elif response.status_code == 200:
            response_data = response.json()
            if 'code' in response_data and response_data['code'] == vanity_url:
                log_message = f"Nighthawk URL Deleted : {vanity_url}"
                self.send_webhook_message(log_message)

    def update_guild_vanity_url(self, guild_id, vanity_url):
        url = f"{self.BASE_URL}/guilds/{guild_id}/vanity-url"
        response = requests.patch(url, json={"code": vanity_url}, headers=self.headers)
        
        if response.status_code == 200:
            log_message = f"Nighthawk Server URL Updated : {vanity_url}"
            self.send_webhook_message(log_message)

if __name__ == "__main__":
    main()
