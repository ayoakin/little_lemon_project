# LittleLemon REST API application

This is an API project for Little Lemon Restaurant that allows booking and menu data to be created, updated, deleted and shared.

The entire application is built on the Django REST framework  contained within the `littlelemon` folder.


## Features

## Guide

## Usage

## API Endpoints

* __User Registration and Token Generation Endpoints__

|Endpoint |Link   |Method  |Purpose  |
| :---:   | :---: | :---: | :---: |
| Restaurant API User List | http://127.0.0.1:8000/api/users   | POST  | Creates a new user with name, email and password |
| Restaurant API Valid User | http://127.0.0.1:8000/api/users/me   | GET  | Displays only the current user|
| Restaurant API Token Create | http://127.0.0.1:8000/api/token/login |POST |Generates access tokens that can be used in other API calls in this project|


* __Menu Endpoints__
|Endpoint |Link   |Method  |Purpose  |
| :---:   | :---: | :---: | :---: |
| Restaurant Menu List | http://127.0.0.1:8000/restaurant/menu/   |Purpose  | __   |
| Restaurant Menu Single Item | http://127.0.0.1:8000/restaurant/menu/<int:pk>/|Purpose  |__   |
| Restaurant Table List| http://127.0.0.1:8000/restaurant/table/   | Purpose  |__   |
| Restaurant Table Single Item  | http://127.0.0.1:8000/restaurant/table/<int:pk>/ |Purpose  | __   |
| Restaurant Menu List | (http://127.0.0.1:8000/restaurant/menu/)   | Purpose  |__   |


* __Table Management Endpoints__
* __User Group Management Endpoints__
* __Order Management Endpoint__
* __Cart Management Endpoint__
* __Menu Endpoints__


## Features

## Technologies

## Author

## License



