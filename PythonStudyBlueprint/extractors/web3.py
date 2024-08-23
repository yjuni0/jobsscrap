import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

class Wb3Scrapper:
    all_jobs = []
    first_job = None  # 페이지가 몇개인지 몰라서 페이지별 첫번째 직무를 비교하기 위한 변수

    @staticmethod
    def wb3(url):
        """주어진 URL에서 직무 목록을 추출"""
        try:
            response = requests.get(url, headers=header)
            if response.status_code != 200:
                print(f"페이지 오류 {url}, status code: {response.status_code}")
                return False

            soup = BeautifulSoup(response.text, "html.parser")
            jobs = soup.find_all("tr", class_="table_row")
            
            if not jobs: # 더 이상 직무가 없을경우 false를 반환 페이지네이션 종료 
                return False

            first_job_title = jobs[0].find("h2", class_="fs-6 fs-md-5 fw-bold my-primary").text.strip()

            if Wb3Scrapper.first_job == first_job_title:
                print("이미 같은 첫 번째 직무가 존재합니다. 반복을 중단합니다.")
                return False
            else: #새 페이지에 첫번째 직무 업로드
                Wb3Scrapper.first_job = first_job_title

            for job in jobs:
                title = job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary").text.strip() if job.find("h2") else "No title"
                company = job.find("h3").text.strip() if job.find("h3") else "No company"
                link = job.find("a")["href"] if job.find("a") else "No link"
                                                                        #👇🏻 링크가 제대로 로드되지않아서 작성 
                job_data = {"title": title, "company": company, "link": "https://web3.career/" + link} 
                Wb3Scrapper.all_jobs.append(job_data)

            return True

        except requests.exceptions.RequestException as e:
            print(f"페이지 오류 {url}: {e}")
            return False
            
    @staticmethod
    def website_wb3(keyword):
        """페이지를 계속 요청하며 직무를 추출"""
        Wb3Scrapper.all_jobs = []  # 크롤링 시작 전에 리스트 초기화
        Wb3Scrapper.first_job = None  # 첫번째 직무 초기화
        page = 1
        while True:  # 페이지의 개수를 알 수 없어서 1부터 순환
            url = f"https://web3.career/{keyword}-jobs?page={page}"
            if Wb3Scrapper.wb3(url):  # wb3 직무를 추출하면 페이지 수 증가
                page += 1 
            else:  # wb3 메서드가 False를 반환하면 페이지네이션 종료
                break
        return Wb3Scrapper.all_jobs  # 크롤링이 끝난 후 모든 직무 목록 반환