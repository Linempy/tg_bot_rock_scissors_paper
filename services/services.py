import random

from lexicon.lexicon_ru import LEXICON_RU


def get_bot_choice() -> str:
    return random.choice(['rock', 'scissors', 'paper', 'spok', 'lizard'])


def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': ('scissors', 'lizard'),
                             'scissors': ('paper', 'lizard'),
                             'paper': ('rock', 'spok'),
                             'spok': ('rock', 'scissors'),
                             'lizard': ('paper', 'spok')}
    
    if user_choice == bot_choice:
        return 'nobody_won'
    elif bot_choice in rules[user_choice]:
        return 'user_won'
    else:
        return 'bot_won'