from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
import joblib
from .logger import logger
import redis
import json
import os

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

from lime.lime_text import LimeTextExplainer

# redis client creation
redis_client = redis.Redis(
    host = 'localhost',
    port = 6379,
    decode_responses = True
)


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
BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "sentiment_model.pkl"
)
pipeline = joblib.load(MODEL_PATH)


# class names
class_names = ['Negative', 'Positive', 'Neutral']
explainer = LimeTextExplainer(
    class_names = class_names
) 

# schema
class CommentInput(BaseModel):
    comment : str = Field(..., min_length=1)

# routes
@app.get("/")
async def home():
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
    comment = data.comment

    # checking redis
    cached_result = redis_client.get(comment)
    if cached_result:
        logger.info("Cache Hit")
        return json.loads(cached_result)
    logger.info("Cache Miss")

    # prediction
    prediction = int(pipeline.predict([comment])[0])

    label_map = {
        0 : 'Negative', 
        1 : 'Positive', 
        2 : 'Neutral'
    }

    sentiment = label_map[prediction]

    # result format
    result =  {
        'Comment': data.comment,
        'Sentiment': sentiment
    }
    
    # stores in redis
    redis_client.setex(
        comment,
        3600,
        json.dumps(result)
    )
    return result


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