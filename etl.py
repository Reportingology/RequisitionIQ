import pandas as pd
import numpy as np
import datetime

import filled_requisitions

requisition_date_columns = [
  "requisition_opened_date",   ### Date the requisition was opened in the system
  "date_first_screen",         ### Date the first screen occured on the requisition
  "requisition_filled_date"    ### Date requisition was filled. All reqs are singleheded for ReqIQ MVP
]

def format_date_columns(data_frame, requisition_date_columns):
  for column in date_columns:
    data_frame[column] = pd.to_datetime(data_frame[column])
    data_frame[f"{column}_month"] = data_frame[column].dt.month
    data_frame[f"{column}_year"] = data_frame[column].dt.year

  return
  data_frame

#### FORMAT DATES #####
format_date_columns(filled_requisitions, date_columns)
