def on_button_pressed_a():
    global LetterToSend
    LetterToSend = "" + LetterToSend + "."
    basic.show_string(LetterToSend)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global LetterToSend
    radio.send_string(LetterToSend)
    LetterToSend = ""
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global LetterToSend
    LetterToSend = "" + LetterToSend + "-"
    basic.show_string(LetterToSend)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_string_deprecated(receivedString):
    global LetterToSend
    basic.show_string("" + (receivedString))
    LetterToSend = ""
radio.on_received_string_deprecated(on_received_string_deprecated)

LetterToSend = ""
LetterToSend = ""
radio.set_group(1)
morse = [".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
    "-----"]
alphabet = ["a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"]