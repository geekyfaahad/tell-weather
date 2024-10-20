# Weather App with Image Background

This Flask application provides current weather information for a specified city. It also retrieves a beautiful background image related to the city using the Unsplash API, enhancing the visual appeal of the weather data display.

## Features

- **Weather Information:** Fetches current weather data (temperature and weather icon) based on user-specified city.
- **Dynamic Background Images:** Uses the Unsplash API to fetch a random image based on the city name for a visually appealing background.
- **User-Friendly Interface:** Displays the weather data and background image on a clean, responsive web page.


## Project Structure

├── api_secret.py<br>
├── LICENSE<br>
├── pycache<br>
├── README.md<br>
├── server/<br>
├── templates/<br>
│   ├── index.html<br>
│   └── output.html<br>
├── env/<br>
├── main.py<br>
├── requirements.txt<br>
└── static/<br>

## Prerequisites

- Python 3.x
- Flask (`pip install Flask`)
- Other dependencies listed in `requirements.txt`.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/geekyfaahad/tell-weather.git
    cd tell-weather
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv env
    source env/bin/activate  # For Windows use: env\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your API keys in `api_secret.py`.

5. Run the application:

    ```bash
    python main.py
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

- The application will prompt you to allow location access.
- Upon granting permission, it will retrieve the weather data based on your location.
- The weather information will be displayed in a user-friendly format.

## License

This project is licensed under the MIT License.
