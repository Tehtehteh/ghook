import os

from aiohttp import web
from api import app


def main():
    web.run_app(app, port=int(os.environ.get('PORT')))


if __name__ == '__main__':
    main()
