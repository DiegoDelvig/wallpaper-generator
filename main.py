import requests
import string
import os
import random


def get_random_wallpaper(query: str = '', page: int = 1, nsfw: bool = False) -> str:
    if nsfw:
        purity = 111
    else:
        purity = 100

    url = f"https://wallhaven.cc/api/v1/search?q={query}&page={page}&purity={purity}&category=100"
    

    wallpapers_path = "/home/pavel/Images/wallpapers/"
    
    res = requests.get(url)
    json_data = res.json()
    wallpapers = []
    
    for data in json_data["data"]:
        wallpaper_path = data["path"]
        wallpapers.append(wallpaper_path)
    
    return random.choice(wallpapers)


def generate_id(length: int) -> str:
    id = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return f"wallpaper-{id}"


def download_wallpaper(wallpaper_link: str, filename: str):
    img_data = requests.get(wallpaper_link).content
    
    with open(f'wallpapers/{filename}.jpg', 'wb') as handler: 
        handler.write(img_data)


if __name__ == "__main__":
    wallpaper_link = get_random_wallpaper(page=random.randint(1, 3), nsfw=False)

    filename = generate_id(6)
    download_wallpaper(wallpaper_link, filename)
    random.choice(os.listdir('/home/pavel/prog/wallpaper-generator/wallpapers'))
    os.system(f"gsettings set org.gnome.desktop.background picture-uri 'file:///home/pavel/prog/wallpaper-generator/wallpapers/{filename}.jpg'")

















