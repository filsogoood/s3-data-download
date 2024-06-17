# S3 data download

## 1. 사전작업
- AWS IAM 사용자 생성(AmazonS3FullAccess 권한 설정 필수)
- Common Crawl 등 데이터 paths 파일 준비
  
## 2. 해당 서버 접속하여 AWS CLI 설치 및 configure
```
$ sudo apt install awscli
$ aws configure 
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]:
Default output format [None]:
```
## 3. 데이터 해당 디렉토리에 다운로드<br />(압축파일이라면 압축해제하고 .paths 파일)
```
#cd /<directory to store data> 
$ cd /mnt/nas/.

$ wget <download url>
```
## 4. paths 파일 split_paths.py 로 3등분으로 나뉘어 파일 저장
ex) warc.paths => warc_part1.paths, warc_part2.paths, warc_part3.paths<br />
split_paths.py에서 input_file, output_file 변경 후 실행
```
python3 split_paths.py
```
## 5. download_s3_part1.py로 저장경로와 지정파일 설정 후 스크립트 실행

- a tmux 로 접속해서 저장경로와 지정파일 설정<br />
ex) download_s3_part1.py 은 warc_part1.paths, download_s3_part2.py 은 warc_part2.paths
- b 스크립트 실행(실행이 되면 해당 디렉토리에 다운로드 시작)

```
python3 download_s3_part1.py
```
- c 위에 a,b 새로운 터미널 열어서 2번 더 반복(part2, part3 까지 해야 함.)
         
