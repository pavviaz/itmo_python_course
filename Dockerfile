FROM python:3.11

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y -q apt-utils python3-pip

RUN apt-get install -y --no-install-recommends texlive-latex-recommended texlive-fonts-recommended && \
    apt-get install -y --no-install-recommends texlive-latex-extra texlive-fonts-extra texlive-lang-all && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -i https://test.pypi.org/simple/ latex-renderer==0.0.2

COPY app3.py .
CMD ["python3", "app3.py"]