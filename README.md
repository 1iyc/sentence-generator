# sentence-generator
sentence-generator

Install Mecab
reference http://incredible.ai/nlp/2016/12/28/NLP/

sudo pip3 install konlpy

#https://bitbucket.org/eunjeon/mecab-ko/downloads/

wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
tar -zxvf mecab-*-ko-*.tar.gz
cd mecab-*-ko-*
./configure
make
make check
sudo make install

mecab --version

#error
mecab-dict 설치

우분투 계열에서 아래와 같은 에러 발생

/usr/local/libexec/mecab/mecab-dict-index -d . -o . -f UTF-8 -t UTF-8
/usr/local/libexec/mecab/mecab-dict-index: error while loading shared libraries: libmecab.so.2: cannot open shared object file: No such file or directory
make: *** [model.bin] Error 127

아래의 방법으로 해결 합니다.

arnold@es-test:~/mecab-ko-dic-1.6.1-20140515$ sudo ldconfig
arnold@es-test:~/mecab-ko-dic-1.6.1-20140515$ ldconfig -p | grep /usr/local/lib
    libmecab.so.2 (libc6,x86-64) => /usr/local/lib/libmecab.so.2
    libmecab.so (libc6,x86-64) => /usr/local/lib/libmecab.so



출처: http://springofmylife.tistory.com/entry/elasticsearch은전한닢-설치 [행복한 개발자]
