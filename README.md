# jibrish_to_hebrew

## Description

`jibrish_to_hebrew` is a Python function that simplifies the conversion between garbled text and Hebrew. It can convert a garbled Hebrew string to plain Hebrew or transform Hebrew text into gibberish and vice versa. 

## Usage

The function takes the following parameters:

- **Parameter 1**: *garbled Hebrew string*  
  Provide a garbled Hebrew string as input to be converted.

- **Parameter 2 (optional)**: *Conversion mode*  
  You can specify the conversion mode using this optional parameter. It accepts two values:
  - `"heb"`: To convert the input to Hebrew.
  - `"jib"`: To convert the input to gibrish.

## Example

```
from jibrish_to_hebrew import fix_jibrish

# Convert garbled text to plain Hebrew
result = fix_jibrish("your_garbled_string", conversion_mode="heb")

# Convert Hebrew text to gibberish
result = fix_jibrish("your_hebrew_string", conversion_mode="jib")
```

## Installation

You can install this package using pip:

```
pip install jibrish_to_hebrew
```

## Acknowledgments

This software is created and maintained by nh.local11@gmail.com.