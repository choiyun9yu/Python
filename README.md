# Python

## Conda
- 콘다시작 : conda init zsh
- 가상환경 생성 : conda create -n[가상환경이름] python=3.
- 가상환경 목록 조회 : conda env list
- 가상환경 활성화 : conda activate [가상환경 이름]
- 가상환경 비활성화 : conda deactivate [가상환경 이름]
- 가상환경 삭제 : conda remove -n[가상환경이름] --all
- 가상환경 복제 : conda create -clone [가상환경 이름] -n[복제할 가상환경 이름]
- 가상환경 자동활성화 해제 : conda config --set auto_auctivate_base false
- 패키지 설치 : conda install [패키지이름]
- 패키지 조회 : conda list

## Jupyter whit vscode
- conda install ipykernel (해당 가상환경에 커널 설치)
- 가상환경 생성
  python -m ipykernel install --user --name [가상환경이름] --display-name[가상환경이름]
  vscode [cmd + shift + p] - [select interpreter] - 가상 환경 선택
- vscode 업데이트 후 jupyer 안될 때
  vscode 터미널에서 주피터 노트북 실행 -> 주소복사 -> [cmd + shift + p]
  -> Jupyter : Specify Jupyter Server for Connections 
  -> Exist -> 주소 입력
  
## Pycharm
