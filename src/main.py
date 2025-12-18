import uvicorn

from app.config import api_config_provider
from app.api import create_api


def main():
    config = api_config_provider()

    app = create_api(config)

    uvicorn.run(app, host=config.app_host, port=config.app_port)


if __name__ == "__main__":
    main()
