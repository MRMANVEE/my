from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/date")
def time_duration():
    country_time_format = "%I:%M %p"

    intime_str = "03:35 PM"
    outtime_str = "04:00 PM"

    # Remove double quotes from input strings, if present
    intime_str = intime_str.strip('"')
    outtime_str = outtime_str.strip('"')

    # Convert the time strings to datetime objects using the custom format
    intime = datetime.strptime(intime_str, country_time_format)
    outtime = datetime.strptime(outtime_str, country_time_format)

    # Calculate the duration (outtime - intime)
    duration = outtime - intime

    # Format the datetime objects as strings for printing
    intime_str = intime.strftime(country_time_format)
    outtime_str = outtime.strftime(country_time_format)
    duration_str = str(duration)

    print(f"Intime: {intime_str}")
    print(f"Outtime: {outtime_str}")
    print(f"Duration: {duration_str}")

    return ("This is the duration... : ", duration_str)

if __name__ == "__main__":
    app.run(debug=True)
