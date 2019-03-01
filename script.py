# ALL LOCAL VARIABLES
# initialize lists
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"];
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']];

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
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  # destination index
  destination_index = get_destination_index(destination);
  # attractions in the destination city
  attractions_in_city = attractions[destination_index];
  attractions_with_interests = [];
  # compare each attraction tag with the list of interests. If matched, append said attraction.
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1];
    for interest in interests:
      if (attraction_tags.count(interest) > 0):
        attractions_with_interests.append(possible_attraction[0]);
  return attractions_with_interests;

# tests
la_arts = find_attractions("Los Angeles, USA", ['art']);
print(la_arts);

# main event
def get_attraction_for_traveler(traveler):
  traveler_destination = traveler[1];
  traveler_interests = traveler[2];
  traveler_attractions = find_attractions(traveler_destination, traveler_interests);
  
  interests_string = "Hi ";
  interests_string += traveler[0];
  interests_string += ", we think you'll like these places around ";
  interests_string += traveler[1] + ": ";
  
  # for attraction in traveler_attractions:
  for index in range(0, len(traveler_attractions)):
    if (index < len(traveler_attractions)-1):
      interests_string += traveler_attractions[index] + ", ";
    if (index == len(traveler_attractions)-1):
      interests_string += "and the " + traveler_attractions[index] + ".";
  return interests_string;

smills_france = get_attraction_for_traveler(['Dereck Smill', 'Paris, France', ['monument', 'art']]);

print(smills_france);
  
  

    
    
    
    
    
    
  
  











  
  

  
   



