import dearpygui.dearpygui as dpg
import threading
from pynput import mouse
from win32api import mouse_event
from time import sleep
import os

PLUS = 5
MINUS = -5
SLEEP_TIME = 0.00001
RUNNING = False
BUTTON_PRESSED = False
CURRENT_LISTENER = None

def SLEEP(timing=SLEEP_TIME):
    sleep(timing)

def MSEVENT(plusPXL, minusPXL):
    mouse_event(0x01, plusPXL, minusPXL)

def jitter_loop(control_button):
    global RUNNING, BUTTON_PRESSED, CURRENT_LISTENER, PLUS, MINUS, SLEEP_TIME

    if CURRENT_LISTENER is not None:
        CURRENT_LISTENER.stop()
        CURRENT_LISTENER = None

    def on_click(x, y, button, pressed):
        global BUTTON_PRESSED
        if button == control_button:
            BUTTON_PRESSED = pressed

    listener = mouse.Listener(on_click=on_click)
    CURRENT_LISTENER = listener
    listener.start()

    while RUNNING:
        if BUTTON_PRESSED:
            MSEVENT(PLUS, 0)
            MSEVENT(PLUS, 0)
            SLEEP()
            
            MSEVENT(0, MINUS)
            MSEVENT(0, MINUS)
            SLEEP()
            
            MSEVENT(MINUS, 0)
            MSEVENT(MINUS, 0)
            SLEEP()
            
            MSEVENT(0, PLUS)
            MSEVENT(0, PLUS)
            SLEEP()
        else:
            sleep(0.01)

    if CURRENT_LISTENER is not None:
        CURRENT_LISTENER.stop()
        CURRENT_LISTENER = None

def start_jitter(sender, app_data, user_data):
    global RUNNING
    if not RUNNING:
        RUNNING = True
        button_str = dpg.get_value("button_combo").lower().replace(" ", "_")
        if button_str == "mouse4":
            button_str = "button4"
        elif button_str == "mouse5":
            button_str = "button5"
        control_button = getattr(mouse.Button, button_str)
        threading.Thread(target=jitter_loop, args=(control_button,), daemon=True).start()
        dpg.set_value("status_text", "Status: Enabled")
        dpg.configure_item("status_text", color=[0, 255, 0])
        dpg.configure_item("start_button", enabled=False)
        dpg.configure_item("stop_button", enabled=True)

def stop_jitter(sender, app_data, user_data):
    global RUNNING, BUTTON_PRESSED, CURRENT_LISTENER
    if RUNNING:
        RUNNING = False
        BUTTON_PRESSED = False
        if CURRENT_LISTENER is not None:
            CURRENT_LISTENER.stop()
            CURRENT_LISTENER = None
        dpg.set_value("status_text", "Status: Disabled")
        dpg.configure_item("status_text", color=[255, 0, 0])
        dpg.configure_item("start_button", enabled=True)
        dpg.configure_item("stop_button", enabled=False)

def update_plus(sender, app_data):
    global PLUS
    PLUS = app_data

def update_minus(sender, app_data):
    global MINUS
    MINUS = app_data

def update_sleep_time(sender, app_data):
    global SLEEP_TIME
    SLEEP_TIME = app_data

# Setup Dear PyGui
dpg.create_context()
dpg.create_viewport(title="JitterForApex", width=400, height=500, resizable=True)

# Load font at the start
with dpg.font_registry():
    try:
        default_font = dpg.add_font("C:/Windows/Fonts/Arial.ttf", 16, tag="default_font")
    except:
        default_font = None
dpg.bind_font(default_font)

# Load the background image
image_path = ""
print(f"Попытка загрузки изображения: {image_path}")

with dpg.texture_registry():
    if os.path.exists(image_path):
        print(f"Файл изображения найден: {image_path}")
        try:
            result = dpg.load_image(image_path)
            if result is not None:
                width, height, channels, data = result
                print(f"Изображение успешно загружено: {width}x{height}, каналов: {channels}")
                dpg.add_static_texture(width=width, height=height, default_value=data, tag="background_texture")
            else:
                print("Ошибка: dpg.load_image вернул None")
                dpg.add_static_texture(width=1, height=1, default_value=[0, 0, 0, 255], tag="background_texture")
        except Exception as e:
            print(f"Не удалось загрузить изображение: {e}")
            dpg.add_static_texture(width=1, height=1, default_value=[0, 0, 0, 255], tag="background_texture")
    else:
        print(f"Файл изображения не найден: {image_path}")
        dpg.add_static_texture(width=1, height=1, default_value=[0, 0, 0, 255], tag="background_texture")

# Setup styles
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, [50, 50, 50, 255])
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, [0, 0, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0)

    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [70, 70, 70, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [100, 100, 100, 255])
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

