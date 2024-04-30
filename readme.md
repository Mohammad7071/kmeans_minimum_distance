# MINIMUM_DISTANCE AND CLUSTRING (PROJECT)
this project calculate minimum distance between list of the points and centroids by manhattan method and clustring points with closest centroid
## INTRODUCTION
you can use this codes in python when you have list of the points,program choose randomly 3 point among of points and calculate minimum distance
## CODE
important section of code is
```python
def manhattan_distance (point1 , point2):
    x1,y1,z1=point1
    x2,y2,z2=point2
    return abs(x1-x2)+abs(y1-y2)+ abs(z1-z2)
```
