import asyncio
import edge_tts

TEXT_SSML = """<speak version='1.0' xml:lang='en-US'>
  <prosody rate='85%' pitch='-2st'>
    Hello<break time='180ms'/>… nice to meet you.
  </prosody>
</speak>"""

TEXT_SSML2 = """Hello… nice to meet you."""

voice = "en-US-JennyNeural"
voice2 = "en-US-AvaNeural"

async def main():
    communicate = edge_tts.Communicate(TEXT_SSML2, voice=voice2)
    await communicate.save("hello_2.mp3")

asyncio.run(main())
