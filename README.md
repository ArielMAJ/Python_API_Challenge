# Python API Challenge

## Table of Contents

- [About](#about)
- [Requirements](#requirements)
- [Running the application](#running-the-application)
  - [Prepare the environment](#prepare-the-environment)
  - [Run the application](#run-the-application)
- [SWAGGER](#swagger)
- [Running the unit tests](#running-the-unit-tests)
- [Compatibility](#compatibility)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)



## About

This is a Python API back-end challenge, built with Python and Flask.

The application is a REST API that can be accessed via HTTP requests. It stores and retrieve data about `partners` and `plants` in a database. The API is documented with [Swagger](#swagger).

## Requirements

- Written and tested with Python 3.11.0 on a Windows 11 machine;
- [pyproject.toml](pyproject.toml) contains the dependencies;
- [requirements.txt](requirements.txt) also contains the dependencies;
- [requirements-dev.txt](requirements-dev.txt) contains the dependencies for development.

## Running the application

To run the application, follow these steps:

### Prepare the environment

#### Clone the repository

- Make sure you have [Git](https://git-scm.com/downloads) installed (you can check your version with `git --version`);
- Open a terminal and navigate to the directory where you want to clone the repository;
- Clone the repository with `git clone https://github.com/ArielMAJ/Python_API_Challenge.git` (or download the zip file);
- Navigate to the project's root directory with `cd Python_API_Challenge`.

#### Python API

- Make sure you have [Python 3.11.0](https://www.python.org/downloads/) or higher installed (you can check your version with `python --version`);
- Create a virtual environment with `python -m venv venv`;
- Activate the virtual environment with `venv\Scripts\activate` (on Windows) or `source venv/bin/activate` (on Linux/Mac);
- Install the dependencies with `pip install -r requirements.txt`.

#### React Front-end

- Make sure you have [Node.js 19.7.0](https://nodejs.org/en/) (and npm 9.6.0) installed (you can check your version with `node --version` and `npm --version`);
- Open a terminal and (assuming you already are in the `Python_API_Challenge` directory) run  `cd ./react-app`;
- Install the dependencies with `npm ci`.

### Run the application

#### Python API
- On the root folder (`Python_API_Challenge`), run the application with `python ./src/server.py`;
- The application will be running on `http://127.0.0.1:3000/` (unless a .env file is defined at the server's root folder specifying another path).

#### React Front-end

- On the `react-app` folder, run the application with `npm start`;
- You will be able to see the app's link on your terminal, Ctrl+Click it to access it;
  - Use the "On Your Network" link. `http://localhost:3000` should be taken by the Python API.
- The back-end server must be running for the front-end to work.

## SWAGGER

- [Start the server](#running-the-application) with `python ./src/server.py`;
- The Swagger documentation will be available at `http://127.0.0.1:3000/apidocs/`.

## Running the unit tests

- Change directory to `./src` with `cd ./src`;
- `python -m unittest` to run all the tests;

## Compatibility

- Windows: works and is the primary development platform;
- Linux & WSL: should work, still needs testers;
- MacOS: should work, still needs testers.

This application was tested on Windows 11 with Python 3.11.0 and on WSL (Ubuntu 22.04 LTS) with Python 3.10.4. It worked as expected on both platforms and all tests passed. It should work on other platforms as well.

## Documentation

You can find the API's documentation [here](#swagger).

## Contributing

Any and everyone is welcome to test this tool locally and leave feedback at #28. If you have some free time and are interested in it, please do. I would love to hear your thoughts and suggestions.

If you want to contribute to the project in any way, feel free to start issues, discussions and open pull requests. Check the [CONTRIBUTING](CONTRIBUTING.md) file for more information.

## Author

- [@ArielMAJ](https://ariel.artadevs.tech/): ariel.maj@hotmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
