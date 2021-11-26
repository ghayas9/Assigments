from pynput.keyboard import Key, Listener

def on_press(key):
    x=10
    y=10
    if key == Key.up:
        while True:
            x=+1
            print(x,y)
    if key == Key.down:
        while True:
            y=+1
            print(x,y)


# Collect events until released
with Listener(on_press=on_press) as listener:
            listener.join()