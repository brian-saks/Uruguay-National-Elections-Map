
# 🗳️ Uruguay National Elections Map

This is a map of Uruguay with every voting centre in de city of Montevideo for the National Elections of 2024. 

## About
This proyect is designed to help people visualize their assigned voting centers for the National Elections of Uruguay in 2024.

The data for the voting centers was sourced from the Uruguayan National Electoral Court website. Then using the [Google Geocododing API](https://developers.google.com/maps/documentation/geocoding/overview?hl=es-419),  I retrieved the geographic coordinates for each center. Each voting center is displayed on an interactive map using Folium, with a popup that includes the center’s name, address, and a list of all the voting circuits available there.

To make navigation easier, a search bar is also included, allowing users to quickly find specific voting centers.

## Prerequisites
- **Python:** 3.6 or above
- **folium:** 0.14.0

## Instalation
Clone the repositry

        git clone https://github.com/brian-saks/

## Usage

You can access the app online at: [Election Map](google.com)

To run the application locally:  
 
Navigate to the project directory
        
        cd Election Map

Run the app

        python main.py

If using VSCode LiveServer, open at

        http://localhost:3000 



