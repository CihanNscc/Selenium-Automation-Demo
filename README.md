
![portfolio-selenium-video](https://github.com/user-attachments/assets/a3a29730-966a-4245-8d53-0430757cf265)

# Selenium Automation Demo

This project demonstrates the use of Selenium for automating the navigation through app slides on a portfolio website. It includes performing a Google search, navigating to a portfolio, and interacting with buttons to view sample app slides.

## Features

- Automates a Google search for "Cihan Alcin" and navigates to the portfolio website.
- Simulates user interaction by clicking the "Apps" button to view the list of apps.
- Loops through app slides, automatically clicking the "Next" button and closing each slide.

## Requirements

- Python 3.x
- [Selenium](https://www.selenium.dev/) Python package
- Chrome WebDriver

## Installation

1. Clone the repository or download the source code.
2. Install the required Python packages by running:

```bash
pip install selenium
```

3. Download and place the [ChromeDriver](https://sites.google.com/chromium.org/driver/) in the project directory.

## Usage

1. Ensure the ChromeDriver is executable.

2. Run the script:

```bash
python main.py
```

The script will open a Chrome browser, perform the search, and automate interaction with the app slides on the portfolio.

## License

This project is licensed under the MIT License. Feel free to modify and use it for your own projects.
