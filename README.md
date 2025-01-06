## VIEWZEN CLASSIFIER

viewzen_classifier/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── iris.py
│   ├── processors/
│   │   └── model_processor.py
│   ├── main.py  # FastAPI app
├── streamlit_app/
│   └── iris_predictor.py  # Streamlit app
├── requirements.txt


### Docker run :
docker-compose build
docker-compose up

### Local - Run :
uvicorn app.main:app 
streamlit run app/app.py
