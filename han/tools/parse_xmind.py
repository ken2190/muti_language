from xmindparser import xmind_to_dict
import tkinter as tk
from tkinter import filedialog


class ParseXmind:
    # 统计文件中用例数
    def count_case(self, li):
        for i in range(len(li)):
            if li[i].__contains__('topics'):  # 带topics标签意味着有子标题，递归执行方法
                self.count_case(li[i]['topics'])
            else:  # 不带topics意味着无子标题，此级别既是用例
                # print(li[i]['title'])
                if li[i].__contains__('makers'):  # 有标记成功或失败时会有makers标签
                    if li[i]['makers'].__contains__('task-done'):  # 标记成功的
                        self.case_success += 1
                    elif li[i]['makers'].__contains__('symbol-wrong'):  # 标记失败的
                        self.case_fail += 1
                    elif li[i]['makers'].__contains__('symbol-code'):  # 标记阻塞的
                        self.case_block += 1
                self.count += 1  # 用例总数
                # print(self.count)

     # 用例统计表新增一行
    def new_line(self, filename, row_number):
        self.count = 0
        self.case_fail = 0
        self.case_success = 0
        self.case_block = 0
        # 调用python中xmind_to_dict方法,将xmind转成字典
        self.sheets = xmind_to_dict(filename)  # sheets是一个list，可包含多sheet页；
        for sheet in self.sheets:
            print(sheet)
            self.my_list = sheet['topic']['topics']  # 字典的值sheet['topic']['topics']是一个list
            # print(my_list)
            self.count_case(self.my_list)

        # 插入一行统计数据
        lastname = filename.split('/')
        self.label_file = tk.Label(self.frm2, text=lastname[-1], relief='groove', borderwidth='2', width=25)
        self.label_file.grid(row=row_number, column=0)
        self.label_case = tk.Label(self.frm2, text=self.count, relief='groove', borderwidth='2', width=10)
        self.label_case.grid(row=row_number, column=1)
        self.label_pass = tk.Label(self.frm2, text=self.case_success, relief='groove', borderwidth='2', width=10)
        self.label_pass.grid(row=row_number, column=2)
        self.label_fail = tk.Label(self.frm2, text=self.case_fail, relief='groove', borderwidth='2', width=10)
        self.label_fail.grid(row=row_number, column=3)
        self.label_block = tk.Label(self.frm2, text=self.case_block, relief='groove', borderwidth='2', width=10)
        self.label_block.grid(row=row_number, column=4)
        self.total_cases += self.count
        self.total_success += self.case_success
        self.total_fail += self.case_fail
        self.total_block += self.case_block

    # 用例统计表新增多行
    def new_lines(self):
        # total汇总用
        self.total_cases = 0
        self.total_success = 0
        self.total_fail = 0
        self.total_block = 0

        lines = self.text.get(1.0, tk.END)  # 从text中获取所有行
        row_number = 2
        for line in lines.splitlines():  # 分隔成每行
            if line == '':
                break
            print(line)
            self.new_line(line, row_number)
            row_number += 1

        # total汇总行
        self.label_file = tk.Label(self.frm2, text='total', relief='groove', borderwidth='2', width=25)
        self.label_file.grid(row=row_number, column=0)
        self.label_case = tk.Label(self.frm2, text=self.total_cases, relief='groove', borderwidth='2', width=10)
        self.label_case.grid(row=row_number, column=1)
        self.label_pass = tk.Label(self.frm2, text=self.total_success, relief='groove', borderwidth='2', width=10)
        self.label_pass.grid(row=row_number, column=2)
        self.label_fail = tk.Label(self.frm2, text=self.total_fail, relief='groove', borderwidth='2', width=10)
        self.label_fail.grid(row=row_number, column=3)
        self.label_block = tk.Label(self.frm2, text=self.total_block, relief='groove', borderwidth='2', width=10)
        self.label_block.grid(row=row_number, column=4)

    # 上传多个文件，并插入text中
    def upload_files(self):
        select_files = tk.filedialog.askopenfilenames(title="可选择1个或多个文件")
        for file in select_files:
            self.text.insert(tk.END, file + '')
            self.text.update()

    def __init__(self, root):
        # GUI
        root.title('Xmind用例个数统计')
        width = 570
        height = 500
        xscreen = root.winfo_screenwidth()
        yscreen = root.winfo_screenheight()
        xmiddle = (xscreen - width)/2
        ymiddle = (yscreen - height)/2
        root.geometry('%dx%d+%d+%d' % (width, height, xmiddle, ymiddle))

        self.frm1 = tk.Frame(root)
        self.frm2 = tk.Frame(root)
        self.frm1.grid(row=0, padx='20', pady='20')
        self.frm2.grid(row=1, padx='30', pady='30')

        self.but_upload = tk.Button(self.frm1, text='上传xmind文件', command=self.upload_files, bg='#dfdfdf')
        self.but_upload.grid(row=0, column=0, pady='10')
        self.text = tk.Text(self.frm1, width=55, height=10, bg='#f0f0f0')
        self.text.grid(row=1, column=0)
        self.but2 = tk.Button(self.frm2, text="开始统计", command=self.new_lines, bg='#dfdfdf')
        self.but2.grid(row=0, columnspan=5, pady='10')
        self.label_file = tk.Label(self.frm2, text="文件名", relief='groove', borderwidth='2', width=25, bg='#FFD0A2')
        self.label_file.grid(row=1, column=0)
        self.label_case = tk.Label(self.frm2, text="用例数", relief='groove', borderwidth='2', width=10, bg='#FFD0A2').grid(row=1, column=1)
        self.label_pass = tk.Label(self.frm2, text="成功", relief='groove', borderwidth='2', width=10, bg='#FFD0A2').grid(row=1, column=2)
        self.label_fail = tk.Label(self.frm2, text="失败", relief='groove', borderwidth='2', width=10, bg='#FFD0A2').grid(row=1, column=3)
        self.label_block = tk.Label(self.frm2, text="阻塞", relief='groove', borderwidth='2', width=10, bg='#FFD0A2').grid(row=1, column=4)

root = tk.Tk()
ParseXmind(root)
root.mainloop()