import tkinter
import tkinter.font

def click_btn(): # 함수표현 
    labelE = tkinter.Label(root, text = "동", font=("한컴 말랑말랑 Bold", 24))
    labelW = tkinter.Label(root, text = "서", font=("한컴 말랑말랑 Bold", 24))
    labelS = tkinter.Label(root, text = "남", font=("한컴 말랑말랑 Bold", 24))
    labelN = tkinter.Label(root, text = "북", font=("한컴 말랑말랑 Bold", 24))

    labelE.place(x=300,y=200)
    labelW.place(x=100,y=200)
    labelS.place(x=200,y=100)
    labelN.place(x=200,y=300)

    txt = entry. get()
    str1=txt
    labeltxt = tkinter.Label(root, text = str1, font=("한컴 말랑말랑 Bold", 24))
    labeltxt.place(x=250, y=350)

root = tkinter.Tk() 

root.title("첫 번째 윈도우")
root.geometry("800x600")

btn = tkinter.Button(root, text="버튼", font=("한컴 말랑말랑 Bold", 10), command=click_btn)
btn.place(x=205,y=210,width=30, height=30)

entry=tkinter.Entry(width=5)
entry.place(x=200, y=350)

root.mainloop()


