import psutil
import os

# gives a single float value
cpu_load = psutil.cpu_percent()
# gives an object with many fields
v_memory = psutil.virtual_memory()
# you can convert that object to a dictionary 
d = dict(psutil.virtual_memory()._asdict())
# you can have the percentage of used RAM
v_memory_percent = psutil.virtual_memory().percent
79.2
# you can calculate percentage of available memory
percentage_memory_available = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
20.8

dic = {
    
}
x = 0
for proc in psutil.process_iter(['pid', 'name', 'username']):
    dic[x] = proc.info
    x += 1

print(x)
print(dic)
print(len(dic))
for i in dic:
    if dic[i]['name'] == 'chrome.exe': os.system(f"taskkill /IM {dic[i]['pid']} /F")