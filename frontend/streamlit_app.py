import streamlit as st
import requests

st.set_page_config(
    page_title = "Youtube Comment Sentiment Analysis",
    layout = 'centered'
)

st.title("Youtube Comment Sentiment Analysis")
comment = st.text_area(
    "Enter youtube comment"
)

if st.button("Analyze Sentiment"):
    if comment.strip() == '':
        st.warning("please enter a comment")
    else:
        payload = {
            'comment': comment
        }

        response = requests.post(
        "http://127.0.0.1:8000/predict",
        json = payload
        )

        if response.status_code == 200:
            result = response.json()
            sentiment = result['Sentiment']
            if sentiment == 'Positive':
                st.success(
                    f"Sentiment:{sentiment}"
                )
            elif sentiment == 'Negative':
                st.error(
                    f"Sentiment:{sentiment}"
                )
            else:
                st.info(
                    f"Sentiment:{sentiment}"
                )
        else :
            st.error("API Error")


if st.button("Explain Prediction"):

    payload = {
        "comment": comment
    }
    response = requests.post(
        "http://127.0.0.1:8000/explain",
        json=payload
    )

    result = response.json()
    prediction = result["prediction"]
    
    st.subheader("Prediction")
    if prediction == "Positive":
        st.success(prediction)

    elif prediction == "Negative":
        st.error(prediction)

    else:
        st.info(prediction)

    st.subheader("Word Importance")
    for word, score in result["explanation"]:
        st.write(
            f"{word} : {round(score, 3)}"
        )