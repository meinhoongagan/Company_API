# Company API Project

This project is a RESTful API built using Django Rest Framework (DRF) to manage companies and their employees.

## Features

- CRUD operations for managing companies and employees.
- Relationships established between companies and employees.
- Authentication and authorization for API endpoints.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/meinhoongagan/company-api.git
    ```

2. Navigate to the project directory:
    ```bash
    cd companyapi
    ```

3. Install dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the API endpoints:
    - Companies: `/api/v1/companies/`
    - Employees: `/api/v1/employees/`
    - Companies-Employees:  `/api/v1/companies/{Company-ID}/employees/`

## Endpoints

### Companies

- `GET /api/v1/companies/`: Retrieve all companies.
- `POST /api/v1/companies/`: Create a new company.
- `GET /api/v1/companies/<company_id>/`: Retrieve details of a specific company.
- `PUT /api/v1/companies/<company_id>/`: Update details of a specific company.
- `DELETE /api/v1/companies/<company_id>/`: Delete a specific company.

### Employees

- `GET /api/v1/employees/`: Retrieve all employees.
- `POST /api/v1/employees/`: Create a new employee.
- `GET /api/v1/employees/<employee_id>/`: Retrieve details of a specific employee.
- `PUT /api/v1/employees/<employee_id>/`: Update details of a specific employee.
- `DELETE /api/v1/employees/<employee_id>/`: Delete a specific employee.

## Authentication

- Authentication is required for certain endpoints. Use tokens or other authentication mechanisms provided by Django Rest Framework.

## Contributing

Feel free to contribute by forking the repository and creating pull requests. Please follow the contribution guidelines.

