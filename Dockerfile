FROM six8/pyinstaller-alpine:latest as pyinstaller
WORKDIR /home/yamler
COPY yamler.py requirements.txt ./

RUN /pyinstaller/pyinstaller.sh --noconfirm --clean --onefile yamler.py

FROM alpine:3.6

ENTRYPOINT ["/usr/local/bin/yamler"]
COPY --from=pyinstaller /home/yamler/dist/yamler /usr/local/bin/yamler
