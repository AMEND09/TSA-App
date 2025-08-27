# TSA Club App

A comprehensive web application built with Flet and Django for managing Technology Student Association (TSA) club activities.

## Features

- **Organize Workshops**: Create and manage workshop events with details like name, date, and description
- **Organize Tryouts**: Set up tryout sessions for TSA competitions
- **Manage IDs & Passwords**: Maintain member credentials and access information
- **Event Help**: Access resources and guidelines for TSA events
- **Required Documents**: Download templates and forms including portfolio templates
- **Manage Dues**: Track member dues payments and amounts
- **Attendance**: Mark and track attendance for events

## Installation

### Prerequisites
- Python 3.8 or higher
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AMEND09/TSA-App.git
   cd TSA-App
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

## Running the Application

### Web Version (Recommended)
To run the app as a web server:

```bash
python manage.py run_app --view flet_app_hidden
```

Then open your browser and navigate to `http://localhost:8085`

### Desktop Version
To run as a desktop application:

```bash
python manage.py run_app
```

## Usage

1. **Home Page**: Navigate to different sections using the buttons
2. **Workshops**: Fill in workshop details and create events
3. **Tryouts**: Set up tryout information and requirements
4. **Manage IDs**: View and manage member credentials
5. **Event Help**: Access TSA event resources and guidelines
6. **Documents**: Download required forms and templates
7. **Manage Dues**: Track payment status and amounts
8. **Attendance**: Mark attendance for events

## Project Structure

```
TSA-App/
├── TSAFlet/              # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main_app.py           # Main Flet application
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## Technologies Used

- **Django**: Web framework for backend
- **Flet**: UI framework for building web, mobile, and desktop apps
- **flet-django**: Integration package for Flet and Django

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the application
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, please open an issue on GitHub or contact the maintainers.
