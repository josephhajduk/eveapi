import eveapi
import asyncio # Requires Python 3.4


async def main():
    # Put your userID and apiKey (full access) here before running this script.
    YOUR_KEYID = 111111111
    YOUR_VCODE = "KiF5SwEEwaaazYpzGtBfGSYc6GBl7cil9y3nofkjCO3yOMVp9gM4Hp6bZeEtmyu7"

    # Provide a good User-Agent header
    eveapi.set_user_agent("eveapi.py/1.3")
    api = eveapi.EVEAPIConnection()

    auth = api.auth(keyID=YOUR_KEYID, vCode=YOUR_VCODE)

    result2 = await auth.account.Characters()

    # Some tracking for later examples.
    rich = 0
    rich_charID = 0

    # Now the best way to iterate over the characters on your account and show
    # the isk balance is probably this way:
    for character in result2.characters:
        wallet = await auth.char.AccountBalance(characterID=character.characterID)
        isk = wallet.accounts[0].balance
        print(character.name, "has", isk, "ISK.")

        if isk > rich:
            rich = isk
            rich_charID = character.characterID


loop = asyncio.get_event_loop()

loop.run_until_complete(main())

loop.run_forever()