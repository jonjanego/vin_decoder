import re

# WMI (World Manufacturer Identifier) mapping
WMI_MAPPING = {
    "1": "United States",
    "2": "Canada",
    "3": "Mexico",
    "J": "Japan",
    "K": "South Korea",
    "S": "United Kingdom",
    "W": "Germany",
    "Z": "Italy",
    "4": "United States",
    "5": "United States",
    "7": "United States"
    # Add more mappings as needed
}

# Year code mapping (for 1980-2039)
YEAR_MAPPING = {
    "A": 1980, "B": 1981, "C": 1982, "D": 1983, "E": 1984, "F": 1985, "G": 1986, "H": 1987,
    "J": 1988, "K": 1989, "L": 1990, "M": 1991, "N": 1992, "P": 1993, "R": 1994, "S": 1995,
    "T": 1996, "V": 1997, "W": 1998, "X": 1999, "Y": 2000, "1": 2001, "2": 2002, "3": 2003,
    "4": 2004, "5": 2005, "6": 2006, "7": 2007, "8": 2008, "9": 2009, "A": 2010, "B": 2011,
    "C": 2012, "D": 2013, "E": 2014, "F": 2015, "G": 2016, "H": 2017, "J": 2018, "K": 2019,
    "L": 2020, "M": 2021, "N": 2022, "P": 2023, "R": 2024, "S": 2025, "T": 2026, "V": 2027,
    "W": 2028, "X": 2029, "Y": 2030,
}

def decode_vin(vin):
    """
    Decodes a Vehicle Identification Number (VIN) and extracts key details.
    :param vin: The 17-character VIN string.
    :return: A dictionary with decoded details.
    """
    if not re.match(r"^[A-HJ-NPR-Z0-9]{17}$", vin):
        raise ValueError("Invalid VIN format. Ensure it is 17 characters long and excludes I, O, and Q.")

    # Extract WMI (first 3 characters)
    wmi = vin[:3]
    country = WMI_MAPPING.get(wmi[0], "Unknown")
    manufacturer = wmi  # In practice, you'd map this to a manufacturer database.

    # Extract year (10th character)
    year_code = vin[9]
    year = YEAR_MAPPING.get(year_code, "Unknown")

    # Extract plant code (11th character)
    plant_code = vin[10]

    return {
        "VIN": vin,
        "Country of Manufacture": country,
        "Manufacturer": manufacturer,
        "Year of Manufacture": year,
        "Plant Code": plant_code,
    }

# Example usage
if __name__ == "__main__":
    vin_input = input("Enter a 17-character VIN: ").strip()
    try:
        decoded_details = decode_vin(vin_input)
        print("\nDecoded VIN Details:")
        for key, value in decoded_details.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error: {e}")