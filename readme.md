
<a name="readme-top"></a>

<h1 align="center">Exhibitor List</h1>
<div align="center">
<img src="Assets/map-to-sheets.png" width="85%">
</div>
    This script takes the Gen Con Exhibitor maps, extracts the vendor/booth number, then adds the data to a google sheet with each map as a new tab.
    <br />
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>

  </ol>
</details>





<!-- ABOUT THE PROJECT -->
## About The Project



This project was designed to take the vendor and their associated booth numbers from the Exhibit Hall map and put them into a Google Sheet. Currently, Gen Con does not have a method to filter/export for specific vendors or booth easily and this script was designed to make it easier. 

At this moment - the script does **not** support the sponsors listed but the feature is coming. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Cloud](https://img.shields.io/badge/Google_Sheets-%2334A853.svg?style=for-the-badge&logo=googlesheets&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mriffey1/vendor-hall-exhibitors.git
   ```
2. Generate a service account key json at <a href="https://console.cloud.google.com/">Google Cloud Console</a>
3. Save the json file as **sheet.json**
4. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
5. Rename the **.env-sample** to **.env**
6. In the .env file, update **MAIN_FOLDER_PATH** with the directory's path
7. Also update the link to **GOOGLE_WORKBOOK** that you wish to put the data in
8. Ensure you have given the service account access to the spreadsheet by sharing and giving the email address associated with the service account, Edit access
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage
1. To run the script, navigate to the directory with vendor_hall.py and use the following terminal command
   ```sh
   python vendor_hall.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Roadmap
- [ ] Adding Sponsor names and booth locations
<p align="right">(<a href="#readme-top">back to top</a>)</p>

