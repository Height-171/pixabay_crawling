"""
Last Modification: 2022.10.18
https://github.com/Height-171/pixabay_crawling
"""

import sys
import os
import pixabay_crawler as pc


# 검색 키워드
keyword = sys.argv[1]

# 이미지 장 수
numImages = int(sys.argv[2])

# 결과물을 저장할 폴더 이름
result_dir = sys.argv[3]
os.mkdir(result_dir)

# 크롤링을 수행합니다
pc.crawling(keyword, numImages, result_dir)






