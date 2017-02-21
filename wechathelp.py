#-*-coding:utf-8-*-3
import itchat, time
from tkinter import *
from tkinter import messagebox
class Weixingui:
    def __init__(self):
        self.top=Tk()
        self.top.geometry("600x100")
        self.top.title("微信群发助手")
        self.top.columnconfigure(0, minsize=50)
        self.top.rowconfigure(0, minsize=50)
        self.groupname = Label(self.top, text="群名").grid(row=0)
        self.wishname = Label(self.top, text="祝福话语").grid(row=0, column=2)
        self.entry_qunming=StringVar()
        self.grouptext=Entry(self.top,textvariable=self.entry_qunming).grid(row=0,column=1)
        self.entry_wish = StringVar()
        self.wishtext=Entry(self.top,textvariable=self.entry_wish).grid(row=0,column=3)
        self.send=Button(self.top,text="发送祝福",command=self.weixin).grid(row=1,column=2,sticky=W)

    def weixin(self):
        wish=self.entry_wish.get()
        sendwish="%s，"+str(wish)
        chatroomName=self.entry_qunming.get()
        itchat.auto_login(hotReload=True)
        itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(name=chatroomName)
        chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
        for friend in chatroom['MemberList']:
            friend = itchat.search_friends(userName=friend['UserName'])
            itchat.send(sendwish % (friend['RemarkName'] or friend["NickName"]), friend['UserName'])
            time.sleep(1)
        messagebox.showinfo("SB","发送完毕啦")
def main():
    d=Weixingui()
    mainloop()
if __name__== "__main__":
    main()

