# 🏢 Meilleurtaux - Proposition de solution au test de recrutement Data Engineer 


# Partie 1 : Analyse

### Question 1 :
**Question ouverte :** 

En vous concentrant sur les personnes ayant soumis des opportunités (c’est-à-dire les demandeurs de prêt immobilier), déterminez le profil type de ces personnes.

Vous pouvez vous intéresser aux champs suivants : 
- `Age_emprunteur__c`
- `BanquePrincipaleEmp__c`
- `Deja_souscrit_credit_immo__c`
- `TechMail_CategorieProfessionnelleEmpru__c`
- `TechMail_ContratDeTravailEmprunteur__c`

### Question 2 : 
Pour la partie 2, je devais utiliser SQL. Donc j'ai installer duckDB afin de pouvoir faire la requets SQL directement sur les fichiers CSV. La réponse se trouve dans le fichier analysis.ipynb

# Partie 2 : Récupération des informations d’une opportunité


1. **Option  : API REST with FastAPI** 
Le script qui répond á cette question est dans le fichier myapi.py. 
Il y'a un fichier requirements.txt qui est associé et qui contient les dépendances
`pip install -r requirements.txt`


> **Note** : `response_id` doit être un UUID généré aléatoirement.

```json
{
  "response_id": "0cc12fda-deca-4f24-918b-f0884d2bb910",
  "id": "0065q00000AlAK0AAN",
  "age_emprunteur": 33,
  "banque_principale": "CIC",
  "deja_souscrit_credit_immo": true,
  "categorie_professionnelle": "Salarié du privé",
  "contrat_travail": "CDI période d'essai terminée",
  "revenu_total": 7731.67,
  "montant_pret_principal": 235055,
  "stage_name": "6-Perdue"
}
```

# 🚀 Partie 3 : Réflexion

Imaginons que Julie, une data analyst de l’équipe marketing, souhaite accéder aux informations des utilisateurs et aux actions qu’ils effectuent sur le site (consultations de pages, clics, etc.) afin d’améliorer les analyses marketing. Ces données sont disponibles via une API, mais elles doivent être mises à disposition de manière structurée et accessible pour Julie.

🎯 **Votre mission**  
En tant que data engineer Meilleurtaux, votre rôle est de répondre à cette demande en mettant en place un processus pour récupérer et stocker les données de l’API, afin que Julie puisse les utiliser facilement dans ses analyses.

### Question:  **Comment vous y prendriez-vous ? Quels outils et technologies choisiriez-vous ?**  

> **Tips**  
> Pensez aux aspects suivants pour guider votre réflexion :
> 1. 🔗 **Accès aux données** : Comment allez-vous récupérer les données de l’API ?  
> 2. 💾 **Stockage** : Où allez-vous stocker les données pour qu’elles soient facilement accessibles pour Julie et l’équipe marketing ?  
> 3. 🔄 **Automatisation** : Comment mettre en place un processus automatisé (par exemple, toutes les heures ou chaque jour) pour garantir que les données sont toujours à jour ?  
> 4. 🛠️ **Déploiement et Outils** : Comment allez-vous déployer votre solution, et quels outils ou technologies utiliseriez-vous ?




