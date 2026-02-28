# IBIMjr

![IBIMjr Logo](BIMI.svg)

IBIMjr (IBIM Junior) is a lightweight implementation framework designed for learning and prototyping.

## Overview

IBIMjr provides a simple, modular approach to building and managing components with a focus on ease of use and extensibility.

## Features

- Simple and intuitive API
- Modular component architecture
- Easy to extend and customize
- Minimal dependencies
- Component status tracking and validation

## Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from ibim import IBIM

# Create an IBIM instance
ibim = IBIM(name="MyProject")

# Add components
ibim.add_component("component1", {"type": "basic"})

# Process components
ibim.process()

# Check if all components are successfully processed
if ibim.all_good():
    print("All components processed successfully!")

# Get detailed status summary
summary = ibim.get_status_summary()
print(f"Total: {summary['total']}, Status: {summary['status_counts']}")
```

## Project Structure

```
IBIMjr/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── ibim/
│       ├── __init__.py
│       └── core.py
├── examples/
│   ├── basic_usage.py
│   └── status_checking.py
└── tests/
    └── test_ibim.py
```

## Logo and BIMI Compliance

The IBIMjr logo is BIMI (Brand Indicators for Message Identification) compliant and publicly accessible at:
- `https://jelvanricolcol.pro/BIMI.svg`
- `https://vgen-solutions-main.github.io/BIMI.svg`

For detailed information about BIMI compliance, see [BIMI_COMPLIANCE.md](BIMI_COMPLIANCE.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
