# 🔭 Zwiadowca Rozwiązań

Strona: https://damiangrok5-droid.github.io/grok-zwiadowca/

Serwery MCP, skille (SKILL.md), prompty, szablony agentów, automatyzacje, narzędzia CLI i dashboardy HTML, które można wykorzystać z Grok Botem. Przy każdej pozycji: ocena przydatności 1–10, trudność, kroki i gotowy prompt do skopiowania.

- `data.json` – dane zwiadu (gwiazdki, licencje i daty pobrane z GitHub API w dniu zwiadu)
- `index.html` – strona (dane wbudowane + odświeżane z `data.json`), bez zewnętrznych zależności
- `build_data.py` → `data.json`, `embed.py` → `index.html` (z `template.html`)

Ulubione, wypróbowane i archiwum zapisują się w localStorage przeglądarki.
