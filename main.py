import os
from pathlib import Path
from random import randint

from dotenv import load_dotenv

from utils import get_comic
from utils import get_group_detail
from utils import get_url_for_upload_photo
from utils import publication_comics
from utils import save_photo_VK
from utils import upload_photo_VK

def main():
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    Path('comics').mkdir(parents=True, exist_ok=True)
    max_comic_number = 2689
    comic_number = randint(1, max_comic_number)
    try:
        comic_comment, comic_image_name = get_comic(comic_number)
        vk_group_id = get_group_detail(vk_token)
        upload_photo_url = get_url_for_upload_photo(vk_token, vk_group_id)
        upload_details = upload_photo_VK(Path(f'comics/{comic_image_name}'), upload_photo_url)
        saving_photo_details = save_photo_VK(vk_token, upload_details, vk_group_id)
        publication_comics(vk_token, saving_photo_details['response'][0]['id'],
                       saving_photo_details['response'][0]['owner_id'],
                       comic_comment, vk_group_id)
    finally: 
        os.remove(f'comics/{comic_image_name}')


if __name__ == '__main__':
    main()
