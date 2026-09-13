# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Vũ Bá Anh  
> **Mã Sinh Viên / Mã Học viên:** 2A202602893  
> **Chủ đề Lựa chọn:** Trợ lý Đơn hàng & Kho vận (Supply Chain Agent)  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4/ 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 5/ 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 4/ 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 4/ 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | **17/ 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin vận đơn có mã Order #1.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "tracking_delivery_id",
    "arguments": {
      "tracking_id": "Order #1"
    },
    "observation": {
      "status": "SUCCESS",
      "tracking_id": "Order #1",
      "data": {
        "order_id": "Order #1",
        "name": "Điện thoại",
        "price": 1000000,
        "quantity": 10,
        "tracking_id": "123456789",
        "status": "Đang giao hàng",
        "place": "Hà Nội",
        "datetime": "2026-09-13 12:00:00"
      }
    },
    "latency_ms": 4047.49
  },
  {
    "step": 2,
    "query": "Hãy tra cứu thông tin vận đơn có mã Order #1.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Thông tin đơn hàng Order #1 (Mã vận đơn: 123456789): Sản phẩm: Điện thoại, Giá: 1,000,000 VNĐ, Số lượng: 10, Trạng thái: Đang giao hàng, Địa điểm: Hà Nội, Thời gian: 2026-09-13 12:00:00.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (OpenAI / Gemini).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 5 / 5 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã hoàn thiện toàn bộ mã nguồn và sẵn sàng Commit / Push lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
