from aiogram.types import Message
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.types import CallbackQuery


SOURCE_GROUP = -1002025427828
TARGET_GROUP = -1002079452691

router = Router()

@router.message()
async def forward_messages(message: Message):
    if message.chat.id != SOURCE_GROUP:
        return

    builder = InlineKeyboardBuilder()  # Create the builder inside the function
    builder.add(InlineKeyboardButton(
    text="Заблокировать пользователя",
    callback_data="detele_user")
)

    await message.bot.send_message(TARGET_GROUP, "Имя пользователя: " + message.from_user.full_name + "\nID пользователя: " + str(message.from_user.id), reply_markup=builder.as_markup())
    await message.forward(TARGET_GROUP)

@router.callback_query(F.data == "detele_user")
async def on_callback_query(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    print(user_id)
    with open('blocked_users.txt', 'a') as file:
        file.write(str(user_id) + '\n')
    await callback_query.answer(
        text="Пользователь заблокирован",
        show_alert=True
    )
