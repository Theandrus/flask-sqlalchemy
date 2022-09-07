from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from models import Regions, Employees

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:SQListhebest@localhost/flsk'
db = SQLAlchemy(app)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('Employee_id', type=int, required=True)
parser.add_argument('First_name', type=str, required=True)
parser.add_argument('Last_name', type=str, required=True)
parser.add_argument('Email', type=str, required=True)
parser.add_argument('Phone_number', type=int, required=True)
parser.add_argument('End_date', type=str, required=True)
parser.add_argument('Job_id', type=int, required=True)
parser.add_argument('Salary', type=int, required=True)
parser.add_argument('Commission_pct', type=int, required=True)
parser.add_argument('Manager_id', type=int, required=False)
parser.add_argument('Department_id', type=int, required=False)

class RegionsList(Resource):
    def get(self):
        records = Regions.query.all()
        return [Regions.serialize(record) for record in records]


class RegionsFind(Resource):
    def get(self, record_id):
        return Regions.serialize(
            Regions.query.filter_by(Region_id=record_id).first_or_404(description='Record with id={} is not available'
                                                                      .format(record_id)))


class EmployeesList(Resource):
    def get(self):
        employees = Employees.query.all()
        return [Employees.serialize(employee) for employee in employees]


class EmployeesFind(Resource):
    def get(self, employee_id):
        return Employees.serialize(
            Employees.query.filter_by(Employee_id=employee_id).
            first_or_404(description='Record with id={} is not available'.format(employee_id)))

    def delete(self, employee_id):
        record = Employees.query.filter_by(Employee_id=employee_id) \
            .first_or_404(description='Record with id={} is not available'.format(employee_id))
        db.session.delete(record)
        db.session.commit()
        return '', 204

    def put(self, employee_id):
        record = Employees.query.filter_by(id=employee_id) \
            .first_or_404(description='Record with id={} is not available'.format(employee_id))
        db.session.commit()
        return Employees.serialize(record), 201

    def post(self):
        args = parser.parse_args()
        record = Employees(Employee_id=args['Employee_id'], First_name=args['First_name'], Last_name=args['Last_name'],
                           Email=args['Email'], Phone_number=args['Phone_number'], End_date=args['End_date'],
                           Job_id=args['Job_id'], Salary=args['Salary'], Commission_pct=args['Commission_pct'],
                           Manager_id=args['Manager_id'], Department_id=args['Department_id'])
        db.session.add(record)
        db.session.commit()
        return Employees.serialize(record), 201


class EmployeesFind2(Resource):
    def get(self, employee_name):
        return Employees.serialize(
            Employees.query.filter_by(First_name=employee_name).first_or_404(description='Record with name={} is not available'
                                                                      .format(employee_name)))

    def delete(self, employee_name):
        record = Employees.query.filter_by(First_name=employee_name) \
            .first_or_404(description='Record with id={} is not available'.format(employee_name))
        db.session.delete(record)
        db.session.commit()
        return '', 204

    def put(self, employee_name):
        record = Employees.query.filter_by(First_name=employee_name) \
            .first_or_404(description='Record with id={} is not available'.format(employee_name))
        db.session.commit()
        return Employees.serialize(record), 201


class EmployeesFind3(Resource):
    def get(self, employee_end_date):
        return Employees.serialize(
            Employees.query.filter_by(End_date=employee_end_date).first_or_404(description='Record with end date={} is not available'
                                                                      .format(employee_end_date)))

    def delete(self, employee_end_date):
        record = Employees.query.filter_by(End_date=employee_end_date) \
            .first_or_404(description='Record with id={} is not available'.format(employee_end_date))
        db.session.delete(record)
        db.session.commit()
        return '', 204

    def put(self, employee_end_date):
        record = Employees.query.filter_by(End_date=employee_end_date) \
            .first_or_404(description='Record with id={} is not available'.format(employee_end_date))
        db.session.commit()
        return Employees.serialize(record), 201



api.add_resource(EmployeesList, '/')
api.add_resource(EmployeesFind, '/employee_id/<employee_id>')
api.add_resource(EmployeesFind2, '/employee_name/<employee_name>')
api.add_resource(EmployeesFind3, '/employee_end_date/<employee_end_date>')

if __name__ =='__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')








