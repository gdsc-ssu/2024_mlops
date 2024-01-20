from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import joblib
import pandas as pd

    
# 모델 로드
model1 = joblib.load('loanlimit_model.pkl')


app = FastAPI()

class LoanApplication(BaseModel):
    birth_year : float
    gender : float
    credit_score : float
    yearly_income : float
    company_enter_month : float
    existing_loan_cnt : float
    existing_loan_amt : float
    personal_rehabilitation_ing : int
    personal_rehabliltation_done : int
    한국은행_기준금리 : float
    pc1 : float
    income_type_EARNEDINCOME2 : bool
    income_type_FREELANCER : bool
    income_type_OTHERINCOME : bool
    income_type_PRACTITIONER : bool
    income_type_PRIVATEBUSINESS : bool
    employment_type_기타 : bool
    employment_type_일용직 : bool
    employment_type_정규직 : bool
    houseown_type_배우자 : bool
    houseown_type_자가 : bool
    houseown_type_전월세 : bool
    purpose_BUYCAR : bool
    purpose_HOUSEDEPOSIT : bool
    purpose_기타 : bool
    purpose_대환대출 : bool
    purpose_사업자금 : bool
    purpose_생활비 : bool
    purpose_자동차구입 : bool
    purpose_전월세보증금 : bool
    purpose_주택구입 : bool
    purpose_투자 : bool

class predict_output(BaseModel):
    predicted_loan_limit : float


@app.post("/predict_loan_limit", response_model=predict_output)
def predict_loan_limit(application: LoanApplication):
    # 입력 데이터를 DataFrame으로 변환
    input_df = pd.DataFrame([dict(application)])

    # "한국은행_기준금리"를 "한국은행 기준금리"로 변경
    input_df.rename(columns={"한국은행_기준금리": "한국은행 기준금리"}, inplace=True)

    # 예측 수행
    prediction = model1.predict(input_df)

    # 예측 결과 반환
    return {"predicted_loan_limit": prediction[0]}

