import tkinter

def btn_click():
    num1 =int(entry1.get())
    num2= int(entry2.get())


    str1 = str(num1)+"을(를)" +str(num2)+"(으)로 나눈 몫은"+ str(num1//num2) +"입니다."
    str2 = str(num1)+"을(를)" +str(num2)+"(으)로 나눈 나머지는"+ str(num1%num2) +"입니다."
    labelRes1 = tkinter.Label(root, text=str1, font=("맑은 고딕",10))
    labelRes1.place(x=21, y=86)
    labelRes2 = tkinter.Label(root, text=str2, font=("맑은 고딕",10))
    labelRes2.place(x=21, y=116)
def mouseMove(event):
    x= event.x
    y= event.y
    labelMouse.config(text=str(x)+","+str(y))
    labelMouse.place(x=0, y=280)#라벨을 붙인다

root = tkinter.Tk()
root.title("산수 연산자")
root.geometry("400x300")

#좌표 출력기
root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text="," , font=("맑은 고딕",10))#라벨을 만든다
labelMouse.place(x=0, y=130)

label1 =tkinter.Label(root, text= "나눠지는 수", font=("맑은 고딕",10))
label2=tkinter.Label(root, text= "나눠지는 수", font=("맑은 고딕",10))

label1.place(x=20,y=20)
label2 .place(x=25, y=45)

entry1 = tkinter.Entry(width=8)
entry2 = tkinter.Entry(width=8)
entry1.place(x=102, y=20)
entry2.place(x=102, y=48)

btn =tkinter.Button(root, text="계산", font=("맑은 고딕",10), command=btn_click)
btn.place(x=186, y=20,width=54, height=48)
root.mainloop()