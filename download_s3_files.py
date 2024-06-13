import boto3
import os
import time

# AWS S3 설정
# 변경해야할 부분!!
s3 = boto3.client('s3')
bucket_name = 'commoncrawl'
local_dir = '/mnt/nas2/warc/'  # 로컬 경로로 변경
segment_file = 'warc_part1.paths'  # 경로 목록이 저장된 파일

def download_file(s3_key):
    """단일 파일을 S3에서 로컬 디렉토리로 다운로드"""
    file_name = os.path.basename(s3_key)
    local_path = os.path.join(local_dir, file_name)

    print(f'{s3_key}를 {local_path}로 다운로드 중...')
    start_time = time.time()  # 파일 다운로드 시작 시간 기록

    try:
        s3.download_file(bucket_name, s3_key, local_path)

        end_time = time.time()  # 파일 다운로드 완료 시간 기록
        elapsed_time = end_time - start_time  # 파일 다운로드에 소요된 시간 계산

        file_size = os.path.getsize(local_path)  # 파일 크기 (바이트 단위)
        download_speed = file_size / elapsed_time  # 다운로드 속도 (바이트/초)
        download_speed_mb = download_speed / (1024 * 1024)  # 다운로드 속도 (MB/초)

        print(f'{s3_key} 다운로드 완료. 파일 크기: {file_size} 바이트, 시간: {elapsed_time:.2f} 초, 속도: {download_speed_mb:.2f} MB/초.')

    except Exception as e:
        print(f'{s3_key} 다운로드 중 오류 발생: {e}')
        if os.path.exists(local_path):
            os.remove(local_path)

def download_files(s3_keys):
    """지정된 S3 경로에서 모든 파일을 로컬 디렉토리로 다운로드"""
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    total_start_time = time.time()  # 전체 다운로드 시작 시간 기록

    for s3_key in s3_keys:
        download_file(s3_key)

    total_end_time = time.time()  # 전체 다운로드 완료 시간 기록
    total_elapsed_time = total_end_time - total_start_time  # 전체 다운로드에 소요된 시간 계산

    # 총 시간 계산을 시, 분, 초로 변환
    total_hours = int(total_elapsed_time // 3600)
    total_minutes = int((total_elapsed_time % 3600) // 60)
    total_seconds = total_elapsed_time % 60

    print(f'전체 파일 다운로드 완료. 총 시간: {total_hours} 시간 {total_minutes} 분 {total_seconds:.2f} 초')

def read_paths_from_file(file_path):
    """텍스트 파일에서 경로 목록을 읽음"""
    with open(file_path, 'r') as f:
        paths = f.readlines()
    return [path.strip() for path in paths]

if __name__ == '__main__':
    # 텍스트 파일에서 경로 목록 읽기
    s3_paths = read_paths_from_file(segment_file)

    # 순차적으로 파일 다운로드 수행
    download_files(s3_paths)
