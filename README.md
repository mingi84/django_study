# django_study
장고 학습 프로젝트 입니다.
-------------------------
*개발환경 설정*
>**-  python 3.11.1 (pip 23.0)**
>python -m pip install --upgrade pip
>**- django 4.1.6**
>pip install django==4.1.6 (설치는 가상환경 설정 이후 가상환경 위에 설치)
>개발툴 Visual Studio Code 최신버전

*1. 가상환경 설정*
- ProjectRootFolder에서 실행>python -m venv mingstagram

이후 작업은 가상환경 위에서 작업

*2. django설치*
- 가상환경 접속 (./Scripts/activate.bat)
- pip install django==4.1.6

*3. 프로젝트 생성*
- 가상환경 접속 (./Scripts/activate.bat)
- django-admin startproject *ProjectName*

*4. 서버 실행*
- 가상환경 접속 (./Scripts/activate.bat)
- python manage.py runserver

*5. 추가 라이브러리설치*
- 가상환경 접속 (./Scripts/activate.bat)
- pip install djangorestframework
- pip install markdown
- pip install django-filter

*template Path를 찾지 못하는 문제. 환경설정*
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')], # <- 내용 수정
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

*setting.py에서 SECRET_KEY 노출로 인한 보안문제 해결
#환경변수 추가
export INSTA_SECRET_KEY='본인의 고유 비밀 키 추가'
# 환경변수 확인 명령
$ echo $INSTA_SECRET_KEY
