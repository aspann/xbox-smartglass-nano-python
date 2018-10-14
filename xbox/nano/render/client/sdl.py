from xbox.nano.render.client.base import Client
from xbox.nano.render.video.sdl import SDLVideoRenderer
from xbox.nano.render.audio.sdl import SDLAudioRenderer
from xbox.nano.render.input.sdl import SDLInputHandler


class SDLClient(Client):
    def __init__(self, width, height, fullscreen=False):
        super(SDLClient, self).__init__(
            SDLVideoRenderer(width, height, fullscreen),
            SDLAudioRenderer(),
            SDLInputHandler()
        )
