import os
from pathlib import Path
from urllib import parse

import requests


def get_group_detail(token):
    url = 'https://api.vk.com/method/groups.get'
    payload = {'access_token': token, 'extended': '1', 'v': '5.131'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['response']['items'][0]['id']


def download_comic(comic_number):
    url = f'https://xkcd.com/{comic_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comic_details = response.json()
    response_image = requests.get(comic_details['img'])
    response_image.raise_for_status()
    url_parse = parse.urlsplit(comic_details['img'])
    image_name_dirty = os.path.split(url_parse.path)
    image_name = parse.unquote(image_name_dirty[-1])
    with open(Path(f'comics/{image_name}'), 'wb') as file:
        file.write(response_image.content)
    return comic_details['alt'], image_name


def get_url_for_upload_photo(token, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    payload = {'group_id': group_id, 'access_token': token,
               'extended': '1', 'v': '5.131'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    vk_groups = response.json()
    return vk_groups['response']['upload_url']


def upload_photo_vk(file_path, upload_url):
    with open(file_path, 'rb') as file:
        files = {'photo': file, }
        response = requests.post(upload_url, files=files)
    response.raise_for_status()
    return response.json()


def save_photo_vk(token, upl_hash, upl_photo, upl_server, group_id):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    payload = {'group_id': group_id, 'access_token': token,
               'hash': upl_hash, 'photo': upl_photo, 'server': upl_server,
               'extended': '1', 'v': '5.131'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def publish_comic(token, media_id, owner_id, message, group_id):
    url = 'https://api.vk.com/method/wall.post'
    payload = {'owner_id': f'-{group_id}', 'access_token': token,
               'attachments': f'photo{owner_id}_{media_id}',
               'message': message, 'extended': '1', 'v': '5.131'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response
