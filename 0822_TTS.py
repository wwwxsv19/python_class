from gtts import gTTS

text = "안녕하세요 부소마 감자입니다"
tts = gTTS(text=text, lang='ko')
tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3") 