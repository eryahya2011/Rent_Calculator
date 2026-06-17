# Rent_Calculator
A simple Python-based Rent Calculator that computes the total living cost (rent, food, and electricity) and splits it equally among roommates for quick and hassle-free expense sharing.

# 🏠 Rent Calculator (Python CLI)

A beginner-friendly Python program that calculates total living expenses and splits them equally among roommates.

---

## 🚀 Features

* 🧮 Calculates total cost including:

  * Rent
  * Food expenses
  * Electricity bill
* ⚡ Automatically computes electricity bill using:

  * Units consumed
  * Cost per unit
* 👥 Splits total amount equally among all roommates
* 💻 Simple command-line interface (CLI)

---

## 🧠 How It Works

The program takes user input for:

* Rent amount
* Food expenses
* Electricity units consumed
* Cost per electricity unit
* Number of roommates

Then it:

1. Calculates electricity bill
2. Adds all expenses
3. Divides total by number of roommates

---

## 🛠️ Tech Stack

* Language: Python 🐍
* Type: CLI (Command Line Tool)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/rent-calculator.git
cd rent-calculator
```

---

## ▶️ Usage

Run the Python script:

```bash
python main.py
```

---

## 📸 Example Run

```
Enter The Rent of Flat: 10000
Enter the Food Expenses: 3000
Enter The Electricity units consumed: 100
Enter the Cost Per Unit Of Electricity: 10
Enter the Number of Flat mates: 4
```

### ✅ Output:

```
Total Amount To Be Paid Individually:  4000.0
```

---

## 📊 Formula Used

```
Electricity Bill = Units Consumed × Cost per Unit

Total Expense = Rent + Food Expenses + Electricity Bill

Per Person Share = Total Expense ÷ Number of Roommates
```

---

## ⚠️ Limitations

* Equal split only (no custom distribution)
* No input validation (e.g., negative values or zero roommates)
* CLI-based (no GUI)

---

## 🔮 Future Improvements

* Input validation & error handling
* Unequal rent splitting (based on room size)
* GUI (Web or Desktop App)
* Expense history tracking

---

## 🤝 Contributing

Feel free to fork this project and improve it!

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/your-username

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!
