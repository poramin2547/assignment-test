# จงเขียนฟังก์ชัน assignRider(order, riders) เพื่อหา Rider ที่เหมาะสมที่สุด

import math
import time

def haversine(pickup_lat, pickup_lon, rider_lat, rider_lon):
  
    R = 6371  #รัศมีโลกหน่วย KM

    lat = math.radians(rider_lat - pickup_lat)
    lon = math.radians(rider_lon - pickup_lon)

    a = math.sin(lat / 2) ** 2 + math.cos(math.radians(pickup_lat)) * math.cos(math.radians(rider_lat)) * math.sin(lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance #หน่วย KM
  
def assignRider(order,riders):
  max_radius_km = 5 #หน่วย KM
  time_limit = 120 #หน่วยวินาที
  
  now = time.time()
  
  valid_riders = []
  
  for rider in riders:
    
    if now - rider['last_updated'] > time_limit:
      continue
    
    distance = haversine(
      order['pickup_lat'], 
      order['pickup_long'], 
      rider['current_lat'], 
      rider['current_long']
    )
    
    rider['distance'] = distance
      
    if distance <= max_radius_km:
      valid_riders.append((rider))
  
  if not valid_riders:
    return 'No rider within 5 km'
  
  valid_riders.sort(key=lambda x: x['distance'])
  best_rider = valid_riders[0] 
    
  for rider in valid_riders[1:]:  
    if abs(rider['distance'] - best_rider['distance']) <= 0.5:
      if rider['rating'] > best_rider['rating']:
          best_rider = rider

  return best_rider['id']
  
  
order = {
  "pickup_lat": 13.7563,
  "pickup_long": 100.5018
}

riders = [
    {
        "id": 1,
        "current_lat": 13.7600,
        "current_long": 100.5100,
        "rating": 4.5,
        "last_updated": time.time()
    },
    {
        "id": 2,
        "current_lat": 13.7580,
        "current_long": 100.5030,
        "rating": 4.9,
        "last_updated": time.time()
    }
]

result = assignRider(order, riders)

print(result)
    
  