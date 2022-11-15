FROM amazonlinux:2.0.20220121.0

WORKDIR /apa-gui

COPY *.py .
COPY templates/ ./templates/
COPY requirements.txt .

RUN yum update -y  && \
  yum install -y curl unzip fontconfig python3 && \
  echo 'alias python=python3' >> ~/.bashrc && \
  source ~/.bashrc && \
  pip3 install --upgrade pip && \
  pip3 install -r requirements.txt && \
  curl -OL https://moji.or.jp/wp-content/ipafont/IPAexfont/IPAexfont00401.zip && \
  unzip IPAexfont00401.zip  && \
  mv IPAexfont00401/*.ttf /usr/share/fonts/ && \
  fc-cache -fv && \
  rm -rf ~/.cache

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
