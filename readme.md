# **Football Shoes Shop Backend**

## **Giới thiệu**
Dự án **Football Shoes Shop** là hệ thống backend REST API được xây dựng bằng **Django REST Framework** để quản lý một trang web bán giày bóng đá. Hệ thống hỗ trợ các chức năng như:
- Quản lý sản phẩm.
- Quản lý đơn hàng.
- Hỗ trợ nhiều loại người dùng: **Admin**, **Seller**, và **Buyer**.
- Phân quyền linh hoạt dựa trên **Group Permission**.
- Hỗ trợ xác thực người dùng với **JWT**.

---

## **Tính năng chính**
### **Người dùng (User Management)**
- **Admin**: Toàn quyền quản lý hệ thống, bao gồm:
  - Quản lý sản phẩm.
  - Quản lý người dùng.
  - Quản lý cả các đơn hàng.
- **Buyer**:
  - Đặt hàng.
  - Xem lịch sử mua hàng.

### **Quản lý sản phẩm (Product Management)**
- Danh sách sản phẩm.
- Tìm kiếm, lọc theo tên, giá, danh mục.
- Thêm, sửa, xóa sản phẩm (chỉ dành cho Seller và Admin).

### **Quản lý đơn hàng (Order Management)**
- Tạo đơn hàng.
- Xem trạng thái đơn hàng.
- Quản lý giao dịch.

---

## **Công nghệ sử dụng**
- **Backend Framework**: Django + Django REST Framework.
- **Database**: PostgreSQL.
- **Authentication**: JWT (JSON Web Token).
- **Access Control**: Group Permission-based Access Control (PBAC).

---

## **Yêu cầu hệ thống**
- **Python**: >= 3.10
- **PostgreSQL**: >= 12.0
- **Django**: >= 4.2
- **Django REST Framework**: >= 3.14
