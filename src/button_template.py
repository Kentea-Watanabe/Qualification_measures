import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("ボタンの作成(Windowsスタイル)")     # ウィンドウタイトル
        self.master.geometry("580x580")       # ウィンドウサイズ(幅x高さ)

        # ボタンの作成
        button1 = tk.Button(self.master, text = "ボタン")
        # クリックイベントの指定
        button2 = tk.Button(self.master, text = "クリック", 
                            command = self.button_click # クリック時に呼び出されるメソッド名
                            )
        # 無効ボタン
        button3 = tk.Button(self.master, text = "無効ボタン",
                            state = tk.DISABLED # 無効：tk.DISABLED　有効：tk.NORMAL
                            )
        # ボタンサイズ
        button4 = tk.Button(self.master, text = "ボタンサイズ", 
                            width = 20, height = 2      # サイズは文字数で指定
                            )
        # フォントサイズ
        button5 = tk.Button(self.master, text = "フォントサイズ", 
                            font = ("", 18) # フォントサイズの変更
                            )
        # ボタンスタイル
        button6 = tk.Button(self.master, text = "RAISED", 
                            relief = tk.RAISED      
                            )
        button7 = tk.Button(self.master, text = "GROOVE", 
                            relief = tk.GROOVE      
                            )
        button8 = tk.Button(self.master, text = "SUNKEN", 
                            relief = tk.SUNKEN      # 凹んだ状態（クリックはできる）
                            )
        button9 = tk.Button(self.master, text = "RIDGE", 
                            relief = tk.RIDGE      
                            )
        button10 = tk.Button(self.master, text = "FLAT", 
                            relief = tk.RIDGE      
                            )

        # 文字の位置
        button11 = tk.Button(self.master, text = "NW", 
                            width = 10, height = 2,
                            anchor = tk.NW 
                            )
        button12 = tk.Button(self.master, text = "N", 
                            width = 10, height = 2,
                            anchor = tk.N
                            )
        button13 = tk.Button(self.master, text = "NE", 
                            width = 10, height = 2,
                            anchor = tk.NE
                            )
        button14 = tk.Button(self.master, text = "W", 
                            width = 10, height = 2,
                            anchor = tk.W
                            )
        button15 = tk.Button(self.master, text = "CENTER", 
                            width = 10, height = 2,
                            anchor = tk.CENTER
                            )
        button16 = tk.Button(self.master, text = "E", 
                            width = 10, height = 2,
                            anchor = tk.E
                            )
        button17 = tk.Button(self.master, text = "SW", 
                            width = 10, height = 2,
                            anchor = tk.SW
                            )
        button18 = tk.Button(self.master, text = "S", 
                            width = 10, height = 2,
                            anchor = tk.S
                            )
        button19 = tk.Button(self.master, text = "SE", 
                            width = 10, height = 2,
                            anchor = tk.SE
                            )

        # 文字の左寄せ
        button20 = tk.Button(self.master, text = "o文字左寄せo\noo文字左寄せoo\nooo文字左寄せooo", 
                            width = 25, height = 3,
                            justify = tk.LEFT
                            )       
        
        # 文字の中央寄せ
        button21 = tk.Button(self.master, text = "o文字中央寄せo\noo文字中央寄せoo\nooo文字中央寄せooo", 
                            width = 25, height = 3,
                            justify = tk.CENTER
                            )

        # 文字の右寄せ
        button22 = tk.Button(self.master, text = "o文字右寄せo\noo文字右寄せoo\nooo文字右寄せooo", 
                            width = 25, height = 3,
                            justify = tk.RIGHT
                            )

        # 枠線幅
        button23 = tk.Button(self.master, text = "枠線幅2", 
                            bd = 2
                            )
        button24 = tk.Button(self.master, text = "枠線幅4", 
                            bd = 4
                            )
        button25 = tk.Button(self.master, text = "枠線幅6", 
                            bd = 6
                            )
        # 横方向のパディング（文字列の両側の隙間）
        button26 = tk.Button(self.master, text = "padx=2", 
                            padx = 2
                            )
        button27 = tk.Button(self.master, text = "padx=10", 
                            padx = 10
                            )
        button28 = tk.Button(self.master, text = "padx=20", 
                            padx = 20
                            )
        # 縦方向のパディング（文字列の上下の隙間）
        button29 = tk.Button(self.master, text = "pady=2", 
                            pady = 2
                            )
        button30 = tk.Button(self.master, text = "pady=10", 
                            pady = 10
                            )
        button31 = tk.Button(self.master, text = "pady=20", 
                            pady = 20
                            )
        # 横、縦方向のパディング組み合わせ
        button32 = tk.Button(self.master, text = "padx=20\npady=10", 
                            padx = 20, pady = 10
                            )
        # wraplength
        button33 = tk.Button(self.master, text = "wraplength文字の折り返し幅", 
                            wraplength = 60
                            )

        # 色の変更
        button34 = tk.Button(self.master, text = "色の変更", 
                            bg = "#00ff00", # 通常時の背景色
                            fg = "#ff00ff", # 通常時の文字色
                            activebackground = "#ff0000", # クリックされた時の背景色
                            activeforeground = "#0000ff"  # クリックされた時の文字色
                            )
        # ハイライトカラー
        button35 = tk.Button(self.master, text = "ハイライトカラー",  # 無効？
                            highlightcolor = "#ffff00" # ハイライトカラー
                            )
        # アンダーライン(１文字)
        button36 = tk.Button(self.master, text = "アンダーライン(１文字)", 
                            underline = 2      # 2番目（0始まり）の文字にアンダーライン、-1で無し
                            ) 
        # アンダーライン(全文字)
        button37 = tk.Button(self.master, text = "アンダーライン（全文字）", 
                            font = ("", 9, "underline")      # 文字全体のアンダーラインはfontで指定
                            ) 

        # ボタンの配置
        button1.grid(row=0, column=0)
        button2.grid(row=0, column=1)
        button3.grid(row=0, column=2)

        button4.grid(row=1, column=0)
        button5.grid(row=1, column=1)

        button6.grid(row=2, column=0)
        button7.grid(row=2, column=1)
        button8.grid(row=2, column=2)
        button9.grid(row=3, column=0)
        button10.grid(row=3, column=1)

        button11.grid(row=4, column=0)
        button12.grid(row=4, column=1)
        button13.grid(row=4, column=2)
        button14.grid(row=5, column=0)
        button15.grid(row=5, column=1)
        button16.grid(row=5, column=2)
        button17.grid(row=6, column=0)
        button18.grid(row=6, column=1)
        button19.grid(row=6, column=2)

        button20.grid(row=7, column=0)
        button21.grid(row=7, column=1)
        button22.grid(row=7, column=2)

        button23.grid(row=8, column=0)
        button24.grid(row=8, column=1)
        button25.grid(row=8, column=2)

        button26.grid(row=9, column=0)
        button27.grid(row=9, column=1)
        button28.grid(row=9, column=2)

        button29.grid(row=10, column=0)
        button30.grid(row=10, column=1)
        button31.grid(row=10, column=2)
        button32.grid(row=11, column=0)

        button33.grid(row=12, column=0)
        button34.grid(row=12, column=1)
        button35.grid(row=12, column=2)

        button36.grid(row=13, column=0)
        button37.grid(row=13, column=1)

    def button_click(self):
        print("ボタンがクリックされた")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()