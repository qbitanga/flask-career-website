from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id" : 1,
    "title" : "Data Analyst",
    "location" : "Makati, Philippines",
    "salary" : "Php 40,000",
  },
  {
    "id" : 2,
    "title" : "Frontend Developer",
    "location" : "Remote",
#    "salary" : "Php 30,000",
  },
  {
    "id" : 3,
    "title" : "Backend Developer",
    "location" : "Remote",
    "salary" : "Php 45,000",
  },
]

@app.route("/")
def home():
  return render_template('home.html', jobs=JOBS, company_name="Jovian")
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)