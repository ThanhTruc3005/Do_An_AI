```powershell
# 1. Tạo môi trường ảo với Python 3.10 (Bắt buộc dùng bản 3.10)
`py -3.10 -m venv .venv`

# 2. Kích hoạt môi trường
`.venv\Scripts\activate`
# Cài PyTorch (Cơ bắp tính toán)
`pip install torch torchvision torchaudio`

# Cài Unity ML-Agents (Bộ não)
`pip install mlagents`

# Ép version Protobuf (BẮT BUỘC để fix lỗi giao tiếp giữa C# và Python)
`pip install protobuf==3.20.3`