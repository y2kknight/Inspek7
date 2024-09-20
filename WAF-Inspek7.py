import requests
# requests module allows me to send HTTP requests

ascii_art = r"""
 ___                              __   _________ 
|   | ____   ____________   ____ |  | _\______  \
|   |/    \ /  ___/\____ \_/ __ \|  |/ /   /    /
|   |   |  \\___ \ |  |_> >  ___/|    <   /    / 
|___|___|  /____  >|   __/ \___  >__|_ \ /____/  
         \/     \/ |__|        \/     \/         """

print(ascii_art)


# Defining the function, (url) is a parameter
def check_cloudflare_waf(url):
      
    try:

        # sends get request
        response = requests.get(url)
        headers = response.headers 

        if "server" in headers and "cloudflare" in headers["server"].lower():
            print("Cloudflare WAF detected.")

        else: 
        
            print("Cloudfare WAF not detected.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
website_url = input("Enter a URL: ")

check_cloudflare_waf(website_url)