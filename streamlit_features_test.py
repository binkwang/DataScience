import streamlit as st
import numpy as np
import pandas as pd
import time

def run_it():
  
  st.title('My first app')
  st.write("Here's our first attempt at using data to create a table:")

  # """
  # # My first app
  # Here's our first attempt at using data to create a table:
  # """

  """
  ## Add text and data
  """

  dataFrame = pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40]
  })

  st.write(dataFrame)


  """
  ## Use magic
  Any time that Streamlit sees a variable or a literal value on its own line,
  it automatically writes that to your app using st.write().
  """

  df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
  })

  df

  """
  ## Draw a line chart
  """

  random1 = np.random.randn(20, 3)  
  st.write(random1)
  chart_data = pd.DataFrame(random1, columns=['a', 'b', 'c'])
  st.line_chart(chart_data)

  """
  ## Plot a map
  """

  random2 = np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4]
  st.write(random2)
  map_data = pd.DataFrame(random2, columns=['lat', 'lon'])
  st.map(map_data)


  """
  ## Use checkboxes to show/hide data
  """

  if st.checkbox('Show dataframe'):
      chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
      chart_data

  """
  ## Use a selectbox for options
  """

  first_column = df['first column']
  option1 = st.selectbox('Which number do you like best?', first_column, key="1")
  'You selected: ', option1

  """
  ## Use the expander
  """
  expander = st.beta_expander("FAQ")
  expander.write("Here you could put in some really, really long explanations...")


  """
  ## Use beta_columns
  """

  left_column, right_column = st.beta_columns(2)
  pressed = left_column.button('Press me?')
  if pressed:
      right_column.write("Woohoo!")

  """
  ## Use a sidebar
  Most of the elements you can put into your app can also be put 
  into a sidebar using this syntax: st.sidebar.element_name().
  """

  option2 = st.sidebar.selectbox('Which number do you like best?', first_column, key="2")
  'You selected:', option2


  """
  ## Show progress bar
  """

  'Starting a long computation...'

  # Add a placeholder
  latest_iteration = st.empty()
  bar = st.progress(0)

  for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

  '...and now we\'re done!'


  """
  ## Share your app
  """







