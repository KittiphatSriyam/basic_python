from googletrans import Translator

text = 'สวัสดี'

LAM = Translator()
vocab = LAM.translate(text,dest='zh-cn')

print('คำศัพท์ : ',vocab.text)
print('คำแปล : ' ,vocab.pronunciation)
