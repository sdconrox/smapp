import logging
import sys
import random
import string
import argparse
import os

import requests
from faker import Faker
from requests.exceptions import SSLError, ProxyError

# Get the value of an environment variable
pubproxy_api_key = os.getenv('PUBPROXY_API_KEY')

fake = Faker()

fake_emails = set()

# create logger
logger = logging.getLogger('smapp')
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler(stream=sys.stdout)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def random_pass():
    length = random.randint(8, 16)
    letters = string.ascii_lowercase
    fake_password = ''.join(random.choice(letters) for i in range(length))
    logger.debug(f'Generated random password: {fake_password}')
    return fake_password


def random_user_agent():
    user_agent_fakers = (
        fake.opera(),
        fake.firefox(),
        fake.safari(),
        fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899),
        fake.internet_explorer(),
        fake.user_agent()
    )
    fake_user_agent = random.choice(user_agent_fakers)
    logger.debug(f'Generated random user agent: {fake_user_agent}')
    return fake_user_agent


def random_email():
    email_fakers = (fake.free_email(),
                    fake.company_email(),
                    fake.ascii_free_email(),
                    fake.ascii_company_email(),
                    fake.ascii_safe_email(),
                    fake.ascii_email(),
                    fake.safe_email(),
                    fake.email()
                    )
    fake_email = random.choice(email_fakers)
    logger.debug(f'Generated random email: {fake_email}')
    return fake_email


def generate_smapp_data(data_count=10):
    fake_data = list()
    for _ in range(data_count):
        fake_email = random_email()
        fake_pass = random_pass()
        form_data = {'email': fake_email, 'password': fake_pass}
        logger.debug(f'Generated random data: {form_data}')
        fake_data.append(form_data)
    return fake_data


def get_proxy_list(iterator_range, list_limit):
    proxy_list = list()

    for _ in range(iterator_range):
        response = requests.get('http://pubproxy.com/api/proxy',
                                params={'api': pubproxy_api_key,
                                        'limit': list_limit,
                                        'post': True,
                                        'level': 'elite',
                                        'https': True})
        try:
            new_proxy_list = response.json()['data']
            proxy_list = proxy_list + new_proxy_list
            logger.info(f'Generated proxy list. Proxy count: {len(proxy_list)}')
        except ValueError as ve:
            logger.error(f'ValueError: {ve}')
            pass
    return proxy_list


def smapp_dat_ass(smapp_count: int, iterator_range, list_limit, url):
    random_proxies = get_proxy_list(iterator_range, list_limit)
    random_data = generate_smapp_data(smapp_count)

    for form_data in random_data:
        random_proxy = random.choice(random_proxies)
        logger.debug(f'Chose random Proxy: {random_proxy}')
        proxies = {'http': f"{random_proxy['ipPort']}",
                   'https': f"{random_proxy['ipPort']}"}

        logger.debug(f'Request Proxy: {proxies}')

        fake_user_agent = random_user_agent()
        logger.debug(f'Request User Agent: {fake_user_agent}')
        try:
            logger.info(f'Sending bogus data to {url}...')
            response = requests.post(url,
                                     data=form_data,
                                     headers={'user-agent': fake_user_agent},
                                     proxies=proxies)
            logger.info(f'Response received: {response.status_code}')
        except SSLError as ssle:
            logger.error(f'SSLError: {ssle}')
            pass
        except ProxyError as proxye:
            logger.error(f'ProxyError: {proxye}')
            pass
