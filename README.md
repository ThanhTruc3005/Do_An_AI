# 🛠️ Hướng dẫn Setup Unity ML-Agents Toolkit



---

## 📋 1. Yêu cầu hệ thống (Prerequisites)
- **Unity Editor**: Phiên bản `2021.3 LTS` trở lên thông qua Unity Hud.
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


4. Kiểm tra cài đặt
Sau khi hoàn tất, hãy gõ lệnh sau trong Terminal (đã kích hoạt venv):

Bash
mlagents-learn --help
