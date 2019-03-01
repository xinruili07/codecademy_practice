# initialize lists
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"];
test_traveler = ['Erin Wilkes', 'Shanghai, China', 'historical site', 'art'];

# method to find index
def get_destination_index(destination):
  destination_index = destinations.index(destination);
  
  return destination_index;

# method to find traveler's destination's index
def get_traveler_location(traveler):
  traveler_destination = traveler[1];
  # call previous method to find index
  traveler_destination_index = get_destination_index(traveler_destination);
  # return index
  return traveler_destination_index;

#local variable with traveler's index
test_destination_index = get_traveler_location(test_traveler);

print(test_destination_index);




  
  

  
   



