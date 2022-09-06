import uvicorn
from fastapi import FastAPI
from core.application import Application
from api import root_router

app = Application.load_app(
    routers=root_router
)


def main() -> None:
    uvicorn.run(app=app, host="0.0.0.0", port=9090)


if __name__ == "__main__":
    main()
