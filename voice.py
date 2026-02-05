import asyncio
import edge_tts

TEXT_SSML2 = """Hi, Marc Mendoza..."""

voice = "en-US-JennyNeural"
voice2 = "en-US-AvaNeural"
voice3 = "en-US-AriaNeural"
pitch = "-25Hz"
rate = "-20%"

async def main():
    communicate = edge_tts.Communicate(text=TEXT_SSML2, voice=voice3, pitch=pitch, rate=rate)
    await communicate.save("hello_mm.mp3")

asyncio.run(main())
