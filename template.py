# -------------------------------
# ShareMali Extension: Simple Message
# -------------------------------

trigger_sharemali = "myextension"
description_sharemali = "My first extension"

# trigger_sharemali & description_sharemali is essential without this the extension will not work

async def run(message, args):
    """
    Sends a simple reply when triggered.
    """
    await message.reply("Hello! This is a simple ShareMali extension.")
