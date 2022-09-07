from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:SQListhebest@localhost/flsk'
db = SQLAlchemy(app)


class Regions(db.Model):
    Region_id = db.Column(db.Integer, primary_key=True)
    Region_name = db.Column(db.String(23), nullable=False)

    def serialize(self):
        return {
            'Region_id': self.Region_id,
            'Region_name': self.Region_name,
        }


class Countries(db.Model):
    Country_id = db.Column(db.Integer, primary_key=True)
    Country_name = db.Column(db.String(23), nullable=False)
    Region_id = db.Column(db.Integer)


class Locations(db.Model):
    Location_id = db.Column(db.Integer, primary_key=True)
    Street_address = db.Column(db.String(33), nullable=False)
    Postal_code = db.Column(db.Integer, nullable=False)
    City = db.Column(db.String(23), nullable=False)
    State_province = db.Column(db.String(23), nullable=False)
    Country_id = db.Column(db.Integer)


class Departments(db.Model):
    Department_id = db.Column(db.Integer, primary_key=True)
    Department_name = db.Column(db.String(23), nullable=False)
    Manager_id = db.Column(db.Integer)
    Location_id = db.Column(db.Integer)


class Jobs(db.Model):
    Job_id = db.Column(db.Integer, primary_key=True)
    Job_title = db.Column(db.String(23), nullable=False)
    Min_salary = db.Column(db.Integer, nullable=False)
    Max_salary = db.Column(db.Integer, nullable=False)


class JobHistory(db.Model):
    Employee_id = db.Column(db.Integer, primary_key=True)
    Start_date = db.Column(db.Date, nullable=False)
    End_date = db.Column(db.Date, nullable=False)
    Job_id = db.Column(db.Integer)
    Department_id = db.Column(db.Integer)


class Employees(db.Model):
    Employee_id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(23), nullable=False)
    Last_name = db.Column(db.String(23), nullable=False)
    Email = db.Column(db.String(23), nullable=False)
    Phone_number = db.Column(db.BIGINT, nullable=False)
    End_date = db.Column(db.String(23), nullable=False)
    Job_id = db.Column(db.Integer, nullable=False)
    Salary = db.Column(db.Integer, nullable=False)
    Commission_pct = db.Column(db.Integer, nullable=False)
    Manager_id = db.Column(db.Integer)
    Department_id = db.Column(db.Integer)

    def serialize(self):
        return {
            'Employee_id': self.Employee_id,
            'First_name': self.First_name,
            'Last_name': self.Last_name,
            'Email': self.Email,
            'Phone_number': self.Phone_number,
            'End_date': self.End_date,
            'Job_id': self.Job_id,
            'Salary': self.Salary,
            'Commission_pct': self.Commission_pct,
            'Manager_id': self.Manager_id,
            'Department_id': self.Department_id,
        }


