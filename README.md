---

# **EcoWave**  
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

EcoWave is part of the **EcoWave** project, providing a seamless and eco-friendly shopping experience.

---

## **Prerequisites**

- **Python**: Ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/)
- **Git**: Required for cloning the repository. [Download Git](https://git-scm.com/downloads)

---

## **Installation**

### Step 1: Clone the Repository
```bash
git clone https://github.com/vidushichauhan/EcoWave_Team_Project && cd EcoWave
```

---

### Step 2: Set Up a Virtual Environment

#### **Option 1: Using `virtualenv`**
```bash
pip install virtualenv
virtualenv venv
```

#### **Option 2: Using `venv` (Built-in Python module)**
```bash
python3 -m venv venv  # Create a virtual environment
```

---

### Step 3: Activate the Virtual Environment

#### **For Mac/Linux**
```bash
source venv/bin/activate  # Activate the virtual environment
pip install -r requirements.txt  # Install dependencies
```

#### **For Windows**
```bash
.\venv\Scripts\activate  # Activate the virtual environment
pip install -r requirements.txt  # Install dependencies
```

---

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## **Adding Initial Data**

To load initial data for the project, run the following command:
```bash
python manage.py loaddata sample.json
```

### Default Credentials
- **Admin**  
  - **Email**: `admin@ecowave.com`  
  - **Password**: `Admin@123`

- **Test User**  
  - **Email**: `test@ecowave.com`  
  - **Password**: `Test@123`

---

### **Happy Shopping!** 🌱
