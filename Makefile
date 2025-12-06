install:
	pip install -r requirements.txt

train:
	python src/train.py

run-api:
	python src/api/main.py

clean:
	rm -rf __pycache__
	rm -rf mlruns
	rm -rf data/ml-latest-small