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

#### Install
    % curl -sSL https://install.python-poetry.org | python3 -
    % echo 'export PATH="/home/choiyungyu/.local/bin:$PATH"' >> ~/.zprofile
    % . ~/.zprofile
    % poetry --version

#### Virtual Env Management
    % poerty env use {파이썬경로}       // 환경변수 PATH에 잡혀 있으면 그냥 경로에 python3만 입력
    % poerty env info                // 가상환경 정보 보기
    % poerty env info -path          // 가상환경 경로 보기
    % poetry env list                // 가상환경 목록 보기
    % poerty env remove {파이썬경로}   // 가상환경 삭제

#### Dependency Management
    % poerty --version           // 버전 확인
    % poerty new {프로젝트명}       // 새로운 프로젝트 만들기
    
    % poerty init                // pyproject.toml 파일 생성
    % poerty add {패키지명}        // 의존성 추가 

    % poerty install             // 의존성 설치
    % poerty install --no-deb    // 개발환경 의존성 빼고 설치
    % poerty install -E(or --extra) {패키지명}    // 추가 의존성 설치

    % poetry update {패키지명}    // 패키지 업데이트
    % poerty remove {패키지명}    // 패키지 삭제
    % poerty show               // 의존성 보기
    
    % poerty build              // 소스를 배포가능한 형태로 빌드
    % poetry publish            // PyPI에 배포
    

### 2-2. Pyenv
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

## 3. Jupyter whit vscode

    % conda install ipykernel (해당 가상환경에 커널 설치)

    % python -m ipykernel install --user --name [가상환경이름] --display-name[가상환경이름]

    vscode [cmd + shift + p] - [select interpreter] - 가상 환경 선택

#### vscode 업데이트 후 jupyer 안될 때
    vscode 터미널에서 주피터 노트북 실행 -> 주소복사 -> [cmd + shift + p]
    -> Jupyter : Specify Jupyter Server for Connections 
    -> Exist -> 주소 입력
