import os
from llama_cpp import Llama

class NeuralEngine:
    def __init__(self, model_path='./models/mistral-7b-v0.1.Q4_0.gguf', n_gpu_layers=None, seed=None, n_ctx=None):
        self.llm = Llama(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            seed=seed,
            n_ctx=n_ctx
        )

    def generate_text(self, prompt, max_tokens=None, stop=None, echo=False):
        res = self.llm(
            prompt,
            max_tokens=max_tokens,
            stop=stop,
            echo=echo
        )
        return res[0]['text']
    
# # Resolve the project directory at runtime
# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# # Example usage
# if __name__ == '__main__':
#     model_path = os.path.join(PROJECT_DIR, 'models/7B/llama-model.gguf')
#     neural_engine = NeuralEngine(model_path)

#     prompt = "Q: Name the planets in the solar system? A: "
#     max_tokens = 32
#     stop = ["Q:", "\n"]
#     echo = True

#     output = neural_engine.generate_text(prompt, max_tokens, stop, echo)
#     print(output)
