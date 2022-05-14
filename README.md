# Dino Project (Pygame07)
> For educational purposes, not for economic purposes<br />
> Language: Vi<br />
> Preview at the end of this post<br />
> Supported OS: Windows / Mac OS (python3) / Linux <br />
## Giới thiệu:
- Dino Game là một tựa game được tích hợp trong Chrome ở trường hợp không có kết nối internet
- Tựa game gốc (chỉ mở ở Chrome hoặc ít nhất là những ứng dụng dùng nhân Chromium): [Dino Game](chrome://dino)

## Yêu cầu:

### 0. Changelog:

- **10/5/2022 LTS 100522 (1.1.3):**
- [x] Darkmode được kích hoạt ở Configurator.exe
- [x] Các Variable sẽ ấn khi người chơi không ở Dev mode
```
[+] Thử nghiệm: Darkmode
[+] Debug-hotkey: Thêm [F2] để chỉnh light/dark liên tục
```

- **10/5/2022 LTS 100522 (1.1.3):**
- [x] Thay thế Seed Configurator bằng Configurator 
- [x] Configurator sử dụng GUI, thêm Dev Mode để thử nghiệm những tính năng mới
- [x] Chỉ sử dụng [F3] để debug
- [x] Thêm lock_fps, dev, version và debug-hotkey trong save_game.json 
```
[+] Thử nghiệm: Mở khoá FPS cho game (chưa hoạt động)
```
- **9/5/2022 LTS 090522 (1.1.2):**
- [x] Thêm Custom Seed cho người chơi (Sử dụng Seed Configurator.exe)
- [x] Thêm Seed ở debug
- [x] Tối ưu tốc độ khủng long dựa trên số điểm
- [x] Sửa lỗi tự động tắt debug khi chơi lượt mới
```
[!] main - dddt và main - old sẽ KHÔNG sử dụng được Seed Configurator. Chỉ bản main mới chạy được*
[+] Đồng bộ điểm của main - dddt và main - old vẫn hoạt động ở save-game.json
```

- **7/5/2022 LTS 070522 (1.1.1):**
- [x] Hotfix: Tốc độ người chơi giữ nguyên ở lượt chơi sau (obs_speed error)
- [x] Chỉnh tốc độ tăng điểm lên 0.2/frame
- [x] Thêm Current Build Date, last_check_score ở debug
 
- **6/5/2022 LTS 0605229 (1.1)*:**
- [x] Thêm chế độ Debug [F3] [F4]
- [x] Sửa lỗi animation bird, duck
- [x] Sửa lỗi trùng vật thể spawn (có thể)
- [x] Huỷ bỏ DDDT do không phù hợp
- [x] Tắt decrypt, encrypt
- [x] Chỉnh sử tốc độ, cân bằng
- [x] Chức năng chạy nhanh theo số điểm đã được sửa (đối với tất cả hệ điều hành)
- [x] Khoá game ở 60 fps (sử dụng phương thức chạy nhanh khác vì độ ổn định kém)
- [x] Sử dụng .exe để chạy trên Windows, MacOS cần Source Code
- [x] Darkmode (Dev Unlocked Only)  
- **20/4/2022: Pre-Release**
- [x] File lưu tiến trình người chơi (highest score)
- **03/5/2022: Pre-Release**
- [x] Sửa các lỗi về điểm / kỉ lục / json
- [x] Sửa lỗi FPS đối với main - dddt.py (Windows)
- [x] Encrypt Source Code (Decrypt SC .exe)
- [x] Thêm tính năng tốc độ chạy tỉ lệ với số điểm hiện có (Windows Supported) 
- **28/4/2022: Beta**
- [x] Fix bug kông hiện fps trong debug
- [x] Tăng chỉ số điểm (+0.5 thay vì 0.1 như trước)
- [x] Ngưng sử dụng vsync (tránh gặp giới hạn fps ở Windows)
- [x] Hỗ trợ linux(test ở Ubuntu / Pop!OS)
- Lưu ý! Ở riêng MacOS (Test ở Monterey), khung hình đang bị giới hạn ở 60 fps(lỗi) và sẽ được sửa trong thời gian tới.
- **24/4/2022 Beta**:
- [x] Beta DDDT: thử nghiệm nhảy dao động điều hòa của game (main-dddt.py)
- [x] Giới hạn fps bằng pygame.display:
- [x] Hỗ trợ native với Mac OS (hoạt động tốt ở BigSur & Monterey (yêu cầu python 3.x)) 

### 1.Theo đề bài:
- [x] Thay đổi 2 ảnh liên tiếp của khủng long (dino1.png và dino2.png trong ./Asset/dino)
- [x] Nhảy lên cao nếu ấn phím [Space] (thêm sử dụng phím [W] và [UP])
- [x] Hạ xuống trước khi nhảy
- [x] Cây xương rồng tạo ra và di chuyển liên tiếp (obstacle.png trong ./Asset/obstacle)
- [x] Phát âm thanh khi con khủng long chạm vào cây xương rồng.

### 2.Thêm:
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


### 3. Sources:
- Asset: https://github.com/codewmax/chrome-dinosaur/tree/master/Assets
- Sound: Me

