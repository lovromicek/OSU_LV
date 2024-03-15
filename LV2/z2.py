import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    return data

file_path = 'data.csv'
data = load_data(file_path)
gender = data[:, 0].astype(int)
height = data[:, 1]
mass = data[:, 2]

num_measurements = data.shape[0]
print(num_measurements)

plt.figure(figsize=(8, 6))
plt.scatter(height, mass, c=gender, cmap='coolwarm', alpha=0.5)
plt.colorbar(label='Spol')
plt.xlabel('Visina (cm)')
plt.ylabel('Masa (kg)')
plt.title('Odnos visine i mase')
plt.grid(True)
plt.show()

#ponovo ucitaj za svaku pedesetu osobu

file_path = 'data.csv'
data = load_data(file_path)
gender = data[::50, 0].astype(int)
height = data[::50, 1]
mass = data[::50, 2]
    
plt.figure(figsize=(8, 6))
plt.scatter(height, mass, c=gender, cmap='coolwarm', alpha=0.5)
plt.colorbar(label='Spol')
plt.xlabel('Visina (cm)')
plt.ylabel('Masa (kg)')
plt.title('Odnos visine i mase za svaku pedesetu osobu')
plt.grid(True)
plt.show()

#ponovo ucitaj sve osobe iz csv

file_path = 'data.csv'
data = load_data(file_path)
gender = data[:, 0].astype(int)
height = data[:, 1]
mass = data[:, 2]

min_height = np.min(height)
max_height = np.max(height)
mean_height = np.mean(height)
    
print("Statistika za visine:")
print(f"Minimalna: {min_height} cm")
print(f"Maksimalna: {max_height} cm")
print(f"Srednja: {mean_height} cm")

ind_male = (gender == 1)
ind_female = (gender == 0)
    
height_male = height[ind_male]
height_female = height[ind_female]
    
min_height_male = np.min(height_male)
max_height_male = np.max(height_male)
mean_height_male = np.mean(height_male)
    
min_height_female = np.min(height_female)
max_height_female = np.max(height_female)
mean_height_female = np.mean(height_female)
    
print("Statistika za visine:")
print("MUŠKARCI:")
print(f"Minimalna: {min_height_male} cm")
print(f"Maksimalna: {max_height_male} cm")
print(f"Srednja: {mean_height_male} cm")
    
print("\nŽENE:")
print(f"Minimalna: {min_height_female} cm")
print(f"Maksimalna: {max_height_female} cm")
print(f"Srednja: {mean_height_female} cm")