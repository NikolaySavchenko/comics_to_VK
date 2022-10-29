from utils import get_comics
from utils import upload_photo_VK
from utils import save_photo_VK
from utils import get_url_for_upload_photo
from utils import publication_comics
from utils import get_group_detail
from pathlib import Path
from dotenv import load_dotenv
from random import randint
import os



def main():
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    Path('comics').mkdir(parents=True, exist_ok=True)
    comics_number = randint(1, 2889)
    comics = get_comics(comics_number)
    comics_image_name = comics[1]
    comics_comment = comics[0]
    vk_group_id = get_group_detail(vk_token)
    upload_photo_url = get_url_for_upload_photo(vk_token, vk_group_id)
    upload_details = upload_photo_VK(Path(f'comics/{comics_image_name}'), upload_photo_url)
    saving_photo_details = save_photo_VK(vk_token, upload_details, vk_group_id)
    publication_comics(vk_token, saving_photo_details['response'][0]['id'],
                       saving_photo_details['response'][0]['owner_id'], comics_comment, vk_group_id)
    os.remove(f'comics/{comics_image_name}')


if __name__ == '__main__':
    main()
