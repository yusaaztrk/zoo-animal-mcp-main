from mcp.server.fastmcp import FastMCP
from app import getRandomAnimals, searchAnimalByName, getAnimalsByType

# Initialize MCP server
mcp = FastMCP("zoo-animals-mcp")

@mcp.tool()
async def get_random_animals(count: int = 5) -> str:
    """
    Get random zoo animals.
    
    Args:
        count: Number of random animals to fetch (1-10, default: 5)
    
    Returns:
        Information about random zoo animals including name, habitat, diet, size, and image
    """
    # Limit count to reasonable range
    count = max(1, min(count, 10))
    
    # Get random animals from the app
    animals_info = getRandomAnimals(count)
    if not animals_info:
        return "No animal information found."

    return animals_info

@mcp.tool()
async def search_animal(name: str) -> str:
    """
    Search for a specific animal by name.
    
    Args:
        name: The animal name to search for (e.g., "lion", "elephant", "giraffe")
    
    Returns:
        Detailed information about the animal including habitat, diet, size, lifespan, and image
    """
    if not name or not name.strip():
        return "Please provide an animal name to search for."
    
    # Search for the animal
    animal_info = searchAnimalByName(name.strip())
    if not animal_info:
        return f"No information found for '{name}'."

    return animal_info

@mcp.tool()
async def get_animals_by_type(animal_type: str) -> str:
    """
    Get animals by their type/category.
    
    Args:
        animal_type: Type of animals to fetch (e.g., "mammal", "bird", "reptile", "fish")
    
    Returns:
        List of animals of the specified type with basic information
    """
    if not animal_type or not animal_type.strip():
        return "Please provide an animal type (mammal, bird, reptile, fish, amphibian)."
    
    # Get animals by type
    animals_info = getAnimalsByType(animal_type.strip())
    if not animals_info:
        return f"No {animal_type} animals found."

    return animals_info

if __name__ == "__main__":
    mcp.run(transport="stdio")
