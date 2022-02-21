from talon import ui, Module, Context, registry, actions, imgui, cron, app

mod = Module()
ctx_zoom_mouse_enabled_use_pedal = Context()
ctx_zoom_mouse_enabled_use_pedal.matches = r"""
tag: talon_plugins.eye_zoom_mouse.zoom_mouse_enabled
and not tag: talon_plugins.eye_zoom_mouse.zoom_mouse_activated
#and not tag: talon_plugins.eye_zoom_mouse.zoom_mouse_pedal
"""


ctx_zoom_mouse_triggered_use_pedal = Context()
ctx_zoom_mouse_triggered_use_pedal.matches = r"""
tag: talon_plugins.eye_zoom_mouse.zoom_mouse_enabled
and tag: talon_plugins.eye_zoom_mouse.zoom_mouse_activated
#and not tag: talon_plugins.eye_zoom_mouse.zoom_mouse_pedal
"""


@mod.action_class
class Actions:
    def hitch2_s1():
        """document string goes here"""

    def hitch2_s2():
        """document string goes here"""
        if app.platform == "mac":
            actions.key("ctrl-f")
        elif app.platform == "windows":
            actions.key("ctrl-m")

    def hitch2_s3():
        """document string goes here"""
        actions.user.mouse_scroll_down()

    def hitch2_s4():
        """document string goes here"""
        #print('scroll up')
        actions.user.mouse_scroll_up()

    def hitch2_s5():
        """document string goes here"""

    def hitch2_s6():
        """document"""

    def hitch2_s7():
        """document string goes here"""
        actions.user.mouse_toggle_zoom_mouse()

    def hitch2_s8():
        """document string goes here"""
        actions.user.microphone_toggle()

@ctx_zoom_mouse_enabled_use_pedal.action_class("user")
class WindowsZoomMouseInactiveActions:
    def hitch2_s1():
        """document string goes here"""
        actions.talon_plugins.eye_zoom_mouse.mouse_trigger()

    def hitch2_s2():
        """document string goes here"""
        if app.platform == "mac":
            actions.key("ctrl-f")
        elif app.platform == "windows":
            actions.key("ctrl-m")


    def hitch2_s3():
        """document string goes here"""
        actions.user.mouse_scroll_down()

    def hitch2_s4():
        """document string goes here"""
        #print('scroll up')
        actions.user.mouse_scroll_up()

    def hitch2_s5():
        """document string goes here"""
        #actions.user.system_task_view()
        actions.user.system_switcher()

    def hitch2_s6():
        """document"""
        actions.user.system_last_application()
        
    def hitch2_s7():
        """document string goes here"""
        actions.user.mouse_toggle_zoom_mouse()

    def hitch2_s8():
        """document string goes here"""
        actions.user.microphone_toggle()


@ctx_zoom_mouse_triggered_use_pedal.action_class("user")
class WindowsZoomMouseActiveActions:
    def hitch2_s1():
        """document string goes here"""
        actions.talon_plugins.eye_zoom_mouse.mouse_trigger()

    def hitch2_s2():
        """document string goes here"""
        actions.talon_plugins.eye_zoom_mouse.right_click()

    def hitch2_s3():
        """document string goes here"""
        actions.talon_plugins.eye_zoom_mouse.double_click()

    def hitch2_s4():
        """document string goes here"""
        actions.talon_plugins.eye_zoom_mouse.triple_click()

    def hitch2_s5():
        """document string goes here"""
        actions.talon_plugins.eye_zoom_mouse.mouse_drag()

    def hitch2_s6():
        """document"""
        actions.talon_plugins.eye_zoom_mouse.mouse_move()

    def hitch2_s7():
        """document string goes here"""

    def hitch2_s8():
        """document string goes here"""