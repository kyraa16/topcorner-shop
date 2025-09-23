from django.test import TestCase, Client
from .models import Product
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

class FootballShopFunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create single browser instance for all tests
        # cls.browser = webdriver.Chrome()

        options = webdriver.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        cls.browser = webdriver.Chrome(options=options)


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Close browser after all tests complete
        cls.browser.quit()

    def setUp(self):
        # Create user for testing
        self.test_user = User.objects.create_user(
            username='testadmin',
            password='testpassword'
        )

    def tearDown(self):
        # Clean up browser state between tests
        self.browser.delete_all_cookies()
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.execute_script("window.sessionStorage.clear();")
        # Navigate to blank page to reset state
        self.browser.get("about:blank")

    def login_user(self):
        """Helper method to login user"""
        self.browser.get(f"{self.live_server_url}/login/")
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("testadmin")
        password_input.send_keys("testpassword")
        password_input.submit()

    def test_login_page(self):
        # Test login functionality
        self.login_user()

        # Check if login is successful
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text.strip(), "Topcorner Shop")

        # logout_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        logout_link = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        self.assertTrue(logout_link.is_displayed())

    def test_register_page(self):
        # Test register functionality
        self.browser.get(f"{self.live_server_url}/register/")

        # Check if register page opens
        h2_element = self.browser.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2_element.text.strip(), "Create your account")

        # Fill register form
        username_input = self.browser.find_element(By.NAME, "username")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")

        username_input.send_keys("newuser")
        password1_input.send_keys("complexpass123")
        password2_input.send_keys("complexpass123")
        password2_input.submit()

        # Check redirect to login page
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
        h2_element = self.browser.find_element(By.TAG_NAME, "h2")
        self.assertIn("Please Login", h2_element.text)

    def test_create_product(self):
        # Test create product functionality (requires login)
        self.login_user()

        # Go to create news page
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        add_button = self.browser.find_element(By.ID, "add-product-link")
        add_button.click()

        # Fill form
        name_input = wait.until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        stock_input = self.browser.find_element(By.NAME, "stock")
        brand_input = self.browser.find_element(By.NAME, "brand")
        price_input = self.browser.find_element(By.NAME, "price")
        rating_input = self.browser.find_element(By.NAME, "rating")
        category_select = self.browser.find_element(By.NAME, "category")
        description_input = self.browser.find_element(By.NAME, "description")
        thumbnail_input = self.browser.find_element(By.NAME, "thumbnail")

        name_input.send_keys("Test Product")
        stock_input.send_keys("5")
        brand_input.send_keys("Test Brand")
        price_input.send_keys("5000")
        rating_input.send_keys("4")
        description_input.send_keys("This is a test product description")
        thumbnail_input.send_keys("https://example.com/test.jpg")

        # Set category (select 'match' from dropdown)

        select = Select(category_select)
        select.select_by_value("jersey")


        # Submit form
        name_input.submit()

        # Check if returned to main page and news appears
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h2"), "Daftar Produk"))
        self.assertIn("Test Product", self.browser.page_source)

    def test_product_detail(self):
        # Test product details page

        # Login first because of @login_required decorator
        self.login_user()

        # Create product for testing
        product = Product.objects.create(
            name="Detail Test Product",
            price=50000,
            stock=10,
            brand="BrandX",
            rating=5,
            category="jersey",   # sesuaikan dengan kategori kamu
            description="Description for testing",
            user=self.test_user
        )

        # Open product detail page
        self.browser.get(f"{self.live_server_url}/product/{product.id}/")

        # Check if detail page opens correctly
        self.assertIn("Detail Test Product", self.browser.page_source)
        self.assertIn("Description for testing", self.browser.page_source)

    def test_logout(self):
        # Test logout functionality
        self.login_user()

        # Click logout button - text is inside button, not link
        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        logout_button.click()

        # Check if redirected to login page
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
        h2_element = self.browser.find_element(By.TAG_NAME, "h2")
        self.assertIn("Please Login", h2_element.text)

    def test_filter_main_page(self):
        # Test filter functionality on main page
        #         
        # Create product for testing
        Product.objects.create(
            name="My Test Product",
            price=50000,
            stock=3,
            brand="Brand A",
            rating=4,
            category="jersey",
            description="desc1",
            user=self.test_user
        )
        Product.objects.create(
            name="Other User Product",
            price=50000,
            stock=8,
            brand="Brand B",
            rating=5,
            category="jersey",
            description="desc2",
            user=self.test_user
        )

        self.login_user()

        # filter "All Products"
        all_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'All Products')]")
        all_button.click()
        self.assertIn("My Test Product", self.browser.page_source)
        self.assertIn("Other User Product", self.browser.page_source)

        # filter "My Products"
        my_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'My Products')]")
        my_button.click()
        self.assertIn("My Test Product", self.browser.page_source)

        
    
   