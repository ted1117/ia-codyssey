# 수행 과정
## python 설치
```bash
sudo apt install python
```

## Python 환경 변수 등록
```bash
which python3
nano ~/.profile
```

```
export PATH=/usr/bin/python3:$PATH
```

```bash
source ~/.profile
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

## VSCode 설치
1. 터미널에서 ```sudo apt update'''` 입력
2. 필요한 의존성 패키지 설치
  ```bash
  sudo apt install software-properties-conmmon apt-transport-https curl
  ```
  - ```software-properties-conmmon```: 추가 저장소를 관리하는 데 필요한 패키지
  - ```apt-transport-https```: HTTPS로 패키지를 다운로드할 수 있게 하는 패키지
  - ```curl```: 외부 URL에서 데이터를 다운로드 할 때 사용하는 도구
3. MS GPG키 가져오기
  ```bash
  curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
 ```
  - MS의 패키지를 신뢰할 수 있는지 확인하기 위해 GPG 키를 다운로드하여 시스템에 추가
  - 해당 저장소에서 제공하는 패키지가 공식적인 것을 검증
4. MS 저장소 추가
  ```bash
  sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
  ```
5. 패키지 목록 업데이트
 ```bash
 sudo apt update
 ```

6. VSCode 설치
 ```bash
 sudo apt install code
 ```

