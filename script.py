# ALL LOCAL VARIABLES
# initialize lists
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"];
test_traveler = ['Erin Wilkes', 'Shanghai, China', 'historical site', 'art'];

# list of attractions
attractions = [[] for index in range(0, len(destinations))];

# ALL METHODS
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

#local variable with test traveler's index
test_destination_index = get_traveler_location(test_traveler);

# method to add attraction
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination);
    attractions[destination_index].append(attraction);
    return;
  except ValueError:
    print("Destination does not exist.");
    return;

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']]);
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions);
  











  
  

  
   