# Create window
with dpg.window(label="CIS Jitter", no_resize=False, no_title_bar=False, tag="main_window", width=400, height=500, pos=[0, 0], no_scrollbar=True, no_scroll_with_mouse=True):
    dpg.add_image("background_texture", tag="background_image", pos=[0, 0], width=400, height=500)
    
    with dpg.group(tag="main_group"):
        dpg.add_text("Jitter for m&k v2.0", tag="title_text", color=[255, 255, 255, 255])
        dpg.add_spacer(height=10, tag="spacer1")
        dpg.add_text("Select activation button:", tag="button_label", color=[200, 200, 200, 255])
        dpg.add_combo(items=["right", "left", "middle", "mouse4", "mouse5"], default_value="right", tag="button_combo", width=0)
        dpg.add_spacer(height=10, tag="spacer2")
        dpg.add_text("Shake strength (PLUS):", tag="plus_label", color=[200, 200, 200, 255])
        dpg.add_slider_int(label="", default_value=PLUS, min_value=1, max_value=20, callback=update_plus, tag="plus_slider", width=0)
        dpg.add_spacer(height=5, tag="spacer3")
        dpg.add_text("Shake strength (MINUS):", tag="minus_label", color=[200, 200, 200, 255])
        dpg.add_slider_int(label="", default_value=MINUS, min_value=-20, max_value=-1, callback=update_minus, tag="minus_slider", width=0)
        dpg.add_spacer(height=5, tag="spacer4")
        dpg.add_text("Delay (SLEEP_TIME):", tag="sleep_label", color=[200, 200, 200, 255])
        dpg.add_slider_float(label="", default_value=SLEEP_TIME, min_value=0.00001, max_value=0.001, callback=update_sleep_time, tag="sleep_slider", width=0)
        dpg.add_spacer(height=10, tag="spacer5")
        dpg.add_button(label="Enable", callback=start_jitter, tag="start_button", width=0, height=0)
        with dpg.theme() as start_theme:
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button, [76, 175, 80, 255])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [69, 160, 73, 255])
        dpg.bind_item_theme("start_button", start_theme)
        dpg.add_spacer(height=10, tag="spacer6")
        dpg.add_button(label="Disable", callback=stop_jitter, tag="stop_button", width=0, height=0, enabled=False)
        with dpg.theme() as stop_theme:
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button, [244, 67, 54, 255])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [220, 60, 48, 255])
        dpg.bind_item_theme("stop_button", stop_theme)
        dpg.add_spacer(height=10, tag="spacer7")
        dpg.add_text("Status: Disabled", tag="status_text", color=[255, 0, 0, 255])
        dpg.add_spacer(height=5, tag="spacer8")
        dpg.add_text("Hold the selected button", tag="instruction_text", color=[200, 200, 200, 255])
        dpg.add_spacer(height=5, tag="spacer9")
        dpg.add_text("Made by rMononoke", tag="signature_text", color=[150, 150, 150, 255])

def resize_callback(sender, app_data):
    viewport_width, viewport_height = app_data[0], app_data[1]
    dpg.configure_item("main_window", width=viewport_width, height=viewport_height, pos=[0, 0])
    dpg.configure_item("background_image", width=viewport_width, height=viewport_height)
    padding = max(10, viewport_width * 0.05)
    element_width = int(viewport_width * 0.8)
    button_height = int(viewport_height * 0.08)
    font_scale = max(1.0, min(viewport_width / 400, viewport_height / 500))
    with dpg.font_registry():
        try:
            default_font = dpg.add_font("C:/Windows/Fonts/Arial.ttf", 16 * font_scale, tag="default_font")
            dpg.bind_font(default_font)
        except:
            pass
    dpg.configure_item("button_combo", width=element_width)
    dpg.configure_item("plus_slider", width=element_width)
    dpg.configure_item("minus_slider", width=element_width)
    dpg.configure_item("sleep_slider", width=element_width)
    dpg.configure_item("start_button", width=element_width, height=button_height)
    dpg.configure_item("stop_button", width=element_width, height=button_height)
    indent = (viewport_width - element_width) // 2
    for tag in ["title_text", "button_label", "button_combo", "plus_label", "plus_slider", 
                "minus_label", "minus_slider", "sleep_label", "sleep_slider", 
                "start_button", "stop_button", "status_text", "instruction_text", "signature_text"]:
        dpg.configure_item(tag, indent=indent)
    total_elements_height = (
        30 + 10 +
        20 + 30 + 10 +
        20 + 30 + 5 +
        20 + 30 + 5 +
        20 + 30 + 10 +
        button_height + 10 +
        button_height + 10 +
        20 + 5 +
        20 + 5 +
        20
    )
    vertical_offset = (viewport_height - total_elements_height) // 2
    if vertical_offset < padding:
        vertical_offset = padding
    dpg.configure_item("spacer1", height=vertical_offset)

dpg.bind_theme(global_theme)
dpg.set_viewport_resize_callback(resize_callback)
resize_callback(None, [400, 500])
dpg.setup_dearpygui()
dpg.show_viewport()
print("Чтобы выйти, закройте окно или нажмите CTRL+C")
dpg.start_dearpygui()
dpg.destroy_context()
stop_jitter(None, None, None)