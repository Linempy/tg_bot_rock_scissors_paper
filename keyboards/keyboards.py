from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# ------------------Создаем клавиатуру через Builder---------------------------

button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True)

# ----------Создаем игровую клавиатуру через Builder----------

button_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])
button_spok: KeyboardButton = KeyboardButton(text=LEXICON_RU['spok'])
button_lizard: KeyboardButton = KeyboardButton(text=LEXICON_RU['lizard'])


kb_builder_for_game: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

kb_builder_for_game.row(button_rock, button_scissors, button_paper, 
                        button_spok, button_lizard,
                        width=1)

game_kb: ReplyKeyboardMarkup = kb_builder_for_game.as_markup(resize_keyboard=True)





