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
        # Wait for app launch
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Find the email field and enter an email
        email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
        email_field.send_keys('user@example.com')
        # Enter the password
        password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
        password_field.send_keys('password123')
        # Click Login button
        login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
        login_button.click()

    def test_invalid_inputs(self):
        # If on login screen, perform login
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('user@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            time.sleep(5)  # Wait for survey page to load
        except Exception:
            pass

        # Clear survey fields
        name_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Name"')
        name_field.clear()
        surname_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Surname"')
        surname_field.clear()
        benefits_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "What are the daily life benefits of using AI models?"')
        benefits_field.clear()

        # Select AI model using the updated accessibility ID
        select_ai_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select AI Model\nSelect AI Model')
        select_ai_button.click()
        time.sleep(1)
        
        # Choose "ChatGPT" from the dropdown items
        chatgpt_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "ChatGPT"')
        chatgpt_option.click()
        time.sleep(1)

        # Click Submit Survey button
        submit_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Submit Survey"')
        submit_button.click()
        time.sleep(2)

        # Verify validation error messages
        error_name = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Please enter your name"')
        error_surname = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Please enter your surname"')
        error_benefits = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Please share your thoughts on AI benefits"')

        self.assertTrue(error_name.is_displayed(), "Name error not displayed")
        self.assertTrue(error_surname.is_displayed(), "Surname error not displayed")
        self.assertTrue(error_benefits.is_displayed(), "Benefits error not displayed")

    def test_submit_button_state(self):
        # Perform login if needed
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('user@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            time.sleep(5)
        except Exception:
            pass

        # Verify Submit Survey button is disabled when no AI model is selected
        submit_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Submit Survey"')
        self.assertFalse(submit_button.is_enabled(), "Submit button should be disabled when no AI model is selected")

        # Select an AI model
        select_ai_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select AI Model\nSelect AI Model')
        select_ai_button.click()
        time.sleep(1)
        chatgpt_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "ChatGPT"')
        chatgpt_option.click()
        time.sleep(1)

        # Verify Submit Survey button is enabled
        submit_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Submit Survey"')
        self.assertTrue(submit_button.is_enabled(), "Submit button should be enabled when an AI model is selected")

    def test_pros_cons_fields_for_selected_models(self):
        # If on the login screen, perform login
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('user@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            time.sleep(5)  # Wait for the survey page to load
        except Exception:
            # Assume already logged in and on the survey page
            pass

        # List of available AI models
        available_models = ["ChatGPT", "Claude", "Gemini", "Copilot"]
        # Use random.sample to select a random non-repeating subset of AI models
        num_to_select = random.randint(1, len(available_models))
        selected_models = random.sample(available_models, num_to_select)

        # For each model in the random subset, select it via the dropdown
        for model in selected_models:
            select_ai_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select AI Model\nSelect AI Model')
            select_ai_button.click()
            time.sleep(1)  # Wait for the dropdown to appear
            model_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, f'name == "{model}"')
            model_option.click()
            time.sleep(1)  # Allow selection to be applied

        # Updated locator: for every selected model use accessibility id formatted as "{model}\nDefects or Cons"
        for model in selected_models:
            accessibility_value = f'{model}\nDefects or Cons'
            try:
                cons_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, accessibility_value)
                self.assertTrue(cons_field.is_displayed(), f'"{model}" field not displayed using locator {accessibility_value}')
            except Exception as e:
                self.fail(f'Field for model "{model}" not found with locator {accessibility_value}: {e}')

    def test_successful_survey_submission_message(self):
        # If on the login screen, perform login
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('user@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            time.sleep(3)  # Wait for the survey page to load
        except Exception:
            pass

        # Fill in valid survey form fields using XPath
        name_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="Name"]'
        )
        surname_field = self.driver.find_element(
            AppiumBy.XPATH, 
            '//XCUIElementTypeTextField[@name="Surname"]'
        )
        
        
        name_field.clear()
        name_field.send_keys("John")
        surname_field.clear() 
        surname_field.send_keys("Doe")

        # Hide the keyboard to ensure elements are re-rendered properly
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

        # Select an AI model (required for a valid submission)
        select_ai_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select AI Model\nSelect AI Model')
        select_ai_button.click()
        time.sleep(1)
        chatgpt_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "ChatGPT"')
        chatgpt_option.click()
        time.sleep(2)
        
        # Enter defects/cons for the selected AI model using XPath
        cons_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="ChatGPT\nDefects or Cons"]'
        )
        
        time.sleep(2)
        cons_field.click()
        time.sleep(2)
        cons_field.send_keys("Some minor issues with ChatGPT")
        time.sleep(4)
        
        # Re-find the element using XPath before further interaction
        cons_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="ChatGPT\nDefects or Cons"]'
        )
        time.sleep(1)

        # Enter benefits
        benefits_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="What are the daily life benefits of using AI models?"]'
        )
        time.sleep(2)

        benefits_field.send_keys("Improved productivity and creativity")
        time.sleep(4)
        benefits_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="What are the daily life benefits of using AI models?"]'
        )

        # Submit the survey
        submit_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Submit Survey"')
        submit_button.click()
        time.sleep(5)  # Increased wait time to let the UI update

        # Re-find and verify that the success validation message is displayed
        success_message = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeOther[@name="Survey submitted successfully!"]'
        )
        self.assertTrue(success_message.is_displayed(), "Success message not displayed after survey submission")

    def test_orientation_change_persistence(self):
        # If on the login screen, perform login
        try:
            email_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Email"')
            email_field.send_keys('user@example.com')
            password_field = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Password"')
            password_field.send_keys('password123')
            login_button = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "Login"')
            login_button.click()
            time.sleep(3)
        except Exception:
            pass
        
        # Fill in name field (find element right before using it)
        name_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="Name"]'
        )
        name_field.clear()
        name_field.send_keys("John")
        
        # Fill in surname field (find element right before using it) 
        surname_field = self.driver.find_element(
            AppiumBy.XPATH, 
            '//XCUIElementTypeTextField[@name="Surname"]'
        )
        surname_field.clear()
        surname_field.send_keys("Doe")
        
        # Select AI model
        select_ai_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select AI Model\nSelect AI Model')
        select_ai_button.click()
        time.sleep(1)
        
        # Find and click ChatGPT option
        chatgpt_option = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "ChatGPT"')
        chatgpt_option.click()
        time.sleep(2)
        
        # Enter text in cons field (find element right before using it)
        cons_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="ChatGPT\nDefects or Cons"]'
        )
        cons_field.click()
        cons_field.send_keys("Some limitations in complex reasoning")
        
        # Enter text in benefits field (find element right before using it)
        benefits_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="What are the daily life benefits of using AI models?"]'
        )
        benefits_field.click()
        benefits_field.send_keys("Helps with creative tasks and information retrieval")
        
        # Change orientation to landscape
        self.driver.orientation = "LANDSCAPE"
        time.sleep(3)  # Wait for orientation change to complete
        
        # Verify name field still contains the entered text
        name_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="Name"]'
        )
        name_value = name_field.get_attribute("value")
        self.assertEqual(name_value, "John", "Name field value changed after orientation change")
        
        # Verify surname field still contains the entered text
        surname_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="Surname"]'
        )
        surname_value = surname_field.get_attribute("value")
        self.assertEqual(surname_value, "Doe", "Surname field value changed after orientation change")
        
        # Verify cons field still contains the entered text
        cons_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="ChatGPT\nDefects or Cons"]'
        )
        cons_value = cons_field.get_attribute("value")
        self.assertEqual(cons_value, "Some limitations in complex reasoning", 
                        "Cons field value changed after orientation change")
        
        # Verify benefits field still contains the entered text
        benefits_field = self.driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeTextField[@name="What are the daily life benefits of using AI models?"]'
        )
        benefits_value = benefits_field.get_attribute("value")
        self.assertEqual(benefits_value, "Helps with creative tasks and information retrieval", 
                        "Benefits field value changed after orientation change")
        
        # Change orientation back to portrait
        self.driver.orientation = "PORTRAIT"
        time.sleep(2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FlutterLoginTest('test_orientation_change_persistence'))
    unittest.TextTestRunner(verbosity=2).run(suite)
