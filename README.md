# Python

## 1. pip(Package Installer for Python), 파이썬 패키지 매니저
pip는 파이썬에 기본적으로 내장되어 있는 패키지 매니저이다. pip를 사용하면 Python Package Index에 다른 개발자들이 올려놓은 패키지를 쉽게 다운로드하고 설칠할 수 있다.

    % pip install {패키지명}    // 패키지 설치
    % pip show {패키지명}       // 패키지 확인
    % pip install -U {패키지명} // 패키지 업데이트
    % pip uninstall {패키지명}  // 패키지 삭제

    % pip freeze > requirements.txt    // 현재 설치되어 있는 전체 패키지 목록을 저장
    % pip install -r requirements.txt  // 텍스트 파일에 있는 전체 패키지 목록을 설치

<br>

## 2. Virtual Environment, 가상 환경
### 2-1. Poetry

#### PyCharm 이 자동으로 가상환경을 찾지 못한 경우 
> [File] -> [Settings]
> 검색: "Interpreter"
> [Project Interpreter] -> [Add New Interpreter] -> [Poetry Environment]
> [Install packages from pyproejct.toml] -> [OK]

#### Install
    % curl -sSL https://install.python-poetry.org | python3 -
    % echo 'export PATH="/home/{사용자이름}/.local/bin:$PATH"' >> ~/.zprofile
    % . ~/.zprofile
    % poetry --version

    % poetry self update 

#### Virtual Env Management 
    % poetry new {프로젝트명}         // 프로젝트 생성 
>  poetry-demo  
            ├── pyproject.toml  
            ├── README.rst  
            ├── poetry_demo  
            │   └── __init__.py  
            └── tests  
            ├── __init__.py  
            └── test_poetry_demo.py  
    
    % poetry shell                    // Poetry 쉘 활성화
    % exit                            // Poetry 쉘 비활성화

    % poerty env info                 // 가상환경 정보 보기
    % poetry env list                 // 가상환경 목록 보기
    % poerty env remove {파이썬경로}    // 가상환경 삭제

#### Dependency Management 

    % poerty show                     // 의존성 보기
    % poetry install                  // 의존성 설치
    % poerty install --no-deb                   // 개발환경 의존성 빼고 설치
    % poerty install -E(or --extra) {패키지명}    // 추가 의존성 설치

    % poetry add {패키지명}             // 패키지 추가 설치
    % poetry add {패키지명}@{버전}

    % poetry update {패키지명}          // 패키지 업데이트
    % poerty remove {패키지명}          // 패키지 삭제

    % poetry export -f requirements.txt > requirements.txt    // requirements.txt 추출 

    % poerty build              // 소스를 배포가능한 형태로 빌드
    % poetry publish            // PyPI에 배포

#### PyCharm에서 Poetry 사용하기
    % poetry install
        PyCharm 열기- 메뉴에서 "File" > "Settings" 선택
        왼쪽 탐색 창에서 "Project: [프로젝트 이름]" 선택 - "Python Interpreter" 선택 - "Add Interpreter" 선택
        "Poetry Environment"를 선택하고, 프로젝트 디렉토리에 있는 Poetry 가상환경을 선택
        (보통은 ~/.cache/pypoetry/virtualenvs/프로젝트이름-랜덤문자열/bin/python3.10)

#### 기존 프로젝트 안에 가상환경 추가하기
    % poetry init                   // pyproject.toml 파일 생성
        Package name: {패키지명}
        Version: {이 프로젝트의 버전}
        Description: {설명}
        Author: {작성자}
        License: {라이센스}
        Compatible Python versions: >=3.9
        Package to add or search for: {추가할 패키지}

#### 가상환경 
    % pip install ipykernel
    % python -m ipykernel install --user --name 가상환경이름 --display-name 가상환경이름

### 2-2. Pyenv
#### freeze

    % pip install pipreqs
    % pipreqs /절대경로                 // 필요한 것 만 딱 설치

    %pip freeze > requirements.txt    // 너무 많은 것을 설치

#### for Ubuntu
    % sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev

    % git clone https://github.com/pyenv/pyenv.git ~/.pyenv

    % echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    % echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    % echo 'eval "$(pyenv init --path)"' >> ~/.profile
    % echo 'if [ -n "$PS1" -a -n "$BASH_VERSION" ]; then source ~/.bashrc; fi' >> ~/.profile

    % echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
    % echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    % echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

    % source ~/.zshrc

    % git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

    % eval "$(pyenv virtualenv-init -)"
    % source ~/.zshrc

    % pyenv install --list    # 설치가능한 리스트    
    % pyenv install 3.7.13    # 파이썬 3.7.13 설치
    % pyenv install 3.8.13    # 파이썬 3.8.13 설치
    % pyenv versions          # 설치된 버전 리스트

    % pyenv virtualenv 3.7.13 [envName]   // 가상환경 생성
    % pyenv uninstall [envName]           // 가상환경 제거
    % pyenv global 3.8.13                 // global 설정
    % pyenv local [envName]               // loval 설정 (해당 경로에서)

