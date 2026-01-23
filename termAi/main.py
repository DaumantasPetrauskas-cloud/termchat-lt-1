# main.py
import numpy as np
from termAi import Tensor, Linear

# 1. Create some data using termAi Tensors
x_data = np.array([[1.0, 2.0], [3.0, 4.0]])
input_tensor = Tensor(x_data)

print(f"Input: {input_tensor}")

# 2. Define a model (Neural Network Layer)
layer = Linear(in_features=2, out_features=1)

# 3. Run the data through the model (Forward Pass)
output = layer(input_tensor)

print(f"Output: {output}")