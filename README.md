# Student Performance Tracker

A simple, web-based application built with **Flask** to help educators track student grades, calculate averages, and view performance reports. The app uses **SQLite** for data storage and is ready for deployment on **Heroku**.

---

## Features

- ✅ Add students (Name + Roll Number)
- 🧮 Assign grades by subject (0–100)
- 📋 View student details and subject-wise grades
- 📊 Calculate and display average grades
- 💾 Persistent data storage using SQLite
- 🌐 Flask-based web interface
- ☁️ Deployable to Heroku

---

## Project Structure

```

/student\_tracker\_web
├── app.py                  # Main Flask application
├── templates/              # HTML templates
│   ├── index.html
│   ├── add\_student.html
│   ├── add\_grades.html
│   └── view\_student.html
├── schema.sql              # SQLite DB schema
├── requirements.txt        # Python dependencies
├── Procfile                # Heroku entry point
└── README.md               # This file

````

---

##  Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/student-tracker.git
cd student-tracker
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up the database:**

```bash
sqlite3 database.db < schema.sql
```

4. **Run the application:**

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Usage

* Go to `/` to view all students.
* Click **"Add Student"** to enter a new student.
* Click **"Add Grades"** to assign marks by subject.
* Click **"View"** to see full student report and average.

---

##  Deployment (Heroku)

1. **Create `requirements.txt`**:

```bash
pip freeze > requirements.txt
```

2. **Create `Procfile`**:

```
web: gunicorn app:app
```

3. **Push to Heroku**:

```bash
git init
heroku create
git add .
git commit -m "Initial commit"
git push heroku master
```

---

## Requirements

* Python 3.8+
* Flask
* gunicorn
* sqlite3

---

## Optional Enhancements

* 🔍 Search students by name or roll number
* 📈 Show class average per subject
* 🏆 Highlight top-performing students
* 📤 Export to CSV

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👩‍💻 Author
Anyam Anitha @Anyam0510

```
