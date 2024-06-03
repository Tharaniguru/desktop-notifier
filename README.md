# desktop-notifier

A Python script that fetches the latest tech news headlines from TechNewsWorld and displays desktop notifications using Win10Toast.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

The Tech News Notifier is a simple script that periodically fetches the latest headlines from the TechNewsWorld tech blog and displays them as desktop notifications on Windows. This is useful for staying up-to-date with the latest tech news without having to manually check the website.

## Features

- Fetches the latest tech news headlines from TechNewsWorld.
- Displays desktop notifications with the headline and a link to the full article.
- Configurable notification interval.


## Requirements

- Python 3.x
- An internet connection to fetch the latest headlines.
- Required Python Libraries:
  - `requests`
  - `beautifulsoup4`
  - `win10toast`

## Installation

1. **Clone the repository**:
   ```bash
   https://github.com/Tharaniguru/desktop-notifier.git
   run the main.py file
2.**Install the required Python packages**:
```bash
pip install -r requirements.txt
```
## Usage
**Script Functionality**:

The script will fetch the latest headlines from TechNewsWorld and display a desktop notification every 30 minutes by default.
Clicking the notification will open the full article in your default web browser.


