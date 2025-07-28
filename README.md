# Customer Segmentation with KMeans

A web application to predict customer clusters using KMeans clustering based on:

- Age
- Annual Income (k$)
- Spending Score (1-100)

Built with **Python (Flask)**, **Scikit-learn**, and a frontend hosted on **Vercel**.

---


## 📊 Features

✅ Predicts which customer cluster a user belongs to  
✅ Displays a meaningful description for each cluster  
✅ Interactive web interface  
✅ Clean, modern UI design  
✅ Frontend and backend fully separated for easy deployment

---

## 🖼️ Clusters and Their Meaning

| Cluster | Description |
|---------|-------------|
| 0 | Young, high-spending customers |
| 1 | Older, low-spending customers |
| 2 | Average income and spending |
| 3 | Wealthy but low-spending customers |
| 4 | Low income but high spending |
| 5 | Other segment |

---

## 🏗️ Tech Stack

- **Backend**: Python, Flask, Scikit-learn, Flask-CORS
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**:
  - Backend: Render.com (or PythonAnywhere, Heroku)
  - Frontend: Vercel  https://customer-rev.vercel.app/

---

## 🔧 How It Works

### 1. Train Model

- Data used: `Mall_Customers.csv`
- Trained multiple KMeans models:
  - Age vs Spending Score
  - Annual Income vs Spending Score
  - Age, Annual Income, and Spending Score
- Chose best model (6 clusters)

## 🚀 Demo

👉 **[Live Frontend on Vercel]([[https://customer-analysis-624n.vercel.app/]](https://customer-analysis-624n.vercel.app/))**  https://customer-analysis-624n.vercel.app/
👉 **API Endpoint:** (https://customer-r-3.onrender.com)

---
