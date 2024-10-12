from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key

def get_db_connection():
    conn = sqlite3.connect('prison_management_system.db')
    conn.row_factory = sqlite3.Row
    return conn

def generate_uuid():
    return str(uuid.uuid4())

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/management')
def management():
    return render_template('management.html')

@app.route('/add_prisoner', methods=['GET', 'POST'])
def add_prisoner():
    if request.method == 'POST':
        prisoner_id = generate_uuid()
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        gender = request.form['gender']
        sentence_start_date = request.form['sentence_start_date']
        sentence_end_date = request.form['sentence_end_date']
        background_info = request.form['background_info']
        
        conn = get_db_connection()
        try:
            conn.execute('''INSERT INTO Prisoner 
                            (prisoner_id, first_name, last_name, date_of_birth, gender, 
                            sentence_start_date, sentence_end_date, background_info) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                         (prisoner_id, first_name, last_name, date_of_birth, gender,
                          sentence_start_date, sentence_end_date, background_info))
            conn.commit()
            flash('Prisoner added successfully!', 'success')
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            conn.close()
        return redirect(url_for('view_prisoners'))
    
    return render_template('add_prisoner.html')

@app.route('/view_prisoners')
def view_prisoners():
    conn = get_db_connection()
    prisoners = conn.execute('SELECT * FROM Prisoner').fetchall()
    conn.close()
    return render_template('view_prisoners.html', prisoners=prisoners)

@app.route('/add_prison', methods=['GET', 'POST'])
def add_prison():
    if request.method == 'POST':
        prison_id = generate_uuid()
        prison_name = request.form['prison_name']
        location = request.form['location']
        capacity = int(request.form['capacity'])
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO Prison (prison_id, prison_name, location, capacity) VALUES (?, ?, ?, ?)',
                         (prison_id, prison_name, location, capacity))
            conn.execute('INSERT INTO PrisonCapacity (prison_id, total_capacity, current_occupancy) VALUES (?, ?, ?)',
                         (prison_id, capacity, 0))
            conn.commit()
            flash('Prison added successfully!', 'success')
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            conn.close()
        return redirect(url_for('view_prisons'))
    
    return render_template('add_prison.html')

@app.route('/view_prisons')
def view_prisons():
    conn = get_db_connection()
    prisons = conn.execute('''SELECT Prison.*, PrisonCapacity.current_occupancy 
                              FROM Prison 
                              LEFT JOIN PrisonCapacity ON Prison.prison_id = PrisonCapacity.prison_id''').fetchall()
    conn.close()
    return render_template('view_prisons.html', prisons=prisons)

@app.route('/add_block', methods=['GET', 'POST'])
def add_block():
    if request.method == 'POST':
        block_id = generate_uuid()
        block_name = request.form['block_name']
        prison_id = request.form['prison_id']
        capacity = int(request.form['capacity'])
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO Block (block_id, block_name, prison_id, capacity) VALUES (?, ?, ?, ?)',
                         (block_id, block_name, prison_id, capacity))
            conn.commit()
            flash('Block added successfully!', 'success')
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            conn.close()
        return redirect(url_for('view_blocks'))
    
    conn = get_db_connection()
    prisons = conn.execute('SELECT prison_id, prison_name FROM Prison').fetchall()
    conn.close()
    return render_template('add_block.html', prisons=prisons)

@app.route('/view_blocks')
def view_blocks():
    conn = get_db_connection()
    blocks = conn.execute('''SELECT Block.*, Prison.prison_name 
                             FROM Block 
                             JOIN Prison ON Block.prison_id = Prison.prison_id''').fetchall()
    conn.close()
    return render_template('view_blocks.html', blocks=blocks)

@app.route('/add_cell', methods=['GET', 'POST'])
def add_cell():
    if request.method == 'POST':
        cell_id = generate_uuid()
        cell_number = request.form['cell_number']
        block_id = request.form['block_id']
        capacity = int(request.form['capacity'])
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO Cell (cell_id, cell_number, block_id, capacity) VALUES (?, ?, ?, ?)',
                         (cell_id, cell_number, block_id, capacity))
            conn.commit()
            flash('Cell added successfully!', 'success')
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            conn.close()
        return redirect(url_for('view_cells'))
    
    conn = get_db_connection()
    blocks = conn.execute('SELECT block_id, block_name FROM Block').fetchall()
    conn.close()
    return render_template('add_cell.html', blocks=blocks)

@app.route('/view_cells')
def view_cells():
    conn = get_db_connection()
    cells = conn.execute('''SELECT Cell.*, Block.block_name, Prison.prison_name 
                            FROM Cell 
                            JOIN Block ON Cell.block_id = Block.block_id 
                            JOIN Prison ON Block.prison_id = Prison.prison_id''').fetchall()
    conn.close()
    return render_template('view_cells.html', cells=cells)

@app.route('/report_incident', methods=['GET', 'POST'])
def report_incident():
    if request.method == 'POST':
        incident_id = generate_uuid()
        prisoner_id = request.form['prisoner_id']
        incident_type = request.form['incident_type']
        incident_description = request.form['incident_description']
        incident_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        location_prison_id = request.form['location_prison_id']
        location_block_id = request.form['location_block_id']
        location_cell_id = request.form['location_cell_id']
        
        conn = get_db_connection()
        try:
            conn.execute('''INSERT INTO Incident 
                            (incident_id, prisoner_id, incident_type, incident_description, incident_date, 
                            location_prison_id, location_block_id, location_cell_id) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                         (incident_id, prisoner_id, incident_type, incident_description, incident_date,
                          location_prison_id, location_block_id, location_cell_id))
            conn.commit()
            flash('Incident reported successfully!', 'success')
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            conn.close()
        return redirect(url_for('view_incidents'))
    
    conn = get_db_connection()
    prisoners = conn.execute('SELECT prisoner_id, first_name, last_name FROM Prisoner').fetchall()
    prisons = conn.execute('SELECT prison_id, prison_name FROM Prison').fetchall()
    blocks = conn.execute('SELECT block_id, block_name FROM Block').fetchall()
    cells = conn.execute('SELECT cell_id, cell_number FROM Cell').fetchall()
    conn.close()
    return render_template('report_incident.html', prisoners=prisoners, prisons=prisons, blocks=blocks, cells=cells)

@app.route('/view_incidents')
def view_incidents():
    conn = get_db_connection()
    incidents = conn.execute('''SELECT Incident.*, 
                                Prisoner.first_name, Prisoner.last_name,
                                Prison.prison_name,
                                Block.block_name,
                                Cell.cell_number
                                FROM Incident
                                JOIN Prisoner ON Incident.prisoner_id = Prisoner.prisoner_id
                                JOIN Prison ON Incident.location_prison_id = Prison.prison_id
                                JOIN Block ON Incident.location_block_id = Block.block_id
                                JOIN Cell ON Incident.location_cell_id = Cell.cell_id''').fetchall()
    conn.close()
    return render_template('view_incidents.html', incidents=incidents)

if __name__ == '__main__':
    app.run(debug=True)