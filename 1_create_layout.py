# Project) 여러 이미지를 합치는 프로그램을 만드시오.

# [사용자 시나리오]
# 1. 사용자는 합치려는 이미지를 1개 이상 선택한다.
# 2. 합쳐진 이미지가 저장될 경로를 지정한다.
# 3. 가로넓이, 간격, 포맷 옵션을 지정한다.
# 4. 시작 버튼을 통해 이미지를 합친다.
# 5. 닫기 버튼을 통해 프로그램을 종료한다.

# [기능 명세]
# 1. 파일 추가 : 리스트 박스에 파일 추가
# 2. 선택 삭제 : 리스트 박스에서 선택된 항목 삭제
# 3. 찾아 보기 : 저장 폴더를 선태갛면 텍스트 위젯에 입력
# 4. 가로 넓이 : 이미지 넓이 지정 (원본유지 , 1024,800,640)
# 5. 간격: 이미지 간의 간격 지정(없음, 좁게, 보통 , 넓게)
# 6. 포맷 : 저장 이미지 포맷 지정(PNG,JPG,BMP)
# 7. 시작 : 이미지 합치기 작업 실행
# 8. 진행 상황  : 현재 진행 중인 파일 순서에 맞게 반영
# 9. 닫기 : 프로그램 종료 
from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.title("Nado GUI")


#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x',padx=5,pady=5) #pad로 간격 띄우기

btn_add_file = Button(file_frame,padx=5,pady=5,width=12,text="파일 추가")
btn_add_file.pack(side="left")
# btn_add_file = Button(file_frame,padx=5,pady=5,width=12,text="파일 추가")
# btn_add_file.pack(side="left")
btn_del_file = Button(file_frame,padx=5,pady=5,width=12,text="선택 삭제")
btn_del_file.pack(side="right")

# btn_del_file = Button(file_frame,padx=5,pady=5,width=12,text="선택 삭제")
# btn_del_file.pack(side="right")

# #리스트 프레임 
# list_frame = Frame(root)
# list_frame.pack(fill="both",padx=5,pady=5) #빈공간 채우기
list_frame = Frame(root)
list_frame.pack(fill='both',padx=5,pady=5)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame,selectmode="extended",height=15,yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both",expand = True) #both 위아래 좌우로 펼쳐지도록
scrollbar.config(command=list_file.yview)

#저장경로 프레임
path_frame = LabelFrame(root,text="저장경로")
path_frame.pack(fill="x",padx=5,pady=5,ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="x",expand=True,padx=5,pady=5,ipady=4) #높이 변경

btn_dest_path = Button(path_frame,text="찾아보기",padx=5,pady=5,width = 10)
btn_dest_path.pack(side="right")

#옵션 프레임
frame_option = LabelFrame(root,text="옵션")
frame_option.pack(padx=5,pady=5,ipady=5)

#1.가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(frame_option,text="가로넓이",width=8)
lbl_width.pack(side="left",padx=5,pady=5)
# #가로 넓이 콤보
opt_width = ["원본유지","1024","800","640"]
cmb_width = ttk.Combobox(frame_option,state="readonly",values=opt_width,width=10)
cmb_width.current(0) #첫번째 값을 자동으로 선택
cmb_width.pack(side="left",padx=5,pady=5)
#2.간격 옵션
# #간격 옵션 레이블
lbl_space = Label(frame_option,text="간격",width=8)
lbl_space.pack(side="left",padx=5,pady=5)
#간격 옵션 콤보
opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(frame_option,state="readonly",values=opt_space,width=10)
cmb_space.current(0) #첫번째 값을 자동으로 선택
cmb_space.pack(side="left",padx=5,pady=5)

#3.파일 포맷 옵션
#파일 옵션 레이블
lbl_format = Label(frame_option,text="포맷",width=8)
lbl_format.pack(side="left",padx=5,pady=5)

#파일 옵션 콤보
opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(frame_option,state="readonly",values=opt_format,width=10)
cmb_format.current(0) #첫번째 값을 자동으로 선택
cmb_format.pack(side="left",padx=5,pady=5)

#진행상황 프로그레스바
frame_progress= LabelFrame(root,text="진행상황")
frame_progress.pack(fill="x",padx=5,pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress,maximum=100,variable=p_var)
progress_bar.pack(fill="x",padx=5,pady=5)

#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x",padx=5,pady=5)

btn_close = Button(frame_run,text="닫기",padx=5,pady=5,width=12)
btn_close.pack(side="right",padx=5,pady=5)

btn_start = Button(frame_run,text="시작",padx=5,pady=5,width=12)
btn_start.pack(side="right",padx=5,pady=5)


root.resizable(False,False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()
