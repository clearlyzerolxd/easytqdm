# easytqdm
This is a simple tqdm to avoid some errors that may occur when using tqdm during training.
such as https://github.com/lilv98/PUDA/issues/1
or https://github.com/tqdm/tqdm/issues/487#issuecomment-948860972


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
    #you can use
    dataloadar.dec("epoch{}".format(epoch)
    your train code
    '''''''
```
![image](https://github.com/clearlyzerolxd/easytqdm/assets/128237886/c68aef96-b3f3-4768-b787-7c6dff231cb5)


 If you have any good ideas or suggestions, or encounter any problems, please contact me.
 <a href="mailto:clearlyzero@stu.cqut.edu.cn">联系我</a>
