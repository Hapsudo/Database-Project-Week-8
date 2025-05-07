"""
Question 2
For this question, you will be creating a RESTful API using Flask and MySQL.
The API will allow you to perform CRUD operations on a student database. 
The database should have a table named 'students' with the following fields: name, email, course.   
""" 

from flask import Flask, request, jsonify
from db_config import get_db_connection

app = Flask(__name__)

@app.route("/students", methods=["POST"])
def create_student():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
                   (data["name"], data["email"], data["course"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student created successfully"}), 201

@app.route("/students", methods=["GET"])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return jsonify(students)

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, email=%s, course=%s WHERE id=%s",
                   (data["name"], data["email"], data["course"], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student updated"})

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student deleted"})


#Course CRUD operations
@app.route("/courses", methods=["POST"])
def create_course():
    # Get the data from the request (Expecting JSON data)
    data = request.json

    # Establish a database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute the SQL query to insert a new course
    cursor.execute("INSERT INTO Courses (title, description) VALUES (%s, %s)",
                   (data["title"], data["description"]))
    
    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    conn.close()

    # Return a success message
    return jsonify({"message": "Course created successfully"}), 201

@app.route("/courses", methods=["GET"])
def get_courses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Courses")
    courses = cursor.fetchall()
    conn.close()
    return jsonify(courses)

@app.route("/courses/<int:id>", methods=["PUT"])
def update_course(id):
    data = request.json
    title = data.get("title")
    description = data.get("description")
    
    if not title or not description:
        return jsonify({"error": "Title and description are required."}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Courses SET title = %s, description = %s WHERE id = %s",
                   (title, description, id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Course updated successfully"})

@app.route("/courses/<int:id>", methods=["DELETE"])
def delete_course(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Courses WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Course deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)


