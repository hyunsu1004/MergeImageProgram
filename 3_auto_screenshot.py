import time
from PIL import ImageGrab
#(파이썬 이미지 라이브러리 의 약자)

time.sleep(5) #5초 대기 : 사용자가 준비하는 시간

for i in range(1,11): #2초 간격으로 총 10장 이미지 저장
    img = ImageGrab.grab() #현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i)) #파일로 저장 
    time.sleep(2) # 2초 단위 
