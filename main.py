from flask import Flask, request, send_file
import pandas as pd
import io
import seaborn as sns

app = Flask(__name__)

@app.get('/')
def home():
    return """
    <html>
        <h1>Welcome to the CSV transformer page!</h1>
        <p>Click here to transform your CSV file into a beautiful format!</p>
        <form action="/transform" method="POST" enctype="multipart/form-data">
            <input type="file" name="csv" accept=".csv" required>
            <input type="submit" value="Transform CSV">
        </form>
    </html>
    """

@app.post('/transform')
def transform():
    print("Transforming CSV...")
    file = request.files['csv']
    # Checking if file is present in the request.
    if 'csv' not in request.files:
        return "No file part", 400
    # Checking if a file is selected.
    if file.filename == '':
        return "Go back and select a file ding dong!", 400
    file.save('file.csv')
    # Checking if file is a CSV.
    if file:
        # TODO: Add a check to ensure CSV is correctly formatted.
        df = pd.read_csv('file.csv')
        df['owner_name'] = df['owner_name'].str.upper()
        df['date_coming'] = pd.to_datetime(df['date_coming'])+pd.DateOffset(days=3)
        df['num_dogs'] = df['num_dogs'].astype(int) **2
        df['dog_breed'] = df['dog_breed'].str.upper()
        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)
        return f"""
        <html>
        <h1>Your Beautiful Transformation</h1>
        <pre>{output.getvalue()}</pre>
        
        </html>
        """