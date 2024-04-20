# jibrish to hebrew

## Description

`jibrish_to_hebrew` is a Python function that simplifies the conversion between garbled text and Hebrew. It can convert a garbled Hebrew string to plain Hebrew or transform Hebrew text into jibrish and vice versa.

for example: 'ùìåí ìëåìí' --> 'שלום לכולם'
 

## Usage

### convert function - fix_jibrish

The function takes the following parameters:

- **Parameter 1**: *garbled Hebrew string*  
  Provide a garbled Hebrew string as input to be converted.

- **Parameter 2 (optional)**: *Conversion mode*  
  You can specify the conversion mode using this optional parameter. It accepts two values:
  - `"heb"`: To convert the input to Hebrew.
  - `"jib"`: To convert the input to gibrish.
  
  Default is `heb`
  

### test function - check_jibrish

A function to check if a certain string contains correct Hebrew or corrupted Hebrew

Suitable for checking metadata of songs

- **Parameter**:
  A text string

- **return value**:
  `True` If the string is garbled, or `False` if she is ok
  


## Example

```
from jibrish_to_hebrew import fix_jibrish, check_jibrish


jibrish_string = 'ùìåí ìëåìí'
hebrew_string = 'שלום לכולם'

# Convert garbled text to plain Hebrew
heb_result = fix_jibrish(jibrish_string, "heb")

# Convert Hebrew text to gibrish
jib_result = fix_jibrish(hebrew_string, "jib")

# Check if a string contains garbled text
bool_result = check_jibrish(jibrish_string)

```

## Return

```
print(f'{garbled_string}: {result_heb}')
print(bool_result)

ùìåí ìëåìí: שלום לכולם
True

```



## Installation

You can install this package using pip:

```
pip install jibrish-to-hebrew
```

## Acknowledgments

This software is created and maintained by nh.local11@gmail.com.
