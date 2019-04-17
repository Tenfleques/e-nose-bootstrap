FROM python:3

RUN pip install numpy 
RUN pip install scipy 
RUN pip install pandas 
RUN pip install matplotlib 
RUN pip install flask
ADD ./app /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
