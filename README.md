# OnePixel
![logo](https://github.com/KriperPlay/OnePixel/assets/92634754/ea21acc3-841d-42fe-83b0-76855cc7ada7)

# About 
OnePixel - brainfuck interpreter where instead of text, pictures are one pixel high

All functions are the same as in the original brainfuck (only there are no loops)

OnePixel have 1024 memory cells 0 each

'* = 0-255'

# Functions(RGBA)
```
+ = {43,*,*,255}
- = {45,*,*,255}
< = {60,*,*,255}
> = {62,*,*,255}
. = {46,*,*,255}
, = {44,*,*,255}
```

# Example

Hello World! => 
![a](https://github.com/KriperPlay/OnePixel/assets/92634754/62bcd2e0-8ea3-4a8d-bf9e-aa7c655d7040)

# Rules:
* The image file must be .png only
* Input must be number only

# Need to download
* python3 and pip
* PIL/pillow python lib
* termcolor python lib

# How to run
```
python3 onepixel.py [yourfile.png]
```
