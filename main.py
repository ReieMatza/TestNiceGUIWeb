import asyncio
from functools import partial

import uvicorn
from fastapi import FastAPI
from nicegui import ui

app = FastAPI()
ui.run_with(app)

async def create_response(text: ui.textarea):
    video_text = text.value
    text.value = "soing stuff"
    asyncio.sleep(2)
    text.value = "Taj you are the king"
    ui.notify("Taj make me kids")



@ui.page('/')
def main():
    ui.label("this is an auto report app")
    text = ui.textarea(label='Text', placeholder='enter the video text here')
    ui.button('Click me!', on_click=partial(create_response,text))

uvicorn.run(app, host="0.0.0.0")