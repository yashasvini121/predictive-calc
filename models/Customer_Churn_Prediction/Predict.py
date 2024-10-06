from Model import customer_churn_prediction
def get_prediction(cs,geo,gen,age,tenure,bal,nop,hcc,iam,es):
    prediction,probability=customer_churn_prediction(cs,geo,gen,age,tenure,bal,nop,hcc,iam,es)
    output=""
    if prediction == 1:
        output=f"The customer is likely to churn with a probability of {probability:.2f}"
    else:
        output=f"The customer is likely to stay with a probability of {1-probability:.2f}"
    return output




