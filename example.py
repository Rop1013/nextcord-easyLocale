from module import BotContent # the class you can use for easier locale
from nextcord import *

# ping command
@BOT.slash_command(
    name="ping",
    name_localizations={Locale.ko: "ν"},
    description="π€ Checks how long does it takes to respond.",
    description_localizations={Locale.ko: "π€ μλ΅μκ°μ νμΈν΄μ."}
)
async def ping(inte: Interaction):
    txt = BotContent({
            Locale.ko: [" μλ΅μλ ".center(12, 'β'), "ν! `{:.2f}ms` π"],
            Locale.en_US: ["Pong!",'π `{:.2f}ms`']
        }, inte)
    await inte.send(embed=Embed(title=txt.get(), description=txt.get().format(BOT.latency * 1000)))

# Example of divide method use
@BOT.slash_command(
    name="test",
    description="test",
)
async def test(inte: Interaction):
    txt = BotContent({
            Locale.ko: [
              "ABC",
              "DEF
            ],
            Locale.en_US: [
              "κ°λλ€",
              "λ§λ°μ¬"
            ]
        }, inte)
    txt.divde(1) # Divides the list at index 1.
    if True: # If the given statement is True,
      await inte.send(txt.get(0)) # The first content ("ABC" or "κ°λλ€") is returend.
    else: # If the given statement is False,
      await inte.send(txt.get(1)) # The second content ("DEF" or "λ§λ°μ¬") is returned.
