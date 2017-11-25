import os
import sys
import logging

from aiohttp import web
from api import app

logging.getLogger().setLevel(0)
log = logging.getLogger('application')
log.setLevel(0)
formatter = logging.Formatter('[%(asctime)s] [%(pathname)s:%(lineno)d] %(levelname)8s: %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)


def main():
    logging.info('Starting application...')
    web.run_app(app, port=int(os.environ.get('PORT')))


if __name__ == '__main__':
    main()
