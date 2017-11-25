from aiohttp import web
from api import app


def main():
    web.run_app(app)


if __name__ == '__main__':
    main()
