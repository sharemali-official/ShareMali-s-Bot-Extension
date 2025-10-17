# MyExtension for ShareMali

A **simple ShareMali extension** that sends a message when triggered. This template helps you create your own custom ShareMali extension with ease.

---

## Features
- `sharemali?myextension` → Replies with a simple message.
- Fully customizable trigger name.
- Ready for ShareMali bot upload and approval.

---

## Installation / Uploading to ShareMali

Follow these steps to turn the template into a working ShareMali extension:

1. **Download the template**  
   Get `template.py` from this repository.

2. **Open in a code editor**  
   Use any editor you like (VS Code, PyCharm, etc.) to code your extension logic.

3. **Customize the file**  
   - Change the filename from `template.py` to a unique name for your extension.  
   - Edit the `trigger_sharemali` in the file to set your custom command.
  
   - like this: `trigger_sharemali = "mycustomtrigger"`
   - also edit the `description_sharemali = "Your own description"`
    
4. **Save the file**  
   After coding, save it to your device.

5. **Upload to ShareMali**  
   - Go to Discord.  
   - Choose a server where the ShareMali bot is available and admin 
   - Type:  
     ```
     sharemali?smextension_upload
     ```  
     Attach your `.py` file when prompted.

6. **Wait for approval**  
   ShareMali reviews all extensions before publishing to ensure safety and compatibility.  

7. **Install your extension**  
   Once approved, install it using:  
   ```
   sharemali?smextension_install <your-extension-name>
   ```
   e.g `sharemali?smextension_install template`

8. **Use your custom trigger**  
   After installation, your command works like:  
   ```
   sharemali?<your-trigger>
   ```  
   Example:  
   ```
   sharemali?mycustomtrigger
   ```

---

## Deleting Extensions / Changing the Default Prefix

By default, ShareMali uses:  

```
sharemali?
```

So you can't use another prefix like (!,$ etc)

Now, For Deleting Your Own Extension Just Go to server where sharemali bot available and admin > in that server type `sharemali?smextension_delete <your extension name>` e.g `sharemali?smextension_delete template`

Done — Your Extension will be deleted forever from ShareMali Bot

Note: Only you and sharemali can delete your extensions 

Why sharemali can delete my extension?

If you violate the ShareMali's Rules your extension might be delete or rejected by sharemali


Remember **ShareMali** don't delete any extensions so fast — he reviewed it so deeply (like 1 or 2 weeks)

---

## Must Avoid
avoid these imports to sharemali extension because sharemali don't allow these
dangerous_patterns = [
            'os.', 'subprocess', 'eval', '__import__', 'open(', 
            'import os', 'import sys', 'import subprocess', 'import shutil',
            'import socket', 'import requests', 'import urllib', 'import http',
            'import builtins', 'import globals', 'import locals', 'breakpoint',
            'import threading', 'import multiprocessing', 'import ctypes',
            'import mmap', 'import signal', 'import fcntl', 'import pty',
            'import resource', 'import spwd', 'import crypt', 'import dl',
            'import imp', 'import platform', 'import tempfile', 'import zipfile',
            'import tarfile', 'import pickle', 'import marshal', 'import shelve',
            'import dbm', 'import sqlite3', 'import winreg', 'import _winreg',
        ]

for advance safety — obeying sharemali rules is essential 

## Tips for Creating Extensions
- Keep your extension **safe and secure**: no harmful code or unauthorized actions.  
- Test your code locally before uploading.  
- Use meaningful triggers to avoid conflicts with other extensions.  
- Add comments in your code for easier understanding and future updates.

---

## License
MIT
