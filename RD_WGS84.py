# RD to WGS84
from rijksdriehoek import rijksdriehoek 
import streamlit as st
import numpy as np
import pandas as pd

rd = rijksdriehoek.Rijksdriehoek()

st.write('RD naar WGS84')

rd.rd_x = st.number_input('X-Coördinaat')
rd.rd_y = st.number_input('Y-Coördinaat')

# print("Orginal coordinates in RD: {},{}".format(str(rd.rd_x), str(rd.rd_y)))
lat, lon = rd.to_wgs()

lat = round(lat,6)
lon = round(lon,6)

st.write("X-Coördinaat RD {} -> WGS84 {}".format(rd.rd_x,lat))
st.write("Y-Coördinaat RD {} -> WGS84 {}".format(rd.rd_y,lon))

loc = np.array([lat,lon])

df = pd.DataFrame(
    [loc],
    columns=['lat', 'lon']
)

st.map(df, size=2, zoom=14)