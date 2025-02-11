# 🌐 Medical Shop Management System

Welcome to the **Medical Shop Management System**! This Django-based web application streamlines the management of medical inventory, customer orders, and sales, making it easy for pharmacies and medical shops to efficiently manage their day-to-day operations.

---

## 💡 Features

- **Inventory Management**: Add, update, and delete medicine details.
- **Real-time Search**: Quickly search for medicines in stock.
- **Order Management**: Process customer orders seamlessly.
- **Sales Tracking**: Monitor sales and generate reports.
- **User Authentication**: Secure login/logout functionality.
- **Responsive UI**: Clean and intuitive interface with HTML, CSS, and JavaScript.

---

## 🎓 Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default Django DB, can be upgraded to PostgreSQL/MySQL)
- **Templates**: Django Templates for dynamic content rendering

---

## 🚀 Getting Started

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
https://github.com/hayat29/medical_shop_management.git
cd medical_shop_management
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

---

## 📂 Project Structure

```
medical_shop_management/
├── inventory/
│   ├── migrations/
│   ├── templates/
│   │   ├── inventory/
│   │       ├── medicines_list.html
│   │       ├── add_medicine.html
│   │       ├── update_medicine.html
│   │       └── delete_medicine.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── medical_shop_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

---

## 💪 Key Functionalities

- **medicines_list.html**: Displays the list of all medicines.
- **add_medicine.html**: Form to add new medicine to the inventory.
- **update_medicine.html**: Update existing medicine details.
- **delete_medicine.html**: Delete medicine from the inventory.

---

## 🔧 Future Enhancements

- **Barcode Scanning**: Integrate barcode scanners for quick product lookup.
- **Advanced Analytics**: Generate detailed sales and inventory reports.
- **Multi-user Roles**: Implement different roles for admin, staff, and customers.
- **Notifications**: Low stock and expiry notifications.

---

## 🌟 Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and create a pull request.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

---

## 😎 Author

**Faisal Hayat**  
Final-year Computer Science Engineering student at Integral University  
Passionate about data science, AI, and building practical solutions.

---

## 📍 Contact

- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/faisal-hayat-734b4a2b0)
- **Email**: your.email@example.com

Feel free to reach out for any queries or collaboration ideas!

---

Thank you for checking out the **Medical Shop Management System**! 🎉🌐

