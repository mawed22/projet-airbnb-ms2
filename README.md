### README.md

````markdown
# Prédiction des Prix des Logements Airbnb

Ce projet est une application Streamlit permettant de prédire les prix des logements Airbnb dans différentes villes de France. L'application utilise un modèle de machine learning (Random Forest) entraîné sur des données de locations Airbnb pour effectuer des prédictions en fonction de divers paramètres.

---

## Fonctionnalités

* **Prédiction du prix des logements Airbnb :** Basé sur les paramètres suivants :

  * Ville
  * Type de logement (appartement entier, chambre privée, etc.)
  * Saison (printemps, été, automne, hiver)
  * Nombre de nuits minimum
  * Nombre de personnes
* **Interface utilisateur conviviale :**

  * Interface principale avec affichage des résultats.
  * Barre latérale intuitive pour configurer les paramètres.
* **Visualisation des logements :** Deux images de logements Airbnb affichées sur la page principale.
* **Lien vers un tableau de bord Power BI interactif :** Permet d'explorer les données d'analyse.

---

## Installation et Configuration

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/votre-utilisateur/airbnb-price-prediction.git
   cd airbnb_price_prediction
   ```

2. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application :**

   ```bash
   streamlit run app/main.py
   ```

---

## Utilisation

1. **Configurer les paramètres :**

   * Sélectionnez une ville, un type de logement et une saison dans la barre latérale.
   * Ajustez le nombre de nuits minimum et le nombre de personnes.

2. **Prédire le prix :**

   * Cliquez sur le bouton "Prédire le prix" pour obtenir une estimation.

3. **Consulter le tableau de bord :**

   * Suivez le lien "Consultez le Dashboard" pour explorer les analyses Power BI.

---

## Détails Techniques

* **Modèle utilisé :** Random Forest Regressor
* **Langage :** Python
* **Framework :** Streamlit
* **Données :** Fichier CSV contenant des données de logements Airbnb.

---

## Tableau de Bord Power BI

Consultez le tableau de bord interactif pour plus d'analyses :
[Accéder au Dashboard Power BI](https://app.powerbi.com/groups/me/reports/62cb6eb5-1725-4434-bbc1-cef66de8964a/de2f6777deea833daaa4?redirectedFromSignup=1&experience=power-bi)

---

## Contribution

Les contributions sont les bienvenues ! Suivez ces étapes pour proposer des modifications :

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité ou correction :

   ```bash
   git checkout -b ma-fonctionnalite
   ```
3. Faites vos modifications et soumettez une Pull Request.

---

## Licence

Ce projet est sous licence [MIT](LICENSE).

---

## Auteur

Développé avec par le Groupe C MS2 DATA & IA.

```
```
