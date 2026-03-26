# 🍃 AuraSense: Intelligent Indoor Air Quality (IAQ) & Cognitive Monitor

AuraSense is an analytics platform that acts as an aura or umbrella over the data about your space. The system serves as a predictive analytics dashboard and sensor platform for the monitoring of conditions inside a space and their effect on brain function. The system incorporates sensor technology for CO2, temperature and humidity in order to give a historical view of the conditions as well as a projection of their influence on the brains function and thereby on the ability to work and perform. The data allows you to better prepare for deep work sessions, understand when you are at risk for Sick Building Syndrome and better plan travel or living in foreign environments.

## ✨ Key Features
- **Real-time IAQ Gauges**: Using high-fidelity Plotly gauges to display in real-time the current CO2 reading and environmental conditions.
- **Cognitive Focus Scoring:** Our unique logic engine that determines cognitive focus based on levels of CO2 saturation.
- **Predictive Status Alerts:** Dynamically updates health recommendations (Optimal, Warning, Critical).
1. What Is Ventilation? 2. Air Change Rate 3. Indoor Air Quality 4. Local vs. System Ventilation 5. Interactive Simulation: Control bars to demonstrate rooms of different occupancy and different ventilation states.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **UI Framework:** Streamlit
- **Data Visualization:** Plotly (Express & Graph Objects)
- **Data Handling:** Pandas & NumPy

## 🚦 Quick Start
1. ** Clone the Project:**
```bash
git clone [https://github.com/rujula25bai10455/AuraSense.git](https://github.com/rujula25bai10455/AuraSense.git)
cd AuraSense
🛠️ Installation & Setup Guide
Follow these steps to get AuraSense running on your local machine.
1. Prerequisities:
Ensure you have Python 3.9 or higher installed . You can check your version by running:
Bash
python --version
2. Clone the repository:
Open your command prompt or terminal and run:
Bash
git clone https://github.com/rujula25bai10455/AuraSense.git
cd AuraSense
3. Set up a virtual environment:
To keep your global python installation clean , create a virtual environment:
WINDOWS:
DOS
python -m venv venv
.\venv\Scripts\activate
MAC/LINUX:
Bash
python3 -m venv venv
source venv/bin/activate
4. Install dependencies:
Install the required libraries (Pandas,Streamlit,andPlotly) using the provided requirements file:
Bash
pip install -r requirements.txt
NOTE: If you don't have reqirements file, run: pip install streamlit pandas plotly numpy
🚀 Running the Project:
The project consists of two parts: the Data Engine and the Dashboard UI.
Step1: Generate Sensor data
Before launching the dashboard , you need to genearte the simulated 24-hour environment data . Run the folloeing command:
Bash
python app.py
Check that a folder named /data has been created with a file called sensor_readings.csv inside it.
Step2: Launch the dashboard
Now,start the interactive Streamlit web interface:
Bash
streamlit run app.py
Step3:View in browser
Once the command is running, your terminal will provide a URL . If it dosen't open automatically, copy and paste this into your browser:
http://localhost:8501
🛑 Troubleshooting:
1. Command not found: If streamlit is not recognized, try running python -m streamlit run app.py .
2. Missing data: If the dashboard shows an error, ensure you ran python app.py first to sreate the CSV file.


        " Developed as a capstone project for the VITyarthi platform to                    demonstrate proficiency in Python Data Analytics and UI Design." 





