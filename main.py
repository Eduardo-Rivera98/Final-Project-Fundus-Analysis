

import streamlit as st

from pages import home
from pages import diagnosis
from pages import graphs
from pages import photos
from multipage import MultiPage
app = MultiPage()

app.add_page("Home", home.app)
app.add_page("Diagnosis", diagnosis.app)
app.add_page('Graphs', graphs.app)
app.add_page('Photographs',photos.app)
app.run()





    