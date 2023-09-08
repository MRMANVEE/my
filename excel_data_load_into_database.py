from flask import Flask, request, jsonify, render_template
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__, template_folder='templates')

db_connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=SABARMATI\SQLEXPRESS;DATABASE=campusmgmt;UID=sa;PWD=sadguru'
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={db_connection_string}')

@app.route("/")
def index():
    return render_template("upload_form.html")

@app.route('/upload', methods=['POST'])
def upload_excel():
    try:
        if 'file' not in request.files:
            return jsonify({'Message': 'No File Path.'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'Message': 'No Selected file here.'}), 400
        
        if file:
            df = pd.read_excel(file)

            try:

                engine = create_engine('sqlite:///campusmgmt.db')

                df.to_sql('Registrations', con = engine, if_exists='replace' , index=False)
                return jsonify({'Message': 'File uploaded successfully and the data was inserted successfully.'})
            except Exception as e:
                return jsonify({f'Error' : f'Error the inserting the data : {str(e)}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
