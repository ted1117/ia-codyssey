# 수행 과정
## python 설치
```
sudo apt install python
```

## python 환경 변수 등록
- Windows에서만 필요
- Linux나 macOS는 불필요

## flask 설치
1. 디렉토리 생성
2. cd 명령어로 디렉토리로 이동  
  ```cd ~/Documents/YSJ```
3. 파이썬 가상환경 설정  
  ```python -m venv .venv```
4. 가상환결 활성화
  ```source .venv/bin/activate```
5. pip로 flask 설치
  ```python
  pip install flask
  ```

## Hello 출력 함수 작성
```python
# my_solution.py
def hello() -> None:
    print("Hello")
```

