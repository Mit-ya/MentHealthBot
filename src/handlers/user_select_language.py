from states import UserStates
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
from utils.find_user import find_user
from utils.update_user_state import update_user_state

from .message_templates import USER_SELECTION_LANGUAGE_MESSAGE


def user_select_language(update: Update, context: CallbackContext):
    telegram_user = update.effective_user
    user = find_user(telegram_user)
    print(user.state)
    if user.state == UserStates.SELECT_PROBLEM_STATE:
        update_user_state(user, UserStates.LANGUAGE_SELECTION_STATE)
        language_buttons = [InlineKeyboardButton(
                                text="Русский", 
                                callback_data="set_russian_lang_button"),
                            InlineKeyboardButton(
                                text="Английский", 
                                callback_data="set_english_lang_button")]

        kb = InlineKeyboardMarkup([[*language_buttons]])

        context.bot.send_message(
            chat_id=telegram_user.id,
            text=USER_SELECTION_LANGUAGE_MESSAGE,
            reply_markup=kb
        )
    else:
        print("StateError")
