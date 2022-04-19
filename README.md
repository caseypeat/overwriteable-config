# Install

`pip install git+https://github.com/caseypeat/overwriteable-config`

# OverwriteableConfig

This is a barebones overwriteable config project. Most notably, it's function is to import and merge an arbitary number of configurations with overwrite priority given to later configurations. The imported configuration can then be used as a dictionary subclass with dot notation access.

To demonstrate this lets take two configuration files "a.yaml" and "b.yaml"

```yaml
# a.yaml
network:
  width: 256
  height: 8
training:
  batch_size: 64
  num_iters: 100

```
```yaml
# b.yaml
network:
  width: 128
  activation: 'ReLU'
optimizer:
  learning_rate: 1e-3
```

And pass them as arguments to a script using this project

`$ python example.py ./a.yaml ./b.yaml`

```python
# example.py
from config import cfg

print('Network width: ', cfg.network.width)
print('Network height: ',cfg.network.height)
print('Learning rate: ', cfg.optimizer.learning_rate)
print()
print(cfg.as_block())
print()
print(cfg)
```

We get the following output

```
Network width:  128
Network height:  8
Learning rate:  0.001

network:
  width: 128
  height: 8
  activation: ReLU
training:
  batch_size: 64
  num_iters: 100
optimizer:
  learning_rate: 1e-3


{'network': {'width': 128, 'height': 8, 'activation': 'ReLU'}, 'training': {'batch_size': 64, 'num_iters': 100}, 'optimizer': {'learning_rate': '1e-3'}}
```

Note that the combined set of atributes from both "a.yaml" and "b.yaml" are present, and the conflicting atribute "network.width" is overwritten by the later "b.yaml" value.

## To Run

This example can be run from the "./example" directory after installation with the command

`$ python example.py ./a.yaml ./b.yaml`

or without installation from the root directory with

`$ python -m example.example ./example/a.yaml ./example/b.yaml`

# Other notable functionality
- This project __does not__ currently have extensive testing of edge cases or protections against overwritting critial atributes. So if one is looking for a way to break this, they need not look very hard...
- Scientific notation will be detected and converted to float when accessed via dot notation, but not when accessed using the standard dictionary square brackets

```python
>>> cfg.optimizer.learning_rate
0.001
>>> cfg['optimizer']['learning_rate']
'1e-3'
```