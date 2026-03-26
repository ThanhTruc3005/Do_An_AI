# Clone repo này về trước:
vào thư mục cần lưu -> git clone https://github.com/ThanhTruc3005/Do_An_AI.git

# 🛠️ Hướng dẫn Setup Unity ML-Agents Toolkit

Tài liệu này hướng dẫn các thành viên team **CTU** thiết lập môi trường để bắt đầu dự án. Vui lòng cài đặt theo đúng thứ tự bên dưới.

---

## 📋 1. Yêu cầu hệ thống (Prerequisites)
- **Unity Editor**: Phiên bản `2021.3 LTS` trở lên.
- **Python**: Phiên bản `3.8.x` đến `3.10.x` (Khuyến nghị **3.10.11**).
- **Git**: Để clone và quản lý mã nguồn.

---

## 🛠️ 2. Các bước cài đặt chi tiết

### Bước 1: Thiết lập môi trường ảo Python
Mở Terminal/PowerShell và thực hiện các lệnh sau:
```bash
# Tạo môi trường ảo (Virtual Environment)
python -m venv ml-agents

# Kích hoạt môi trường (Windows)
ml-agents\Scripts\activate

# Cài đặt PyTorch (Bản CPU - Ổn định nhất cho đa số máy)
pip3 install torch torchvision torchaudio

# Cài đặt bộ công cụ ML-Agents
pip3 install mlagents


Bước 2: Cài đặt SDK trong Unity
Mở dự án bằng Unity Hub.

Trên thanh menu, chọn Window > Package Manager.

Nhấn dấu + (góc trái trên) > Add package by name...

Nhập chính xác dòng sau: com.unity.ml-agents và nhấn Add.
4. Kiểm tra cài đặt
Sau khi hoàn tất, hãy gõ lệnh sau trong Terminal (đã kích hoạt venv):

Bash
mlagents-learn --help
