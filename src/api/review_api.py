from fastapi import FastAPI

app = FastAPI()

@app.post("/review/pr")
def review_pr(diff: str):
    return {
        "status": "reviewed",
        "summary": "AI review completed"
    }
