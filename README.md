# 🏢 Meilleurtaux - Processus de Recrutement Data Engineer

Bienvenue dans le repository du test technique pour le poste de **Data Engineer** chez [Meilleurtaux](https://www.meilleurtaux.com/) ! Ce test a été conçu pour évaluer vos compétences en :

- 💻 **Codage**
- 📊 **Analyse**
- 📝 **Présentation**

---

## 📂 Structure des données 

Dans le dossier [data_sources](data_sources/) , vous trouverez un fichier zip contenant trois fichiers CSV :

- **banques_test.csv** : contient la liste des banques qui peuvent proposer des offres de prêt immobilier aux clients.
- **opportunity_test.csv** : contient les opportunités, c’est-à-dire les demandes de prêt immobilier faites par des personnes. Il contient des informations sur le profil des demandeurs de prêt immobilier, les caractéristiques du projet immobilier...
- **propositions_test.csv** : contient les propositions de prêt faites pour chaque opportunité. Une opportunité peut avoir plusieurs propositions de prêt de la part de différentes banques, avec des conditions telles que le taux d’intérêt, la durée et le taux d’assurance.

> **Remarque :** Les noms des champs sont généralement explicites. Certains champs spécifiques sont expliqués ci-dessous :

### Champs dans `opportunity_test.csv`
- **MontPretPricip__c** : Montant du prêt principal.
- **SituActu__c** : Situation actuelle de l’emprunteur.
- **TotRev__c** : Revenus total de l’emprunteur.
- **BanquePrincipaleEmp__c** : La banque actuelle de l'emprunteur

### Champs dans `propositions_test.csv`
- **Id** : Identifiant unique de la proposition.
- **CreatedDate** : Date de création de la proposition.
- **Opportunity__c** : Identifiant de l’opportunité associée.
- **Partenaire__c** : Identifiant de la banque ayant fait la proposition.
- **TXHA__c** : Taux d'intérêt hors assurance.
- **DureePret_Mois__c** : Durée du prêt en mois.
- **TauxAss__c** : Taux de l’assurance emprunteur.
- **Etape_Source__c** : Étape de traitement de la proposition.

---

## 📝 Instructions pour répondre au test

Pour commencer l’exercice, suivez ces étapes :

1. **Clonez** ce repo sur votre machine locale.
2. **Une fois dans le bon dossier, créez un environnement Python virtuel** avec Python 3.8 ou supérieur.

   ```bash
   python -m venv venv

3. **Activer ensuite l'env virtuel :**

	```bash 
    source venv/bin/activate  #pour macOS
    venv\Scripts\activate     #pour Windows

N'hésitez pas à utiliser l’IDE de votre choix pour interagir avec Jupyter Notebook.


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
En utilisant SQL:
Pour chaque opportunité, sélectionnez la proposition de prêt la plus avantageuse parmi toutes les propositions disponibles.

Dans votre requête SQL, ne sélectionnez que les colonnes suivantes dans votre résultat final :  
- **ID de l’opportunité** 
- **ID de la proposition**  
- **Taux d’intérêt**  
- **Durée du prêt** 
- **Nom de la banque**  

# Partie 2 : Récupération des informations d’une opportunité

> **Choisissez l'option 1 ou 2 qui correspond le mieux à vos compétences (API REST ou script simple).** 

1. **Option 1 : API REST**  
   Créez une API REST en Python avec le framework de votre choix. Cette API doit recevoir un paramètre `id` correspondant à l’identifiant unique de l’opportunité et renvoyer les informations principales de l’opportunité au format JSON (voir exemple de réponse attendue ci-dessous).

2. **Option 2 : Script Python**  
   Créez un script Python simple qui, en fonction de l'ID fourni, récupère les informations de l’opportunité et les retourne au format JSON (voir exemple de réponse attendue ci-dessous).

### Exemple de réponse attendue (valide pour les deux options) :

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

> 💡💡 Pensez aux solutions de stockage et d’orchestration etc.. qui s’intègreraient facilement à notre Data Platform Meilleurtaux existante.

⚠️ **Note** : Il n'y a pas de bonne ou de mauvaise réponse ! 😊 Partagez simplement votre approche et les raisons pour lesquelles vous choisiriez certaines solutions.



# Instructions pour soumettre votre test
Si votre code nécessite des packages supplémentaires, listez les dans le fichier `requirements.txt`

❗ : ❗ La réponse attendue pour ce test doit être partagée sous forme de **repo GitHub privé** avec les membres de l’équipe data engineering de Meilleurtaux (voir adresses emails ci-dessous).
⚠️ Pour la Partie 4, vous pouvez également inclure votre réflexion dans une documentation directement dans le repo. ❗ : ❗


🔹 **Tips** : [Comment partager un repo privé ?](https://docs.github.com/fr/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)

Une fois terminé, nous examinerons rapidement votre test et organiserons une réunion pour vous permettre de présenter votre solution, d’expliquer votre approche, votre méthodologie et les défis rencontrés au cours de cet exercice.

📧 **N'hésitez pas à nous contactez si vous avez des questions ou besoin de précisions sur les instructions de l’exercice** :
- zkhalmadani@meilleurtaux.com
- glouasse@meilleurtaux.com

