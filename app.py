import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="AuraSense | Smart Environment", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
.main { background-color: #0e1117; }
.stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; -moz-border-radius:10px; -webkit-border-radius:10px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
 st.image("https://img.icons8.com/fluency/96/000000/leaf.png", width=80)
 st.title("Control Center")
 st.divider()
 room_occupancy = st.slider("Room Occupancy (People)", 1, 10, 2)
 window_status = st.radio("Window Status", ["Closed", "Open"])
 st.info("Adjusting these simulates real-world environmental changes.")

@st.cache_data
def get_data():
 df = pd.read_csv('data/sensor_readings.csv')
 df['Timestamp'] = pd.to_datetime(df['Timestamp'])
 return df

df = get_data()
latest = df.iloc[-1]

col_h1, col_h2 = st.columns([3, 1])
with col_h1:
 st.title("🍃 AuraSense Intelligence")
 st.subheader("Predictive Indoor Air Quality & Cognitive Load Monitor")

st.divider()
m1, m2, m3, m4 = st.columns(4)

def create_gauge(value, title, color):
    fig = go.Figure() 
    
    fig.add_trace(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': title, 'font': {'size': 18}},
        gauge = {'axis': {'range': [None, 2000] if "CO2" in title else [None, 100]},
                 'bar': {'color': color}}
    ))
    
    fig.update_layout(
        height=250, 
        margin=dict(l=20, r=20, t=50, b=20), 
        paper_bgcolor='rgba(0,0,0,0)', 
        font={'color': "white"}
    )
    return fig

with m1:
 st.plotly_chart(create_gauge(latest['CO2_ppm'], "CO2 (ppm)", "#ff4b4b" if latest['CO2_ppm'] > 1000 else "#00d4ff"), use_container_width=True)

focus_score = max(0, min(100, 100 - (latest['CO2_ppm'] - 400) * 0.08))
with m2:
 st.plotly_chart(create_gauge(focus_score, "Focus Score %", "#00ffcc"), use_container_width=True)

with m3:
 st.metric("Temperature", f"{latest['Temperature_C']:.1f} °C", "1.2 °C")
with m4:
 st.metric("Humidity", f"{latest['Humidity_%']:.0f} %", "-2%")

st.write("### 📈 Environmental Trend Analysis")
tab1, tab2 = st.tabs(["CO2 Saturation", "Heat Map"])

with tab1:
 fig_main = px.area(df, x='Timestamp', y='CO2_ppm',
 title="24-Hour Air Quality Flux",
 color_discrete_sequence=['#00d4ff'])
 fig_main.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')
 st.plotly_chart(fig_main, use_container_width=True)

with tab2:
 fig_heat = px.density_heatmap(df, x="Temperature_C", y="Humidity_%", z="CO2_ppm",
 color_continuous_scale="Viridis")
 fig_heat.update_layout(template="plotly_dark")
 st.plotly_chart(fig_heat, use_container_width=True)

st.divider()
if latest['CO2_ppm'] > 1000:
 st.error(f"🚨 **CRITICAL:** CO2 is at {latest['CO2_ppm']:.0f}ppm. Cognitive performance expected to drop by 15%. ** Action: Open Window.**")
else:
 st.success("✅ **OPTIMAL:** Environment is perfect for deep focus work.")
