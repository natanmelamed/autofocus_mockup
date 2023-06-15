import uvicorn
import autofocus
from fastapi import FastAPI

app: FastAPI = FastAPI()
base_url: str = "/autofocus.paloaltonetworks.com"
app.include_router(autofocus.router, prefix=base_url)

if __name__ == '__main__':
    uvicorn.run('autofocus_main:app', host='0.0.0.0', port=80, reload=True)
