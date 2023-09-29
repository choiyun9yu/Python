# Python

## Pyenv

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
    
## Conda

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

## Jupyter whit vscode

    % conda install ipykernel (해당 가상환경에 커널 설치)

    % python -m ipykernel install --user --name [가상환경이름] --display-name[가상환경이름]

    vscode [cmd + shift + p] - [select interpreter] - 가상 환경 선택

#### vscode 업데이트 후 jupyer 안될 때
    vscode 터미널에서 주피터 노트북 실행 -> 주소복사 -> [cmd + shift + p]
    -> Jupyter : Specify Jupyter Server for Connections 
    -> Exist -> 주소 입력
    

