FROM six8/pyinstaller-alpine:latest as pyinstaller
WORKDIR /home/yamler
COPY yamler.py requirements.txt ./

RUN /pyinstaller/pyinstaller.sh --noconfirm --clean yamler.py

FROM alpine:3.6

ENTRYPOINT ["/usr/lib/yamler/yamler"]
COPY --from=pyinstaller /home/yamler/dist/yamler /usr/lib/yamler
