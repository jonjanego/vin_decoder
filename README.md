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

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you’d like to improve the script.

## License

This project is licensed under the MIT License.

---

Let me know if you want to tweak the tone or add more details!
