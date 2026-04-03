import logging
import logging.config
import asyncio
import time

# Logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from LuciferMoringstar_Robot import Media
from Config import SESSION, API_ID, API_HASH, BOT_TOKEN
import pyromod.listen

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            # സമയം നോക്കാതെ തന്നെ കണക്ട് ചെയ്യാൻ ഇത് സഹായിക്കും
            sleep_threshold=60, 
            workers=50,
            plugins={"root": "LuciferMoringstar_Robot"}
        )

    async def start(self):
        # സമയം സിങ്ക് ആകുന്നതുവരെ വെയിറ്റ് ചെയ്യാതെ നിർബന്ധപൂർവ്വം സ്റ്റാർട്ട് ചെയ്യാൻ
        try:
            await super().start()
        except Exception as e:
            # msg_id എറർ വന്നാൽ 5 സെക്കൻഡ് വെയിറ്റ് ചെയ്ത് വീണ്ടും നോക്കാം
            if "[16] The msg_id is too low" in str(e):
                print("Time Sync issue detected, adjusting and retrying...")
                await asyncio.sleep(5)
                await super().start()
            else:
                raise e

        await Media.ensure_indexes()
        me = await self.get_me()
        self.username = '@' + me.username
        print(f"Bot Started: {me.first_name} (@{me.username})")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped.")

if __name__ == "__main__":
    # സെർവർ ക്ലോക്ക് സിങ്ക് ആകാൻ സമയം നൽകാതെ തന്നെ റൺ ചെയ്യുന്നു
    app = Bot()
    app.run()
