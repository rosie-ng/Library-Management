from tkinter import *
from tkinter import ttk, font
from Modelqltv import Modelqltv
from datetime import date

class Viewqltv():
    def __init__(self):
        self.root = Tk()
        self.root.title("Quản lý thư viện")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        #frames
        self.mainFrame=Frame(self.root)
        self.mainFrame.pack()
        #top frames

        #Left Frame
        LeftFrame= Frame(self.mainFrame,width=100,height=680,bg='#e0f0f0',borderwidth=2,relief='sunken')
        LeftFrame.pack(side=LEFT, fill=BOTH)
        #right frame
        RightFrame= Frame(self.mainFrame,width=1400,height=680,bg='#e0f0f0')
        RightFrame.pack(side=RIGHT,fill=BOTH)

        TopRightFrame= Frame(RightFrame,width=1400, height=40, bg='#e0f0f0')
        TopRightFrame.pack(side=TOP,fill=BOTH)
        BotRightFrame= Frame(RightFrame, width=1400, height=640,bg='#e0f0f0')
        BotRightFrame.pack(side=BOTTOM,fill=BOTH)
        #search bar
        search_bar =LabelFrame(LeftFrame,width=100,height=120,text='Khung tìm kiếm',bg='#008898')
        search_bar.pack(side=TOP,fill=BOTH)
        self.lbl_search=Label(search_bar,text='Tìm kiếm :', font='arial 12 bold',bg='#008898',fg='white')
        self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
        self.ent_search=Entry(search_bar,width=25,bd=10)
        self.ent_search.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
        self.btn_search=Button(search_bar,text='Tìm kiếm',font='arial 12',bg='#D9D9D9',fg='#000000',
                               command=self.call_searchBooks)
        self.btn_search.grid(row=0,column=3,padx=20,pady=10)

        #list bar
        list_bar = LabelFrame(LeftFrame, width=100, height=160, text='List Box', bg='#008898')
        list_bar.pack(fill=BOTH)

        lbl_list = Label(list_bar, text='Lọc theo', font='arial 16 bold', fg='#000000', bg='#008898')
        lbl_list.grid(row=0, column=0, padx=20, pady=5, sticky='w')

        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text='Tất cả sách', var=self.listChoice, value=1, bg='#008898')
        rb2 = Radiobutton(list_bar, text='Sách đang còn trong thư viện', var=self.listChoice, value=2, bg='#008898')
        rb3 = Radiobutton(list_bar, text='Sách đã cho mượn', var=self.listChoice, value=3, bg='#008898')
        rb1.grid(row=1, column=0, padx=20, pady=5, sticky='w')
        rb2.grid(row=2, column=0, padx=20, pady=5, sticky='w')
        rb3.grid(row=3, column=0, padx=20, pady=5, sticky='w')

        btn_list = Button(list_bar, text='Danh sách các quyển sách', bg='#0078D7', fg='white', font='arial 12',
                          command=self.call_listbooks)
        btn_list.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='w')

        #title and image
        image_bar=Frame(LeftFrame,width=100,height=400)
        image_bar.pack(fill=BOTH)
        self.title_right=Label(image_bar,text='Chào mừng đến với thư viện',font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library=PhotoImage(file='icons/library.png')
        self.lblImg=Label(image_bar,image=self.img_library)
        self.lblImg.grid(row=1)

        #Tool Bar########################################
        #add book
        self.iconbook=PhotoImage(file='icons/add_book.png')
        self.btnbook= Button(TopRightFrame,text='Sách',image=self.iconbook,compound=LEFT,
                             font='arial 12 bold',width=150, height=40,command=self.open_setbook)
        self.btnbook.pack(side=LEFT)
        #add member button
        self.iconmember= PhotoImage(file ='icons/users.png')
        self.btnmember=Button(TopRightFrame,text='Thành Viên',font='arial 12 bold',width=150, height=40,command=self.open_setmem)
        self.btnmember.configure(image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT)
        #give book
        self.icongive=PhotoImage(file ='icons/givebook.png')
        self.btngive=Button(TopRightFrame,text='Mượn Sách',font='arial 12 bold',image=self.icongive,compound=LEFT,width=150, height=40,command=self.open_givebook)
        self.btngive.pack(side=LEFT)
        #give back
        self.icongiveback=PhotoImage(file ='icons/givebook.png')
        self.btngiveback=Button(TopRightFrame,text='Trả Sách',font='arial 12 bold',
                            image=self.icongiveback,compound=LEFT,width=150, height=40,command=self.open_giveback)
        self.btngiveback.pack(side=LEFT)
######################################Tabs#########################################
            ###############tab1###############################
        self.tabs= ttk.Notebook(BotRightFrame,width=1400,height=680)
        self.tabs.pack()
        self.tab1_icon=PhotoImage(file='icons/books.png')
        self.tab2_icon=PhotoImage(file='icons/bold.png')
        self.tab3_icon=PhotoImage(file='icons/members.png')
        self.tab1=ttk.Frame(self.tabs)
        self.tab2=ttk.Frame(self.tabs)
        self.tab3=ttk.Frame(self.tabs)
        self.tabs.add(self.tab1,text='Quản lý thư viện', image=self.tab1_icon,compound=LEFT)
        self.tabs.add(self.tab2,text='Thông tin thành viên',image=self.tab2_icon,compound=LEFT)
        self.tabs.add(self.tab3,text='Thống kê',image=self.tab3_icon,compound=LEFT)

        #list books
        self.list_books= Listbox(self.tab1,width=50,height=30,bd=5,font='arial 12 bold')
        self.sb=Scrollbar(self.tab1,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_books.yview)

        self.list_books.config(yscrollcommand=self.sb.set)

        self.sb.grid(row=0,column=0,sticky=N+S+E)
        #list mem
        self.list_mem= Listbox(self.tab2,width=40,height=30,bd=5,font='arial 12 bold')
        self.sb=Scrollbar(self.tab2,orient=VERTICAL)
        self.list_mem.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_mem.yview)
        self.list_mem.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)
        #list details
        self.list_details=Listbox(self.tab1,width=80,height=30,bd=5,font='arial 12 bold')
        self.list_details.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)
        #mem details
        self.mem_details=Listbox(self.tab2,width=80,height=30,bd=5,font='arial 12 bold')
        self.mem_details.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)
        ##########################tab2####################################
        #statistics
        self.lbl_book_count= Label(self.tab3,text="adfafs",pady=20,font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count=Label(self.tab3,text="asdfadsf",pady=20,font='verdana 14 bold')
        self.lbl_member_count.grid(row=1,sticky=W)
        self.lbl_taken_count=Label(self.tab3,text="asdfdafd",pady=20,font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2,sticky=W)



    def open_givebook(self):
        giveback_window = GiveBook()
        giveback_window.mainloop()
    def open_giveback(self):
        giveback_window = GiveBack()
        giveback_window.mainloop()
    def open_setmem(self):
        giveback_window = SetMember()
        giveback_window.mainloop()
    def open_setbook(self):
        giveback_window = SetBook()
        giveback_window.mainloop()
    def call_searchBooks(self):
        value = self.ent_search.get()
        Modelqltv().searchBooks(value, self.list_books)
    def call_listbooks(self):
        Modelqltv().listBooks(self.listChoice, self.list_books)
    def start(self):
        self.root.mainloop()
class NewWindow(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Kích thước cửa sổ
        window_width = 500
        window_height = 550

        # Tính toán vị trí x và y để căn giữa cửa sổ
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Đặt vị trí và kích thước cửa sổ
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.title("Trả Sách")
        self.resizable(False, False)
        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=BOTH)
        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#008898')
        self.bottomFrame.pack(fill=BOTH)

class CustomEntry(Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.insert(0, self.placeholder)
        self.config(fg='gray', width=30, bd=4)

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, END)
            self.config(fg='black')

    def on_focus_out(self, event):
        if self.get() == '':
            self.insert(0, self.placeholder)
            self.config(fg='gray')



class CustomCombobox(ttk.Combobox):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.set_placeholder()
        self.config(width = 30, foreground = 'gray')

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.set('')
            self.config(foreground='gray')

    def on_focus_out(self, event):
        if self.get() == '':
            self.set_placeholder()
            self.config(foreground='gray')

    def set_placeholder(self):
        self.set(self.placeholder)
        self.config(foreground='gray')

    def get(self):
        value = super().get()
        if value == self.placeholder:
            return ''
        return value
class GiveBook(NewWindow):
    def __init__(self):
        super().__init__()
        self.title("Mượn Sách")
        self.resizable(False, False)



        book_list = Modelqltv().books_list_in_library()
        member_list = Modelqltv().members_list()

        #######################Frames#######################
        # heading, image
        self.top_image = PhotoImage(file='icons/addperson.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=100, y=10)
        heading = Label(self.topFrame, text='  Cho Mượn Sách ', font='arial 20 bold', fg='#003f8a', bg='white')
        heading.place(x=200, y=50)

        ###########################################Entries and Labels########################3

        # member name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text='Sách: ', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_name.place(x=40, y=40)
        self.combo_name = CustomCombobox(self.bottomFrame, placeholder='Nhập sách',textvariable=self.book_name)
        self.combo_name['values'] = book_list
        self.combo_name.place(x=150, y=45)

        # member
        self.member_name = StringVar()
        self.lbl_ThanhVien = Label(self.bottomFrame, text='Thành Viên: ', font='arial 12 bold', fg='white',
                                   bg='#008898')
        self.lbl_ThanhVien.place(x=40, y=80)
        self.combo_member = CustomCombobox(self.bottomFrame, placeholder='Nhập thành viên', textvariable=self.member_name)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=150, y=85)

        # Ngày Mượn
        self.Ngay_Muon = StringVar()
        self.lbl_NgayMuon = Label(self.bottomFrame, text='Ngày Mượn: ', font='arial 12 bold', fg='white',
                                  bg='#008898')
        self.lbl_NgayMuon.place(x=40, y=120)
        self.ent_NgayMuon = Entry(self.bottomFrame, width=32, bd=4)
        self.today = date.today()
        self.ent_NgayMuon.insert(0, str(self.today))
        self.ent_NgayMuon.place(x=150, y=125)
        # Button
        self.bntGiveBook = Button(self.bottomFrame, text='Cho mượn sách', command=self.call_GiveBook)
        self.bntGiveBook.place(x=211, y=200)

    def call_GiveBook(self):
        tenSach = self.book_name.get()
        self.maSach = tenSach.split('-')[0]
        tenThanhVien = self.member_name.get()
        self.maThanhVien = tenThanhVien.split('-')[0]
        ngayMuon = self.ent_NgayMuon.get()
        Modelqltv().lenbook(self.maSach, self.maThanhVien, ngayMuon)

class SetMember(NewWindow):
    def __init__(self):
        super().__init__()
        self.title("Thành viên")
        self.resizable(False,False)

        #heading, image
        self.top_image= PhotoImage(file='icons/addperson.png')
        top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
        top_image_lbl.place(x=110,y=10)
        heading=Label(self.topFrame, text='Thành viên',font='arial 22 bold',fg='#003f8a',bg='white')
        heading.place(x=210,y=50)

        ###########################################Entries and Labels########################3

        #member ID
        self.lbl_MaThanhVien = Label(self.bottomFrame, text='Mã Thành Viên :', font='arial 12 bold', fg='white',bg='#008898')
        self.lbl_MaThanhVien.place(x=40, y=40)
        self.ent_MaThanhVien = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập mã thành viên")
        self.ent_MaThanhVien.place(x=200, y=45)
        #member name
        self.lbl_TenThanhVien=Label(self.bottomFrame,text='Tên Thành Viên :',font='arial 12 bold',fg='white',bg='#008898')
        self.lbl_TenThanhVien.place(x=40,y=80)
        self.ent_TenThanhVien = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập tên thành viên")
        self.ent_TenThanhVien.place(x=200,y=85)
        # phone
        self.lbl_SDT = Label(self.bottomFrame, text='Số Điện Thoại :', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_SDT.place(x=40, y=120)
        self.ent_SDT = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập số điện thoại")
        self.ent_SDT.place(x=200, y=125)
        #Button
        self.buttonAdd=Button(self.bottomFrame,text='Thêm thành viên', command=self.call_addMember)
        self.buttonAdd.place(x=170,y=180)
        self.buttonUpdate=Button(self.bottomFrame,text='Cập nhật',command=self.call_updateMember)
        self.buttonUpdate.place(x=290,y=180)
        self.buttonDel=Button(self.bottomFrame,text='Xóa thành viên', command=self.call_deleteMember)
        self.buttonDel.place(x=370,y=180)


    def call_addMember(self):
        maThanhVien = self.ent_MaThanhVien.get()
        tenThanhVien = self.ent_TenThanhVien.get()
        soDienThoai = self.ent_SDT.get()
        Modelqltv().addMember(maThanhVien, tenThanhVien, soDienThoai)

    def call_updateMember(self):
        maThanhVien = self.ent_MaThanhVien.get()
        tenThanhVien = self.ent_TenThanhVien.get()
        soDienThoai = self.ent_SDT.get()
        Modelqltv().updateMember(maThanhVien, tenThanhVien, soDienThoai)

    def call_deleteMember(self):
        maThanhVien = self.ent_MaThanhVien.get()
        Modelqltv().deleteMember(maThanhVien)
class SetBook(NewWindow):
    def __init__(self):
        super().__init__()

        self.title("Sách")
        self.resizable(False,False)

        #heading, image
        self.top_image= PhotoImage(file='icons/addbook.png')
        top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
        top_image_lbl.place(x=120,y=10)
        heading=Label(self.topFrame, text='Sách',font='arial 22 bold',fg='#003f8a',bg='white')
        heading.place(x=270,y=60)

        ###########################################Entries and Labels########################3
        #ID
        self.lbl_MaSach = Label(self.bottomFrame, text='Mã Sách :', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_MaSach.place(x=40, y=40)
        self.ent_MaSach = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập mã sách")
        self.ent_MaSach.place(x=150, y=45)

        #name
        self.lbl_TenSach=Label(self.bottomFrame,text='Tên Sách :',font='arial 12 bold',fg='white',bg='#008898')
        self.lbl_TenSach.place(x=40,y=80)
        self.ent_TenSach = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập tên sách")
        self.ent_TenSach.place(x=150,y=85)

        # author
        self.lbl_TacGia = Label(self.bottomFrame, text='Tác Giả :', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_TacGia.place(x=40, y=120)
        self.ent_TacGia = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập tác giả")
        self.ent_TacGia.place(x=150, y=125)

        # page
        self.lbl_SoTrang = Label(self.bottomFrame, text='Số Trang :', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_SoTrang.place(x=40, y=160)
        self.ent_SoTrang = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập số trang")
        self.ent_SoTrang.place(x=150, y=165)

        # language
        self.lbl_NgonNgu = Label(self.bottomFrame, text='Ngôn Ngữ :', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_NgonNgu.place(x=40, y=200)
        self.ent_NgonNgu = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập ngôn ngữ")
        self.ent_NgonNgu.place(x=150, y=205)

        #Thể Loại
        self.lbl_TheLoai = Label(self.bottomFrame, text='Thể Loại :', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_TheLoai.place(x=40, y=240)
        self.ent_TheLoai = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập thể loại")
        self.ent_TheLoai.place(x=150, y=245)

        #Nhà Xuất Bản
        self.lbl_NXB = Label(self.bottomFrame, text='Nhà Xuất Bản :', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_NXB.place(x=40, y=280)
        self.ent_NXB = CustomEntry(self.bottomFrame,  placeholder="Vui lòng nhập nhà xuất bản")
        self.ent_NXB.place(x=150, y=285)

        #Button
        self.buttonAddBook=Button(self.bottomFrame,text='Thêm', command=self.call_addBook)
        self.buttonAddBook.place(x=120,y=350)
        self.buttonUpdateBook=Button(self.bottomFrame,text='Cập nhật', command=self.call_updateBook)
        self.buttonUpdateBook.place(x=220,y=350)
        self.buttonDelBook=Button(self.bottomFrame,text='Xóa', command=self.call_deleteBook)
        self.buttonDelBook.place(x=340,y=350)

    def call_addBook(self):
        self.maSach = self.ent_MaSach.get()
        self.tenSach = self.ent_TenSach.get()
        self.tacGia = self.ent_TacGia.get()
        self.soTrang = self.ent_SoTrang.get()
        self.ngonNgu = self.ent_NgonNgu.get()
        self.theLoai = self.ent_TheLoai.get()
        self.nhaXuatBan = self.ent_NXB.get()
        self.trangThai = 0
        Modelqltv().addBook(self.maSach, self.tenSach, self.tacGia, self.soTrang, self.ngonNgu, self.theLoai, self.nhaXuatBan, self.trangThai)

    def call_updateBook(self):
        self.maSach = self.ent_MaSach.get()
        self.tenSach = self.ent_TenSach.get()
        self.tacGia = self.ent_TacGia.get()
        self.soTrang = self.ent_SoTrang.get()
        self.ngonNgu = self.ent_NgonNgu.get()
        self.theLoai = self.ent_TheLoai.get()
        self.nhaXuatBan = self.ent_NXB.get()
        Modelqltv().updateBook(self.maSach, self.tenSach, self.tacGia, self.soTrang, self.ngonNgu, self.theLoai, self.nhaXuatBan)

    def call_deleteBook(self):
        self.maSach = self.ent_MaSach.get()
        Modelqltv().deleteBook(self.maSach)
class GiveBack(NewWindow):
    def __init__(self):
        super().__init__()

        book_list = Modelqltv().book_list_lending()

        # heading, image
        self.top_image = PhotoImage(file='icons/addperson.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=110, y=10)
        heading = Label(self.topFrame, text='  Trả Sách ', font='arial 20 bold', fg='#003f8a', bg='white')
        heading.place(x=210, y=50)

        ###########################################Entries and Labels########################3

        # book name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text='Sách: ', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_name.place(x=40, y=40)
        self.combo_name = CustomCombobox(self.bottomFrame, placeholder='Nhập Sách', textvariable=self.book_name)
        self.combo_name['values'] = book_list
        self.combo_name.place(x=150, y=45)
        # Ngày Trả
        self.Ngay_Tra = StringVar()
        self.lbl_Ngay_Tra = Label(self.bottomFrame, text='Ngày Trả: ', font='arial 12 bold', fg='white', bg='#008898')
        self.lbl_Ngay_Tra.place(x=40, y=90)
        self.ent_Ngay_Tra = CustomEntry(self.bottomFrame,  placeholder='')
        self.ent_Ngay_Tra = Entry(self.bottomFrame, width=32, bd=4)
        self.today = date.today()
        self.ent_Ngay_Tra.insert(0, str(self.today))
        self.ent_Ngay_Tra.place(x=150, y=90)
        # Button
        self.buttonGiveBack = Button(self.bottomFrame, text='Trả sách', command=self.call_giveback)
        self.buttonGiveBack.place(x=220, y=160)

    def call_giveback(self):
        tenSach = self.book_name.get()
        self.maSach = tenSach.split('-')[0]
        ngayTra = self.ent_Ngay_Tra.get()
        Modelqltv().giveback(self.maSach, ngayTra)
