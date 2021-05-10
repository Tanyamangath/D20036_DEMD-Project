FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /app/
COPY shipment_ecom.pkl .
COPY requirements.txt .
RUN pip install -r ./requirements.txt
#EXPOSE 8000
COPY shipment_ecom.pkl .
COPY main.py __init__.py  /app/
CMD ["python", "main.py"]
