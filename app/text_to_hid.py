import re

import js_to_hid as js
from hid import keycodes as hid

# Mappings of characters to codes that are shared among different keyboard
# layouts.
COMMON_CHAR_TO_JS_MAP = {
    "\t": "Tab",
    "\n": "Enter",
    " ": "Space",
    "1": "Digit1",
    "2": "Digit2",
    "3": "Digit3",
    "4": "Digit4",
    "5": "Digit5",
    "6": "Digit6",
    "7": "Digit7",
    "8": "Digit8",
    "9": "Digit9",
    "0": "Digit0",
    "$": "Digit4",
    "!": "Digit1",
    "%": "Digit5",
    "^": "Digit6",
    "&": "Digit7",
    "*": "Digit8",
    "(": "Digit9",
    ")": "Digit0",
    "_": "Minus",
    "-": "Minus",
    "+": "Equal",
    "=": "Equal",
    ":": "Semicolon",
    ";": "Semicolon",
    "a": "KeyA",
    "b": "KeyB",
    "c": "KeyC",
    "d": "KeyD",
    "e": "KeyE",
    "f": "KeyF",
    "g": "KeyG",
    "h": "KeyH",
    "i": "KeyI",
    "j": "KeyJ",
    "k": "KeyK",
    "l": "KeyL",
    "m": "KeyM",
    "n": "KeyN",
    "o": "KeyO",
    "p": "KeyP",
    "q": "KeyQ",
    "r": "KeyR",
    "s": "KeyS",
    "t": "KeyT",
    "u": "KeyU",
    "v": "KeyV",
    "w": "KeyW",
    "x": "KeyX",
    "y": "KeyY",
    "z": "KeyZ",
    ",": "Comma",
    "<": "Comma",
    ".": "Period",
    ">": "Period",
    "/": "Slash",
    "?": "Slash",
    "[": "BracketLeft",
    "{": "BracketLeft",
    "]": "BracketRight",
    "}": "BracketRight",
    "'": "Quote",
}

US_CHAR_TO_JS_MAP = COMMON_CHAR_TO_JS_MAP | {
    "@": "Digit2",
    "#": "Digit3",
    "~": "Backquote",
    "`": "Backquote",
    "\\": "Backslash",
    "|": "Backslash",
    "\"": "Quote",
}

GB_CHAR_TO_JS_MAP = COMMON_CHAR_TO_JS_MAP | {
    "\"": "Digit2",
    "£": "Digit3",
    "\\": "IntlBackslash",
    "|": "IntlBackslash",
    "~": "Backslash",
    "#": "Backslash",
    "`": "Backquote",
    "¬": "Backquote",
    "@": "Quote",
}

US_CHAR_TO_HID_MAP = {
    char: js._MAPPING[js_code] for char, js_code in US_CHAR_TO_JS_MAP.items()  # pylint: disable=protected-access
}
GB_CHAR_TO_HID_MAP = {
    char: js._MAPPING[js_code] for char, js_code in GB_CHAR_TO_JS_MAP.items()  # pylint: disable=protected-access
}

# I think this might be wrong and depends on the chosen language. It's just a
# matter of time before shifted and non-shifted characters start conflicting.
NEEDS_SHIFT_REGEX = re.compile(r'[A-Z¬!"£$%^&*()_+{}|<>?:@~#]')


def convert(char, language):
    hid_code = {
        "en-GB": GB_CHAR_TO_HID_MAP,
        "en-US": US_CHAR_TO_HID_MAP
    }[language][char.lower()]
    hid_modifier = hid.MODIFIER_LEFT_SHIFT if NEEDS_SHIFT_REGEX.match(
        char) else hid.KEYCODE_NONE
    return hid_code, hid_modifier
