from talon_plugins import eye_zoom_mouse
from talon import noise,ctrl
def on_pop(active):
    if not eye_zoom_mouse.zoom_mouse.enabled:
        ctrl.mouse_click(button=0, hold=16000)
noise.register('pop', on_pop)