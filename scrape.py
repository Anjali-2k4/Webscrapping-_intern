import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

def download_zip_file(url, download_path):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    
    zip_links = soup.find_all('a', href=lambda href: href and href.endswith('.zip'))

    if zip_links:
        for zip_link in zip_links:
            zip_url = urljoin(url, zip_link['href'])  
            zip_name = os.path.basename(zip_url)

            
            os.makedirs(download_path, exist_ok=True)

        
            file_path = os.path.join(download_path, zip_name)
            with open(file_path, 'wb') as f:
                zip_response = requests.get(zip_url)
                f.write(zip_response.content)

            print(f"Zip file '{zip_name}' downloaded to: {file_path}")

        sys.exit()  

    else:
        print("No zip file links found on the website.")

if _name_ == "_main_":
    website_url = "https://nvd.nist.gov/vuln/data-feeds"  
    download_directory = "C:/Users/91949/Documents"
    download_zip_file(website_url, download_directory)