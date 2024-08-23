import requests
from bs4 import BeautifulSoup

# User-Agent 설정
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/"
}

# 스킬 리스트
keywords = ["python", "typescript", "javascript", "rust"]
all_jobs = []

def wwr_get(url):
    """주어진 URL에서 직무 목록을 추출."""
    try:
        response = requests.get(url, headers=header)
        if response.status_code != 200:
            print(f"페이지오류 {url}, status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("li", class_="feature")  # 직무 목록을 가진 모든 li 요소 찾기

        for job in jobs:
            title = job.find("span", class_="title").text.strip()  # 제목 추출
            company = job.find("span", class_="company").text.strip()  # 회사 이름 추출
            link = job.find("div").find_next_sibling("a")["href"]  # 링크 추출

            job_data = {"title": title, "company": company, "link": link}
            all_jobs.append(job_data)

    except requests.exceptions.RequestException as e:
        print(f"페이지오류 {url}: {e}")

def website_wwr(keyword):
    """주어진 키워드로 직무를 추출"""
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    wwr_get(url)
    jobs = all_jobs.copy()
    return jobs
