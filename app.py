from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the database URI (adjust the user, password, and dbname accordingly)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'names'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

# Create the tables and insert sample data if not already present
def create_db_and_insert_data():
    # Make sure to run this inside the app context
    with app.app_context():
        # Create the tables
        db.create_all()
        
        # Insert sample data if the table is empty
        sample_users = [
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Ahmed', email='ahmed@gmail.com'),
                User(name='asad', email='asad@example.com'),
                User(name='abdi', email='charlie@example.com'),
                User(name='Zaki', email='zaki')
                
                
                

            ]
        db.session.bulk_save_objects(sample_users)
        db.session.commit()

# Run the function to create the table and insert data
create_db_and_insert_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users')
def get_users():
    # Get page, per_page, and filter parameters from the request query
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    name_filter = request.args.get('name', type=str)  # Optional name filter
    email_filter = request.args.get('email', type=str)  # Optional email filter

    # Base query
    query = User.query

    # Apply filters if provided
    if name_filter:
        query = query.filter(User.name.ilike(f'%{name_filter}%'))
    if email_filter:
        query = query.filter(User.email.ilike(f'%{email_filter}%'))

    # Paginate the query
    users = query.paginate(page=page, per_page=per_page, error_out=False)

    # Prepare the response
    return jsonify({
        'users': [{'id': user.id, 'name': user.name, 'email': user.email} for user in users.items],
        'total': users.total,  # Total number of users (after applying filters)
        'pages': users.pages   # Total number of pages
    })
if __name__ == '__main__':
    app.run(debug=True)
