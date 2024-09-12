import os
import requests
from bs4 import BeautifulSoup

# Create directories to save the images
cat_images_dir = 'cat_images'
non_cat_images_dir = 'non_cat_images'

if not os.path.exists(cat_images_dir):
    os.mkdir(cat_images_dir)

if not os.path.exists(non_cat_images_dir):
    os.mkdir(non_cat_images_dir)

# URLs of the websites containing images
cat_url = 'https://www.google.com/search?sca_esv=708ca891a389fdf3&sxsrf=ADLYWIIcaag6csYmYk0nvKv2YxBkpYeJkg:1726120309997&q=cats&udm=2&fbs=AEQNm0B8dVdIWR07uWWlg1TdKnNtA1cwMugrQsIKmAo5AEZHWRFlUeGLxYlhagMfUatSvHu3MSamP9Qd2SfjyZyVIdPFrZFmdorP0BQX-5QUvERZ7CgntLysKxPYR85LNkkQ-ODVQlzCBgHDwYGwBEtb1wyzIiqYOAGOFOhRLG73H-MUdJY1ZFjTgiSsk2gQgTHDHU_Mnn5ewYy4nGfZAENFgsXyYdMtYQ&sa=X&ved=2ahUKEwiK2qqf27yIAxUwzDgGHTlDCXYQtKgLegQIGRAB&biw=1920&bih=911'
non_cat_url = 'https://www.google.com/search?sca_esv=708ca891a389fdf3&sxsrf=ADLYWIIcaag6csYmYk0nvKv2YxBkpYeJkg:1726120309997&q=dogs&udm=2&fbs=AEQNm0B8dVdIWR07uWWlg1TdKnNtA1cwMugrQsIKmAo5AEZHWRFlUeGLxYlhagMfUatSvHu3MSamP9Qd2SfjyZyVIdPFrZFmdorP0BQX-5QUvERZ7CgntLysKxPYR85LNkkQ-ODVQlzCBgHDwYGwBEtb1wyzIiqYOAGOFOhRLG73H-MUdJY1ZFjTgiSsk2gQgTHDHU_Mnn5ewYy4nGfZAENFgsXyYdMtYQ&sa=X&ved=2ahUKEwiK2qqf27yIAxUwzDgGHTlDCXYQtKgLegQIGRAB&biw=1920&bih=911'

# Function to download images
def download_images(url, directory, keyword):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')
    count = 0

    for img in img_tags:
        img_url = img.get('src')

        if not img_url.startswith('http'):
            img_url = f'{url}/{img_url}'

        try:
            img_data = requests.get(img_url).content

            with open(f'{directory}/{keyword}_image_{count}.jpg', 'wb') as img_file:
                img_file.write(img_data)

            count += 1
            print(f'Downloaded {img_url}')
        except Exception as e:
            print(f'Failed to download {img_url}: {e}')

    print(f"Downloaded {count} {keyword} images!")

# Download cat images
download_images(cat_url, cat_images_dir, 'cat')

# Download non-cat images
download_images(non_cat_url, non_cat_images_dir, 'non_cat')
