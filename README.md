# Zoo Animals MCP Server


[![smithery badge](https://smithery.ai/badge/@yusaaztrk/zoo-animal-mcp-main)](https://smithery.ai/server/@yusaaztrk/zoo-animal-mcp-main)

A Model Context Protocol (MCP) server that provides zoo animal information using RapidAPI's Zoo Animals API.

## Features

- Get random zoo animals with detailed information
- Search for specific animals by name
- Filter animals by type (mammal, bird, reptile, etc.)
- Comprehensive animal data including:
  - Name and Latin name
  - Physical characteristics (size, weight)
  - Habitat and geographic range
  - Diet and active time
  - Lifespan information
  - High-quality images

## Usage

The server provides three tools:

### get_random_animals(count: int = 5)

Get random zoo animals.

**Parameters:**
- `count`: Number of animals to fetch (1-10, default: 5)

**Returns:**
- Detailed information about random animals

### search_animal(name: str)

Search for a specific animal by name.

**Parameters:**
- `name`: Animal name to search for (e.g., "lion", "elephant")

**Returns:**
- Comprehensive information about the found animal

### get_animals_by_type(animal_type: str)

Get animals by their type/category.

**Parameters:**
- `animal_type`: Type of animals (e.g., "mammal", "bird", "reptile")

**Returns:**
- List of animals of the specified type

## Installation

### Installing via Smithery

To install zoo-animal-mcp-main for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@yusaaztrk/zoo-animal-mcp-main):

```bash
npx -y @smithery/cli install @yusaaztrk/zoo-animal-mcp-main --client claude
```

### Manual Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python server.py
```

## API

This MCP server uses RapidAPI's Zoo Animals API which provides comprehensive animal data from zoos worldwide.
