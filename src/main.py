import tkinter as tk

import pandas as pd

CSV_FILE = "..\workbook\sample.csv"

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("ボタンの作成(Windowsスタイル)")     # ウィンドウタイトル
        self.master.geometry("700x300")       # ウィンドウサイズ(幅x高さ)
        self.quiz_list = [] # クイズデータリスト

        df = pd.read_csv(CSV_FILE)
        # CSVの各行をリスト化
        self.quiz_list = [list(quiz) for quiz in zip(df["問題文"],df["解答1"],df["解答2"],df["解答3"],df["解答4"],df["答え"])]
        self.get_quiz()
        
    def get_quiz(self):   # 問題文の表示
        question = tk.Label(self.master, text=self.quiz_list[0][0], width=20, height=5)
        # question = tk.Message(text=quiz_list[0][0])
        # クリックイベントの指定
        anser1 = tk.Button(self.master, text = self.quiz_list[0][1], 
                            command = self.button_click, # クリック時に呼び出されるメソッド名
                            width = 20, height = 2
                            )
        anser2 = tk.Button(self.master, text = self.quiz_list[0][2], 
                            command = self.button_click, # クリック時に呼び出されるメソッド名
                            width = 20, height = 2
                            )
        anser3 = tk.Button(self.master, text = self.quiz_list[0][3], 
                            command = self.button_click, # クリック時に呼び出されるメソッド名
                            width = 20, height = 2
                            )
        anser4 = tk.Button(self.master, text = self.quiz_list[0][4], 
                            command = self.button_click, # クリック時に呼び出されるメソッド名
                            width = 20, height = 2
                            )
        # ボタンの配置
        question.grid(row=0, column=1)
        anser1.grid(row=5, column=1)
        anser2.grid(row=5, column=2)
        anser3.grid(row=5, column=3)
        anser4.grid(row=5, column=4)

    def button_click(self):
        # 答えの表示
        anser_index = self.quiz_list[0][5] + 1
        self.anser = tk.Label(self.master, text="答え : " + self.quiz_list[0][anser_index], width=20, height=5)
        self.next = tk.Button(self.master, text = "Next", command = self.quiz_remove,width = 20, height = 2)
        # ボタンの配置
        self.anser.grid(row=6, column=1)
        self.next.grid(row=7, column=4)
    
    def quiz_remove(self):
        # 答えの表示
        self.quiz_list.pop(0)
        self.anser.destroy() # 次の問題の際にボタンの削除
        self.next.destroy() # 次の問題の際にボタンの削除
        if self.quiz_list:
            # まだクイズがある場合は次のクイズを表示する
            self.get_quiz()
        else:
            # もうクイズがない場合はアプリを終了する
            self.end_app()

    def end_app(self):
        '''アプリを終了する'''
        root.quit()
        exit()
        


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()