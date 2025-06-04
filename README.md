# Prosperia Website

## Overview
Prosperia is a web application that manages project visibility and user access through a dynamic CSS generation system.

## Project Structure
```
├── .css                 # CSS files
├── csv/                 # CSV data files
├── fonts/              # Font files
├── .github/            # GitHub configuration
└── various HTML files  # Website pages
```

## Features
- Dynamic project visibility management
- User-specific project access control
- Responsive design
- Modern UI components

## CSV and CSS Generation System

### Overview
The project uses a CSV-based system to manage project visibility for users. The system consists of:

1. **CSV Data Structure** (`csv/clubdeal.csv`):
   - Contains user-project relationships
   - Columns: `userid`, `projectid`
   - Example:
     ```
     userid,projectid
     406953,34771
     405735,34771
     ```

2. **CSS Generation** (`generate_css_rules.py`):
   - Reads the CSV file
   - Generates CSS rules for project visibility
   - Outputs to `generated_rules.css`

### How It Works
- The system generates CSS rules that control project box visibility
- Rules are based on user IDs and project IDs from the CSV
- When a user visits their profile, only their authorized projects are displayed

### Usage
Generate CSS rules using either:
```bash
python3 generate_css_rules.py
```


## Development


## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
[Add your license information here] 
