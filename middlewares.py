from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # You can add custom pre-processing logic here
        print("Pre-processing request")

        response = await call_next(request)

        # You can add custom post-processing logic here
        print("Post-processing request")

        return response
```
