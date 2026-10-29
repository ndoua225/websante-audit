---
name: web-audit-agent
description: Construire agent audit passif depuis spec avec code réel et preuves brutes.
trigger: Spec fourni et demande construction directe avec preuves.
always_on:
  - Lire spec avant d'écrire
  - Aucun pass, TODO, fonction vide, commentaire au lieu de code
  - Clés uniquement dans .env.example
  - Ne pas dire terminé sans preuves (fichiers lignes, pip, pytest, audit localhost et domaine, JSON/HTML)
  - Blocage réseau/module manquant déclaré, jamais simulé
  - Audit passif uniquement
---
Procédure : structure agent.yaml + websante/* + tests + reports. Écrire chaque module avec vrai code. audit.py valide domaine (refuser localhost, IP privée, chemin). Corriger requirements (lignes séparées). Exécuter pytest (échecs honnêtes). Exécuter audit.py localhost (REFUS attendu) et domaine réel. Vérifier reports/ ; si absent car aucun audit réussi, le dire.
Pitfalls : import manquant (whois) - try/except + message, pas blocage pipeline. Requirements mal formaté - lignes séparées obligatoires. Domaine non résolu - refus honnête avec raison brute.
