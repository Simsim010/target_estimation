import random
import math
import matplotlib.pyplot as plt

#verilen ilk hız, hedefin ortasına olan uzak hedefe ulaşmak için gerekli 
def calculate_required_velocity(v_initial, distance, height, angle):
    g = 9.81  
    
    theta = math.radians(angle)
    
    v_initial_y = (v_initial * math.sin(theta))  
    time_to_max_height =  v_initial_y / g
    max_height = height + ( ( v_initial_y**2 ) / (2 * g) )
    fall_time = math.sqrt(2 * max_height / g)
    total_time_of_flight = time_to_max_height + fall_time
    required_velocity = distance / (math.cos(theta) * total_time_of_flight)
    
    return required_velocity, total_time_of_flight

#normalde okul numaram 3 ve grafikte yükseklik farkı çok oladığı için yükseklik olarak 1200mt kullandım
height = 1200  
rand_dist = random.randint(-10,10) * 200
distance_to_target = 20000 + rand_dist 
rand_len = random.randint(-2,2) * 100
target_length = 1000 + rand_len
angle = 30  
min_velocity = 330  
max_velocity = 1800  
v_initial = (min_velocity + max_velocity) / 2
iterations = 0

while True:
    iterations += 1
    
    required_velocity, time_of_flight = calculate_required_velocity(v_initial, distance_to_target, height, angle)
    
    if int(required_velocity) > int(v_initial):
        print("Hedefin önüne düştü")
        min_velocity = v_initial
    elif int(required_velocity) < int(v_initial):
        print("Hedefine arkasına düştü")
        max_velocity = v_initial

    tolerance = 0.5

    if abs(required_velocity - v_initial) < tolerance:
        print("Hedef Vuruldu!")
        print("Toplam Atış Sayısı: ", iterations)
        print("Hedefi vurmak için gerekli hız: ", required_velocity, "m/s")
        break
        
    v_initial = (min_velocity + max_velocity) / 2

#Hedefi vuran atışın grafiği çizdiriliyor

x_values = []
y_values = []

time_intervals = int(math.ceil(time_of_flight)) 
for t in range(time_intervals + 1):
    x_position = required_velocity * math.cos(math.radians(angle)) * t
    y_position = height + (required_velocity * math.sin(math.radians(angle)) * t) - (0.5 * 9.81 * (t ** 2))
    
    x_values.append(x_position)
    y_values.append(y_position)

plt.plot(x_values, y_values, linestyle='-', color='b')
plt.xlabel('Uzaklık (m)')
plt.ylabel('Yükseklik (m)')
plt.title('Top Atışı Grafiği')
plt.grid(True)

plt.plot(0, height, marker='s', color='r', label='Top')  
plt.plot(distance_to_target, 0, marker='^', color='g', label='Hedef')  
plt.legend()

plt.show()
