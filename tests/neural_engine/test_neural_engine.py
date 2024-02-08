import unittest
from unittest.mock import patch
from neural_engine.neural_engine import NeuralEngine

class TestNeuralEngine(unittest.TestCase):
    @patch('neural_engine.neural_engine.load_model')
    @patch('neural_engine.neural_engine.generate_text')
    def test_generate(self, mock_generate_text, mock_load_model):
        # Mock the load_model function to return a mock model object
        mock_model = mock_load_model.return_value = 'mock_model'
        
        # Mock the generate_text function to return a specific output
        mock_generate_text.return_value = "Paris"
        
        # Initialize NeuralEngine with a test model
        neural_engine = NeuralEngine("test-model.gguf")
        
        # Test generate function
        prompt = "The capital of France is"
        output = neural_engine.generate_text(prompt, max_tokens=3)
        
        # Assertions
        mock_load_model.assert_called_once_with(neural_engine.model_path)
        mock_generate_text.assert_called_once_with(mock_model, prompt, max_tokens=3)
        self.assertEqual(output, "Paris")

if __name__ == '__main__':
    unittest.main()
