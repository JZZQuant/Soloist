# Setting Up and Running Your Kivy Application

## Step 1: Create and Activate the Conda Environment

1. **Create the environment**:
   ```sh
   conda env create -f environment.yaml
2. **Activate Environment**:
   ```sh
   conda activate audio_tool
3. **Run Applicaiton**:
   ```sh
   python main.py
4. **Freeze requirements for Windows**:
   ```sh
   pip list --format=freeze > requirements.txt
# Running on WIndows
5. **Install Requirements**:
   ```sh
   pip install -r requirements.txt
6. **Compile and run With pyinstaller on windows**:
   ```CMD
   cd C:\Users\JZZQuant\Downloads\Misc
   pyinstaller "\\wsl.localhost\Ubuntu\home\brahmagupta\workspace\Soloist\main.spec"
   C:\Users\JZZQuant\Downloads\Misc\dist\main.exe