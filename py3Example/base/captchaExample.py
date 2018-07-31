# -*- coding: utf-8 -*-
# Created by bida on 2018/7/30
from base64 import b64encode, b64decode
from io import BytesIO

from PIL import Image
from captcha.image import ImageCaptcha

# 生成验证码图片
captcha = ImageCaptcha(width=160, height=60,
                       fonts=['/Library/Fonts/Georgia.ttf', '/Library/Fonts/Courier New.ttf'])

cap = captcha.generate_image('JAVA')
# or
cap = captcha.create_captcha_image('JAVA', (0, 255, 255), (123, 123, 123))
captcha.create_noise_curve(cap, (0, 127, 127))
captcha.create_noise_dots(cap, (0, 255, 255), width=2, number=30)

cap.save('captcha.JPEG')
cap.show()

# 直接使用ImageCpatcha生成base64
output_buffer = BytesIO()
cap.save(output_buffer, format='JPEG')
byte_data = output_buffer.getvalue()
b64_str = b64encode(byte_data)

# base64转换为图片
image_bytes = b64decode(b64_str)
image_data = BytesIO(image_bytes)
img = Image.open(image_data)
img.save('captcha2.JPEG')
img.show()
