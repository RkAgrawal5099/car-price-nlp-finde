# Car Price & Variant Finder Web App (With NLP Search)

This is a simple AI-powered Python Flask web application to search car details like:

- ✅ Car Variant Prices (Base, Mid, Top)
- ✅ Ex-Showroom & On-Road Prices
- ✅ Car Specifications & Seating Capacity
- ✅ Suggested City to Buy
- ✅ **NLP-based Car Name Matching** (Auto-correct for misspelled names)

### 🧑‍💻 How to Use
1. Download or clone the project.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   pip install flask
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

### 📁 Project Structure
```
car-price-finder/
├── app.py                # Main Flask app with NLP
├── car_data.py           # Car data
├── car_data.json         # JSON version
├── templates/
│   └── index.html        # Web form
├── static/               # CSS/JS folder (optional)
└── README.md             # Project instructions
```

---

Made for BSc 1st year AI project – includes NLP, frontend, and real-world use case.