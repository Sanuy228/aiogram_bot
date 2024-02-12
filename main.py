import asyncio
import logging

from aiogram import Bot, Dispatcher, Router

from handlers.user.forward import router as forward_router


async def main():
    # Объект бота
    bot = Bot(token="6531524954:AAEf3Wxh5Zi8ojHjTBDLThcjzY4KoMmk-5M")
    dp = Dispatcher()

    dp.include_router(forward_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
