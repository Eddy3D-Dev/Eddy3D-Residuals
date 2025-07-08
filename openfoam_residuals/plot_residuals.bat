cd /D "%~dp0"
call C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3
pip install -r requirements.txt
python batch_plot.py
