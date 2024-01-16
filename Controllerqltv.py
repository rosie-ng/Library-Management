from Viewqltv import Viewqltv
from  Modelqltv import Modelqltv
import Viewqltv
from MSSQLConnection import MSSQLConnection
from tkinter import *
conn = MSSQLConnection()
con = conn.connect()
cur = con.cursor()
class Controllerqltv:
    def __init__(self, model: Modelqltv, view: Viewqltv):
        self.model = model
        self.view = view

        self.view.list_books.bind('<Double-Button-1>', self.setBookTab)
        self.view.list_mem.bind('<Double-Button-1>',self.setMemberTab)
        self.view.tabs.bind('<ButtonRelease-1>', self.displayMember)
        self.view.tabs.bind('<ButtonRelease-1>', self.displayStatistics)
        self.view.tabs.bind('<<NotebookTabChanged>>', self.displayStatistics)
        self.view.tabs.bind('<<NotebookTabChanged>>', self.displayMember)
        self.view.tabs.bind('<<NotebookTabChanged>>', self.displayBooks)
        self.view.tabs.bind('<ButtonRelease-1>', self.displayBooks)
        self.displayMember(self)
        self.displayStatistics(self)

    def setMemberTab(self, evt):
        edit = Viewqltv.SetMember()
    def setBookTab(self, event):
        run = Viewqltv.SetBook()


    def displayMember(self, evt):
        members = cur.execute("SELECT * FROM ThanhVien").fetchall()
        count = 0

        self.view.list_mem.delete(0, END)
        for mem in members:
            self.view.list_mem.insert(count, str(mem[0]) + "-" + mem[1])
            count += 1

        def memberInfo(evt):
            if self.view.list_mem.curselection():
                value = str(self.view.list_mem.get(self.view.list_mem.curselection()))
                id = value.split('-')[0]
                lmem = cur.execute("SELECT * FROM ThanhVien WHERE MaThanhVien=?", (id,))
                mem_info = lmem.fetchall()
                self.view.mem_details.delete(0, 'end')
                self.view.mem_details.insert(0, "Tên Thành Viên : " + mem_info[0][1])
                self.view.mem_details.insert(1, "Số Điện Thoại : " + mem_info[0][2])

        self.view.list_mem.bind('<<ListboxSelect>>', memberInfo)

    def displayStatistics(self,evt):
        count_books = cur.execute("SELECT count(MaSach) FROM Sach").fetchall()
        count_members = cur.execute("SELECT count(MaThanhVien) FROM ThanhVien").fetchall()
        taken_books = cur.execute("SELECT count(TrangThai) FROM Sach WHERE TrangThai=1").fetchall()
        print(count_books)
        self.view.lbl_book_count.config(text='Tổng cộng:  ' + str(count_books[0][0]) + ' sách trong thư viện')
        self.view.lbl_member_count.config(text="Thành viên : " + str(count_members[0][0]))
        self.view.lbl_taken_count.config(text="Số sách đang cho mượn: " + str(taken_books[0][0]))


    def displayBooks(self,evt):
        books = cur.execute("SELECT * FROM Sach").fetchall()
        count = 0

        self.view.list_books.delete(0, END)
        for book in books:
            self.view.list_books.insert(count, str(book[0]) + "-" + book[1])
            count += 1


        def bookInfo(event):
            if self.view.list_books.curselection():
                value = str(self.view.list_books.get(self.view.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM Sach WHERE MaSach=?", (id,))
                book_info = book.fetchall()
                self.view.list_details.delete(0, 'end')
                self.view.list_details.insert(0, "Tên Sách : " + book_info[0][1])
                self.view.list_details.insert(1, "Tác Giả : " + book_info[0][2])
                self.view.list_details.insert(2, "Số Trang : " + str(book_info[0][3]))
                self.view.list_details.insert(3, "Ngôn Ngữ : " + book_info[0][4])
                self.view.list_details.insert(4, "Thể loại : " + book_info[0][5])
                self.view.list_details.insert(5, "Nhà Xuất Bản : " + book_info[0][6])
                self.view.list_details.insert(6, "Trạng Thái : " + str(book_info[0][7]))
                if book_info[0][7] == 1:
                    cur.execute(
                        "SELECT tv.TenThanhVien FROM ThanhVien tv JOIN MuonSach ms ON tv.MaThanhVien = ms.MaThanhVien WHERE ms.MaSach=?",
                        (id,))
                    muon = cur.fetchone()
                    self.view.list_details.insert(7, "Người mượn : " + str(muon[0]))

        self.view.list_books.bind('<<ListboxSelect>>', bookInfo)












