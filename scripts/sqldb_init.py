import sqlite3
import csv

db_path = 'SQL/houseplants.db'

plant_assessments = 'data/Indoor_Plant_Health_and_Growth_Factors.csv'
plant_weather_daily = 'data/eleven_year_weather_by_species.csv'

def create_connection(db_path):
    return sqlite3.connect(db_path)

def create_tables(conn):
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plant_assessments (
            plant_ID TEXT PRIMARY KEY,
            assessment_id INTEGER,
            height_cm REAL,
            leaf_count INTEGER,
            new_growth_count INTEGER,
            watering_amount_ml REAL,
            watering_frequency_days INTEGER,
            sunlight_exposure TEXT,
            room_temp_c REAL,
            humidity_percentage REAL,
            fertilizer_type TEXT,
            fertilizer_amount_ml REAL,
            pest_presence INTEGER,
            pest_severity TEXT,
            soil_moisture_percentage REAL,
            soil_type TEXT,
            health_score INTEGER
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plant_weather_daily (
            plant_ID TEXT PRIMARY KEY,
            date DATETIME,
            temperature_2m_min REAL,
            temperature_2m_max REAL,
            humidity_2m_mean REAL,
            cloudcover_mean TEXT,
            precipitation_sum REAL,
            soil_moisture_mean REAL,
            soil_temperature_mean REAL,
            sunshine_duration REAL
        )
    ''')
    
    conn.commit()

conn = create_connection(db_path)
create_tables(conn)
conn.close()