from talon import app, actions, cron, ui

class PageDownPoller:
    enabled = False
    content = None
    
    def press_key(self):
        ui.active_window().focus()
        actions.key("pagedown")
    
    def enable(self):
        if not self.enabled:
            self.enabled = True
            status_icon = self.content.create_status_icon( "pagedownbutton", "bottom", "pagedown", "", lambda _, _2, self=self: self.press_key())
            self.content.publish_event("status_icons", "pagedownbutton", "replace", status_icon)

    def disable(self):
        if self.enabled:
            self.enabled = False

def talon_hud_ready():
    poller = PageDownPoller()
    actions.user.hud_add_poller("pagedown", poller, True)
    actions.user.hud_activate_poller("pagedown")

app.register("ready", talon_hud_ready)