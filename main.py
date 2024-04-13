import requests as rq
import logging

#logger = logging.getLogger('RequestsLogger')
logging.basicConfig(level=logging.INFO)


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

#Создаем объекты логгирования
success_log = logging.getLogger('SuccessLog')
success_log.setLevel(logging.INFO)
success_handler = logging.FileHandler('success_responses.log')
success_handler.setLevel(logging.INFO)
success_formatter = logging.Formatter('%(levelname)s: %(message)s')
success_handler.setFormatter(success_formatter)
success_log.addHandler(success_handler)

bad_log = logging.getLogger('BadLog')
bad_log.setLevel(logging.INFO)
bad_handler = logging.FileHandler('bad_responses.log')
bad_handler.setLevel(logging.INFO)
bad_formatter = logging.Formatter('%(levelname)s: %(message)s')
bad_handler.setFormatter(success_formatter)
bad_log.addHandler(bad_handler)

blocked_log = logging.getLogger('BlockedLog')
blocked_log.setLevel(logging.INFO)
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_handler.setLevel(logging.INFO)
blocked_formatter = logging.Formatter('%(levelname)s: %(message)s')
blocked_handler.setFormatter(blocked_formatter)
blocked_log.addHandler(blocked_handler)

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            success_log.info(f'{site}, response - {response.status_code}')
        elif response.status_code == 403 or response.status_code == 503:
            bad_log.warning(f'{site}, response - {response.status_code}')
        else:
            blocked_log.error(f"{site}, NO CONNECTION")
    except rq.exceptions.RequestException as e:
        blocked_log.error(f"{site}, NO CONNECTION")

