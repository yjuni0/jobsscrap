import requests
from bs4 import BeautifulSoup

# User-Agent 설정
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
keywords = ["python", "typescript", "javascript", "rust"]

# 직무를 저장할 클래스
class GetJobs:
    all_jobs = []

    @staticmethod
    def get_jobs(url):
        """주어진 URL에서 직무 목록을 추출."""
        try:
            response = requests.get(url, headers=header)
            if response.status_code != 200:
                print(f"페이지오류 {url}, status code: {response.status_code}")
                return

            soup = BeautifulSoup(response.text, "html.parser")
            jobs = soup.find("ul", class_="jobs-list-items").find_all("li")

            for job in jobs:
                title = job.find("h4", class_="bjs-jlid__h").text.strip()
                company = job.find("a", class_="bjs-jlid__b").text.strip()
                link = job.find("h4").find("a")["href"]
                job_data = {"title": title, "company": company, "link": link}
                GetJobs.all_jobs.append(job_data)

        except requests.exceptions.RequestException as e:
            print(f"페이지오류 {url}: {e}")

    @staticmethod
    def pagination():
        """페이지네이션을 처리하여 모든 페이지에서 직무를 추출"""
        try:
            response = requests.get("https://berlinstartupjobs.com/engineering/", headers=header)
            if response.status_code != 200:
                print(f"페이지 오류, status code: {response.status_code}")
                return

            soup = BeautifulSoup(response.text, "html.parser")
            pages = len(soup.find("ul", class_="bsj-nav").find_all(class_="page-numbers")[1:-1])
            for x in range(pages):
                url = f"https://berlinstartupjobs.com/engineering/page/{x+1}/"
                GetJobs.get_jobs(url)
        except requests.exceptions.RequestException as e:
            print(f"페이지 오류: {e}")

class SkillJobs(GetJobs):
    @staticmethod
    def website_berlinstartup(keyword):
        """주어진 키워드로 직무를 추출"""
        url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
        SkillJobs.get_jobs(url)
        jobs = GetJobs.all_jobs.copy()
        GetJobs.all_jobs.clear() # 직무 초기화 
        return jobs
    
