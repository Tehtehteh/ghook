from aiohttp import web
from api import app


def main():
    web.run_app(app, port=8080)


if __name__ == '__main__':
    main()
