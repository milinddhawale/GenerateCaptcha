"""
Generate captcha(Image) using python

from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280,height=90)

captcha_text = 'Milind Dhawale'

data = image.generate(captcha_text)

image.write(captcha_text,'milind.png')
------------------------------------------------------
Generate captcha(Audio) using python
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()

Captcha_text = '152836'

audio_data = audio.generate(Captcha_text)

audio_file = 'C:/Users/Milind/Downloads/data_science_lecture/audio.wav'

audio.write(Captcha_text,audio_file)
"""
