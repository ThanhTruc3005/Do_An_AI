# 📜 LUẬT HUẤN LUYỆN AI (REWARD LOGIC & RULES)

**Người thiết kế luật (AI/Logic):** Hùng
**Người code C# (Unity):** Trúc

File này quy định toàn bộ hệ thống Thưởng (+), Phạt (-) và các thiết lập thông số cho chiếc xe AI trong Unity. Bất cứ khi nào Hùng cập nhật luật mới, Trúc sẽ dựa vào đây để sửa file `CarAgent.cs`.

---

## 1. HỆ THỐNG HÀNH ĐỘNG (ACTIONS)
Trong component `Behavior Parameters` của xe, setup như sau:
- **Continuous Actions (Size = 2):**
  - Index `[0]`: Chân Ga / Phanh (Giá trị từ -1.0 đến 1.0)
  - Index `[1]`: Bẻ lái Trái / Phải (Giá trị từ -1.0 đến 1.0)
- **Discrete Actions (Size = 1, Branch 0 Size = 3):**
  - Giá trị `0`: Tắt xi nhan
  - Giá trị `1`: Bật xi nhan TRÁI
  - Giá trị `2`: Bật xi nhan PHẢI

---

## 2. HỆ THỐNG CẢM BIẾN (RAYCAST SENSORS)
Tia Raycast là "mắt" của xe. Cần add đủ các Tag này vào `Detectable Tags` trong Inspector:
- `Wall`: Tường, lề đường, vỉa hè, các vật cản tĩnh.
- `Target`: Điểm đích đến (khối tàng hình).
- `NPCVehicle`: Các xe cộ khác đang chạy trên đường.
- `Pedestrian`: Người đi bộ.
- `RedLight`: Đèn đỏ (Chỉ xuất hiện khi đèn chuyển đỏ).
- `GreenLight`: Đèn xanh.

---

## 3. MA TRẬN THƯỞNG / PHẠT (REWARD MATRIX)

Trúc viết các logic này vào hàm `OnCollisionEnter`, `OnTriggerEnter`, và `OnActionReceived` / `FixedUpdate`.

### 🟢 Nhóm Thưởng (Khuyến khích làm)
| Hành vi | Thưởng | Kết thúc ván (EndEpisode)? | Ghi chú |
| :--- | :---: | :---: | :--- |
| **Đến đích (Chạm Tag `Target`)** | `+2.0f` | **CÓ** | Mục tiêu tối thượng của game. |
| **Đỗ chờ đèn đỏ** | `+0.05f` | KHÔNG | Cộng liên tục (mỗi step) khi tia quét trúng `RedLight` VÀ vận tốc xe == 0. |
| **Bật đúng Xi nhan** | `+0.5f` | KHÔNG | Khi xe đi vào `TurnZone` và check Action rời rạc khớp với hướng rẽ. |
| **Di chuyển đúng hướng** | `+0.01f` | KHÔNG | Cộng nhẹ khi xe tiến về phía đích (vận tốc > 0). |

### 🔴 Nhóm Phạt (Cấm tuyệt đối)
| Hành vi | Phạt | Kết thúc ván (EndEpisode)? | Ghi chú |
| :--- | :---: | :---: | :--- |
| **Tông Tường / Lề đường (`Wall`)** | `-1.0f` | **CÓ** | Reset ngay để tránh kẹt map. |
| **Tông Xe Khác (`NPCVehicle`)** | `-1.0f` | **CÓ** | Ép AI học cách lách và né xe. |
| **Tông Người đi bộ (`Pedestrian`)**| `-5.0f` | **CÓ** | Phạt CỰC NẶNG (Luật số 1). |
| **Vượt Đèn Đỏ** | `-1.0f` | **CÓ** | Quét trúng `RedLight` MÀ đi qua vạch ngã tư (vận tốc > 0). |
| **Quá Tốc Độ (Speeding)** | `-0.01f` | KHÔNG | Trừ liên tục (mỗi step) nếu `vận tốc > 15f`. |
| **Quên / Bật sai Xi nhan** | `-0.2f` | KHÔNG | Trừ điểm khi nằm trong `TurnZone` mà bật sai hoặc không bật. |

---

## 4. LƯU Ý KHI CODE
- Dùng `Time.fixedDeltaTime` cho mọi di chuyển vật lý.
- Vận tốc đo bằng `rb.velocity.magnitude`.
- Khi gọi `EndEpisode()`, nhớ viết thêm logic reset xe về lại `Vạch xuất phát (Start)` trong hàm `OnEpisodeBegin()`.