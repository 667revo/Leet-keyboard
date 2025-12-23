import keyboard

mapping = {
    'i': '1',
    'a': '4',
    'o': '0',
    'e': '3'
}

def key_handler(event):
    key = event.name
    if key in mapping:
        keyboard.write(mapping[key])

for key in mapping:
    keyboard.on_press_key(key, key_handler, suppress=True)

print("Macro aktif (i→1, a→4, o→0, e→3)")
print("Çıkmak için ESC tuşuna bas.")
keyboard.wait('esc')
