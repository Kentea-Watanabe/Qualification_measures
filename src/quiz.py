# import csv
import random
import tkinter as tk
from tkinter import messagebox

import pandas as pd

# クイズの情報を格納したファイル
CSV_FILE = "..\workbook\sample.csv"


class Quiz():
    def __init__(self, master):
        '''コンストラクタ
            master:クイズ画面を配置するウィジェット
        '''

        # 親ウィジェット
        self.master = master

        # クイズデータリスト
        self.quiz_list = []

        # 現在表示中のクイズ
        self.now_quiz = None

        # 現在選択中の選択肢番号
        self.choice_value = tk.IntVar()

        self.getQuiz()
        self.createWidgets()
        self.showQuiz()

    def getQuiz(self):
        '''クイズの情報を取得する'''

        csv_data = pd.read_csv(CSV_FILE)

        # CSVの各行をリスト化
        for quiz in csv_data.itertuples():
            print(quiz)
            self.quiz_list.append(quiz)

    def createWidgets(self):
        '''ウィジェットを作成・配置する'''

        # フレームを作成する
        self.frame = tk.Frame(
            self.master,
            width=400,
            height=200,
        )
        self.frame.pack()

        # ボタンを作成する
        self.button = tk.Button(
            self.master,
            text="OK",
            command=self.checkAnswer
        )
        self.button.pack()

    def showQuiz(self):
        '''問題と選択肢を表示'''

        # まだ表示していないクイズからクイズ情報をランダムに取得
        num_quiz = random.randrange(len(self.quiz_list))
        quiz = self.quiz_list[num_quiz]

        # 問題を表示するラベルを作成
        self.problem = tk.Label(
            self.frame,
            text=quiz[1]
        )
        self.problem.grid(
            column=0,
            row=0,
            columnspan=4,
            pady=10
        )

        # 選択肢を表示するラジオボタンを４つ作成
        self.choices = []
        for i in range(1, 5):
            # ラジオボタンウィジェットを作成・配置
            choice = tk.Radiobutton(
                self.frame,
                text=quiz[i+1],
                variable=self.choice_value,
                value=i
            )
            choice.grid(
                row=1,
                column=i,
                padx=10,
                pady=10,
            )
            # ウィジェットを覚えておく
            self.choices.append(choice)

        # 表示したクイズは再度表示しないようにリストから削除
        self.quiz_list.remove(quiz)

        # 現在表示中のクイズを覚えておく
        self.now_quiz = quiz
        print(quiz)

    def deleteQuiz(self):
        '''問題と選択肢を削除'''

        # 問題を表示するラベルを削除
        self.problem.destroy()

        # 選択肢を表示するラジオボタンを削除
        for choice in self.choices:
            choice.destroy()

    def checkAnswer(self):
        '''解答が正解かどうかを表示し、次のクイズを表示する'''

        # 正解かどうかを確認してメッセージを表示
        if self.choice_value.get() == int(self.now_quiz[6]):
            messagebox.showinfo("結果", "正解です！！")
        else:
            messagebox.showerror("結果", "不正解です...")
            messagebox.showerror("正解は", str(self.choice_value.get()))

        # 表示中のクイズを非表示にする
        self.deleteQuiz()

        if self.quiz_list:
            # まだクイズがある場合は次のクイズを表示する
            self.showQuiz()
        else:
            # もうクイズがない場合はアプリを終了する
            self.endAppli()

    def endAppli(self):
        '''アプリを終了する'''

        # クイズがもうないことを表示
        self.problem = tk.Label(
            self.frame,
            text="クイズは全て出題ずみです"
        )
        self.problem.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )

        # OKボタンのcommandを変更
        self.button.config(
            command=self.master.destroy
        )

app = tk.Tk()
quiz = Quiz(app)
app.mainloop()