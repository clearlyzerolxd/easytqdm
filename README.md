# easytqdm
This is a simple tqdm to avoid some errors😞 that may occur when using tqdm during training.
such as https://github.com/lilv98/PUDA/issues/1
or https://github.com/tqdm/tqdm/issues/487#issuecomment-948860972


## How to use?
```bash
pip install easytqdm==1.5
```
I have completed 
- [x] the display of the progress bar
- [x] real-time updating of text
- [x]  time calculation.
- [ ]  Byte stream calculation
- [ ]  change bar's color
- [ ]  Length, width, and animation of the progress bar




# Like tqdm😋
```
from easytqdm import easytqdm
for epoch in epochs:
  dataloadar = easytqdm(dataloadar)

  for step ,data in dataloadar:
    #you can use
    dataloadar.dec("epoch{}".format(epoch))
    your train code
    '''''''
```
![image](https://github.com/clearlyzerolxd/easytqdm/assets/128237886/7e0ba01d-41c4-4b06-9eec-b268cde3925d)



 If you have any good ideas or suggestions, or encounter any problems, please contact me.
 <a href="mailto:>clearlyzero@stu.cqut.edu.cn" style="color: #ff0000;">clearlyzero@stu.cqut.edu.cn</a>
 Thank you very much for your advice.


