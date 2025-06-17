# Imoge Studio Pro

![Imoge Studio App Screenshot](https://github.com/RandomCatUser/IMOGE/blob/main/image.png)
*Replace this with an actual screenshot of your application.*

`Imoge Studio Pro` is a desktop application built with `Python` and `Tkinter` that allows you to securely convert and store your image and video files into a custom `.imoge` format, and then revert them back to their original form. This tool utilizes a simple `XOR` encryption method to obfuscate your media files.

---

## ✨ Features

* **`Convert to .imoge`**: Transform media files (`.png`, `.jpg`, `.jpeg`, `.mp4`, `.webm`, `.avi`, `.mov`, `.mkv`) into the secure `.imoge` format.
* **`Export from .imoge`**: Decrypt `.imoge` files back into their original image or video format, preserving the detected `media_type` and `mime_type` from the file's internal header.
* **Simple `XOR` Encryption**: Uses a fixed `XOR` `KEY` (`123`) for basic file obfuscation, defined at the top of the `imoge_app.py` script:
    ```python
    KEY = 123  # XOR key for encryption
    VERSION = b"IMOGEv2\n" # File format version
    ```
* **Real-time Progress**: A dynamic `ttk.Progressbar` and informative `status_label` provide updates during `encode_imoge()` and `decode_imoge()` operations.
* **Cancel Operations**: Stop ongoing conversions or exports using the `cancel_btn` which sets a `threading.Event` (`stop_flag`).
* **Intuitive UI**: A clean, modern graphical interface built with `tkinter.ttk` themed widgets and `Pillow`-powered icons for a better user experience.
* **Cross-Platform**: Designed to work on any system where `Python` and `Tkinter` are supported (Windows, macOS, Linux).

---

## 🚀 Getting Started

Follow these steps to get `Imoge Studio Pro` up and running on your machine.

### Prerequisites

* `Python 3.x` installed on your system. You can download it from [python.org](https://www.python.org/).
* The `Pillow` library for image processing (used for handling UI icons).

### Installation

1.  **Clone the repository (or download the code):**
    Open your terminal or command prompt and run:
    ```bash
    git clone [https://github.com/YourUsername/ImogeStudio.git](https://github.com/YourUsername/ImogeStudio.git)
    cd ImogeStudio
    ```
    *(If you downloaded a ZIP file, extract it to your desired location and navigate into the extracted folder.)*

2.  **Install the required Python library:**
    ```bash
    pip install Pillow
    ```

3.  **Prepare Icons (Optional but Recommended):**
    For the best visual experience, the application uses small icons on its buttons.
    * Create a folder named `icons` in the same directory where your `imoge_app.py` file is located.
    * Inside this `icons` folder, place three small (e.g., 28x28 pixel) `PNG` or `ICO` image files with these exact names:
        * `convert_icon.png`
        * `export_icon.png`
        * `cancel_icon.png`
    *(If these icon files are missing, the application will still run, but the buttons will appear without their visual icons, and you'll see a warning message.)*

### Running the Application

Once you've completed the installation and icon preparation steps, you can launch the application:

```bash
python imoge_app.py
