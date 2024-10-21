from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from udp_audio_receiver import udp_audio_receiver
import os
import asyncio
import threading

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

template_dir = os.environ.get('TEMPLATE_DIR', 'templates')
templates = Jinja2Templates(directory=template_dir)

audio_file1 = os.environ.get('AUDIO_PATH_OUTPUT1')
audio_file2 = os.environ.get('AUDIO_PATH_OUTPUT2')

def start_udp_receiver():
    print("Initializing the UDP receiver...")
    asyncio.run(udp_audio_receiver())

threading.Thread(target=start_udp_receiver, daemon=True).start()

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/audio1")
async def audio_stream1():
    return FileResponse(audio_file1, media_type='audio/wav')

@app.get("/audio2")
async def audio_stream2():
    return FileResponse(audio_file2, media_type='audio/wav')

@app.exception_handler(404)
async def not_found(request, exc):
    return RedirectResponse(url="/")

#Project commando execution "uvicorn server:app --host 0.0.0.0 --port 5000"