# 🏦 Banking System Database Schema

A robust and secure **Banking System Database** designed for managing operations including branches, customers, accounts, transactions, users, loans, cards, and audit logging.
Did Optional Question 2 as a challenge but look at Question 1 as my main Project.
---

(./A_Entity-Relationship_Diagram_(ERD)_of_a_banking_d.png) ![image](https://github.com/user-attachments/assets/7ad3d353-967d-4e98-8d8d-e9435049d3c2)


---

## 📂 Database Overview

This schema supports essential banking operations and ensures data integrity, traceability, and relational coherence between tables.

### 📑 Main Features:
- Customer and account management
- Multiple account types and branches
- Transaction logging and audit trails
- Staff login sessions and access roles
- Loan and card management
- Multi-currency support

---

## 🧩 Tables Breakdown

### 🔹 Branches
Stores physical locations of bank branches.

| Field | Type | Description |
|-------|------|-------------|
| `branchId` | INT | Primary Key |
| `branchName` | VARCHAR | Branch Name |
| `branchLocation` | VARCHAR | Location |

---

### 👤 Customers
Holds user profiles of banking customers.

| Field | Type | Description |
|-------|------|-------------|
| `customerId` | INT | Primary Key |
| `fullName`, `email`, `phone`, `address` | VARCHAR | Personal Info |
| `date_Of_Birth` | DATE | DOB |
| `CreatedAt` | TIMESTAMP | Record timestamp |

---

### 🧾 AccountTypes
Types of accounts like savings, checking, etc.

| Field | Type |
|-------|------|
| `account_Type_Id` | INT (PK) |
| `typeName`, `Description` | VARCHAR |

---

### 💼 Accounts
Details each customer account.

| Field | Type |
|-------|------|
| `accountId` | INT (PK) |
| `customerId`, `account_Type_Id`, `branchId` | FK |
| `balance`, `createdAt` | DECIMAL, TIMESTAMP |

---

### 💸 Transactions
Logs deposits, withdrawals, and transfers.

| Field | Type |
|-------|------|
| `transactionId` | INT (PK) |
| `accountId` | FK |
| `amount`, `transactionType`, `transactionDate` | DECIMAL, ENUM, TIMESTAMP |

---

### 👨‍💼 Users (Staff)
Bank personnel accounts and roles.

| Field | Type |
|-------|------|
| `userId`, `fullName`, `email` | VARCHAR |
| `role` | ENUM('Admin', 'Teller', etc.) |
| `passwordHash`, `createdAt` | VARCHAR, TIMESTAMP |

---

### 💳 Cards
Issued debit/credit cards.

| Field | Type |
|-------|------|
| `cardId`, `accountId` | INT |
| `cardNumber`, `cardType`, `expiryDate`, `CVV` | VARCHAR, ENUM |

---

### 🧾 Loans
Customer loan records.

| Field | Type |
|-------|------|
| `loanId`, `customerId` | INT |
| `amount`, `interestRate`, `startDate`, `endDate`, `status` | DECIMAL, DATE, ENUM |

---

### 🔐 LoginSessions
Tracks staff login/logout activities.

| Field | Type |
|-------|------|
| `sessionId`, `userId` | INT |
| `loginTime`, `logoutTime`, `IPAddress` | TIMESTAMP, VARCHAR |

---

### 📜 TransactionLogs
Tracks changes/actions to transactions.

---

### 🕵️ AuditLogs
Monitors internal data changes for transparency.

---

### 💱 Currencies
Supports different currency types.

---

## 🧠 ERD (Entity Relationship Diagram)

![image](https://github.com/user-attachments/assets/052da734-bb19-4534-b5b4-17c59c50f032)
(./A_Entity-Relationship_Diagram_(ERD)_of_a_banking_d.png)

---

## 📎 Usage

This schema is ideal for:
- Educational Projects
- Bank Simulation Systems
- Backend API development with MySQL

---

## 🚀 Tech Stack

- **MySQL 8+**
- Diagram tools: draw.io / dbdiagram.io

---

## 📌 License

This project is licensed under the MIT License - feel free to use and adapt it.

