# clipdrop-api

Basic Python environment and script for using ClipDrop API to generate Depth + Normals from images

## Instructions

Sign up for ClipDrop API (and claim 100 free credits)
https://clipdrop.co/apis/

- From Command Line, clone the repo and setup the virtual environment
```
git clone https://github.com/hack-mans/clipdrop-api.git
cd clipdrop-api
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
- Edit main.py to add ClipDrop api key in **API_KEY = ''**
- Place jpg files in root directory
- Run the python script
```
python main.py
```
- Enter jpg filename without extension
- Depth and Normal maps are saved to root directory
