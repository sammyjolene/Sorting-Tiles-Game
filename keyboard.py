from pynput import keyboard

def on_press(key):
    try:
        print(key) 
    except AttributeError:
        print(key)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()


### MY CHANGES

# def on_press(key):
#     try:
#         if key == keyboard.Key.up:
#             print("up")
#         elif key == keyboard.Key.down:
#             print("down")
#         elif key == keyboard.Key.left:
#             print("left")
#         elif key == keyboard.Key.right:
#             print("right")
#         elif key == keyboard.Key.esc:
#             # Stop listener
#             return False
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print("try again")