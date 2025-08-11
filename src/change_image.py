# src/change_image.py

from os.path import isfile
import iterm2
import os
import asyncio
from random import randint

async def set_background_image(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    
    if window is None:
        return

    tab = window.current_tab
    if tab is None:
        return

    session = tab.current_session
    if session is None:
        return
        
    profile = await session.async_get_profile()
    #todo logica para pefar os elementos do diretorio e sortear 
    photos = []
    try:
        current_dir = os.getcwd()
        photos = os.listdir('./fotos')
    except FileNotFoundError:  
        print('errou')
        #todo fazer o erro retornar algo
        return
    choosen_photo = current_dir + '/fotos/' + photos[randint(0, len(photos) - 1)]

    await profile.async_set_background_image_location(choosen_photo)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    iterm2.run_until_complete(set_background_image)

if __name__ == "__main__":
    main()
