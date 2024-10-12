import sqlite3
import uuid
def generate_uuid():
    return str(uuid.uuid4())
connection = sqlite3.connect('prison_management_system.db')
cursor = connection.cursor()
cursor.execute ('''
CREATE TABLE IF NOT EXISTS Prisoner (
    prisoner_id TEXT PRIMARY KEY,
    full_name TEXT,
    date_of_birth DATE,
    sentence_start_date DATE,
    sentence_end_date DATE,
    background_info TEXT,
    risk_status_id TEXT,
    current_prison_id TEXT,
    current_block_id TEXT,
    current_cell_id TEXT,
    FOREIGN KEY (risk_status_id) REFERENCES RiskStatus(risk_status_id),
    FOREIGN KEY (current_prison_id) REFERENCES Prison(prison_id),
    FOREIGN KEY (current_block_id) REFERENCES Block(block_id),
    FOREIGN KEY (current_cell_id) REFERENCES Cell(cell_id)
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Prison (
    prison_id TEXT PRIMARY KEY,
    prison_name TEXT,
    location TEXT,
    capacity INTEGER
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Block (
    block_id TEXT PRIMARY KEY,
    block_name TEXT,
    prison_id TEXT,
    capacity INTEGER,
    FOREIGN KEY (prison_id) REFERENCES Prison(prison_id)
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cell (
    cell_id TEXT PRIMARY KEY,
    cell_number TEXT,
    block_id TEXT,
    capacity INTEGER,
    FOREIGN KEY (block_id) REFERENCES Block(block_id)
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS MovementHistory (
    movement_id TEXT PRIMARY KEY,
    prisoner_id TEXT,
    from_prison_id TEXT,
    from_block_id TEXT,
    from_cell_id TEXT,
    to_prison_id TEXT,
    to_block_id TEXT,
    to_cell_id TEXT,
   movement_date TIMESTAMP,
    FOREIGN KEY (prisoner_id) REFERENCES Prisoner(prisoner_id),
    FOREIGN KEY (from_prison_id) REFERENCES Prison(prison_id),
    FOREIGN KEY (from_block_id) REFERENCES Block(block_id),
    FOREIGN KEY (from_cell_id) REFERENCES Cell(cell_id),
    FOREIGN KEY (to_prison_id) REFERENCES Prison(prison_id),
    FOREIGN KEY (to_block_id) REFERENCES Block(block_id),
    FOREIGN KEY (to_cell_id) REFERENCES Cell(cell_id)
 );
 ''')                                         
cursor.execute('''
CREATE TABLE IF NOT EXISTS RiskStatus(
    risk_status_id TEXT PRIMARY KEY,
    prisoner_id TEXT,
    risk_level TEXT CHECK(risk_level IN ('High', 'Medium', 'Low')),
    risk_assessment_date DATE,
    FOREIGN KEY (prisoner_id) REFERENCES Prisoner(prisoner_id) 
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Incident (
    incident_id TEXT PRIMARY KEY,
    prisoner_id TEXT,
    incident_type TEXT CHECK(incident_type IN ('Violence', 'Self-harm', 'Barricading', 'Escape Attempt')),
    incident_description TEXT,
    incident_date TIMESTAMP,
    location_prison_id TEXT,
    location_block_id TEXT,
    location_cell_id TEXT,
    FOREIGN KEY (prisoner_id) REFERENCES Prisoner(prisoner_id),
    FOREIGN KEY (location_prison_id) REFERENCES Prison(prison_id),
    FOREIGN KEY (location_block_id) REFERENCES Block(block_id),
    FOREIGN KEY (location_cell_id) REFERENCES Cell(cell_id)
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Activity (
    activity_id TEXT PRIMARY KEY,
    prisoner_id TEXT,
    activity_type TEXT CHECK(activity_type IN ('Work', 'Education', 'Vocational Instruction')),
    activity_description TEXT,
    activity_date DATE,
    FOREIGN KEY (prisoner_id) REFERENCES Prisoner(prisoner_id)
);              
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS PrisonCapacity (
    prison_id TEXT PRIMARY KEY,
    total_capacity INTEGER,
    current_occupancy INTEGER,
    FOREIGN KEY (prison_id) REFERENCES Prison(prison_id)
);
''')
connection.commit()
connection.close()
print("Database and tables created successfully")



