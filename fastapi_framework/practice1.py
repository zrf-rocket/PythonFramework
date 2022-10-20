# 最简单的fastapi服务
import uvicorn
import global_settings_base
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
@app.get("/index/{name}")
@app.post("/post")
@app.patch("/patch")
@app.delete("/delete")
async def index(name: str = global_settings_base.author):
    return {"msg": "Hello {}, this is python fastapi framework".format(name)}


if __name__ == '__main__':
    uvicorn.run("practice1:app", host="0.0.0.0", port=80)
