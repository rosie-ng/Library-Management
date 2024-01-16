from tkinter import *
from tkinter import messagebox
from MSSQLConnection import MSSQLConnection

conn = MSSQLConnection()
con = conn.connect()
cur = con.cursor()

class Modelqltv:
    def addMember(self, maThanhVien, tenThanhVien, soDienThoai):
        if (maThanhVien and tenThanhVien and soDienThoai != ""):
            try:
                query = "INSERT INTO ThanhVien (MaThanhVien,TenThanhVien,SoDienThoai) VALUES(?,?,?)"
                cur.execute(query, (maThanhVien, tenThanhVien, soDienThoai))
                con.commit()
                messagebox.showinfo("Success", "Thêm thành viên thành công", icon='info')

            except:
                messagebox.showerror("Error", "Thêm thành viên thất bại", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')
    def updateMember(self, maThanhVien, tenThanhVien, soDienThoai):
        if (maThanhVien and tenThanhVien and soDienThoai != ""):
            try:
                query = "UPDATE ThanhVien SET TenThanhVien=?,SoDienThoai=? WHERE MaThanhVien=?"
                cur.execute(query, (tenThanhVien, soDienThoai,maThanhVien))
                con.commit()
                messagebox.showinfo("Success", "Đã cập nhật thông tin thành viên", icon='info')

            except:
                messagebox.showerror("Error", "Không thể cập nhật thông tin thành viên", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')
    def deleteMember(self, maThanhVien):
        if (maThanhVien  != "") and (maThanhVien != "Vui lòng nhập mã thành viên"):
            try:
                query = "DELETE FROM ThanhVien WHERE MaThanhVien=?"
                cur.execute(query, (maThanhVien))
                con.commit()
                messagebox.showinfo("Success", "Đã xóa thành viên", icon='info')

            except:
                messagebox.showerror("Error", "Không thể xóa thành viên", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')
    def addBook(self,maSach, tenSach, tacGia, soTrang,ngonNgu, theLoai, nhaXuatBan, trangThai):
        if (maSach and tenSach and tacGia and soTrang and ngonNgu and theLoai and nhaXuatBan !=""):
            try:
                query="INSERT INTO Sach (MaSach, TenSach,TacGia,SoTrang,NgonNgu,TheLoai,NhaXuatBan,TrangThai) VALUES(?,?,?,?,?,?,?,?)"
                cur.execute(query,(maSach, tenSach, tacGia, soTrang, ngonNgu, theLoai, nhaXuatBan, trangThai))
                con.commit()
                messagebox.showinfo("Success","Đã thêm sách",icon='info')

            except:
                messagebox.showerror("Error","Không thể thêm sách",icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')

    def updateBook(self, maSach, tenSach, tacGia, soTrang, ngonNgu, theLoai, nhaXuatBan):
        if (maSach and tenSach and tacGia and soTrang and ngonNgu and theLoai and nhaXuatBan != ""):
            try:
                query = "UPDATE Sach SET TenSach=?, TacGia=?, SoTrang=?, NgonNgu=?, TheLoai=?, NhaXuatBan=? WHERE MaSach=?"
                cur.execute(query, (tenSach, tacGia, soTrang, ngonNgu, theLoai, nhaXuatBan, maSach))
                con.commit()
                messagebox.showinfo("Success", "Đã cập nhật thông tin sách", icon='info')
            except:
                messagebox.showerror("Error", "Không thể cập nhật thông tin sách", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cannot be empty", icon='warning')

    def deleteBook(self, maSach):
        if (maSach != "") and (maSach !="Vui lòng nhập mã sách"):
            try:
                query = "DELETE FROM Sach WHERE MaSach=?"
                cur.execute(query, (maSach))
                con.commit()
                messagebox.showinfo("Success", "Đã xóa sách", icon='info')

            except:
                messagebox.showerror("Error", "Không thể xóa sách", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')
    def lenbook(self, maSach, maThanhVien, ngayMuon):
        if (maSach and maThanhVien != ""):
            try:
                query = "INSERT INTO MuonSach (MaSach,MaThanhVien,NgayMuon, NgayTra) VALUES(?,?,?,NULL)"
                cur.execute(query, (maSach, maThanhVien, ngayMuon))
                con.commit()
                messagebox.showinfo("Success", "Mượn sách thành công!", icon='info')
                cur.execute("UPDATE Sach SET TrangThai =? WHERE MaSach=?", (1, maSach))
                con.commit()
            except:
                messagebox.showerror("Error", "Không thể mượn sách", icon='warning')

        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')
    def giveback(self, maSach, ngayTra):
        if (maSach != "") and (maSach != 'Nhập Sách'):
            try:
                cur.execute("UPDATE MuonSach SET NgayTra =? WHERE MaSach =?", (ngayTra, maSach))
                con.commit()
                messagebox.showinfo("Success", "Trả sách thành công!", icon='info')
                cur.execute("UPDATE Sach SET TrangThai =? WHERE MaSach=?", (0, maSach))
                con.commit()
            except:
                messagebox.showerror("Error", "Trả sách thất bại", icon='warning')

        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')

    def list_Book_all(self):
        query="SELECT * FROM Sach WHERE"
        books =cur.execute(query).fetchall()
        book_list=[]
        for book in books:
            book_list.append(str(book[0])+"-"+book[1])
        return book_list
    def books_list_in_library(self):
        query="SELECT * FROM Sach WHERE TrangThai=0"
        books =cur.execute(query).fetchall()
        book_list=[]
        for book in books:
            book_list.append(str(book[0])+"-"+book[1])
        return book_list
    def book_list_lending(self):
        query="SELECT * FROM Sach WHERE TrangThai=1"
        books =cur.execute(query).fetchall()
        book_list=[]
        for book in books:
            book_list.append(str(book[0])+"-"+book[1])
        return book_list
    def members_list(self):
        query2="SELECT * FROM ThanhVien"
        members = cur.execute(query2).fetchall()
        member_list=[]
        for member in members:
            member_list.append(str(member[0])+"-"+member[1])
        return member_list
    def listBooks(self, listChoice, list_books):
        value = listChoice.get()
        if value == 1:
            allbooks= cur.execute("SELECT * FROM Sach").fetchall()
            list_books.delete(0,END)

            count=0
            for book in allbooks:
                list_books.insert(count,str(book[0]) + "-"+book[1])
                count +=1

        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM Sach WHERE TrangThai =?",(0,)).fetchall()
            list_books.delete(0, END)

            count = 0
            for book in books_in_library:
                list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
        else:
            taken_books= cur.execute("SELECT * FROM Sach WHERE TrangThai =?",(1,)).fetchall()
            list_books.delete(0, END)

            count = 0
            for book in taken_books:
                list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1

    def searchBooks(self, value, list_books):
        search= cur.execute("SELECT * FROM Sach WHERE TenSach LIKE ?",('%'+value+'%',)).fetchall()
        print(search)
        list_books.delete(0,END)
        count=0
        for book in search:
            list_books.insert(count,str(book[0])+ "-"+book[1])
            count +=1