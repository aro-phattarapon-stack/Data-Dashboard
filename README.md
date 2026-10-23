# Web Log Analytics Pipeline & Dashboard

สร้างข้อมูล web logs จำลองและเก็บไว้ที่ access.log
หลังจากนั้นนำข้อมูลมาทำความสะอาดผ่านกระบวนการ Data Pipeline จัดเก็บลงฐานข้อมูลใน SQLite
และนำเสนอข้อมูลเป็นภาพให้เข้าใจง่ายด้วย streamlit Framework ใน app.py

## Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas
* **Database:** SQLite3
* **Web Dashboard:** Streamlit

## Data Pipeline Workflow
1. **Data Generation (`generate_logs.py`):**
   * จำลองไฟล์บันทึกการเข้าใช้เว็บไซต์ (`access.log`) ตามรูปแบบ Common Log Format
2. **ETL & Storage (`logs.py`):**
   * อ่านข้อมูลดิบ สกัดฟิลด์สำคัญ ทำความสะอาดข้อความ และแปลงประเภทข้อมูล (Data Type Casting)
   * บันทึกข้อมูลลงฐานข้อมูลเชิงสัมพันธ์ **SQLite** (`logs.db`) รองรับ Primary Key แบบ Auto-increment
3. **Analytics & Visualization (`app.py`):**
   * ดึงข้อมูลผ่าน Pandas เพื่อคำนวณ KPI สรุปผล (Total Requests, Errors, Data Size)
   * แสดงผลตารางข้อมูลและแปลงตัวเลขเป็นแผนภาพด้วย **Streamlit**

## Start & Installation
### ติดตั้ง Dependencies ที่จำเป็น
pip install streamlit pandas

### เปิดใช้งานหน้า Dashboard
streamlit run app.py

## Project Structure
```
├── access.log        # ไฟล์ Raw Web Logs จำลอง
├── generate_logs.py  # สคริปต์สุ่มสร้าง Mock Data
├── logs.py           # สคริปต์ Parsing ทำความสะอาด และบันทึกลง SQLite
├── logs.db           # ฐานข้อมูล SQLite ที่จัดเก็บข้อมูลพร้อมใช้งาน
├── app.py            # สคริปต์หน้า Dashboard ของ Streamlit
└── README.md         # เอกสารอธิบายโปรเจกต์
```