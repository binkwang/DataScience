import streamlit as st
import numpy as np
import pandas as pd
import time

def run_it():

  st.title('My first app')
  st.text("Here's our first attempt at using data to create a table:")

  # """
  # # My first app
  # Here's our first attempt at using data to create a table:
  # """

  #################

  st.subheader("Show data")

  dataFrame1 = pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40]
  })

  st.dataframe(dataFrame1)

  #################

  st.subheader("Draw a line chart")

  random1 = np.random.randn(20, 3)  
  st.write(random1)
  chart_data = pd.DataFrame(random1, columns=['a', 'b', 'c'])
  st.line_chart(chart_data)

  #################

  st.subheader("Plot a map")

  random2 = np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4]
  st.write(random2)
  map_data = pd.DataFrame(random2, columns=['lat', 'lon'])
  st.map(map_data)

  #################

  st.subheader("Use checkbox")

  if st.checkbox('Show dataframe'):
      # random3 = np.random.randn(20, 3)
      chart_data3 = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
      st.write(chart_data3)

  #################

  st.subheader("Use selectbox")

  first_column = dataFrame1['first column']
  option1 = st.selectbox('Which number do you like best?', first_column)
  st.text(f"You selected: {option1}") # st.write("You selected: ", option1)

  #################

  st.subheader("Use expander")

  expander = st.beta_expander("FAQ")
  expander.write("Here you could put in some really, really long explanations...")

  #################

  st.subheader("Use beta columns")

  left_column, right_column = st.beta_columns(2)
  pressed = left_column.button('Press me?')
  if pressed:
      right_column.write("Woohoo!")

  #################

  st.subheader("Show progress bar")
  st.text("Starting a long computation...")

  # Add a placeholder
  latest_iteration = st.empty()
  bar = st.progress(0)

  for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1) # Update the progress bar with each iteration.
    time.sleep(0.02)

  st.text("...and now we\'re done!")

  #################



