import requests
import json
import random

def getRandomAnimals(count: int = 5) -> str:
    """
    Get random zoo animals from RapidAPI.
    """
    try:
        # RapidAPI Zoo Animals API
        url = f"https://zoo-animals-api.p.rapidapi.com/animals/rand/{count}"
        
        headers = {
            'x-rapidapi-host': 'zoo-animals-api.p.rapidapi.com',
            'x-rapidapi-key': '68d81e5f67msh64648b4b2552260p12203fjsneefd1c281123'
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return f"Error: Could not fetch animals (Status: {response.status_code})"
        
        animals_data = response.json()
        
        if not animals_data or len(animals_data) == 0:
            return "No animals found"
        
        # Format the animals information
        animals_info = "🦁 **Random Zoo Animals** 🦁\n\n"
        
        for i, animal in enumerate(animals_data, 1):
            name = animal.get('name', 'Unknown Animal')
            latin_name = animal.get('latin_name', 'Unknown')
            animal_type = animal.get('animal_type', 'Unknown')
            active_time = animal.get('active_time', 'Unknown')
            length_min = animal.get('length_min', 'Unknown')
            length_max = animal.get('length_max', 'Unknown')
            weight_min = animal.get('weight_min', 'Unknown')
            weight_max = animal.get('weight_max', 'Unknown')
            lifespan = animal.get('lifespan', 'Unknown')
            habitat = animal.get('habitat', 'Unknown')
            diet = animal.get('diet', 'Unknown')
            geo_range = animal.get('geo_range', 'Unknown')
            image_link = animal.get('image_link', 'No image available')
            
            # Format size and weight info
            size_info = f"{length_min}-{length_max} cm" if length_min != 'Unknown' and length_max != 'Unknown' else 'Unknown'
            weight_info = f"{weight_min}-{weight_max} kg" if weight_min != 'Unknown' and weight_max != 'Unknown' else 'Unknown'
            
            animal_info = f"""**{i}. {name}** 🐾
📝 **Latin Name:** {latin_name}
🏷️ **Type:** {animal_type}
⏰ **Active Time:** {active_time}
📏 **Size:** {size_info}
⚖️ **Weight:** {weight_info}
🕐 **Lifespan:** {lifespan} years
🏠 **Habitat:** {habitat}
🍽️ **Diet:** {diet}
🌍 **Geographic Range:** {geo_range}
📸 **Image:** {image_link}

"""
            animals_info += animal_info
        
        return animals_info
        
    except Exception as e:
        return f"Error fetching animals: {str(e)}"

def searchAnimalByName(name: str) -> str:
    """
    Search for a specific animal by name.
    """
    try:
        # Get a larger set of random animals to search through
        url = "https://zoo-animals-api.p.rapidapi.com/animals/rand/50"
        
        headers = {
            'x-rapidapi-host': 'zoo-animals-api.p.rapidapi.com',
            'x-rapidapi-key': '68d81e5f67msh64648b4b2552260p12203fjsneefd1c281123'
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return f"Error: Could not search for '{name}' (Status: {response.status_code})"
        
        animals_data = response.json()
        
        if not animals_data:
            return f"No animals found"
        
        # Search for the animal by name (case insensitive)
        search_name = name.lower()
        found_animals = []
        
        for animal in animals_data:
            animal_name = animal.get('name', '').lower()
            if search_name in animal_name or animal_name in search_name:
                found_animals.append(animal)
        
        if not found_animals:
            return f"No animals found matching '{name}'. Try searching for: lion, elephant, giraffe, tiger, bear, etc."
        
        # Return the first match with detailed info
        animal = found_animals[0]
        name = animal.get('name', 'Unknown Animal')
        latin_name = animal.get('latin_name', 'Unknown')
        animal_type = animal.get('animal_type', 'Unknown')
        active_time = animal.get('active_time', 'Unknown')
        length_min = animal.get('length_min', 'Unknown')
        length_max = animal.get('length_max', 'Unknown')
        weight_min = animal.get('weight_min', 'Unknown')
        weight_max = animal.get('weight_max', 'Unknown')
        lifespan = animal.get('lifespan', 'Unknown')
        habitat = animal.get('habitat', 'Unknown')
        diet = animal.get('diet', 'Unknown')
        geo_range = animal.get('geo_range', 'Unknown')
        image_link = animal.get('image_link', 'No image available')
        
        # Format size and weight info
        size_info = f"{length_min}-{length_max} cm" if length_min != 'Unknown' and length_max != 'Unknown' else 'Unknown'
        weight_info = f"{weight_min}-{weight_max} kg" if weight_min != 'Unknown' and weight_max != 'Unknown' else 'Unknown'
        
        animal_info = f"""🦁 **{name}** 🦁

📝 **Latin Name:** {latin_name}
🏷️ **Type:** {animal_type}
⏰ **Active Time:** {active_time}
📏 **Size:** {size_info}
⚖️ **Weight:** {weight_info}
🕐 **Lifespan:** {lifespan} years
🏠 **Habitat:** {habitat}
🍽️ **Diet:** {diet}
🌍 **Geographic Range:** {geo_range}
📸 **Image:** {image_link}

{f"**Other matches found:** {len(found_animals)-1} more animals" if len(found_animals) > 1 else ""}"""
        
        return animal_info
        
    except Exception as e:
        return f"Error searching for '{name}': {str(e)}"

def getAnimalsByType(animal_type: str) -> str:
    """
    Get animals by type (mammal, bird, reptile, etc.).
    """
    try:
        # Get a larger set to filter by type
        url = "https://zoo-animals-api.p.rapidapi.com/animals/rand/50"
        
        headers = {
            'x-rapidapi-host': 'zoo-animals-api.p.rapidapi.com',
            'x-rapidapi-key': '68d81e5f67msh64648b4b2552260p12203fjsneefd1c281123'
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return f"Error: Could not fetch {animal_type} animals (Status: {response.status_code})"
        
        animals_data = response.json()
        
        if not animals_data:
            return f"No animals found"
        
        # Filter by type
        search_type = animal_type.lower()
        filtered_animals = []
        
        for animal in animals_data:
            animal_type_field = animal.get('animal_type', '').lower()
            if search_type in animal_type_field:
                filtered_animals.append(animal)
        
        if not filtered_animals:
            return f"No {animal_type} animals found. Try: mammal, bird, reptile, fish, amphibian"
        
        # Return up to 5 animals of this type
        animals_info = f"🦁 **{animal_type.title()} Animals** 🦁\n\n"
        
        for i, animal in enumerate(filtered_animals[:5], 1):
            name = animal.get('name', 'Unknown Animal')
            latin_name = animal.get('latin_name', 'Unknown')
            habitat = animal.get('habitat', 'Unknown')
            diet = animal.get('diet', 'Unknown')
            
            animal_info = f"""**{i}. {name}**
📝 Latin: {latin_name}
🏠 Habitat: {habitat}
🍽️ Diet: {diet}

"""
            animals_info += animal_info
        
        if len(filtered_animals) > 5:
            animals_info += f"*...and {len(filtered_animals)-5} more {animal_type} animals*"
        
        return animals_info
        
    except Exception as e:
        return f"Error fetching {animal_type} animals: {str(e)}"
