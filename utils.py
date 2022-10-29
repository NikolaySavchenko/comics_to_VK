import requests
from pathlib import Path


def get_image(image_url):
    Path('comics').mkdir(parents=True, exist_ok=True)
    response = requests.get(image_url)
    response.raise_for_status()
    file_name = (image_url.split('/'))[-1]
    with open(Path(f'comics/{file_name}'), 'wb') as file:
        file.write(response.content)
    return file_name


def get_comics(comics_number):
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comics_details = response.json()
    image_name = get_image(comics_details['img'])
    return comics_details['alt'], image_name


def get_url_for_upload_photo(token):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    payload = {'group_id': '216696628', 'access_token': token,
               'extended': '1', 'v': '5.131'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    vk_groups = response.json()
    return vk_groups['response']['upload_url']


def upload_photo_VK(file_path, upload_url):
    with open(file_path, 'rb') as file:
        files = {'photo': file, }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
    return response.json()


def save_photo_VK(token, upload_ansver):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    payload = {'group_id': '216696628', 'access_token': token,
               'extended': '1', 'v': '5.131'}
    payload.update(upload_ansver)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def publication_comics(token, media_id, owner_id, message):
    url = 'https://api.vk.com/method/wall.post'
    payload = {'owner_id': '-216696628', 'access_token': token,
               'attachments': f'photo{owner_id}_{media_id}', 'message': message,
               'extended': '1', 'v': '5.131'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response
