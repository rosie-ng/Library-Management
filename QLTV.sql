
CREATE DATABASE QLTV
USE QLTV
CREATE TABLE Sach (
	MaSach VARCHAR(10) primary key,
	TenSach nvarchar(100),
	TacGia NVARCHAR(MAX),
	SoTrang INT,
	NgonNgu NVARCHAR(MAX),
	TheLoai NVARCHAR(MAX),
	NhaXuatBan NVARCHAR(MAX),
	TrangThai int
);
CREATE TABLE ThanhVien(
	MaThanhVien VARCHAR(10) PRIMARY KEY,
	TenThanhVien NVARCHAR(MAX),
	SoDienThoai VARCHAR(20),
);
CREATE TABLE MuonSach(
	MaSach VARCHAR(10),
	MaThanhVien VARCHAR(10),
	NgayMuon DATETIME,
	NgayTra DATETIME
	PRIMARY KEY (MaSach, MaThanhVien)
);
ALTER TABLE MuonSach ADD FOREIGN KEY (MaThanhVien) REFERENCES ThanhVien(MaThanhVien);
ALTER TABLE MuonSach ADD FOREIGN KEY (MaSach) REFERENCES Sach(MaSach);

INSERT INTO Sach  VALUES
	('S001V',N'Nhà giả kim',N'Paulo Coelho',225,N'Tiếng việt',N'Phiêu lưu', N'tưởng tượng', N'thần bí',N'Nhà xuất bản Hội nhà văn',0),
	('S002E',N'How to Win Friends and Influence People',N'Dale Carnegie',291,N'English',N'Sách tự lực',N'Simon and Schuster',0),
	('S003E',N'Think and Grow Rich',N'Napoleon Hill',238,N'English',N'Sách tự lực',N'The Ralston Society',0),
	('S004E',N'Người giàu có nhất thành Babylon',N'George Samuel Clason',144,N'English',N'Sách tự lực',N'Penguin Books',0),
	('S005V',N'Tội ác và hình phạt Tập 1',N'Fyodor Dostoevsky',462,N'Tiếng việt',N'Truyện ngắn',N'Phương Nam Book',0),
	('S006V',N'Tội ác và hình phạt Tập 2',N'Fyodor Dostoevsky',436,N'Tiếng việt',N'Truyện ngắn',N'Phương Nam Book',0),
	('S007V',N'Tam Quốc Diễn Nghĩa',N'La Quán Trung',1856,N'Tiếng việt',N'Tiểu thuyết',N'NXB Văn Học',0),
	('S008V',N'Vợ Nhặt',N'Kim Lân',232,N'Tiếng việt',N'Truyện ngắn',N'NXB Văn Học',0),
	('S009V',N'Làm Đĩ','Vũ Trọng Phụng',228,N'Tiếng việt',N'Truyện ngắn',N'NXB Văn Học',0),
	('S010V',N'Chí Phèo',N'Nam Cao',196,N'Tiếng việt',N'Truyện ngắn',N'NXB Văn Học',0),
	('S011V',N'Tắt Đèn',N'Ngô Tất Tố',184,N'Tiếng việt',N'Truyện ngắn',N'NXB Văn Học',0),
	('S012V',N'Kinh Dịch',N'Ngô Tất Tố',828,N'Tiếng việt',N'Triết học',N'NXB Văn Học',0),
	('S013V',N'Giáo Trình HSK 1',N'Khương Lệ Bình',141,N'Tiếng việt',N'Giáo trình',N'NXB Tổng Hợp TPHCM',0);

INSERT INTO ThanhVien VALUES
	('TV001',N'Lê Văn Cường','0978273826'),
	('TV002',N"Nguyễn Thị Cẩm Hồng",'0941627848'),
	('TV003',N'Lê Thanh Tuấn Vũ','0983726161'),
	('TV004',N'Trần Văn Nam','0946117283'),
	('TV005',N'Phan Ngọc Nữ','0912787382'),
	('TV006',N'Ngô Thành Đạt','0967829292'),
	('TV007',N'Phạm Tuyền','0923849097');
SELECT * FROM ThanhVien