#  Modular User Authentication System with Input Validation

## 📌 Tech Stack
- **Backend:** Django (Python)  
- **Database:** SQLite (default, can switch to PostgreSQL/MySQL)  
- **Authentication:** Django Sessions / JWT  
- **Password Security:** PBKDF2 (default Django hasher, supports bcrypt)  
- **Email Verification:** Django Email Backend (console in dev, SMTP in prod)  

---

## ⚡ Setup & Run Instructions

### 1️⃣ Clone the repository
```bash
git clone <repo_url>
cd auth_system
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py migrate
```

### 5️⃣ Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server
```bash
python manage.py runserver
```

### 7️⃣ Access endpoints
- Register: `http://127.0.0.1:8000/auth/register/`  
- Login: `http://127.0.0.1:8000/auth/login/`  
- Logout: `http://127.0.0.1:8000/auth/logout/`  
- Admin Panel: `http://127.0.0.1:8000/admin/`  

---

##  Sample Test Credentials
After creating a superuser, you can log in with:  

```
Email: admin@example.com
Password: admin123
```

Or register a new user via `/auth/register/` and verify through the console email link.  

---

This project demonstrates modular coding with **routes, controllers, services, and middleware** while ensuring **secure authentication, validation, and password hashing**.  


## Project-Demo

## REGISTER ##
<img width="1386" height="701" alt="2" src="https://github.com/user-attachments/assets/5fec6756-8e42-4dae-9a64-c61898b4d168" />

## LOGIN ##
<img width="1393" height="783" alt="3" src="https://github.com/user-attachments/assets/d80ac950-0920-4ba2-b136-d5d1a5eb9427" />

## LOGOUT ##
<img width="1379" height="588" alt="4" src="https://github.com/user-attachments/assets/e8db0f63-7447-4844-b9fe-9c9ea0c19ab9" />

