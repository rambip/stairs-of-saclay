import csv
import matplotlib.pyplot as plt
import numpy as np

def get_gps(path):
    with open(path) as file:
        rows = list(csv.reader(file))
        time_list = []
        lat_list = []
        long_list = []
        alt_list = []
        for x in rows[10:]:
            time, lat, long, alt, _, _, _, _, _, _, _ = map(float, x)
            time_list.append(time)
            lat_list.append(lat)
            long_list.append(long)
            alt_list.append(alt)
    return np.array(time_list), np.array(lat_list), np.array(long_list), np.array(alt_list)


R_TERRE = 6.34e6
def coord(lat, long):
    lat=lat*(6.2831/360)
    long=long*(6.2831/360)
    y=lat*R_TERRE
    x=long*np.cos(lat)*R_TERRE
    return x-x[0], y-y[0]


time, lat, long, alt = get_gps("./trajet-guichet/data.csv")
N=20
dt = time[N]
print(dt)

print(lat[16*N], long[16*N], alt[16*N])

x,y=coord(lat, long)
plt.plot(x, y)
plt.scatter(x[::N], y[::N], color='red')
plt.show()
plt.plot(time, alt)
plt.scatter(time[::N], alt[::N], color='red')
plt.show()
