import os
import sqlite3
import re

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('file_info.db')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS files
    (path TEXT, filename TEXT, name TEXT, type TEXT, udim TEXT, extension TEXT, UDIMS BOOLEAN DEFAULT FALSE)
''')

# Define directory to start from
start_dir = 'I:/COWBOT/assets/character/mariachai/surfacing_main/publish/v000/exr'

# Define type dictionary
type_dict = {
    "albedo": ["albedo", "basecolor"],
    "roughness": ["roughness"],
    "metallic": ["metalness", "metallic"],
    "normal": ["normal"],
    "height": ["height","displacement","bump"],
    # Add more types as needed
}

# Walk through directory and subdirectories
for dirpath, dirnames, filenames in os.walk(start_dir):
    for filename in filenames:
        # Get full path
        full_path = os.path.join(dirpath, filename)

        # Get extension
        extension = os.path.splitext(filename)[1][1:]

        # Get type
        type = None
        for key, values in type_dict.items():
            if any(value in filename for value in values):
                type = key
                break

        # Get UDIM
        udim_match = re.search(r'([1-8][0-9]{3})', filename)
        udim = udim_match.group(1) if udim_match else None

        # Get name
        name = filename
        if udim:
            name = name.replace(udim, '')
        if type:
            for value in type_dict[type]:
                name = name.replace(value, '')
        name = os.path.splitext(name)[0]

        # Insert into database
        c.execute('''
            INSERT INTO files (path, filename, name, type, udim, extension, UDIMS)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (full_path, filename, name, type, udim, extension, False))

# Commit changes and close connection
conn.commit()


# Create a temporary table
c.execute('''
    CREATE TEMPORARY TABLE temp_files AS
    SELECT path, filename, name, type, udim, extension, COUNT(*) as count
    FROM files
    GROUP BY name, type
''')

# Clear the original table
c.execute('DELETE FROM files')

# Insert the merged entries into the original table
c.execute('''
    INSERT INTO files (path, filename, name, type, udim, extension, UDIMS)
    SELECT path, filename, name, type, udim, extension, count > 1
    FROM temp_files
''')

# Commit changes
conn.commit()

# Query for distinct names
c.execute('SELECT DISTINCT name FROM files')
unique_names = c.fetchall()

# Convert list of tuples to list of strings
unique_names = [name[0] for name in unique_names]

# Print or export the list
print(unique_names)
print(len(unique_names))


conn.close()