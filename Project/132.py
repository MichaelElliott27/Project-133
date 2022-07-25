low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 100:
    low_gravity_planets.append(planet_data_rows[index])
print(len(low_gravity_planets))
print(headers)
planet_type_values=[]
for planet_data in planet_data_rows:
  planet_type_values.append(planet_data[6])
print(list(set(planet_type_values)))
planet_type_values=[]
for planet_data in planet_data_rows:
  planet_type_values.append(planet_data[6])
print(list(set(planet_type_values)))
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

X = []
for index,planet_mass in enumerate(planet_masses):
  temp_list = [
             planet_radiuses[index],
             planet_mass
  ]
  X.append(temp_list)
wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters = i,init = 'k-means++',random_state = 42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11),wcss,markers='o',color='green')
plt.title("the elbow method")
plt.xlabel("number of clusters")
plt.ylabel('wcss')
plt.show()
planet_masses=[]
planet_radiuses=[]
planet_types=[]
for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_types.append(planet_data[6])

fig=px.scatter(x=planet_radiuses,y=planet_masses,color=planet_types)
fig.show()
suitable_planets = []
for planet_data in low_gravity_planets:
  if planet_data[6].lower() == 'terrestrial' or planet_data[6].lower() == 'super earth':
    suitable_planets.append(planet_data)
print(len(suitable_planets))