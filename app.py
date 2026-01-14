# Nome do arquivo: app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn

# 1. CARREGAR O MODELO TREINADO
# Certifique-se de que o arquivo .pkl esteja na mesma pasta
try:
    model = joblib.load('modelo_churn_xgboost.pkl')
    print("Modelo carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")

app = FastAPI()

# 2. DEFINIR O FORMATO DE ENTRADA (Para validação automática que o projeto pediu la no country)
class ClientData(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Satisfaction_Score: int  # Atenção: O Pydantic não aceita espaço, usei _
    Point_Earned: int        # Atenção: O Pydantic não aceita espaço, usei _
    CardType: str

    class Config:
        # Permite que o JSON venha com nomes reais ("Satisfaction Score")
        # e mapeie para as variáveis com underline
        populate_by_name = True 

# 3. SUA FUNÇÃO DE PREPARAÇÃO (Exatamente a que definimos)
def preparar_dados_para_modelo(data: dict):
    # Converter para DataFrame
    df = pd.DataFrame([data])
    
    # Renomear colunas vindas do Pydantic (com underline) para o original (com espaço)
    df = df.rename(columns={
        'Satisfaction_Score': 'Satisfaction Score',
        'Point_Earned': 'Point Earned'
    })

    # --- INICIO DA SUA LÓGICA ---
    geo_input = str(df['Geography'].iloc[0]).capitalize()
    gender_input = str(df['Gender'].iloc[0]).capitalize()
    
    df['BalanceSalaryRatio'] = df['Balance'] / df['EstimatedSalary']
    df['TenureByAge'] = df['Tenure'] / df['Age']
    df['CreditScoreGivenAge'] = df['CreditScore'] / df['Age']
    df['PointsPerProduct'] = df['Point Earned'] / df['NumOfProducts'] 
    df['HasBalance'] = df['Balance'].apply(lambda x: 1 if x > 0 else 0)
    
    df['Geography_Germany'] = 1 if geo_input == 'Germany' else 0
    df['Geography_Spain'] = 1 if geo_input == 'Spain' else 0
    df['Gender_Male'] = 1 if gender_input == 'Male' else 0
    
    input_card = str(df['CardType'].iloc[0]).upper()
    df['Card Type_GOLD'] = 1 if input_card == 'GOLD' else 0
    df['Card Type_PLATINUM'] = 1 if input_card == 'PLATINUM' else 0
    df['Card Type_SILVER'] = 1 if input_card == 'SILVER' else 0
    
    # --- ORDEM DAS COLUNAS (CRÍTICO: se der problema diga pra que eu veja no feature_names_in_ do jupyter a ordem correta) ---
    cols_modelo = [
        'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 
        'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 
        'Satisfaction Score', 'Point Earned',
        'CreditScoreGivenAge', 'HasBalance', 'PointsPerProduct', 
        'BalanceSalaryRatio', 'TenureByAge', 
        'Geography_Germany', 'Geography_Spain', 
        'Gender_Male', 
        'Card Type_GOLD', 'Card Type_PLATINUM', 'Card Type_SILVER'
    ]
    # --- FIM DA LÓGICA ---

    return df[cols_modelo]

# 4. ENDPOINT
@app.post("/predict")
def predict_churn(client: ClientData):
    try:
        # Converter o objeto validado para dicionário
        input_data = client.dict(by_alias=True)
        
        # 1. Preparar os dados
        df_pronto = preparar_dados_para_modelo(input_data)
        
        # 2. Fazer a predição
        probability = model.predict_proba(df_pronto)[0][1]
        prediction = int(probability > 0.40)  # Limiar de 0.40 conforme definido
        
        # 3. Retornar JSON para o Java
        return {
            "prediction": prediction,               # 0 ou 1
            "churn_probability": float(probability),# ex: 0.85
            "risk_message": "Alto Risco" if prediction == 1 else "Baixo Risco"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Para rodar localmente:
# uvicorn app:app --reload