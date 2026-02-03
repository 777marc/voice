import asyncio
import edge_tts

TEXT_SSML = """<speak version='1.0' xml:lang='en-US'>
  <prosody rate='85%' pitch='-2st'>
    Hello<break time='500ms'/>… nice to meet you.
  </prosody>
</speak>"""

TEXT_SSML2 = """Hello world."""

voice = "en-US-JennyNeural"
voice2 = "en-US-AvaNeural"
voice3 = "en-US-AriaNeural"
pitch = "-25Hz"
rate = "-20%"

async def main():
    communicate = edge_tts.Communicate(text=TEXT_SSML2, voice=voice3, pitch=pitch, rate=rate)
    await communicate.save("hello_t.mp3")

asyncio.run(main())
