# HomeCare 🏡
### Smart Home Management System

HomeCare is a smart home management application designed to help users manage multiple properties, keep track of household appliances, organize important documents, and stay on top of preventive maintenance.

The goal is to provide a centralized platform where homeowners and family members can manage their household information efficiently.

---

## 📌 Project Overview

Managing multiple properties and household appliances can become difficult when information such as purchase dates, warranty periods, manuals, invoices, and maintenance schedules is scattered across different places.

HomeCare aims to solve this problem by bringing essential home management activities together in one application.

## ✨ Key Features

### 🏠 Property Management
- Manage multiple properties under one user account.
- Store property details such as address, city, state, and pincode.
- Support multiple members associated with a property.
- Assign property roles such as Owner and Member.

### 🔌 Appliance Management
- Organize appliances by category.
- Maintain appliance details, including brand and model number.
- Track purchase dates and warranty expiry dates.
- Store appliance-related documents.

### 🔧 Preventive Maintenance
- Plan regular maintenance activities.
- Keep track of upcoming maintenance requirements.
- Maintain appliance service history.

### 📄 Document Management
- Organize appliance manuals, invoices, and warranty documents.
- Keep important household records accessible in one place.

### 🔐 User Authentication
- User registration and login.
- Secure password hashing using Argon2.
- JWT-based authentication.
- Protected API endpoints.

*Note: Features listed as planned are under development.*

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Frontend | React Native |
| Framework | Expo |
| Language | TypeScript |
| Backend | Python |
| Backend Framework | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Data Validation | Pydantic |
| Authentication | JWT |
| Password Security | Argon2 |
| API Documentation | Swagger UI |

---

## 📂 Project Structure

```text
HomeCare/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── core.py
│   │   │   └── appliances.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auth.py
│   │   │   └── home.py
│   │   │
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   └── homes.py
│   │   │
│   │   ├── services/
│   │   │   ├── security.py
│   │   │   └── authentication.py
│   │   │
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── assets/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── constants/
│   │   └── hooks/
│   ├── app.json
│   └── package.json
│
├── database/
│
└── .gitignore
```

---

## ⚙️ Getting Started

Follow these instructions to run HomeCare locally.

### Prerequisites

Make sure you have installed:

- Python 3.11 or later
- Node.js and npm
- Git
- Visual Studio Code (recommended)
- Expo Go (for testing on a mobile device)

### 1. Clone the Repository

```bash
git clone https://github.com/GrishmaGudhka/HomeCare.git
cd HomeCare
```

### 2. Set Up the Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Configure your environment variables in a `.env` file using the variable names expected by `app/config.py`.

**Important:** Never upload your `.env` file or JWT secret to GitHub.

Start the backend server:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

### 3. Explore API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides interactive Swagger documentation for testing available API endpoints.

### 4. Set Up the Frontend

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Expo development server:

```bash
npx expo start
```

Scan the QR code using Expo Go to run the application on your mobile device.

---

## 🔗 Current API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Backend health check |
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate a user |
| GET | `/auth/me` | Get authenticated user details |
| POST | `/homes/` | Create a property |
| GET | `/homes/` | Retrieve user's properties |

**API documentation:** `http://127.0.0.1:8000/docs`

---

## 🗄️ Database Design

HomeCare uses SQLite with SQLAlchemy ORM.

The current database includes the following tables:

- `users`
- `homes`
- `home_members`
- `appliance_categories`
- `appliances`
- `appliance_documents`

The database structure supports multiple properties per user and allows multiple members to be associated with a property.

---

## 🔒 Security

Security is an important part of HomeCare.

The backend currently implements:

- Argon2 password hashing.
- JWT-based authentication.
- Protected routes using authenticated user information.
- Environment-based configuration for sensitive credentials.
- User account validation.

---

## 🚀 Development Roadmap

The project is being developed incrementally.

- [x] Initial React Native and Expo setup
- [x] FastAPI backend setup
- [x] SQLite database integration
- [x] SQLAlchemy database models
- [x] User registration and login
- [x] Argon2 password hashing
- [x] JWT authentication
- [x] Protected user profile endpoint
- [x] Property creation and listing APIs
- [ ] Complete appliance management APIs
- [ ] Appliance document upload and management
- [ ] Preventive maintenance scheduling
- [ ] Maintenance history tracking
- [ ] Expense tracking
- [ ] Service provider management
- [ ] Notifications and reminders
- [ ] Frontend and backend integration
- [ ] Testing and deployment

---

## 🎯 Project Goal

HomeCare aims to become a centralized home management solution that simplifies property management, appliance tracking, and preventive maintenance through a user-friendly mobile application.

---

## 👩‍💻 Developer

**Grishma Gudhka**

GitHub: [@GrishmaGudhka](https://github.com/GrishmaGudhka)

---

*HomeCare — Making home management smarter and simpler.*