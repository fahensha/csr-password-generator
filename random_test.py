import unittest
import string
import secure_password_generator

class TestSecurePasswordGenerator(unittest.TestCase):
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    def test_random_lower(self):
        random_char = secure_password_generator.random_lower()
        self.assertIn(random_char, self.lowercase_letters)
    
    def test_random_upper(self):
        random_char = secure_password_generator.random_upper()
        self.assertIn(random_char, self.uppercase_letters)

    def test_random_number(self):
        random_num = secure_password_generator.random_number()
        self.assertIn(random_num, string.digits)
    
    def test_wildcard(self):
        wildcard = secure_password_generator.wildcard()
        self.assertIn(wildcard, string.ascii_letters + string.digits)

    def test_generate_complex_password(self):
        complex_generation_string = "LUNWLNUW"
        password = secure_password_generator.generate_complex_password(complex_generation_string)
        self.assertEqual(len(password), 8)
    
 