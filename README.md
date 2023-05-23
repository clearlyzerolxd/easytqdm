# easytqdm
This is a simple tqdm to avoid some errors that may occur when using tqdm during training.
such as https://github.com/lilv98/PUDA/issues/1


## How to use?
```bash
pip install easytqdm
```

like tqdm,
```
from easytqdm import easytqdm
for epoch in epochs:
  dataloadar = easytqdm(dataloadar)

  for step ,data in dataloadar:
    your train code
    '''''''
```
![image](https://github.com/clearlyzerolxd/easytqdm/assets/128237886/c68aef96-b3f3-4768-b787-7c6dff231cb5)
