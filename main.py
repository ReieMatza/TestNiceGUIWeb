import asyncio
from functools import partial

import uvicorn
from fastapi import FastAPI
from nicegui import ui

app = FastAPI()
ui.run_with(app)


async def create_response(text: ui.textarea):
    video_text = text.value
    text.value = "doing stuff..."
    await asyncio.sleep(2)
    text.value = "Taj you are the king"
    ui.notify("Taj make me kids")


@ui.page('/')
def main():
    with ui.row().classes('w-full  justify-center'):
        with ui.column().classes('w-1/2 h-full place-center items-center'):
            ui.label("Auto Report Generator").classes('text-4xl')
            text = ui.textarea(label='Text', placeholder='Enter the video text here').classes('w-full')
            ui.button('Click me!', on_click=partial(create_response, text)).classes('self-end')


uvicorn.run(app, host="0.0.0.0")
