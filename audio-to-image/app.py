import base64

import streamlit as st
from agents import Agent, Runner
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
IMAGE_MODEL = "gpt-image-2"  # needs a verified org; switch to "dall-e-3" if you get a verification error

prompt_agent = Agent(
    name="Image Prompt Agent",
    model="gpt-4o-mini",
    instructions=(
        "Turn the user's spoken words into one clear, detailed image prompt. "
        "Keep their main idea, add style and lighting details. Return only the prompt. "
        "If the text is not something that can be drawn, return exactly: NO_IMAGE"
    ),
)

st.title("Audio-to-Image Agent")
audio = st.audio_input("Record your idea") or st.file_uploader("Or upload audio", type=["wav", "mp3", "m4a"])

if audio:
    with st.spinner("Transcribing..."):
        text = client.audio.transcriptions.create(model="whisper-1", file=(audio.name, audio.getvalue())).text
    if not text.strip():
        st.warning("I could not hear anything. Please record again.")
        st.stop()
    st.write("**You said:**", text)

    prompt = Runner.run_sync(prompt_agent, text).final_output
    if prompt.strip() == "NO_IMAGE":
        st.warning("That does not sound like something I can draw. Try describing a scene.")
        st.stop()
    st.write("**Image prompt:**", prompt)

    with st.spinner("Generating image..."):
        kwargs = {"response_format": "b64_json"} if IMAGE_MODEL == "dall-e-3" else {}
        img = client.images.generate(model=IMAGE_MODEL, prompt=prompt, size="1024x1024", **kwargs)
    st.image(base64.b64decode(img.data[0].b64_json))
