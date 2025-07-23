# Subdomain Enumeration and Testing Script

## This script automates the process of subdomain enumeration, IP resolution, port validation, and HTTP status code 200 checks for a target domain. It leverages several popular security tools like subfinder, dnsx, naabu, and httpx to gather and analyze information.
Tools Used

    Subfinder: A tool for discovering subdomains of a target domain.

    DNSX: A tool for resolving DNS and obtaining IPs of discovered subdomains.

    Naabu: A tool for performing port validation on subdomains.

    HTTPX: A tool for performing HTTP tests, checking for 200 status codes and taking screenshots of subdomains.

# Requirements

## Before running the script, you need to make sure the following tools are installed on your system:

    subfinder:

        Installation instructions can be found in the Subfinder repository.

    dnsx:

        Installation instructions can be found in the DNSX repository.

    naabu:

        Installation instructions can be found in the Naabu repository.

    httpx:

        Installation instructions can be found in the HTTPX repository.

    Python 3.x:

        Make sure Python is installed on your system.

# Installation

    Clone the repository to your local directory:

git clone https://github.com/secrets4152/BotRecon.git
cd subdomain-enumeration-script

    Ensure that you have the necessary dependencies to run the script. If you have pip installed, you can verify everything is ready by running:

pip install -r requirements.txt

    Note: The requirements.txt file can be created based on the Python libraries you use in the script, like subprocess, os, and re (which are already part of Python's standard library).

# How to Use
## 1. Running the Script

To run the script, simply execute the Python file in your terminal. The script will prompt you to input the target domain and will automatically carry out the following steps:

python3 BotRecon.py

## 2. What Does the Script Do?

    Step 1: Discover subdomains of the target domain using subfinder.

    Step 2: Resolve the subdomains to IPs using dnsx.

    Step 3: Filter and extract subdomains enclosed in square brackets [] using a regular expression.

    Step 4: Perform port validation on subdomains using naabu.

    Step 5: Check HTTP status codes (200 OK) and take screenshots of subdomains using httpx.

## 3. Output Files:

The script will generate the following output files:

    subdomains.txt: List of discovered subdomains.

    subdomains2.txt: List of subdomains with their corresponding IP addresses.

    resultados_regex.txt: Subdomains filtered using the regular expression.

    subdomains3.txt: List of subdomains with open ports.

    results.txt: Final results with HTTP status code 200 and screenshots.

## 4. Terminal Output

The script will print the contents of the results.txt file, which contains the final HTTP status test results, to the terminal.
Example Execution

Enter the target name: example.com

After entering the domain, the script will automatically perform all steps and display the results in the terminal.
Contributing

If you encounter any issues or wish to improve the script, feel free to open an issue or submit a pull request. Contributions are welcome!

    Fork this repository.

    Create a branch for your modification (git checkout -b new-feature).

    Commit your changes (git commit -am 'Add new feature').

    Push to the branch (git push origin new-feature).

    Open a pull request.

## License

This project is licensed under the WTFPL License:

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2004 Sam Hocevar

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long as
the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION, AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
