
import urllib.request
import sys

import csv
import codecs
        
try: 
  ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/93955?unitGroup=metric&include=days&key=JHWJNB6EF542PWGY772FRBJN8&contentType=csv")
  
  # Parse the results as CSV
  CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
        
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()