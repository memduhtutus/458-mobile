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
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
        # Navigate to the app's URL
        self.driver.get("http://localhost:8080/")
        
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
            #self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='flt-semantic-node-30']"))).click()
            create_button = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Create')]")
            create_button.click()        
            print("Clicked Create Survey")

        except Exception as e:
            print(f"Error during login: {e}")
            self.driver.save_screenshot("login_error.png")
            raise
        except TimeoutException:
            self.fail("Login form did not load or login failed")
    
    # def test_add_checkbox_question_and_preview(self):
    #     time.sleep(2)

    #     # Step 1: Click the 'Text Question' to open the type menu
    #     question_type = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Text Question')]")
    #     question_type.click()
    #     print("Selected 'Text Question' to open type menu")
    #     time.sleep(2)

    #     # Step 2: Select 'Checkbox'
    #     checkbox_option = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Checkbox')]")
    #     checkbox_option.click()
    #     print("Selected 'Checkbox' question type")
    #     time.sleep(2)

    #     # Step 3: Enter the question
    #     question_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Question Text"]')
    #     question_input.send_keys("Which AI models do you use?")
    #     print("Entered question text")
    #     time.sleep(2)

    #     # Step 4: Enter option 1
    #     option_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Option"]')
    #     option_input.send_keys("ChatGPT")
    #     print("Entered option 1: ChatGPT")
    #     time.sleep(2)
        
    #     # Step 5: Click 'Add Option' for ChatGPT
    #     add_option_button = self.driver.find_element(By.XPATH, "//flt-semantics[contains(@aria-label, 'Add Option')]")
    #     add_option_button.click()

    #     # Step 6: Enter option 2
    #     option_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Option"]')
    #     option_input.clear()
    #     option_input.send_keys("Claude")
    #     print("Entered option 2: Claude")
    #     time.sleep(2)

    #     # Step 7: Click 'Add Option' for Claude
    #     add_option_button.click()
    #     print("Clicked add option for Claude")
    #     time.sleep(2)

    #     # Step 8: Add the question
    #     self.driver.find_element(By.XPATH, "//flt-semantics[normalize-space(text())='Add Question']").click()
    #     print("Clicked 'Add Question'")
    #     time.sleep(2)

    #     # Step 9: Verify that ChatGPT and Claude options appear as semantics with matching labels
    #     chatgpt_semantic = self.driver.find_element(By.XPATH, "//flt-semantics[.//span[text()='ChatGPT']]")
    #     claude_semantic = self.driver.find_element(By.XPATH, "//flt-semantics[.//span[text()='Claude']]")

    #     self.assertTrue(chatgpt_semantic.is_displayed(), "ChatGPT option not visible")
    #     self.assertTrue(claude_semantic.is_displayed(), "Claude option not visible")

    #     print("✅ Checkbox options 'ChatGPT' and 'Claude' found and visible.")

    # def test_add_rating_question_and_interact(self):
    #     time.sleep(2)

    #     # Step 1: Click 'Text Question' to open the question type menu
    #     question_type = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Text Question')]")
    #     question_type.click()
    #     print("Opened question type menu")
    #     time.sleep(2)

    #     # Step 2: Select "Rating"
    #     rating_option = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Rating')]")
    #     rating_option.click()
    #     print("Selected 'Rating' question type")
    #     time.sleep(2)

    #     # Step 3: Enter rating question text
    #     question_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Question Text"]')
    #     question_input.send_keys("Rate your satisfaction with AI tools")
    #     print("Entered rating question text")
    #     time.sleep(2)

    #     # Step 4: Add the question
    #     self.driver.find_element(By.XPATH, "//flt-semantics[normalize-space(text())='Add Question']").click()
    #     print("Clicked 'Add Question'")
    #     time.sleep(2)

    #     # Step 5: Click the save icon to go to the survey screen
    #     self.driver.find_element(By.XPATH, "//flt-semantics[contains(@aria-label, 'Save Survey Icon')]").click()
    #     print("Clicked save survey icon to go to survey screen")
    #     time.sleep(2)

    #     # Step 6: Click 5th star using label (after you added Semantics)
    #     fifth_star = self.driver.find_element(By.XPATH, "//flt-semantics[contains(@aria-label, 'Rating Star 5')]")
    #     fifth_star.click()
    #     print("Clicked 5th star")
    #     time.sleep(2)

    #    # Step 7: Optionally verify aria-selected, or assume click was successful
    #     selected = fifth_star.get_attribute("aria-selected")
    #     print(f"aria-selected: {selected}")
    #     self.assertTrue(selected == "true" or selected == "True" or selected is None, "5th star not marked selected")
    #     print("Star selection confirmed")

    #     # Step 8: Confirm survey created by checking for question text on screen
    #     question_label = self.driver.find_element(By.XPATH, "//flt-semantics[contains(@aria-label, 'Rate your satisfaction with AI tools')]")
    #     self.assertTrue(question_label.is_displayed(), "Survey question text not found in final survey view")
    #     print("Survey confirmed as successfully created and displayed.")

    # def test_conditional_question_visibility(self):
    #     time.sleep(2)

    #     # Step 1: Select Radio Question
    #     question_type = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Text Question')]")
    #     question_type.click()
    #     print("Opened question type menu")
    #     time.sleep(2)

    #     radio_option = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Radio')]")
    #     radio_option.click()
    #     print("Selected 'Radio' question type")
    #     time.sleep(2)

    #     # Step 2: Enter question and options
    #     question_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Question Text"]')
    #     question_input.send_keys("Do you use AI?")
    #     print("Entered triggering question")
    #     time.sleep(1)

    #     option_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Option"]')
    #     option_input.send_keys("Yes")
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, "//flt-semantics[@role='button' and @tabindex='0' and @flt-tappable]").click()
    #     print("Added 'Yes' option")
    #     time.sleep(1)

    #     option_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Option"]')
    #     option_input.clear()
    #     option_input.send_keys("No")
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, "//flt-semantics[@role='button' and @tabindex='0' and @flt-tappable]").click()
    #     print("Added 'No' option")
    #     time.sleep(1)

    #     # Step 3: Add the first (trigger) question
    #     self.driver.find_element(By.XPATH, "//flt-semantics[normalize-space(text())='Add Question']").click()
    #     print("Added first question")
    #     time.sleep(2)
    #     # Step 4: Select Text Question (follow-up)
    #     question_type = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Radio Question')]")
    #     question_type.click()
    #     time.sleep(2)
    #     text_option = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Text')]")
    #     text_option.click()
    #     print("Selected 'Text' question type for follow-up")
    #     time.sleep(2)

    #     # Step 5: Enter conditional question
    #     question_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Question Text"]')
    #     question_input.send_keys("Why do you use AI?")
    #     print("Entered conditional question")
    #     time.sleep(2)

    #     # Step 6: Enable 'Make this conditional'
    #     conditional_toggle = self.driver.find_element(By.XPATH, "//flt-semantics[@role='checkbox']")
    #     conditional_toggle.click()
    #     print("Toggled conditional checkbox")
    #     time.sleep(2)

    #     # Step 7: Select condition trigger (first 'Yes' should be default or first visible)
    #     condition_option = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Yes')]")
    #     condition_option.click()
    #     print("Selected condition trigger: Yes")
    #     time.sleep(2)

    #     # Step 8: Add conditional question
    #     self.driver.find_element(By.XPATH, "//flt-semantics[normalize-space(text())='Add Question']").click()
    #     print("Added conditional question")
    #     time.sleep(2)

    #     # Step 9: Save and go to survey screen
    #     self.driver.find_element(By.XPATH, "//flt-semantics[contains(@aria-label, 'Save Survey Icon')]").click()
    #     print("Clicked save survey icon")
    #     time.sleep(2)

    #     # Step 10: Click 'Yes' in the radio question
    #     yes_radio = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Yes')]")
    #     yes_radio.click()
    #     print("Selected 'Yes' answer to trigger conditional question")
    #     time.sleep(2)

    #     # Step 11: Verify conditional question appears
    #     conditional_visible = self.driver.find_element(By.XPATH, "//flt-semantics[contains(@aria-label, 'Why do you use AI?')]")
    #     self.assertTrue(conditional_visible.is_displayed(), "Conditional question did not appear after selecting 'Yes'")
    #     print("✅ Conditional question displayed successfully.")

    # def test_delete_question_removes_it(self):
    #     time.sleep(2)

    #     # Step 1: Add a question
    #     question_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Question Text"]')
    #     question_input.send_keys("What is your favorite AI model?")
    #     print("Entered first question")
    #     time.sleep(2)

    #     self.driver.find_element(By.XPATH, "//flt-semantics[normalize-space(text())='Add Question']").click()
    #     print("Clicked 'Add Question 1'")
    #     time.sleep(2)

    #     # Step 2: Click delete button
    #     delete_button = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Delete 1')]")
    #     delete_button.click()
    #     print("Clicked delete button")
    #     time.sleep(2)

    #     # Step 3: Validate that the question is no longer present using visible text
    #     deleted_question = self.driver.find_elements(By.XPATH,
    #         "//flt-semantics[contains(@aria-label, 'Survey Question: What is your favorite AI model?')]")
    #     self.assertEqual(len(deleted_question), 0, "Deleted question still visible after deletion")

    #     print("✅ Deleted question not found on screen — test passed.")

    def test_save_disabled_without_questions(self):
        time.sleep(2)
        print("Create Survey page loaded with no questions")

        # Step 1: Try to save without any questions
        self.driver.find_element(By.XPATH, "//flt-semantics[contains(@aria-label, 'Save Survey Icon')]").click()
        print("Clicked save icon without any questions")

        dialogs = self.driver.find_elements(By.XPATH, "//flt-semantics[contains(text(), 'Save Survey')]")
        self.assertEqual(len(dialogs), 0, "❌ Survey dialog appeared even though no questions were added")
        print("✅ Save blocked with no questions (no dialog found)")

        # Step 2: Add a question
        question_input = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Question Text"]')
        question_input.send_keys("Temporary question")
        print("Entered temporary question")
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//flt-semantics[normalize-space(text())='Add Question']").click()
        print("Clicked 'Add Question'")
        time.sleep(1)

        # Step 3: Delete the question
        delete_button = self.driver.find_element(By.XPATH, "//flt-semantics[contains(text(), 'Delete 1')]")
        delete_button.click()
        print("Deleted the only question")
        time.sleep(1)

        # Step 4: Try saving again
        self.driver.find_element(By.XPATH, "//flt-semantics[contains(@aria-label, 'Save Survey Icon')]").click()
        print("Clicked save icon after deleting the only question")

        dialogs_after_delete = self.driver.find_elements(By.XPATH, "//flt-semantics[contains(text(), 'Save Survey')]")
        self.assertEqual(len(dialogs_after_delete), 0, "❌ Survey dialog appeared after deleting all questions")
        print("✅ Save blocked after deletion (no dialog found)")

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()