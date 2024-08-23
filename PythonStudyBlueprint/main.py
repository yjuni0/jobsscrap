from flask import Flask, render_template,request, redirect, send_file
from extractors.assignment_8 import SkillJobs
from extractors.web3 import Wb3Scrapper
from file import save_to_file
import math
app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
  return render_template("home.html", name="yejun")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    page = int(request.args.get("page", 1))
    max_list = 50
    if keyword == None:
        return redirect("/")
    if keyword in db:
      jobs = db[keyword]
    else:
      berlinjobs = SkillJobs.website_berlinstartup(keyword)
      web3jobs = Wb3Scrapper.website_wb3(keyword)
      jobs = berlinjobs + web3jobs
      db[keyword] = jobs
      
    # 뷰 함수에서 url_for을 사용하여 페이지네이션 링크 생성 url_for('search', keyword='python', page=2)이 /search?keyword=python&page=2 링크반환 
    jobs = db[keyword]
    total_jobs = len(jobs)
    start = (page - 1) * max_list
    end = start + max_list
    paginated_jobs = jobs[start:end]
    total_pages = math.ceil(total_jobs/max_list)
    return render_template("search.html", keyword=keyword, jobs=paginated_jobs, page=page, total_pages=total_pages)


@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)


app.run("0.0.0.0")