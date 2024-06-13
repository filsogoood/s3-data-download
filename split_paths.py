def read_paths_from_file(file_path):
    """텍스트 파일에서 경로 목록을 읽음"""
    with open(file_path, 'r') as f:
        paths = f.readlines()
    return [path.strip() for path in paths]

def write_paths_to_file(paths, file_path):
    """경로 목록을 텍스트 파일에 저장"""
    with open(file_path, 'w') as f:
        for path in paths:
            f.write(f"{path}\n")

def split_paths(input_file, output_files):
    """입력 파일의 경로 목록을 3등분하여 출력 파일에 저장"""
    paths = read_paths_from_file(input_file)
    
    # 경로 목록을 3등분
    chunk_size = len(paths) // 3
    chunks = [paths[i:i + chunk_size] for i in range(0, len(paths), chunk_size)]
    
    # 각 부분을 출력 파일에 저장
    for i, chunk in enumerate(chunks):
        write_paths_to_file(chunk, output_files[i])

if __name__ == '__main__':
    input_file = 'warc.paths'
    output_files = ['warc_part1.paths', 'warc_part2.paths', 'warc_part3.paths']
    
    split_paths(input_file, output_files)
