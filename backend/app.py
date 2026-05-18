from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
from logger import logger

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

from lime.lime_text import LimeTextExplainer

# initialize limiter
limiter = Limiter(
    key_func = get_remote_address
)

#initialization
app = FastAPI(
    title = "Youtube Comment Sentiment API"
)


# limiter to app state
app.state.limiter = limiter

# adding middleware
app.add_middleware(SlowAPIMiddleware)

# exception handler
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request,exc):
    return JSONResponse(
        status_code= 429,
        content={
            "error":"Rate limit exceeded"
        }
    )



#loading pipeline
pipeline = joblib.load("model/sentiment_model.pkl")


# class names
class_names = ['Negative', 'Positive', 'Neutral']
explainer = LimeTextExplainer(
    class_names = class_names
) 

# schema
class CommentInput(BaseModel):
    comment : str

# routes
@app.get("/")
def home():
    logger.info("Home Endpoint accessed")
    return {
        "message" : "Youtube Comment Sentiment API Running"
    }

# prediction route
@app.post("/predict")
@limiter.limit("5/minute")

async def predict_sentiment(
    request : Request,
    data : CommentInput
):
    logger.info(
        f"Prediction request received: {data.comment}"
    )

    prediction = int(pipeline.predict([data.comment])[0])

    label_map = {
        0 : 'Negative', 
        1 : 'Positive', 
        2 : 'Neutral'
    }

    sentiment = label_map[prediction]

    logger.info(
        f"Prediction result: {sentiment}"
    )

    return {
        'Comment': data.comment,
        'Sentiment': sentiment
    }


@app.post("/explain")
@limiter.limit("5/minute")

async def explain_prediction(
    request : Request,
    data : CommentInput
):
    comment = data.comment

    prediction = int(pipeline.predict([comment])[0])

    label_map = {
        0 : 'Negative', 
        1 : 'Positive', 
        2 : 'Neutral'
    }

    sentiment = label_map[prediction]

    # explanation
    explanation = explainer.explain_instance(
        comment,
        pipeline.predict_proba,
        num_features = 6
    )

    # extraction
    explanation_list = explanation.as_list()

    return {
        'comment':comment,
        'prediction':sentiment,
        'explanation': explanation_list
    }