from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import uvicorn
import uuid , json

app = FastAPI(title="Opportunités API")

# Modèle pour correspondre à l'output attendu
class OpportunityResponse(BaseModel):
    response_id: str
    id: str
    age_emprunteur: str
    banque_principale: str
    deja_souscrit_credit_immo: bool
    categorie_professionnelle: str
    contrat_travail: str
    montant_pret_principal: str
    stage_name: str

# Charger les données depuis un fichier CSV
CSV_FILE = "data_sources/data_samples/opportunity_test.csv"

opportunities_df = pd.read_csv(CSV_FILE)

# Renommer les colonnes pour correspondre au modèle 
opportunities_df.rename(columns={
    'Id': 'id',
    'Age_emprunteur__c': 'age_emprunteur',
    'BanquePrincipaleEmp__c': 'banque_principale',
    'Deja_souscrit_credit_immo__c': 'deja_souscrit_credit_immo',
    'TechMail_CategorieProfessionnelleCoEmpru__c': 'categorie_professionnelle',
    'TechMail_ContratDeTravailEmprunteur__c': 'contrat_travail',
    'TotRev__c': 'revenu_total',
    'MontPretPricip__c': 'montant_pret_principal',
    'StageName': 'stage_name'
}, inplace=True)

@app.get("/api/v1/opportunities/{opportunity_id}")
async def get_opportunity(opportunity_id: str):

    # Selectionner les colonnes du fichier CSV
    selected_columns = [
        'id',
        'age_emprunteur',
        'banque_principale',
        'deja_souscrit_credit_immo',
        'categorie_professionnelle',
        'contrat_travail',
        'revenu_total',
        'montant_pret_principal',
        'stage_name'
    ]
    opportunity = opportunities_df.loc[opportunities_df['id'] == opportunity_id, selected_columns]
    
    if opportunity.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Opportunité {opportunity_id} non trouvée"
        )
    
    # Generer un UUID
    response_uuid = str(uuid.uuid4())
    
    opportunity_dict = opportunity.to_dict(orient='records')[0]
    opportunity_dict['response_id'] = response_uuid


    return OpportunityResponse(**opportunity_dict).json(indent=4)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)