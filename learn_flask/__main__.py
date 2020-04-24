from .app import create_app
from .iplink import createIpLinkShell


def main():
    app = create_app(createIpLinkShell)
    app.run()


if __name__ == '__main__':
    main()
