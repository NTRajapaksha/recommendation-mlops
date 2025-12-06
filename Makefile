install:
	pip install -r requirements.txt

train:
	python src/train.py

run-full-stack:
	uvicorn src.api.main:app --host 0.0.0.0 --port 8000 & \
	python src/web/app.py

clean:
	rm -rf __pycache__
	rm -rf mlruns
	rm -rf data/ml-latest-small