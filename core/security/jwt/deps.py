from fastapi.exceptions import HTTPException
from fastapi import Header
from typing import Any, Union
from .utils import get_payload
import re



class JwtAuthentication:
    def __init__(self) -> None:
        pass

    def __call__(self, Authorization: Union[str, None] = Header()) -> Any:
        find_token = re.match("^[B|b]earer\s(.+)$", Authorization)
        if not find_token:
            raise HTTPException(403, "Token not found")
        else:
            token = find_token.group(1)
            try:
                payload = get_payload(token)
                return payload
            except Exception:
                raise HTTPException(401, "Invalid access token")
            