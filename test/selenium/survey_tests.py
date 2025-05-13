import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


class SurveyAppTests(unittest.TestCase):
    def setUp(self):
        # Setup Chrome options for Flutter web testing
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
        # Navigate to the app's URL
        self.driver.get("http://127.0.0.1:8080/")
        
        # Login to the application
        self._login()
    
    def _login(self):
        """Helper method to log in to the application"""
        try:
            # Wait for login form to load
            print("Waiting for login form to load...")
            print(f"Current URL: {self.driver.current_url}")
            
            # Wait for input fields to appear
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='flt-semantic-node-9']")))
            print("Found input field, continuing...")
        
            
            # Use the specific XPath selector for the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='flt-semantic-node-9']")))
            login_button.click()
            print("Clicked login button using XPath selector")
            
            # Wait for survey page to load
            print("Waiting for survey page...")
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="flt-semantic-node-16"]/input')))
            print("Survey page loaded")
                
        except Exception as e:
            print(f"Error during login: {e}")
            self.driver.save_screenshot("login_error.png")
            raise
        except TimeoutException:
            self.fail("Login form did not load or login failed")

    def _select_question_type(self, question_type):
        """Helper to select a question type from the dropdown
        
        Args:
            question_type: String with options: 'text', 'checkbox', 'radio', 'rating', 'dropdown'
        """
        # Click on question type dropdown
        dropdown = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-109"]')
        dropdown.click()
        
        # Select appropriate question type based on parameter
        if question_type.lower() == 'text':
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flt-semantic-node-46"]')))
            self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-46"]').click()
        elif question_type.lower() == 'checkbox':
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flt-semantic-node-47"]')))
            self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-47"]').click()
        elif question_type.lower() == 'radio':
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flt-semantic-node-48"]')))
            self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-48"]').click()
        elif question_type.lower() == 'rating':
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flt-semantic-node-49"]')))
            self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-49"]').click()
        elif question_type.lower() == 'dropdown':
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flt-semantic-node-50"]')))
            self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-50"]').click()

    def test_successful_survey_submission(self):
        """Test that a user can successfully fill out and submit a survey."""
        # Fill out name field
        name_field = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-16"]/input')
        name_field.clear()
        name_field.send_keys("John")
        
        # Fill out surname field
        surname_field = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-17"]/input')
        surname_field.clear()
        surname_field.send_keys("Doe")
        
        # Select education level
        education_dropdown = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-18"]')
        education_dropdown.click()
        
        # Wait for dropdown options and select Bachelor's Degree
        # Choose from one of the dropdown buttons
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flt-semantic-node-70"]')))
        self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-70"]').click()
        
        # Select AI model
        ai_model_dropdown = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-25"]')
        ai_model_dropdown.click()
        
        # Select ChatGPT from dropdown
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flt-semantic-node-79"]')))
        self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-79"]').click()
        
        # Fill AI model cons
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="flt-semantic-node-93"]/textarea')))
        cons_field = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-93"]/textarea')
        cons_field.send_keys("Sometimes provides incorrect information")
        
        # Fill daily life benefits
        benefits_field = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-26"]/textarea')
        benefits_field.send_keys("Helps me with programming and research tasks")
        
        # Click submit button
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-27"]')
        submit_button.click()
        
        # Verify success message appears (still need to use XPath for the toast message)
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'Survey submitted successfully')]")
        ))
        
        success_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'Survey submitted successfully')]")
        self.assertTrue(success_message.is_displayed())

    def test_form_validation(self):
        """Test that survey form validation works correctly."""
        # Clear any existing values
        name_field = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='name_field']")
        name_field.clear()
        
        surname_field = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='surname_field']")
        surname_field.clear()
        
        # Select AI model (required to enable submit button)
        ai_model_dropdown = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='ai_model_dropdown']")
        ai_model_dropdown.click()
        
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='ChatGPT']")))
        self.driver.find_element(By.XPATH, "//div[text()='ChatGPT']").click()
        
        # Wait for the AI model form to appear and fill it
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="flt-semantic-node-93"]/textarea')))
        cons_field = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-93"]/textarea')
        cons_field.send_keys("Test")

        # Clear benefits field
        benefits_field = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-26"]/textarea')
        benefits_field.clear()

        # Click submit button
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-27"]')
        submit_button.click()
        
        # Check for validation error on name field (using XPath since error message doesn't have a key)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please enter your name')]")))
        name_error = self.driver.find_element(By.XPATH, "//div[contains(text(),'Please enter your name')]")
        self.assertTrue(name_error.is_displayed())
        
        # Check for validation error on surname field
        surname_error = self.driver.find_element(By.XPATH, "//div[contains(text(),'Please enter your surname')]")
        self.assertTrue(surname_error.is_displayed())
        
        # Fill name and surname but leave benefits empty
        name_field = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='name_field']")
        name_field.send_keys("John")
        
        surname_field = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='surname_field']")
        surname_field.send_keys("Doe")
        
        # Click submit again
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='submit_survey_button']")
        submit_button.click()
        
        # Check for validation error on benefits field
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'Please share your thoughts on AI benefits')]")
        ))
        benefits_error = self.driver.find_element(By.XPATH, "//div[contains(text(),'Please share your thoughts on AI benefits')]")
        self.assertTrue(benefits_error.is_displayed())

    def test_create_survey_navigation(self):
        """Test that user can navigate to and use the Create Survey page."""
        # Click the Create button to navigate to Create Survey page
        create_button = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-30"]')
        create_button.click()
        
        # Wait for Create Survey page to load (AppBar title)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Create Survey')]")))
        
        # Verify we're on the Create Survey page
        page_title = self.driver.find_element(By.XPATH, "//div[contains(text(),'Create Survey')]")
        self.assertTrue(page_title.is_displayed())

    def test_create_text_question(self):
        """Test creating a text question in the Create Survey page."""
        # First navigate to Create Survey page
        create_button = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-30"]')
        create_button.click()
        
        # Wait for Create Survey page to load
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="flt-semantic-node-109"]')))
        
        # Select 'text' question type
        self._select_question_type('text')
        
        # Add question text (using XPath selector)
        question_text = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-35"]/input')
        question_text.send_keys("What is your favorite programming language?")

    def test_save_survey(self):
        """Test saving a survey with questions."""
        # First navigate to Create Survey page
        create_button = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-30"]')
        create_button.click()
        
        # Wait for Create Survey page to load
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="flt-semantic-node-109"]')))
        
        # Select 'text' question type
        self._select_question_type('text')  # Or any other type
        
        # Add a text question (using XPath selector)
        question_text = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-35"]/input')
        question_text.send_keys("What is your name?")
        
        # Add question button (using XPath selector)
        add_button = self.driver.find_element(By.XPATH, '//*[@id="flt-semantic-node-36"]')
        add_button.click()
        
        time.sleep(0.5)  # Brief pause to let UI update
        
        # Save the survey using the text content rather than ID
        save_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//flt-semantics[contains(text(),'Save Survey')]")
        ))
        save_button.click()

        # For the dialog buttons as well
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//flt-semantics[contains(text(),'Survey Preview')]")
        ))

        # Click "Save Survey" button in dialog by text
        self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(),'Save Survey') and @role='button']").click()
        
        # Verify success message
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Survey saved successfully!')]")))
        success_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'Survey saved successfully!')]")
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()