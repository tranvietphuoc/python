# -*-coding: utf-8 -*-
# import geopy
# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="my-application")

# location = geolocator.geocode("so 4 cuu long, phuong 2, tan binh, ho chi minh")
# print(location.address)
# print(location)

import re
import unicodedata
import gspread
from oauth2client.service_account import ServiceAccountCredentials
'''
Get town from a address string from gg sheets and write them to gg sheets

'''


# addr = u"59b duy tân , p5 tp tuy hòa phú yên"


hometown = "Yên Thủy|Yên Thế|Yên Thành|Yên Sơn|Yên Phong|Yên Mỹ|Yên Mô|Yên Minh|Yên Lập|Yên Lạc|Yên Khánh|Yên Định|Yên Dũng|Yên Châu|Yên Bình|Yên Bái|Ý Yên|Xuyên Mộc|Xuân Trường|Xuân Lộc|Xín Mần|Vũng Tàu|Vũng Liêm|Vụ Bản|Vũ Thư|Vũ Quang|Võ Nhai|Vĩnh Yên|Vĩnh Tường|Vĩnh Thuận|Vĩnh Thạnh|Vĩnh Thạnh|Vĩnh Lợi|Vĩnh Lộc|Vĩnh Long|Vĩnh Linh|Vĩnh Hưng|Vĩnh Cửu|Vĩnh Châu|Vĩnh Bảo|Vinh|Việt Yên|Việt Trì|Vị Xuyên|Vị Thủy|Vị Thanh|Vân Hồ|Vân Đồn|Vân Canh|Văn Yên|Văn Quan|Văn Lâm|Văn Lãng|Văn Giang|Văn Chấn|Văn Bàn|Vạn Ninh|Ứng Hòa|Uông Bí|U Minh Thượng|U Minh|Tương Dương|Từ Sơn|Tứ Kỳ|Tư Nghĩa|Tuyên Quang|Tuyên Hóa|Tuy Phước|Tuy Phong|Tuy Hòa|Tuy Đức|Tuy An|Tu Mơ Rông|Tuần Giáo|Tủa Chùa|Trường Sa|Trực Ninh|Trùng Khánh|Triệu Sơn|Triệu Phong|Tri Tôn|Trần Văn Thời|Trần Đề|Trấn Yên|Trảng Bom|Trảng Bàng|Tràng Định|Trạm Tấu|Trà Vinh|Trà Ôn|Trà Lĩnh|Trà Cú|Trà Bồng|Tịnh Biên|Tĩnh Gia|Tiểu Cần|Tiên Yên|Tiên Phước|Tiên Lữ|Tiên Lãng|Tiền Hải|Tiên Du|Thường Xuân|Thường Tín|Thủy Nguyên|Thuận Thành|Thuận Nam|Thuận Châu|Thuận Bắc|Thuận An|Thủ Thừa|Thủ Đức|Thủ Dầu Một|Thới Lai|Thới Bình|Thốt Nốt|Thống Nhất|Thông Nông|Thoại Sơn|Thọ Xuân|Thiệu Hóa|Thăng Bình|Tháp Mười|Thạnh Trị|Thạnh Phú|Thạnh Hóa|Thanh Xuân|Thanh Trì|Thanh Thủy|Thanh Sơn|Thanh Oai|Thanh Miện|Thanh Liêm|Thanh Khê|Thanh Hóa|Thanh Hà|Thanh Chương|Thanh Bình|Thanh Ba|Than Uyên|Thái Thụy|Thái Nguyên|Thái Hòa|Thái Bình|Thạch Thất|Thạch Thành|Thạch Hà|Thạch An|Tây Trà|Tây Sơn|Tây Ninh|Tây Hồ|Tây Hòa|Tây Giang|Tân Yên|Tân Uyên|Tân Uyên|Tân Trụ|Tân Thạnh|Tân Sơn|Tân Phước|Tân Phú Đông|Tân Phú|Tân Phú|Tân Lạc|Tân Kỳ|Tân Hưng|Tân Hồng|Tân Hiệp|Tân Châu|Tân Châu|Tân Bình|Tân Biên|Tân An|Tánh Linh|Tam Nông|Tam Nông|Tam Kỳ|Tam Đường|Tam Điệp|Tam Đảo|Tam Dương|Tam Bình|Sơn Trà|Sơn Tịnh|Sơn Tây|Sơn Tây|Sơn La|Sơn Hòa|Sơn Hà|Sơn Dương|Sơn Động|Sốp Cộp|Sông Mã|Sông Lô|Sông Hinh|Sông Công|Sông Cầu|Sóc Trăng|Sóc Sơn|Sìn Hồ|Si Ma Cai|Sầm Sơn|Sa Thầy|Sa Pa|Sa Đéc|Rạch Giá|Quỳnh Phụ|Quỳnh Nhai|Quỳnh Lưu|Quỳ Hợp|Quỳ Châu|Quốc Oai|Quy Nhơn|Quế Võ|Quế Sơn|Quế Phong|Quận 12|Quận 11|Quận 10|Quận 9|Quận 8|Quận 7|Quận 6|Quận 5|Quận 4|Quận 3|Quận 2|Quận 1|Quảng Xương|Quảng Uyên|Quảng Yên|Quảng Trị|Quảng Trạch|Quảng Ninh|Quảng Ngãi|Quảng Điền|Quang Bình|Quản Bạ|Quan Sơn|Quan Hóa|Pleiku|Phước Sơn|Phước Long|Phước Long|Phụng Hiệp|Phục Hòa|Phúc Yên|Phúc Thọ|Phủ Lý|Phù Yên|Phù Ninh|Phù Mỹ|Phù Cừ|Phù Cát|Phú Xuyên|Phú Vang|Phú Thọ|Phú Thiện|Phú Tân|Phú Tân|Phú Riềng|Phú Quốc|Phú Quý|Phú Ninh|Phú Nhuận|Phú Mỹ|Phú Lương|Phú Lộc|Phú Hòa|Phú Giáo|Phú Bình|Phổ Yên|Phong Thổ|Phong Điền|Phong Điền|Phan Thiết|Phan Rang-Tháp Chàm|Pác Nặm|Ô Môn|Núi Thành|Nông Sơn|Nông Cống|Ninh Sơn|Ninh Phước|Ninh Kiều|Ninh Hòa|Ninh Hải|Ninh Giang|Ninh Bình|Như Xuân|Như Thanh|Nhơn Trạch|Nho Quan|Nhà Bè|Nha Trang|Nguyên Bình|Ngũ Hành Sơn|Ngô Quyền|Ngọc Lặc|Ngọc Hồi|Ngọc Hiển|Nghĩa Lộ|Nghĩa Hưng|Nghĩa Hành|Nghĩa Đàn|Nghi Xuân|Nghi Lộc|Ngân Sơn|Ngã Năm|Ngã Bảy|Nga Sơn|Nậm Nhùn|Nậm Pồ|Năm Căn|Nam Từ Liêm|Nam Trực|Nam Trà My|Nam Sách|Nam Giang|Nam Đông|Nam Định|Nam Đàn|Na Rì|Na Hang|Mỹ Xuyên|Mỹ Tú|Mỹ Tho|Mỹ Lộc|Mỹ Hào|Mỹ Đức|Mường Tè|Mường Nhé|Mường Lay|Mường Lát|Mường La|Mường Khương|Mường Chà|Mường Ảng|Mù Cang Chải|Mộc Hóa|Mộc Châu|Mộ Đức|Móng Cái|Mỏ Cày Nam|Mỏ Cày Bắc|Minh Long|Minh Hóa|Mê Linh|Mèo Vạc|M'Đrăk|Mang Yang|Mang Thít|Mai Sơn|Mai Châu|Lý Sơn|Lý Nhân|Lương Tài|Lương Sơn|Lục Yên|Lục Ngạn|Lục Nam|Lộc Ninh|Lộc Hà|Lộc Bình|Long Xuyên|Long Thành|Long Phú|Long Mỹ|Long Mỹ|Long Khánh|Long Hồ|Long Điền|Long Biên|Liên Chiểu|Lệ Thủy|Lê Chân|Lập Thạch|Lấp Vò|Lâm Thao|Lâm Hà|Lâm Bình|Lắk|Lào Cai|Lạng Sơn|Lạng Giang|Lang Chánh|Lai Vung|Lai Châu|Lạc Thủy|Lạc Sơn|Lạc Dương|La Gi|Kỳ Sơn|Kỳ Anh|Kỳ Anh|Krông Pắk|Krông Pa|Krông Nô|Krông Năng|Krông Búk|Krông Bông|Krông Ana|Kông Chro|Kon Tum|Kon Rẫy|Kon Plông|Kinh Môn|Kim Thành|Kim Sơn|Kim Động|Kim Bôi|Kim Bảng|Kiến Tường|Kiến Xương|Kiến Thụy|Kiến An|Kiên Lương|Kiên Hải|Khoái Châu|Khánh Vĩnh|Khánh Sơn|Kế Sách|K'Bang|Ia Pa|Ia H'Drai|Ia Grai|Hữu Lũng|Hướng Hóa|Hương Trà|Hương Thủy|Hương Sơn|Hương Khê|Hưng Yên|Hưng Nguyên|Hưng Hà|Huế|Hồng Ngự|Hồng Ngự|Hồng Lĩnh|Hồng Dân|Hồng Bàng|Hội An|Hớn Quản|Hòn Đất|Hóc Môn|Hoằng Hóa|Hoàng Su Phì|Hoàng Sa|Hoàng Mai|Hoàng Mai|Hoàn Kiếm|Hoài Nhơn|Hoài Đức|Hoài Ân|Hòa Vang|Hòa Thành|Hoà Bình|Hoà Bình|Hòa An|Hoa Lư|Hiệp Hòa|Hiệp Đức|Hậu Lộc|Hàm Yên|Hàm Thuận Nam|Hàm Thuận Bắc|Hàm Tân|Hải Lăng|Hải Hậu|Hải Hà|Hải Dương|Hải Châu|Hải An|Hai Bà Trưng|Hạ Long|Hạ Lang|Hạ Hòa|Hà Trung|Hà Tĩnh|Hà Tiên|Hà Quảng|Hà Giang|Hà Đông|Gò Vấp|Gò Quao|Gò Dầu|Gò Công Tây|Gò Công Đông|Gò Công|Giồng Trôm|Giồng Riềng|Gio Linh|Giao Thủy|Giang Thành|Giá Rai|Gia Viễn|Gia Nghĩa|Gia Lộc|Gia Lâm|Gia Bình|Ea Súp|Ea Kar|Ea H'leo|Đức Trọng|Đức Thọ|Đức Phổ|Đức Linh|Đức Huệ|Đức Hòa|Đức Cơ|Đơn Dương|Đống Đa|Đồng Xuân|Đồng Xoài|Đồng Văn|Đồng Phú|Đồng Hỷ|Đồng Hới|Đông Triều|Đông Sơn|Đông Hưng|Đông Hòa|Đông Hải|Đông Hà|Đông Giang|Đông Anh|Đồ Sơn|Đô Lương|Đoan Hùng|Định Quán|Định Hóa|Đình Lập|Điện Biên Phủ|Điện Biên Đông|Điện Biên|Điện Bàn|Đất Đỏ|Đam Rông|Đầm Hà|Đầm Dơi|Đắk Tô|Đắk Song|Đắk R'lấp|Đắk Mil|Đắk Hà|Đắk Glong|Đắk Glei|Đan Phượng|Đak Pơ|Đắk Đoa|Đại Từ|Đại Lộc|Đạ Tẻh|Đạ Huoai|Đà Lạt|Đà Bắc|Đa Krông|Dương Minh Châu|Dương Kinh|Duyên Hải|Duyên Hải|Duy Xuyên|Duy Tiên|Diễn Châu|Diên Khánh|Dĩ An|Di Linh|Dầu Tiếng|Cửa Lò|Cư M'gar|Cư Jút|Cư Kuin|Củ Chi|Cù Lao Dung|Cờ Đỏ|Cồn Cỏ|Côn Đảo|Cô Tô|Con Cuông|Chương Mỹ|Chư Sê|Chư Pưh|Chư Prông|Chư Păh|Chơn Thành|Chợ Mới|Chợ Mới|Chợ Lách|Chợ Gạo|Chợ Đồn|Chiêm Hóa|Chí Linh|Chi Lăng|Châu Thành A|Châu Thành|Châu Thành|Châu Thành|Châu Thành|Châu Thành|Châu Thành|Châu Thành|Châu Thành|Châu Thành|Châu Thành|Châu Phú|Châu Đức|Châu Đốc|Cầu Ngang|Cầu Kè|Cầu Giấy|Cần Giuộc|Cần Giờ|Cần Đước|Cẩm Xuyên|Cẩm Thủy|Cẩm Phả|Cẩm Mỹ|Cẩm Lệ|Cẩm Khê|Cẩm Giàng|Cát Tiên|Cát Hải|Cao Phong|Cao Lộc|Cao Lãnh|Cao Lãnh|Cao Bằng|Càng Long|Can Lộc|Cam Ranh|Cam Lộ|Cam Lâm|Cái Răng|Cái Nước|Cái Bè|Cai Lậy|Cai Lậy|Cà Mau|Buôn Ma Thuột|Buôn Hồ|Buôn Đôn|Bù Gia Mập|Bù Đốp|Bù Đăng|Bố Trạch|Bình Xuyên|Bình Thủy|Bình Thạnh|Bình Tân|Bình Tân|Bình Sơn|Bình Minh|Bình Lục|Bình Long|Bình Liêu|Bình Giang|Bình Gia|Bình Đại|Bình Chánh|Bỉm Sơn|Biên Hòa|Bến Tre|Bến Lức|Bến Cầu|Bến Cát|Bắc Yên|Bắc Từ Liêm|Bắc Trà My|Bắc Tân Uyên|Bắc Sơn|Bắc Quang|Bắc Ninh|Bắc Mê|Bắc Kạn|Bắc Hà|Bắc Giang|Bắc Bình|Bàu Bàng|Bát Xát|Bảo Yên|Bảo Thắng|Bảo Lộc|Bảo Lâm|Bảo Lâm|Bảo Lạc|Bạch Thông|Bạch Long Vĩ|Bạc Liêu|Bác Ái|Bá Thước|Bà Rịa|Ba Vì|Ba Tri|Ba Tơ|Ba Đồn|Ba Đình|Ba Chẽ|Ba Bể|Ân Thi|Ayun Pa|Anh Sơn|An Phú|An Nhơn|An Minh|An Lão|An Lão|An Khê|An Dương|An Biên|A Lưới"

town_pattern = hometown.replace(' ', '[ ]')

pattern = unicodedata.normalize('NFKD', town_pattern).encode('utf-8')  # convert unicode string to raw
# print(pattern)
reg = re.compile(pattern.decode('utf-8'), re.I)
# print(reg.search(unicodedata.normalize('NFKD', addr)).group())

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('./prettyTown-fa1b06e865ad.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open('Test').sheet1

address = wks.col_values(1)  # get address from the first column
town = wks.col_values(1)
# print(address)
# print(len(address))
for i in range(1,len(address)+1):
    wks.update_cell(i+1, 2, reg.search(unicodedata.normalize('NFKD', address[i])).group())
# print(wks.get_all_records())