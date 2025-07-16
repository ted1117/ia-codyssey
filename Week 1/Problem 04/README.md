## Git 설정
### 개행문자 설정
```bash
git config --global core.autocrlf input
```

### 사용자 이름과 이메일 설정
```bash
git config --global user.name "ted111712"
git config --global user.email "ted111712@gmail.com"
```

### 기본 브랜치 이름을 ```main```으로 변경
```bash
git config --global init.defaultBranch main
```

### Git 전역 설정 목록 확인
```bash
git config --global --list
```

### Git 기본 에디터를 VSCode로 변경
```bash
git config --global core.editor "code --wait"
```
#### 만약에 code 명령어가 안 된다면?
- VS Code 열기
- ```Ctrl + Shift + P```
- "Shell Command: Install 'code' command in PATH"

### Git 저장소 초기화
```bash
# app.py이 있는 디렉토리로 이동
cd (경로명)

# Git 저장소 초기화
git init
```