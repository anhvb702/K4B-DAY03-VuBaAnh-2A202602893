"""
🔌 MODEL CONTEXT PROTOCOL (MCP) SERVER MODULE
Mô phỏng kiến trúc MCP Server (Client-Server Architecture) cung cấp công cụ chuẩn hóa.
"""

import json
import sys
from typing import Dict, Any, List
from tools import TOOLS_SCHEMA, dispatch_tool_call

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MCPAcademicServer:
    """
    Giả lập MCP Server tuân thủ chuẩn giao thức Model Context Protocol
    """
    def __init__(self, server_name: str = "vinuni-academic-mcp-server"):
        self.server_name = server_name
        self.version = "2026.1.0"
        
    def list_tools(self) -> List[Dict[str, Any]]:
        """Trả về danh sách các Tools chuẩn giao thức MCP"""
        return TOOLS_SCHEMA
        
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        [TASK 2.1] HỌC VIÊN HOÀN THIỆN HÀM THỰC THI TOOL TRÊN MCP SERVER
        Thực thi request gọi Tool theo chuẩn MCP JSON-RPC
        """
        # --------------------------------------------------------------------------
        # TODO 2.1: HỌC VIÊN HOÀN THIỆN HÀM GỌI TOOL CHUẨN MCP JSON-RPC
        # 🎯 YÊU CẦU THỰC THI THUẬT TOÁN:
        # 1. Gọi hàm dispatch_tool_call(tool_name, arguments) để lấy chuỗi JSON kết quả từ Tool Router.
        # 2. Chuyển đổi chuỗi JSON kết quả thành Python Dictionary (dùng json.loads).
        # 3. Đóng gói phản hồi và trả về Dict theo đúng chuẩn giao thức MCP JSON-RPC 2.0:
        #    - Các trường bắt buộc: "jsonrpc": "2.0", "server": self.server_name, "tool": tool_name, "result": content
        # --------------------------------------------------------------------------
        # 1. Gọi Tool Router và xử lý JSON
        tool_result_json = dispatch_tool_call(tool_name, arguments)
        
        # 2. Chuyển JSON sang Dictionary
        try:
            result_dict = json.loads(tool_result_json)
        except json.JSONDecodeError:
            # Fallback nếu format trả về không hoàn toàn là JSON
            result_dict = {"raw": tool_result_json}
            
        # 3. Đóng gói phản hồi chuẩn MCP JSON-RPC 2.0
        response = {
            "jsonrpc": "2.0",
            "server": self.server_name,
            "tool": tool_name,
            "result": result_dict
        }
        
        return response


if __name__ == "__main__":
    print("==========================================================")
    print("🔌 KIỂM THỬ ĐỘC LẬP MCP SERVER (vinuni-academic-mcp-server)")
    print("==========================================================")
    
    server = MCPAcademicServer()
    tools = server.list_tools()
    print(f"✅ Khởi tạo thành công MCP Server: {server.server_name} (Version: {server.version})")
    print(f"📦 Số lượng Tools công bố: {len(tools)}")
    
    # Kiểm tra trạng thái TODO 1.2 (Tool Schema)
    for tool_name in ["schedule_appointment", "tracking_delivery_id", "tracking_goods_place", "tracking_order_status"]:
        tool = next((t for t in tools if t.get("name") == tool_name), None)
        if tool:
            if not tool.get("parameters", {}).get("properties"):
                print(f"⏳ [TODO 1.2]: Tool '{tool_name}' chưa được định nghĩa properties trong 'src/tools.py'.")
            else:
                print(f"✅ [TODO 1.2]: Tool '{tool_name}' đã có schema đầy đủ.")

    # Kiểm tra trạng thái TODO 2.1 (call_tool)
    test_result_1 = server.call_tool("academic_query", {"student_id": "SV2026001"})
    if not test_result_1:
        print("⏳ [TODO 2.1]: Hàm call_tool() đang trả về rỗng. Học viên hãy hoàn thiện TODO 2.1 trong 'src/mcp_server.py'!")
    else:
        print(f"✅ [TODO 2.1]: Test dispatch tool 'academic_query' thành công:")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result_1, ensure_ascii=False)}")

    test_result_2 = server.call_tool("tracking_delivery_id", {"tracking_id": "123456789"})
    if not test_result_2:
        print("⏳ [TODO 2.1]: Hàm call_tool() đang trả về rỗng. Học viên hãy hoàn thiện TODO 2.1 trong 'src/mcp_server.py'!")
    else:
        print(f"✅ [TODO 2.1]: Test dispatch tool 'tracking_delivery_id' thành công:")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result_2, ensure_ascii=False)}")

    test_result_3 = server.call_tool("tracking_goods_place", {"tracking_id": "123456788"})
    if not test_result_3:
        print("⏳ [TODO 2.1]: Hàm call_tool() đang trả về rỗng. Học viên hãy hoàn thiện TODO 2.1 trong 'src/mcp_server.py'!")
    else:
        print(f"✅ [TODO 2.1]: Test dispatch tool 'tracking_goods_place' thành công:")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result_3, ensure_ascii=False)}")

    test_result_4 = server.call_tool("tracking_order_status", {"tracking_id": "123456788"})
    if not test_result_4:
        print("⏳ [TODO 2.1]: Hàm call_tool() đang trả về rỗng. Học viên hãy hoàn thiện TODO 2.1 trong 'src/mcp_server.py'!")
    else:
        print(f"✅ [TODO 2.1]: Test dispatch tool 'tracking_order_status' thành công:")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result_4, ensure_ascii=False)}")
