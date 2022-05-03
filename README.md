# Dino Project (Pygame07)
> For educational purposes, not for economic purposes<br />
> Language: Vi<br />
> Preview at the end of this post<br />
## Giới thiệu:
- Dino Game là một tựa game được tích hợp trong Chrome ở trường hợp không có kết nối internet
- Tựa game gốc (chỉ mở ở Chrome hoặc ít nhất là những ứng dụng dùng nhân Chromium): [Dino Game](chrome://dino)

### Yêu cầu:

- Nền tảng được hỗ trợ: Windows / Linux / MacOS (11.0+, 10.0 + chưa test)
- Yêu cầu: python3 + pygame (pip)
**0. Changelog:**
- 03/5/2022:
- [x] Sửa các lỗi về điểm / kỉ lục / json
- [x] Sửa lỗi FPS đối với main - dddt.py (Windows)
- [x] Encrypt Source Code
- 20/4/2022:
- [x] File lưu tiến trình người chơi (highest score)
- 24/4/2022:
- [x] Beta DDDT: thử nghiệm nhảy dao động điều hòa của game (main-dddt.py)
> Lưu ý! DDDT hiện tại đang chưa ổn định, bài nộp chính vẫn là main.py
- [x] Giới hạn fps bằng pygame.display:
- [x] Hỗ trợ native với Mac OS (hoạt động tốt ở BigSur & Monterey (yêu cầu python 3.x))
- 28/4/2022:
- [x] Fix bug kông hiện fps trong debug
- [x] Tăng chỉ số điểm (+0.5 thay vì 0.1 như trước)
- [x] Ngưng sử dụng vsync (tránh gặp giới hạn fps ở Windows)
- [x] Hỗ trợ linux(test ở Ubuntu / Pop!OS)
- Lưu ý! Ở riêng MacOS (Test ở Monterey), khung hình đang bị giới hạn ở 60 fps(lỗi) và sẽ được sửa trong thời gian tới. 

**1.Theo bài cô:**
- [x] Thay đổi 2 ảnh liên tiếp của khủng long (dino1.png và dino2.png trong ./Asset/dino)
- [x] Nhảy lên cao nếu ấn phím [Space] (thêm sử dụng phím [W] và [UP])
- [x] Hạ xuống trước khi nhảy
- [x] Cây xương rồng tạo ra và di chuyển liên tiếp (obstacle.png trong ./Asset/obstacle)
- [x] Phát âm thanh khi con khủng long chạm vào cây xương rồng.

**2.Chức năng thêm:**
- [x] Seed (các ngẫu nhiên trong game dựa trên 1 seed)
- [x] Map di chuyển
- [x] Mây
- [x] Con chim ở trên đầu (2 trạng thái) 
- [x] Trạng thái duck(cúi xuống) của khủng long.
- [x] Nhảy theo quán tính (Đang cải tiến)
- [x] Restart game / Reset player
- [x] Đầy đủ sound giống như ở bản gốc (100 coins / dead sound)
- [x] 6 trạng thái của khủng long (ngoài dino1 và dino2)
- [x] Personal best! (Điểm cao nhất)
- [x] File lưu tiến trùnh người chơi (highest score)
- [x] Cải tiến nhảy của khủng long (Theo dao dộng điều hoà) - Beta
- [ ] \(Optional) Sáng/tối trong game (cần sử dụng alpha)


**4. Sources:**
- Asset: https://github.com/codewmax/chrome-dinosaur/tree/master/Assets
- Sound: Me

