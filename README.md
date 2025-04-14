# VIN Decoder

**VIN Decoder** is a Python script designed to decode Vehicle Identification Numbers (VINs). A VIN is a unique code used to identify motor vehicles, and this tool helps extract meaningful information from it.

## Features

- Decode any valid VIN code.
- Extract details such as:
  - Country of origin
  - Manufacturer
  - Vehicle type
  - Model year
  - Assembly plant
- 100% Python-based for flexibility and portability.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/jonjanego/vin_decoder.git
   ```
2. Navigate to the project folder:
   ```
   cd vin_decoder
   ```

## Usage

Run the script with the following command:

```
python3 vin_decoder.py <VIN>
```

Replace `<VIN>` with the 17-character Vehicle Identification Number you want to decode.

It will also accept a VIN in interactive mode

## Example

```
python vin_decoder.py 1HGCM82633A123456
```

Output:
```
Country of Origin: USA
Manufacturer: Honda
Vehicle Type: Passenger Car
Model Year: 2003
Assembly Plant: Ohio
```

## Source Data

This project relies on the country and manufacturer lookup codes that is published on [Wikipedia](https://en.wikipedia.org/wiki/Vehicle_identification_number#List_of_common_WMI), and is current as of its latest updates in April 2025. There isn't an automatic sync process or anything, so take this "As-is"

The country code and manufacturer looks might also be individually useful:

- [Country code lookup](country_codes.json)
- [Manufacturer lookup](wmi_manufacturers.json)


## Credits

Thank you Copilot + GPT-4o for the help.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you’d like to improve the script.

## License

This project is licensed under the MIT License.

---

Let me know if you want to tweak the tone or add more details!
