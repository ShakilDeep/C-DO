# C DO

"C DO" is a cutting-edge tool designed for developers to enhance their app development process. It is built using FastAPI and PostgreSQL.

## Features

- AI-powered Development
- Multiplatform Development
- Live Preview
- Integrated Development Environment (IDE)
- Collaboration

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- PostgreSQL

### Installation

1. Clone the repository
```bash
git clone 
```

2. Change the working directory
```bash
cd cdo
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a .env file and update your database credentials
```bash
cp .env.example .env
```

5. Run the application
```bash
python main.py
```

## Usage

The application starts a FastAPI server on your localhost on port 8000 (http://localhost:8000/). You can now visit the browser and interact with your FastAPI application.

## File Structure

- `main.py`: The entry point of the application. It initializes the FastAPI application, middleware, and routes.
- `database.py`: Contains the SQLAlchemy setup including the session, engine, and base model.
- `models.py`: Contains the SQLAlchemy models for the User and Project.
- `schemas.py`: Contains the Pydantic models for User and Project.
- `crud.py`: Contains the CRUD operations for the User and Project models.
- `middlewares.py`: Contains a custom middleware for pre-processing and post-processing requests.
- `config.py`: Contains the configuration settings for the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue