"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Đã được định nghĩa mẫu sẵn cho Học viên tham khảo
    {
        "name": "academic_query",
        "description": "Tra cứu hồ sơ và thông tin học vụ của sinh viên VinUni bằng mã sinh viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu (ví dụ: 'SV2026001')"
                }
            },
            "required": ["student_id"]
        }
    },
    
    {
        "name": "schedule_appointment",
        "description": "Đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn (ví dụ: '14:00 15/09/2026')"
                },
                "advisor_name": {
                    "type": "string",
                    "description": "Tên cố vấn học tập"
                }
            },
            "required": ["student_id", "datetime_str"]
        }
    },
    {
        "name": "tracking_delivery_id",
        "description": "Tìm kiếm thông tin vận đơn bằng mã vận đơn hoặc mã đơn hàng.",
        "parameters": {
            "type": "object",
            "properties": {
                "tracking_id": {
                    "type": "string",
                    "description": "Mã vận đơn hoặc mã đơn hàng cần tra cứu (ví dụ: '123456789' hoặc 'Order #1')"
                }
            },
            "required": ["tracking_id"]
        }
    },
    {
        "name": "tracking_goods_place",
        "description": "Tìm kiếm địa chỉ kho hàng hoặc nơi giao hàng bằng mã vận đơn hoặc mã đơn hàng.",
        "parameters": {
            "type": "object",
            "properties": {
                "tracking_id": {
                    "type": "string",
                    "description": "Mã vận đơn hoặc mã đơn hàng cần tra cứu (ví dụ: '123456789' hoặc 'Order #1')"
                }
            },
            "required": ["tracking_id"]
        }
    },
    {
        "name": "tracking_order_status",
        "description": "Kiểm tra trạng thái đơn hàng bằng mã vận đơn hoặc mã đơn hàng.",
        "parameters": {
            "type": "object",
            "properties": {
                "tracking_id": {
                    "type": "string",
                    "description": "Mã vận đơn hoặc mã đơn hàng cần tra cứu (ví dụ: '123456789' hoặc 'Order #1')"
                }
            },
            "required": ["tracking_id"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "SV2026001": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A"
    },
    "SV2026002": {
        "full_name": "Trần Thị Bình",
        "class": "AI-K4",
        "gpa": 3.60,
        "email": "binh.tt@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "TS. Lê Thị B"
    },
    "123456789": {
        "order_id": "Order #1",
        "name": "Điện thoại",
        "price": 1000000,
        "quantity": 10,
        "tracking_id": "123456789",
        "status": "Đang giao hàng",
        "place": "Hà Nội",
        "datetime": "2026-09-13 12:00:00"
    },
    "123456788": {
        "order_id": "Order #2",
        "name": "Máy tính xách tay",
        "price": 2000000,
        "quantity": 20,
        "tracking_id": "123456788",
        "status": "Đang giao hàng",
        "place": "Hà Nội",
        "datetime": "2026-09-13 12:00:00"
    }
}

def _find_order(tracking_id: str):
    """Tìm đơn hàng thông minh theo tracking_id, order_id hoặc mã số đơn"""
    if not tracking_id:
        return None
    tid = str(tracking_id).strip()
    if tid in MOCK_DATABASE and "order_id" in MOCK_DATABASE[tid]:
        return MOCK_DATABASE[tid]
    tid_lower = tid.lower()
    for item in MOCK_DATABASE.values():
        if not isinstance(item, dict) or "order_id" not in item:
            continue
        if item.get("tracking_id", "").lower() == tid_lower:
            return item
        if item.get("order_id", "").lower() == tid_lower:
            return item
        cleaned_order = item.get("order_id", "").lower().replace("order", "").replace("#", "").strip()
        cleaned_tid = tid_lower.replace("order", "").replace("#", "").strip()
        if cleaned_order == cleaned_tid:
            return item
    return None

def tracking_delivery_id(tracking_id: str) -> str:
    """Thực thi tra cứu vận đơn theo mã vận đơn"""
    order = _find_order(tracking_id)
    if order:
        return json.dumps({
            "status": "SUCCESS",
            "tracking_id": tracking_id,
            "data": order
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu vận đơn có mã '{tracking_id}'"
        }, ensure_ascii=False)

def tracking_goods_place(tracking_id: str) -> str:
    """Thực thi tra cứu địa chỉ kho theo mã vận đơn"""
    order = _find_order(tracking_id)
    if order:
        return json.dumps({
            "status": "SUCCESS",
            "tracking_id": tracking_id,
            "data": order
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu kho có mã '{tracking_id}'"
        }, ensure_ascii=False)

def tracking_order_status(tracking_id: str) -> str:
    """Thực thi tra cứu trạng thái đơn hàng theo mã vận đơn"""
    order = _find_order(tracking_id)
    if order:
        return json.dumps({
            "status": "SUCCESS",
            "tracking_id": tracking_id,
            "data": order
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu đơn hàng có mã '{tracking_id}'"
        }, ensure_ascii=False)

def execute_academic_query(student_id: str) -> str:
    """Thực thi tra cứu học vụ theo mã sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if student:
        return json.dumps({
            "status": "SUCCESS",
            "student_id": student_id,
            "data": student
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)


def execute_schedule_appointment(student_id: str, datetime_str: str, advisor_name: str = "PGS.TS Nguyễn Văn A") -> str:
    """Thực thi đặt lịch hẹn tư vấn học vụ"""
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-{student_id}-99",
        "student_id": student_id,
        "datetime": datetime_str,
        "advisor": advisor_name,
        "message": f"Đặt lịch thành công cho sinh viên {student_id} với {advisor_name} vào lúc {datetime_str}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "academic_query": execute_academic_query,
    "schedule_appointment": execute_schedule_appointment,
    "tracking_delivery_id": tracking_delivery_id,
    "tracking_goods_place": tracking_goods_place,
    "tracking_order_status": tracking_order_status
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
