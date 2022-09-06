from fastapi import FastAPI
from starlette.types import ASGIApp
from starlette.staticfiles import StaticFiles


class Application:
    app: FastAPI

    @classmethod
    def get_application_instance(cls) -> ASGIApp:
        return cls.app

    @classmethod
    def load_app(cls, **kwargs) -> ASGIApp:
        cls.app = FastAPI(debug=kwargs.get("debug"))
        cls.load_router(routers=kwargs.get("routers"))
        if kwargs.get("static_dir") is not None and kwargs.get("static_path") is not None:
            cls.load_static_route(dir=kwargs.get("static_dir"), path=kwargs.get("static_path"))

        return cls.app

    @classmethod
    def load_router(cls, *, routers) -> None:
        cls.app.include_router(routers)

    @classmethod
    def load_static_route(cls, *, dir, path) -> None:
        cls.app.mount(path=path, app=StaticFiles(directory=dir), name="static")
        pass
