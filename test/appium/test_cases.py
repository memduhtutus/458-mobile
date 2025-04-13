import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common.base import AppiumOptions
import random

import time

class FlutterLoginTest(unittest.TestCase):
    def setUp(self):
        # Set desired capabilities for the iOS simulator and your Flutter app
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "iOS",
            "appium:deviceName": "iPhone 16 Pro Max",
            "appium:platformVersion": "18.0",
            "appium:automationName": "XCUITest",
            "appium:includeSafariInWebviews": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True,
            "appium:app": "/Users/atillaemresoylemez/Documents/GitHub/458-mobile/build/ios/iphonesimulator/Runner.app",
        })
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        # Connect to Appium server (ensure Appium is running on the given URL)

        time.sleep(5)  # Wait for the app to launch

    def tearDown(self):
        # Quit the driver and close the session
        self.driver.quit()

    def test_login(self):
        # Find the email field using its name predicate and enter an email
        email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
        email_field.send_keys('test@example.com')

        # Find the password field using its name predicate and enter a password
        password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
        password_field.send_keys('password123')

        # Find and click the login button using its name predicate
        login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
        login_button.click()

    def test_invalid_inputs(self):
        # If still on the login screen, perform login
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('test@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            # Wait for the survey page to load after login
            time.sleep(5)
        except Exception:
            # Assume already logged in and on the survey page
            pass

        # Clear survey input fields if they have any pre-filled text
        name_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Name"')
        name_field.clear()
        surname_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Surname"')
        surname_field.clear()
        benefits_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 
                          'name == "What are the daily life benefits of using AI models?"')
        benefits_field.clear()

        # Select an AI model by clicking on the "Select AI Model" button
        select_ai_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Select AI Model"')
        select_ai_button.click()
        time.sleep(1)  # Wait for the dropdown to appear
        
        # Choose "ChatGPT" from the dropdown items
        chatgpt_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "ChatGPT"')
        chatgpt_option.click()
        time.sleep(1)  # Allow selection to be applied

        # Submit the survey form by clicking the "Submit Survey" button
        submit_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Submit Survey"')
        submit_button.click()

        # Wait for validations to be processed and error messages to appear
        time.sleep(2)

        # Verify that the validation error messages are displayed
        error_name = self.driver.find_element(AppiumBy.IOS_PREDICATE, 
                                             'name == "Please enter your name"')
        error_surname = self.driver.find_element(AppiumBy.IOS_PREDICATE, 
                                                'name == "Please enter your surname"')
        error_benefits = self.driver.find_element(AppiumBy.IOS_PREDICATE, 
                                                 'name == "Please share your thoughts on AI benefits"')

        self.assertTrue(error_name.is_displayed(), "Name error not displayed")
        self.assertTrue(error_surname.is_displayed(), "Surname error not displayed")
        self.assertTrue(error_benefits.is_displayed(), "Benefits error not displayed")

    def test_submit_button_state(self):
        # If on the login screen, perform login first
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('test@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            # Wait for the survey page to load
            time.sleep(5)
        except Exception:
            # Assume already logged in and on the survey page
            pass

        # Check that the "Submit Survey" button is disabled when no AI model is selected
        submit_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Submit Survey"')
        self.assertFalse(submit_button.is_enabled(), "Submit button should be disabled when no AI model is selected")

        # Select an AI model by clicking on the "Select AI Model" button
        select_ai_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Select AI Model"')
        select_ai_button.click()
        time.sleep(1)  # Wait for the dropdown to appear
        
        # Choose "ChatGPT" from the dropdown items
        chatgpt_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "ChatGPT"')
        chatgpt_option.click()
        time.sleep(1)  # Allow selection to be applied

        # Verify that the "Submit Survey" button is now enabled
        submit_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Submit Survey"')
        self.assertTrue(submit_button.is_enabled(), "Submit button should be enabled when an AI model is selected")

    def test_pros_cons_fields_for_selected_models(self):
        # If on the login screen, perform login
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('test@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            time.sleep(5)  # Wait for the survey page to load
        except Exception:
            # Assume already logged in and on the survey page
            pass

        # List of available AI models
        available_models = ["ChatGPT", "Claude", "Gemini", "Copilot", "Other"]
        # Select a random non-empty subset (non-repeating)
        num_to_select = random.randint(1, len(available_models))
        selected_models = random.sample(available_models, num_to_select)

        # For each model in the random subset, select it via the dropdown
        for model in selected_models:
            select_ai_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Select AI Model"')
            select_ai_button.click()
            time.sleep(1)  # Wait for the dropdown to appear

            model_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, f'name == "{model}"')
            model_option.click()
            time.sleep(1)  # Allow selection to be applied

        # For each selected model, verify that its "Defects or Cons" text field appears
        for model in selected_models:
            field_locator = f'name == "{model} Defects or Cons"'
            pros_cons_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, field_locator)
            self.assertTrue(pros_cons_field.is_displayed(), f'"{model} Defects or Cons" field not displayed')

    def test_text_fields_persistence_on_orientation_change(self):
        # Login if not already logged in
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('test@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            time.sleep(5)  # Wait for survey page load
        except Exception:
            # Assume already logged in and on the survey page
            pass

        # Define text inputs for the survey fields
        name_text = "Test Name"
        surname_text = "Test Surname"
        benefits_text = "AI makes daily tasks simpler."
        model_defects_text = "Minor UI inconsistencies."

        # Enter text for "Name", "Surname" and benefits text fields
        name_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Name"')
        name_field.clear()
        name_field.send_keys(name_text)

        surname_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Surname"')
        surname_field.clear()
        surname_field.send_keys(surname_text)

        benefits_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "What are the daily life benefits of using AI models?"')
        benefits_field.clear()
        benefits_field.send_keys(benefits_text)

        # Select an AI model ("ChatGPT") and enter text into its associated defects/cons field
        select_ai_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Select AI Model"')
        select_ai_button.click()
        time.sleep(1)

        chatgpt_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "ChatGPT"')
        chatgpt_option.click()
        time.sleep(1)

        # Locate the defects/cons text field for "ChatGPT" and enter text
        defects_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "ChatGPT Defects or Cons"')
        defects_field.clear()
        defects_field.send_keys(model_defects_text)

        # Store the entered values by reading the 'value' attribute
        name_val = name_field.get_attribute("value")
        surname_val = surname_field.get_attribute("value")
        benefits_val = benefits_field.get_attribute("value")
        defects_val = defects_field.get_attribute("value")

        # Change orientation to LANDSCAPE
        self.driver.orientation = "LANDSCAPE"
        time.sleep(2)  # Allow time for orientation change

        # Verify text fields still contain the same text after orientation change to LANDSCAPE
        self.assertEqual(name_field.get_attribute("value"), name_text, "Name text not persisted in LANDSCAPE")
        self.assertEqual(surname_field.get_attribute("value"), surname_text, "Surname text not persisted in LANDSCAPE")
        self.assertEqual(benefits_field.get_attribute("value"), benefits_text, "Benefits text not persisted in LANDSCAPE")
        self.assertEqual(defects_field.get_attribute("value"), model_defects_text, "Model defects text not persisted in LANDSCAPE")

        # Change orientation back to PORTRAIT
        self.driver.orientation = "PORTRAIT"
        time.sleep(2)  # Allow time for orientation change

        # Verify text fields still contain the same text after orientation change back to PORTRAIT
        self.assertEqual(name_field.get_attribute("value"), name_text, "Name text not persisted in PORTRAIT")
        self.assertEqual(surname_field.get_attribute("value"), surname_text, "Surname text not persisted in PORTRAIT")
        self.assertEqual(benefits_field.get_attribute("value"), benefits_text, "Benefits text not persisted in PORTRAIT")
        self.assertEqual(defects_field.get_attribute("value"), model_defects_text, "Model defects text not persisted in PORTRAIT")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FlutterLoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
