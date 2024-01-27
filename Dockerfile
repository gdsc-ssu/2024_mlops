# 기본 이미지 설정
FROM python:3.8

# 작업 디렉토리 설정
WORKDIR /HANDS-ON

# Python 라이브러리 설치
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# 현재 디렉토리의 모든 파일을 컨테이너의 작업 디렉토리로 복사
COPY . /HANDS-ON

# FastAPI 애플리케이션 실행
CMD ["uvicorn", "main_3:app", "--host", "0.0.0.0", "--port", "80"]
