# Chat System


https://github.com/user-attachments/assets/2d50cc40-1b50-4942-990f-7d34eda5279a


A real-time chat application built with Django, HTML, CSS, JavaScript, and PostgreSQL.

## Features

- **Real-Time Messaging**: Send and receive messages in real-time.
- **User Authentication**: Secure login and registration.
- **Database**: PostgreSQL for storing user data and chat history.
- **Responsive Design**: Works well on both desktop and mobile devices.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/ChatSystem.git
   cd ChatSystem
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL**

   - Create a PostgreSQL database and user.
   - Update the `DATABASES` section in `settings.py` with your PostgreSQL credentials.

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   Navigate to `http://127.0.0.1:8000/` in your browser to access the chat application.

## Usage

1. **Register**: Create a new account to start using the chat system.
2. **Login**: Log in with your credentials.
3. **Chat**: Start chatting with other users in real-time.

## Contributing

1. **Fork the Repository**: Click the "Fork" button on GitHub.
2. **Create a Branch**: `git checkout -b feature/YourFeature`
3. **Commit Changes**: `git commit -am 'Add new feature'`
4. **Push to Branch**: `git push origin feature/YourFeature`
5. **Create a Pull Request**: Open a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Django Documentation**: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **PostgreSQL Documentation**: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
