FROM docker.arvancloud.ir/pytorch/pytorch:2.3.1-cuda11.8-cudnn8-devel

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple

COPY . .

# CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"] 