df = {  
    "region": {  
        "asia": {  
            "india": {  
                "population": 1400000000,  
                "capital": "New Delhi",  
                "currency": "INR",  
                "official_language": "Hindi",  
                "financial": {  
                    "gdp": 3170000000000,  
                    "main_exports": ["IT Services", "Textiles", "Pharmaceuticals"],  
                    "major_markets": ["USA", "EU", "China"]  
                },  
                "biological": {  
                    "national_animal": "Tiger",  
                    "forest_cover": "24%",  
                    "biodiversity_hotspots": ["Western Ghats", "Himalayas", "Sundarbans"]  
                },  
                "states": {  
                    "maharashtra": {  
                        "population": 123000000,  
                        "capital": "Mumbai",  
                        "primary_language": "Marathi",  
                        "famous_for": "Bollywood",  
                        "financial": {  
                            "gdp": 400000000000,  
                            "main_exports": ["Agriculture", "Automobiles", "Textiles"],  
                            "major_markets": ["USA", "UAE", "UK"]  
                        },  
                        "biological": {  
                            "national_park": "Sanjay Gandhi National Park",  
                            "endangered_species": ["Leopard", "Indian Rock Python"],  
                            "forest_cover": "20%"  
                        }  
                    },  
                    "karnataka": {  
                        "population": 68000000,  
                        "capital": "Bengaluru",  
                        "primary_language": "Kannada",  
                        "famous_for": "IT Hub",  
                        "financial": {  
                            "gdp": 220000000000,  
                            "main_exports": ["Software Services", "Coffee", "Silk"],  
                            "major_markets": ["Germany", "Japan", "USA"]  
                        },  
                        "biological": {  
                            "national_park": "Bannerghatta National Park",  
                            "endangered_species": ["Elephant", "Sloth Bear"],  
                            "forest_cover": "33%"  
                        }  
                    }  
                }  
            }  
        }  
    }  
}



def extract(json_data, region_name, country_name, state_name):
   
    try:
        # Navigate to the state within the dataset
        region_data = json_data.get("region", {})
        asia_data = region_data.get(region_name, {})
        india_states = asia_data.get(country_name, {}).get("states", {})
        
        state_data = india_states.get(state_name.lower())
        
        if state_data:
            # Restructure financial and biological data
            financial = state_data.get("financial", {})
            biological = state_data.get("biological", {})
            output = {
                "gdp": biological.get("national_park", ""),
                "main_exports": biological.get("endangered_species", []),
                "major_markets": biological.get("forest_cover", "")
            }
            return {"output": output}
        else:
            return {"error": f"State '{state_name}' not found in the dataset."}
    except Exception as e:
        return {"error": str(e)}
    


    
# Example Usage


region_input = input("Enter the region name: ")
country_input = input("Enter the country name: ")
state_input = input("Enter the state name: ")


output = extract(df,region_input,country_input,state_input)
print(output)