#### for MacOs
    % brew install pyenv
    % brew install pyenv-virtualenv

    % echo $SHELL   // zsh shell

    % echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    % echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    % echo 'eval "$(pyenv init --path)"' >> ~/.profile
    % echo 'if [ -n "$PS1" -a -n "$BASH_VERSION" ]; then source ~/.bashrc; fi' >> ~/.profile
    
    % echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    % echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

    % echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
    % echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    % echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
    
    % source ~/.zshrc

    % pyenv --version

######
    % pyenv install --list
    % pyenv install 3.
    % pyenv uninstall 3.
######
    % pyenv virtualenv 3.10 [가상환경명]    // 가상환경 생성
    % pyenv virtualenv-delete [가상환경명]  // 가상환경 삭제
    % pyenv global 3.                    // Global 설정
    % pyenv local [가상환경명]              // Local 설정
    
### 2-3. Conda
    % winget install miniconda3            // win
    % brew install miniconda?              // mac

    % conda init zsh                       // 콘다시작
    % conda create -n[가상환경명] python=3.   // 가상환경 생성
    % conda activate [가상환경 이름]          // 가상환경 활성화
    % conda deactivate [가상환경명]           // 가상환경 비활성화 
    % conda remove -n[가상환경이름] --all     // 가상환경 삭제
    % conda create -clone [가상환경명] -n[복제할 가상환경명]  // 가상환경 복제

    % conda install [패키지명]              // 패키지 설치
    % conda list                          // 패키지 조회

    % conda env list                       // 가상환경 목록 조회
    % conda config --set auto_auctivate_base false    // 가상환경 자동활성화 해제

### 2-4. Pipenv
    % pip install pipenv    // pipenv 설치

    % cd /프로젝트 루트 경로
    % pipenv --python 3.X   // 가상환경에서 사용할 python 설정
    % pipenv shell          // 가상환경 실행 
    % exit                  // 가상환경 종료

    % pipenv install 패키지명 // 가상환경에 패키지 설치
    
    % pipenv --rm           // 가상환경 제거

    % pipenv lock
    % pipenv install
 
<br>

## 3. Jupyter 

### 3-1. JupyterLab Select Kernel
- JupyterLab 의 "Select Kernel" 인터페이스는 노트북이나 코드 셀에서 실행할 때 사용할 커널을 선택하는 기능을 제공한다.
- 커널은 jupyter 노트북의 백엔드에서 코드를 실행하는 프로세스를 말하며, 주로 특정 프로그래밍 언어 또는 가상환경을 기반으로 실행된다.
- **커널 등록**
    - poetry 같은 툴로 가상환경 생성
      
          % poetry shell // 가상환경 활성화
          % poetry add ipykernel  // ipykernel 설치
          % python -m ipykernel install --user --name jupyter-lab-9MopgKzY-py3.10 --display-name "JupyterLab (Poetry)"  // 커널 등록
          % jupyter kernelspec uninstall jupyter-lab-9MopgKzY-py3.10 // 커널 제거
    - 이후 JupyterLab 에서 "MyEnv" 라는 이림의 커널을 선택할 수 있다.  
- **커널 변경**
    - 이미 열려 있는 노트북에서 다른 커널로 전활할 수 있다.
    - 이를 통해 다른 Python 버전 또는 다른 언어로 전환하면서 작업할 수 있다.
- **커널 관리**    
    - 커널을 추가하거나 제거할 수 있다.
    - 각 가상환경은 JupyterLab 에서 커널로 등록될 수 있으며,
      이를 통해 다양한 개발 환경을 쉽게 전환하며 사용할 수 있다.

### 3-5. error with vs code

    % conda install ipykernel (해당 가상환경에 커널 설치)
    % python -m ipykernel install --user --name [가상환경이름] --display-name[가상환경이름]

    vscode [cmd + shift + p] - [select interpreter] - 가상 환경 선택

#### vscode 업데이트 후 jupyer 안될 때
    vscode 터미널에서 주피터 노트북 실행 -> 주소복사 -> [cmd + shift + p]
    -> Jupyter : Specify Jupyter Server for Connections 
    -> Exist -> 주소 입력
