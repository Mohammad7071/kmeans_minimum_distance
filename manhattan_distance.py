import random
#function to calculate euclid distance between tow point
def manhattan_distance (point1 , point2):
    x1,y1,z1=point1
    x2,y2,z2=point2
    return abs(x1-x2)+abs(y1-y2)+ abs(z1-z2)

# read data point from file
def read_data_points(file_path):
    data_points = [] #can be in your Pc
    with open (file_path,"r") as file:
        for line in file:
            try:
                x,y,z = map(float , line.strip().split(","))
                data_points.append((x,y,z))
            except ValueError:
                print(f"warning:invaliddata point '{line.strip()}' skiped.")
    return data_points

#Function to initialize center points (randomly)
def initialize_centroids(data_points,k):
    centroids=random.sample(data_points,k)
    return centroids

#function to assign data point to the closest centroid
def assign_clusters (data_points,centroids):
    clusters = {centroid:[] for centroid in centroids}
    for point in data_points:
        closest_centroid = min(centroids, key = lambda centroid:manhattan_distance(point,centroid))
        clusters [closest_centroid].append(point)
    return clusters
#function to update centroids based on the assigned cluster 
def update_centroids (clusters):
    new_centroids =[]
    for cluster in clusters.values():
        if cluster:
            x_sum,y_sum,z_sum = sum(point[0] for point in cluster),sum(point[1] for point in cluster), sum(point[2] for point in cluster)
            new_centroids=(x_sum//len(cluster),y_sum//len(cluster),z_sum//len(cluster))
            new_centroids.append(new_centroids)
    return new_centroids

def k_means_clustering(data_points,k):
    centroids = initialize_centroids(data_points,k)
    previous_centroids = None
    while centroids != previous_centroids:
        previous_centroids=centroids
        clusters = assign_clusters(data_points,centroids)
        centroids= update_centroids(clusters)
    return clusters

#file path contaning data points
file_path= "data_point.txt"
#read data point from file
deta_points = read_data_points(file_path)
#number of k
k=3
#perform k_means_clustering
clusters = k_means_clustering(deta_points,k)
#print
for centroid,points in clusters.items():
    print(f"centroid:{centroid}")
    print(f"points:{points}")
    print ()