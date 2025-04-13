# Mobile AI Survey App with Appium Test Automation

## Overview

This repository contains the source code and test automation scripts for the Mobile AI Survey App developed as part of CS458 Project Part 2. The app is built using Flutter and implements a mobile-native survey system that incorporates a login mechanism (manual credentials and Google OAuth) and a comprehensive survey form. The survey collects details such as name, surname, birth date, education level, city, gender, AI models used (with defects), and AI benefits in daily life. When all required fields are completed, the survey data is submitted (currently printed and/or sent via email).

Additionally, this project includes an Appium-based test automation suite that validates 5 test cases designed for the survey page.

## Project Structure

```plaintext
458-mobile/
├── lib/
│   ├── main.dart                         # Entry point of the app; sets up the MaterialApp.
│   ├── screens/
│   │   ├── LoginPage.dart                # Handles user login (manual & Google OAuth).
│   │   └── SurveyPage.dart               # Survey form for user input.
│   ├── components/
│   │   └── AiModelForm.dart              # Dynamic form component for AI model details.
│   ├── models/
│   │   └── survey_form_data.dart         # Data structures for survey responses.
│   │   └── login_request.dart
│   └── constants.dart                    # Contains mock credentials for login.
├── test/
│   └── appium/
│       └── test_cases.py                 # Appium test cases
└── README.md                             # This file.

```

## How to Run the Mobile Application

### Prerequisites

- **Flutter SDK**  
  Install [Flutter](https://flutter.dev/docs/get-started/install) and ensure it is properly configured on your system.

- **Device/Emulator**  
  Ensure you have an iOS simulator configured. You can also use a physical device connected via USB.

---

### Steps to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/memduhtutus/458-mobile.git
   cd 458-mobile
   ```

2. **Get Flutter packages**
   ```bash
    flutter pub get
   ```
3. **Launch the Emulator**
4. **Run the application**

   ```bash
    flutter run
   ```

5. **Testing with Appium**
   
   a. **Prerequisites:**
   ```bash
   # Install Appium and required dependencies
   npm install -g appium
   pip install Appium-Python-Client
   ```
   
   b. **Configure Device Settings:**
   
   The test suite is configured for iOS simulators. You may need to adjust device settings in `test/appium/test_cases.py` to match your environment:
   
   ```python
   options.load_capabilities({
       "platformName": "iOS",
       "appium:deviceName": "iPhone 16 Pro Max",  # Adjust to match your simulator
       "appium:platformVersion": "18.0",          # Update to your iOS version
       "appium:automationName": "XCUITest",
       "appium:app": "/path/to/your/app/build/ios/iphonesimulator/Runner.app"
   })
   ```
   
   c. **Build the App for Testing:**
   ```bash
   flutter build ios --simulator
   ```
   
   d. **Start Appium Server:**
   ```bash
   appium
   ```
   
   e. **Run Tests:**
   ```bash
   cd test/appium
   python test_cases.py
   ```
   
   f. **Run Specific Tests:**
   
   To run individual tests, update the main block in `test_cases.py`:
   ```python
   if __name__ == '__main__':
       suite = unittest.TestSuite()
       suite.addTest(FlutterLoginTest('test_login'))  # Replace with desired test name
       unittest.TextTestRunner(verbosity=2).run(suite)
   ```
