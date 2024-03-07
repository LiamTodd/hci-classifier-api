# HCI Classifier
This repository implements a REST API exposing the human-centric issue classifier tool implemented by Khalajzadeh et al. (2022), using Flask.

## Development Environment Setup
The local server will run on port 5000 by default, and can be accessed at http://localhost:5000.

To run the server, follow these instructions:
1. Install the dependencies. Recommended to do this in a virtual environment.

    ```pip install -r requirements.txt```
2. Run the server with

    ```python -m src.server```

To stop the server and deactivate the virtual environment:
1. ctrl/command+C in the terminal where the server was started to stop the server.
2. To exit the virtual environment:

    ```deactivate```

## References
Khalajzadeh, H., Shahin, M., Obie, H. O., Agrawal, P., & Grundy, J. (2022). Supporting developers in addressing human-centric issues in mobile apps. IEEE Transactions on Software Engineering, 49(4), 2149-2168.