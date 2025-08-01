# Customer Segmentation Web App
A web application that predicts customer segments based on demographic and behavioral data using a machine learning model.


 To predict customer clusters using KMeans clustering based on:

- Age
- Annual Income (k$)
- Spending Score (1-100)
---
📦 Tech Stack

| Part     | Technologies Used                          |
| -------- | ------------------------------------------ |
| Frontend | HTML, CSS (dark mode with RGB), JavaScript |
| Backend  | Python, Flask, Flask-CORS                  |
| ML Model | Scikit-learn, joblib                       |
| Hosting  | Render (Flask) + GitHub Pages (UI)         |

---

## 📊 Features

✅ Predicts which customer cluster a user belongs to  
✅ Displays a meaningful description for each cluster  
✅ Interactive web interface  
✅ Clean, modern UI design  
✅ Frontend and backend fully separated for easy deployment
☁️ Deployed backend via Render.



---

| Cluster | Description                                                       |
| ------- | ----------------------------------------------------------------- |
| 0       | High income, younger group — may need cost-effective offers.      |
| 1       | High income, low spenders — attract with luxury offers.           |
| 2       | High income, high spenders — premium products recommended.        |
| 3       | Low income, high spenders — value-seekers with strong engagement. |
| 4       | High income, low spender — potential for targeted upselling.      |
| 5       | Younger high spenders — very responsive to trends.                |


customer-segmentation/
├── index.html          # Frontend UI
├── styl1.css           # CSS (dark theme, RGB colors)
├── script.js           # JS for API calls + logic
├── model.pkl           # Trained ML clustering model
├── mn5.py              # Flask server for predictions
├── README.md           # Project README
└── screenshot.png      # UI screenshot (optional)

---



## 🔧 How It Works

### 1. Train Model

- Data used: `Mall_Customers.csv`
- Trained multiple KMeans models:
  - Age vs Spending Score
  - Annual Income vs Spending Score
  - Age, Annual Income, and Spending Score
- Chose best model (5 clusters)
---
<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/69968a39-2540-4ebe-aa13-5484e4c8dab9" />
<img width="400" height="550" alt="Screenshot 2025-08-01 at 4 45 48 PM" src="https://github.com/user-attachments/assets/4efb6815-0fcd-411f-ab13-bc78fcc071b0" />

---
## 🚀 Demo

👉 **Live Frontend on Vercel** https://customer-rev.vercel.app/


👉 **API Endpoint:** (https://customer-r-3.onrender.com)

---
📘 License
This project is licensed under the MIT License.

