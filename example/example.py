# example.py
from config import cfg

print('Network width: ', cfg.network.width)
print('Network height: ',cfg.network.height)
print('Learning rate: ', cfg.optimizer.learning_rate)
print()
print(cfg.as_block())
print()
print(cfg)