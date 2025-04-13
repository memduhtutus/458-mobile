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
