# jibrish_to_hebrew.py

def fix_jibrish(text, mode='heb'):
    """
    המרת טקסט גס (jibrish) לעברית ולהפך.

    Parameters:
    - text (str): הטקסט הגס או העברי להמרה.
    - mode (str, optional): מצב ההמרה. "heb" להמרה לעברית, "jib" להמרה לג'יבריש. ברירת מחדל היא "heb".

    Returns:
    - str: הטקסט לאחר ההמרה.
    """
    try:
        if mode == 'heb':
            # המרה מטקסט גס (Windows-1252) לעברית (Windows-1255)
            bytes_text = text.encode('windows-1252', errors='replace')
            fixed_text = bytes_text.decode('windows-1255', errors='replace')
            return fixed_text
        elif mode == 'jib':
            # המרה מטקסט עברי (Windows-1255) לג'יבריש (Windows-1252)
            bytes_text = text.encode('windows-1255', errors='replace')
            jib_text = bytes_text.decode('windows-1252', errors='replace')
            return jib_text
        else:
            raise ValueError('Invalid mode. Use "heb" or "jib".')
    except Exception as e:
        print(f"Error in fix_jibrish: {e}")
        return text


def check_jibrish(text):
    """
    בדיקת האם הטקסט מכיל ג'יבריש על ידי זיהוי תווים בטווח Windows-1252.

    Parameters:
    - text (str): הטקסט לבדיקה.

    Returns:
    - bool: True אם הטקסט מכיל ג'יבריש, False אם הטקסט תקין.
    """
    for char in text:
        if 128 <= ord(char) <= 255:
            return True
    return False
