
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':55 ,'anaemia':0 ,'creatinine_phosphokinase':7861 ,'diabetes': 0,'ejection_fraction': 38,'high_blood_pressure':0 ,'platelets': 263358.03,'serum_creatinine':1.1 ,'serum_sodium': 136,'sex': 1,'smoking': 0,'time':6})

print(r.json())

																				55,0,7861,0,38,0,263358.03,1.1,136,1,0,6

