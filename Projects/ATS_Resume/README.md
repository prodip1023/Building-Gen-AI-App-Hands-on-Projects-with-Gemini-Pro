The error `PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?` occurs because the Python library you're using (likely `PyPDF2` or `pdfplumber`) requires `Poppler`, a PDF rendering library, to be installed and accessible in your system's `PATH`.

### Steps to Resolve:

#### 1. **Install Poppler**  
   - **Windows**:
     1. Download the Poppler binaries from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/).
     2. Extract the ZIP file to a folder, e.g., `C:\poppler-xx`.
     3. Add the `bin` directory of Poppler to your system's PATH:
        - Go to **Control Panel > System > Advanced system settings > Environment Variables**.
        - Under "System Variables," find `Path`, click "Edit," and add `C:\poppler-xx\bin`.
     4. Restart your terminal or IDE for the changes to take effect.

   - **Linux**:
     - Install Poppler using your package manager:
       ```bash
       sudo apt-get install poppler-utils   # For Ubuntu/Debian
       sudo yum install poppler-utils      # For CentOS/RHEL
       ```

   - **macOS**:
     - Install Poppler using Homebrew:
       ```bash
       brew install poppler
       ```

#### 2. **Verify Installation**
   - Check if `pdftotext` or other Poppler utilities are accessible:
     ```bash
     pdftotext -v
     ```
   - You should see the version of Poppler installed.

#### 3. **Retry Your Code**
   - After installing Poppler and adding it to your `PATH`, rerun your script. The library should now be able to use `Poppler` for handling PDFs.


# OR 
```
conda install -c conda-forge pdf2image
```
```
conda install -c conda-forge poppler
```
Let me know if you need help with any of these steps!