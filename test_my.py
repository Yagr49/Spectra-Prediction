import torch, sys
print(torch.__version__)
print(torch.__file__)
print(torch.version.cuda, torch.backends.cuda.is_built(), torch.cuda.is_available())
