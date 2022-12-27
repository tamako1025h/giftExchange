from tkinter import ttk, Listbox
import tkinter as tk
import random

# テスト用のデータ
NAME = ["たなか",'やまだ','さとう','さいとう','うえだ','うみの','いとう','たかはし','きむら','しみず']
RESULT = ["抽選結果出力"]

class trade:
    
    def __init__(self,master):
        self.master = master
        self.createWidgth()
        
    def createWidgth(self):
        """各ウィジェットの生成"""
        self.frame1 = tk.Frame(self.master, padx=10, pady=10)
        self.frame2 = tk.Frame(self.master, padx=10, pady=10)
        self.frame3 = tk.Frame(self.master, padx=10, pady=10)
        self.text = tk.Entry(self.master, width=20)
        self.addButton = tk.Button(self.master,text="追加",width=7,command=lambda:self.add_list(self.text.get()))

        """フレーム1"""
        self.listBox = tk.Listbox(self.frame1,height=15,width=40,borderwidth=2)
        for value in RESULT:
            self.listBox.insert(tk.END, value)
        self.listBox.pack()
        
        """フレーム2"""
        self.listName = tk.Listbox(self.frame2,heigh=15,borderwidth=2)
        for name in NAME:
            self.listName.insert(tk.END, name)
        self.listName.pack()
        
        """フレーム3"""
        self.chButton = tk.Button(self.frame3,text="抽選",width=7,command=self.match)
        self.delButton = tk.Button(self.frame3,text="削除",width=7,command=self.delete_list)
        
        self.chButton.pack(pady=95)
        self.delButton.pack()
        
        """各種配置"""
        self.frame1.grid(row=0,column=0)
        self.frame2.grid(row=0,column=1)
        self.frame3.grid(row=0,column=2)
        self.text.grid(row=1,column=1)
        self.addButton.grid(row=1,column=2)
    
    """ボタンの各機能"""       
    def add_list(self):     
        self.listName.insert(tk.END,self.text)
        NAME.append(self.text)
    
    def delete_list(self):
        self.selected_index = self.listName.curselection()
        self.listName.delete(self.selected_index)
        del NAME[self.selected_index[0]]
    
    def match(self):
        self.listBox.delete(0,tk.END)
        if len(NAME) %2 == 0:
            r = random.sample(NAME,len(NAME))
            n = int(len(r)/2)
            
            for i in range(0,n):
                p = f'{r[0+i]}さんと、{r[-1-i]}さんと交換です'
                self.listBox.insert(tk.END,p)
                
        else:
            error = '人数が合いません'
            self.listBox.insert(tk.END,error)
    

def main():
    app = tk.Tk()
    app.geometry("500x300")
    app.resizable(width=False,height=False)
    chtrade = trade(app)
    app.mainloop()
        
if __name__ == "__main__":
    main()