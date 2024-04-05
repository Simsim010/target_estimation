data = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]

c1 = 16
c2 = 22

def manhattan_distance(x, y):
    return abs(x - y)

for i in range(4):
    cluster1 = [age for age in data if manhattan_distance(age, c1) < manhattan_distance(age, c2)]
    cluster2 = [age for age in data if manhattan_distance(age, c1) >= manhattan_distance(age, c2)]

    new_c1 = sum(cluster1) / len(cluster1)
    new_c2 = sum(cluster2) / len(cluster2)

    print(f"Iteration {i+1}:")
    print("  x    c1      c2    Distance 1  Distance 2   New Center")
    for age in data:
        distance1 = manhattan_distance(age, c1)
        distance2 = manhattan_distance(age, c2)
        nearest_cluster = 'Cluster 1' if distance1 < distance2 else 'Cluster 2'
        new_center = new_c1 if nearest_cluster == 'Cluster 1' else new_c2
        print(f"{age:^5}  {c1:^8.2f}  {c2:^8.2f}  {distance1:^10.2f}  {distance2:^10.2f}  {new_center:^10.2f}")

    c1, c2 = new_c1, new_c2
