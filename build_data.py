import json, datetime
raw = {v['full_name']:v for v in json.load(open('raw_github.json')).values()}
# (repo_or_key, kategoria, nazwa, opis, ocena, dlaczego, trudnosc, kroki, prompt)
E = []
def add(*a): E.append(a)

add("anthropics/skills","Skille","Anthropic Agent Skills",
 "Oficjalne repozytorium skilli w formacie SKILL.md od twórców standardu: m.in. skill-creator (tworzenie i testowanie własnych skilli), mcp-builder i frontend-design na licencji Apache-2.0. Skille docx/xlsx/pptx/pdf mają licencję zastrzeżoną (All rights reserved): tylko jako wzór, nie kopiować.",
 10,"To wzorzec dokładnie tego formatu, którego używa Grok Bot – skille na Apache-2.0 (skill-creator, frontend-design, mcp-builder) możesz adaptować, a docx/xlsx/pptx/pdf tylko czytać jako wzór.","łatwa",
 ["Poproś bota o sklonowanie repo na komputer (/workspace).","Wybierz skill (np. skill-creator lub frontend-design).","Każ botowi zaadaptować go jako własny skill i zapisać."],
 "Sklonuj na swoim komputerze repo https://github.com/anthropics/skills do /workspace/skills-anthropic. Przeczytaj skille skill-creator i frontend-design. Na ich wzór zapisz mi jako Twoje własne skille: (1) 'tworzenie-skilli' – jak budujesz i testujesz nowy skill, (2) 'projektowanie-stron' – zasady ładnych stron HTML w stylu iOS. Pisz po polsku i pokaż mi listę zapisanych skilli.")
add("mvanhorn/last30days-skill","Skille","last30days – research z ostatnich 30 dni",
 "Skill, który bada dowolny temat na Reddicie, X, YouTube, Hacker News, Polymarket i w sieci z ostatnich 30 dni i składa z tego raport.",
 10,"Idealny silnik dla cyklicznego zwiadu – dokładnie to, co robi ta strona, tylko na dowolny temat.","średnia",
 ["Bot czyta SKILL.md i skrypty z repo.","Adaptuje go do narzędzi Grok Bota (WebSearch, X, HN API).","Ustawiasz routine, np. co poniedziałek."],
 "Przeczytaj repo https://github.com/mvanhorn/last30days-skill (SKILL.md i skrypty). Zaadaptuj tę metodę jako Twój skill 'research-30-dni' z użyciem Twoich narzędzi (wyszukiwarka, X, Hacker News API). Potem przetestuj go na temacie 'nowe skille dla asystentów AI' i daj mi raport po polsku z linkami.")
add("nextlevelbuilder/ui-ux-pro-max-skill","Skille","UI/UX Pro Max",
 "Skill z „inteligencją projektową”: style, palety, typografia, zasady UX i wzorce dla wielu stacków – żeby agent robił profesjonalne interfejsy.",
 9,"Twoje dashboardy i strony na GitHub Pages od razu wyglądałyby lepiej i spójniej.","łatwa",
 ["Bot klonuje repo i czyta zawartość skilla.","Wyciąga zasady pod czysty HTML/CSS w stylu iOS.","Zapisuje jako skill i używa przy każdej nowej stronie."],
 "Sklonuj https://github.com/nextlevelbuilder/ui-ux-pro-max-skill i przeczytaj jego SKILL.md oraz dane. Zrób z tego Twój skill 'design-pro' dopasowany do moich stron: czysty HTML bez zależności, styl iOS/glass, tryb ciemny, iPhone. Potem popraw według niego stronę centrum dowodzenia i pokaż mi zrzut przed/po.")
add("unclecode/crawl4ai","Narzędzia CLI","Crawl4AI",
 "Otwartoźródłowy crawler/scraper, który zamienia dowolną stronę (także z JavaScriptem) w czysty Markdown gotowy dla LLM.",
 9,"Na komputerze bota możesz zbierać dane ze stron bez API – ceny, ogłoszenia, newsy – i robić z nich dashboardy.","średnia",
 ["Bot instaluje crawl4ai w Pythonie na swoim komputerze.","Podajesz adresy stron.","Bot zapisuje wynik jako JSON/Markdown i np. buduje z tego stronę."],
 "Zainstaluj na swoim komputerze crawl4ai (pip install crawl4ai, potem crawl4ai-setup). Pobierz nim treść stron, które Ci podam, do Markdown w /workspace/crawl, a potem streść mi je po polsku. Na start przetestuj na https://news.ycombinator.com.")
add("tt-a1i/archify","Skille","Archify – interaktywne diagramy",
 "Skill, który zamienia pomysł, plan albo kod w ładny, interaktywny diagram (HTML).",
 9,"Świetny do wizualizacji Twoich projektów (dom, trading, aplikacje) jako strony na GitHub Pages.","łatwa",
 ["Bot czyta skill z repo.","Zapisuje go jako własny skill.","Prosisz o diagram dowolnego planu i publikację na Pages."],
 "Przeczytaj https://github.com/tt-a1i/archify i zapisz jego metodę jako Twój skill 'diagramy'. Potem zrób interaktywny diagram mojego projektu z /workspace/trading-agent (jak działa krok po kroku), opisany po polsku, i pokaż mi go.")
add("modelcontextprotocol/servers","Serwery MCP","Oficjalne serwery MCP (referencyjne)",
 "Repozytorium referencyjnych serwerów MCP (filesystem, git, fetch, memory, time, sequential-thinking) i spis serwerów społeczności.",
 8,"Dobre źródło, żeby zrozumieć, jakie konektory istnieją i które warto podłączyć.","średnia",
 ["Przeglądasz listę serwerów.","Wybierasz potrzebny konektor.","Bot sprawdza, czy jest w katalogu konektorów Grok Bota."],
 "Przejrzyj https://github.com/modelcontextprotocol/servers (README z listą serwerów). Wybierz 10 serwerów MCP najbardziej przydatnych dla mnie (projekty na GitHubie, strony HTML, research, finanse) i dla każdego sprawdź, czy da się go podłączyć jako konektor u Ciebie. Daj mi tabelę po polsku.")
add("punkpeye/awesome-mcp-servers","Serwery MCP","Awesome MCP Servers",
 "Największa kuratorowana lista serwerów MCP w podziale na kategorie (finanse, przeglądarki, bazy danych, komunikacja…).",
 8,"Najszybszy sposób, żeby znaleźć konektor do konkretnej usługi, której używasz.","łatwa",
 ["Podajesz bota usługę, z którą chcesz się połączyć.","Bot przeszukuje listę.","Dostajesz 2–3 propozycje z oceną."],
 "Przeszukaj listę https://github.com/punkpeye/awesome-mcp-servers i znajdź serwery MCP do: (1) danych giełdowych, (2) Telegrama, (3) Notion lub notatek, (4) Home Assistant. Dla każdego podaj link, gwiazdki z GitHub API i czy da się go podłączyć u Ciebie.")
add("github/github-mcp-server","Serwery MCP","GitHub MCP Server (oficjalny)",
 "Oficjalny serwer MCP GitHuba: repozytoria, issues, pull requesty, Actions, wyszukiwanie kodu.",
 7,"Najczęściej polecany konektor; Grok Bot ma już wbudowane narzędzia GitHuba, więc to raczej punkt odniesienia.","łatwa",
 ["Sprawdź, jakie narzędzia GitHuba ma już bot.","Używaj ich do zarządzania repo.","Ewentualnie ustaw routine z raportem z repo."],
 "Pokaż mi, co możesz zrobić z moimi repozytoriami GitHub (damiangrok5-droid) za pomocą swoich narzędzi GitHuba. Zrób mi raport: lista repo, ostatnie zmiany, otwarte issues, które mają GitHub Pages. Porównaj swoje możliwości z https://github.com/github/github-mcp-server.")
add("microsoft/playwright-mcp","Serwery MCP","Playwright MCP",
 "Serwer MCP od Microsoftu do sterowania przeglądarką (klikanie, formularze, zrzuty) przez drzewo dostępności zamiast pikseli.",
 6,"Bot ma już własną przeglądarkę i Playwright można uruchamiać w shellu – przydatne do testów Twoich stron.","średnia",
 ["Bot instaluje Playwright na swoim komputerze.","Pisze skrypt testujący Twoją stronę.","Robi zrzuty w widoku iPhone'a."],
 "Na swoim komputerze użyj Playwright (zobacz https://github.com/microsoft/playwright-mcp dla inspiracji), żeby przetestować moje strony z centrum dowodzenia: otwórz każdą w widoku iPhone'a 390x844, zrób zrzut ekranu i wypisz błędy z konsoli.")
add("upstash/context7","Serwery MCP","Context7 – aktualna dokumentacja",
 "Serwer MCP/platforma, która podaje agentowi aktualną dokumentację bibliotek zamiast przestarzałej wiedzy modelu.",
 7,"Gdy budujesz aplikacje z bibliotekami, bot przestaje wymyślać nieistniejące funkcje.","średnia",
 ["Bot sprawdza, czy Context7 jest w katalogu konektorów.","Jeśli nie – korzysta z publicznego API przez curl.","Używa go przy pracy z kodem."],
 "Sprawdź, czy możesz podłączyć Context7 (https://github.com/upstash/context7) jako konektor. Jeśli nie, pokaż, jak pobrać z niego dokumentację przez curl na swoim komputerze. Przetestuj na dokumentacji Chart.js.")
add("PrefectHQ/fastmcp","Serwery MCP","FastMCP",
 "Najprostszy Pythonowy sposób na zbudowanie własnego serwera (i klienta) MCP w kilkunastu linijkach.",
 6,"Gdy zechcesz własny konektor (np. do swoich danych), to najkrótsza droga.","trudna",
 ["Opisujesz, jakie dane ma udostępniać serwer.","Bot pisze serwer w FastMCP na swoim komputerze.","Testuje go lokalnie (hosting to osobny krok)."],
 "Na swoim komputerze zbuduj w FastMCP (https://github.com/PrefectHQ/fastmcp) prosty serwer MCP, który udostępnia narzędzie 'moje_projekty' zwracające listę moich repo z GitHuba. Przetestuj go lokalnie klientem FastMCP i wytłumacz mi po polsku, jak to działa.")
add("searxng/searxng","Narzędzia CLI","SearXNG",
 "Darmowa metawyszukiwarka zbierająca wyniki z wielu wyszukiwarek, bez śledzenia; ma API JSON.",
 5,"Bot ma już wyszukiwarkę; SearXNG przyda się tylko do masowych, powtarzalnych zapytań.","trudna",
 ["Bot uruchamia SearXNG w Dockerze/Pythonie na swoim komputerze.","Włącza format JSON.","Używa go w skryptach researchu."],
 "Oceń, czy warto postawić na Twoim komputerze SearXNG (https://github.com/searxng/searxng) do masowego researchu. Jeśli tak, uruchom go lokalnie, włącz API JSON i pokaż przykładowe zapytanie.")
add("ComposioHQ/awesome-claude-skills","Skille","Awesome Claude Skills (Composio)",
 "Kuratorowana lista skilli, zasobów i narzędzi do rozszerzania agentów (dokumenty, rozwój, dane, marketing, produktywność).",
 8,"Szybki katalog gotowych skilli do skopiowania.","łatwa",
 ["Bot czyta listę.","Wybiera 5 skilli pasujących do Ciebie.","Adaptuje je i zapisuje."],
 "Przeczytaj https://github.com/ComposioHQ/awesome-claude-skills i wybierz 5 skilli najbardziej przydatnych dla mnie (dashboardy, research, finanse, projekty DIY). Dla każdego: co robi, link, i czy możesz go od razu zaadaptować. Po mojej akceptacji zapisz je jako swoje skille.")
add("VoltAgent/awesome-agent-skills","Skille","Awesome Agent Skills (VoltAgent)",
 "Zbiór 1000+ skilli od oficjalnych zespołów (Anthropic, Vercel, Stripe, Cloudflare…) i społeczności.",
 8,"Największa baza SKILL.md – łatwo znaleźć skill do konkretnej usługi.","łatwa",
 ["Podajesz temat.","Bot przeszukuje listę.","Adaptuje wybrany skill."],
 "Przeszukaj https://github.com/VoltAgent/awesome-agent-skills pod kątem skilli do: tworzenia stron HTML, analizy danych/CSV, researchu i finansów. Podaj top 8 z linkami i powiedz, które mogę u Ciebie zainstalować jako skill.")
add("blader/humanizer","Skille","Humanizer",
 "Skill usuwający typowe ślady „tekstu pisanego przez AI” (szablonowe zwroty, nadmiar myślników, puste podsumowania).",
 7,"Teksty, wiadomości i opisy będą brzmiały naturalniej – warto dopisać zasady dla polszczyzny.","łatwa",
 ["Bot czyta listę wzorców.","Tłumaczy i dopasowuje do polskiego.","Zapisuje skill i stosuje do tekstów."],
 "Przeczytaj https://github.com/blader/humanizer i zrób z niego Twój skill 'naturalny-polski': zasady pisania po polsku bez typowych AI-owych zwrotów. Dopisz polskie przykłady. Potem przepisz według niego opis mojego repo trener-gitara.")
add("ayghri/i-have-adhd","Skille","I-have-ADHD – odpowiedź na początku",
 "Skill, który zmusza agenta, żeby najpierw podał odpowiedź, a potem szczegóły – krótko, czytelnie, bez lania wody.",
 7,"Krótsze, konkretne odpowiedzi na iPhonie.","łatwa",
 ["Bot czyta skill.","Zapisuje zasady jako stałą preferencję lub skill.","Od teraz odpowiada zwięźlej."],
 "Przeczytaj https://github.com/ayghri/i-have-adhd i zapamiętaj te zasady formatowania jako moją preferencję: najpierw odpowiedź w 1–2 zdaniach, potem szczegóły, krótko i po polsku. Pokaż mi, co zapisałeś.")
add("coreyhaines31/marketingskills","Skille","Marketing Skills",
 "Paczka skilli marketingowych: CRO, copywriting, SEO, analityka, wzrost.",
 5,"Przyda się, gdy któryś projekt (np. aplikacja) zechcesz promować.","łatwa",
 ["Wybierasz skill (np. SEO).","Bot adaptuje go.","Stosuje do Twojej strony."],
 "Z repo https://github.com/coreyhaines31/marketingskills wybierz skille do SEO i copywritingu. Zastosuj je do strony mojej aplikacji trener-gitara: zaproponuj lepszy tytuł, opis i meta tagi po polsku.")
add("dontriskit/awesome-ai-system-prompts","Prompty","Awesome AI System Prompts",
 "Kolekcja system promptów popularnych narzędzi AI (ChatGPT, Claude, Perplexity, v0, Manus…) z omówieniem wzorców.",
 7,"Nauczysz się, jak profesjonalne asystenty definiują role i zasady – i skopiujesz najlepsze do własnych skilli.","łatwa",
 ["Bot czyta wybrane prompty.","Wyciąga wzorce.","Proponuje ulepszenia Twoich instrukcji."],
 "Przeczytaj https://github.com/dontriskit/awesome-ai-system-prompts i wyciągnij 10 najlepszych wzorców z system promptów (np. planowanie, sprawdzanie wyników). Zaproponuj, jak dopisać je do Twoich skilli, po polsku.")
add("x1xhlol/system-prompts-and-models-of-ai-tools","Prompty","System prompty narzędzi AI",
 "Ogromne zestawienie wyciekłych/publicznych system promptów i definicji narzędzi agentów kodujących (Cursor, Devin, Claude Code, Lovable…).",
 6,"Dobra lektura o tym, jak budowane są agenty – raczej do nauki niż kopiowania (licencja GPL-3.0).","łatwa",
 ["Bot czyta 2–3 prompty.","Porównuje podejścia.","Streszcza najlepsze praktyki."],
 "Przejrzyj https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools – porównaj, jak 3 agenty (np. Cursor, Devin, Lovable) opisują planowanie i używanie narzędzi. Daj mi po polsku 7 praktyk, które mogę wykorzystać we własnych skillach.")
add("f/prompts.chat","Prompty","prompts.chat (dawniej Awesome ChatGPT Prompts)",
 "Najpopularniejsza baza promptów od społeczności – role, zadania, szablony do kopiowania.",
 6,"Szybkie gotowce do codziennych zadań; warto wybrać kilka i zapisać jako skróty.","łatwa",
 ["Bot przegląda bazę.","Wybiera prompty pasujące do Ciebie.","Tłumaczy na polski i zapisuje."],
 "Przejrzyj https://github.com/f/prompts.chat i wybierz 10 promptów przydatnych dla mnie (nauka gitary, finanse, projekt domu, programowanie). Przetłumacz je na polski i zapisz w pliku /workspace/prompty/ulubione.md.")
add("e2b-dev/awesome-ai-agents","Szablony agentów","Awesome AI Agents (E2B)",
 "Lista autonomicznych agentów AI – otwartych i komercyjnych – w podziale na zastosowania.",
 6,"Przegląd tego, co inni zbudowali; inspiracja dla nowych funkcji Twojego bota.","łatwa",
 ["Bot czyta listę.","Wybiera agentów z ciekawymi pomysłami.","Proponuje, co skopiować jako routine lub skill."],
 "Przeczytaj https://github.com/e2b-dev/awesome-ai-agents i wybierz 5 agentów, których pomysły mogę skopiować u Ciebie jako skille lub routines. Dla każdego: co robi i jak to odtworzyć u Ciebie, po polsku.")
add("Shubhamsaboo/awesome-llm-apps","Szablony agentów","Awesome LLM Apps",
 "100+ gotowych aplikacji z kodem: agenci, multi-agent teams, RAG, agent skills – w Pythonie.",
 8,"Gotowe przepisy (np. agent finansowy, podróżniczy, research) do uruchomienia na komputerze bota.","średnia",
 ["Wybierasz aplikację z listy.","Bot klonuje i uruchamia ją na swoim komputerze.","Adaptuje logikę do własnych narzędzi."],
 "Przejrzyj https://github.com/Shubhamsaboo/awesome-llm-apps i wybierz 3 aplikacje agentowe przydatne dla mnie (finanse/inwestycje, research, nauka). Dla najlepszej odtwórz jej logikę u siebie jako skill i pokaż wynik na przykładzie.")
add("nibzard/awesome-agentic-patterns","Workflow multi-agent","Awesome Agentic Patterns",
 "Katalog sprawdzonych wzorców agentowych: planowanie, refleksja, delegowanie do subagentów, pamięć, kontrola jakości.",
 8,"Pomaga projektować lepsze workflow z subagentami i routines u Ciebie.","łatwa",
 ["Bot czyta katalog.","Wybiera wzorce pasujące do Twoich zadań.","Zapisuje je jako skill 'jak-planować'."],
 "Przeczytaj https://github.com/nibzard/awesome-agentic-patterns i wybierz 6 wzorców, które poprawią to, jak dla mnie pracujesz (np. podział na subagentów, weryfikacja wyników). Zapisz je jako Twój skill 'wzorce-pracy' po polsku.")
add("openai/openai-agents-python","Workflow multi-agent","OpenAI Agents SDK",
 "Lekki framework do workflow wieloagentowych: agenci, handoffy, guardrails, śledzenie.",
 5,"Grok Bot sam ma subagentów; SDK przyda się, jeśli zechcesz własną aplikację z agentami.","trudna",
 ["Bot instaluje SDK na swoim komputerze.","Buduje prosty przykład z 2 agentami.","Uruchomienie wymaga klucza API."],
 "Wytłumacz mi po polsku na przykładzie z https://github.com/openai/openai-agents-python, czym są handoffy i guardrails, i jak to się ma do Twoich subagentów. Nic nie instaluj – tylko porównanie i schemat.")
add("crewAIInc/crewAI","Workflow multi-agent","CrewAI",
 "Framework do „załóg” agentów z rolami (badacz, analityk, pisarz), które współpracują nad zadaniem.",
 6,"Dobry wzór podziału ról – możesz to samo osiągnąć subagentami Grok Bota bez instalacji.","średnia",
 ["Bot czyta przykłady crew.","Odtwarza podział ról subagentami.","Zapisuje jako skill."],
 "Na wzór CrewAI (https://github.com/crewAIInc/crewAI) zrób mi 'załogę' z Twoich subagentów: badacz zbiera newsy o moich spółkach, analityk ocenia, redaktor pisze raport po polsku. Zapisz to jako skill 'zaloga-research' i uruchom raz.")
add("langchain-ai/langgraph","Workflow multi-agent","LangGraph",
 "Framework do budowania odpornych agentów jako grafów stanów – z pamięcią, wznawianiem i kontrolą człowieka.",
 4,"Dla zaawansowanych aplikacji; na co dzień wystarczą skille i routines bota.","trudna",
 ["Tylko gdy budujesz własną aplikację agentową.","Bot pisze graf w Pythonie.","Wymaga klucza API modelu."],
 "Wytłumacz mi prosto po polsku, co daje LangGraph (https://github.com/langchain-ai/langgraph) w porównaniu z Twoimi routines i subagentami, i kiedy warto by go użyć w moim projekcie trading-agent.")
add("HKUDS/nanobot","Szablony agentów","nanobot",
 "Ultralekki, samodzielnie hostowany osobisty agent AI w Pythonie z interfejsem web i integracjami czatów.",
 5,"Ciekawy jako podgląd, jak zbudowany jest osobisty asystent – dobre pomysły do skopiowania.","trudna",
 ["Bot czyta architekturę.","Wypisuje funkcje, których Ci brakuje.","Odtwarza je skillami/routines."],
 "Przeczytaj README i strukturę https://github.com/HKUDS/nanobot. Wypisz funkcje tego osobistego agenta, których jeszcze nie używam u Ciebie, i zaproponuj, jak je odtworzyć skillami lub routines.")
add("TauricResearch/TradingAgents","Workflow multi-agent","TradingAgents",
 "Wieloagentowy framework tradingowy: analitycy fundamentalni, sentymentu i techniczni, debata byk/niedźwiedź, trader i zarządzanie ryzykiem.",
 8,"Pasuje do Twojego projektu trading-agent – gotowy schemat ról do skopiowania (tylko do analizy, nie porada inwestycyjna).","średnia",
 ["Bot czyta prompty ról.","Porównuje z /workspace/trading-agent.","Dodaje brakujące role jako subagentów."],
 "Przeczytaj https://github.com/TauricResearch/TradingAgents (role agentów i prompty). Porównaj z moim projektem /workspace/trading-agent i zaproponuj, jakie role (np. debata byk/niedźwiedź, risk manager) dodać. Pokaż plan zmian przed wdrożeniem.")
add("enescingoz/awesome-n8n-templates","Automatyzacje","Awesome n8n Templates",
 "280+ darmowych szablonów automatyzacji (Gmail, Telegram, Slack, Discord, Google Sheets, AI).",
 7,"Kopalnia pomysłów na automatyzacje – większość odtworzysz jako routines Grok Bota bez n8n.","łatwa",
 ["Bot przegląda kategorie szablonów.","Wybiera 5 przydatnych.","Odtwarza je jako routines."],
 "Przejrzyj https://github.com/enescingoz/awesome-n8n-templates i wybierz 5 automatyzacji przydatnych dla mnie (Telegram, maile, raporty, finanse). Dla każdej opisz, jak odtworzyć ją jako Twoją routine. Nie twórz routines bez mojej zgody.")
add("n8n-io/n8n","Automatyzacje","n8n",
 "Platforma automatyzacji workflow (wizualny edytor + kod) z natywnymi funkcjami AI i 400+ integracjami.",
 5,"Mocne narzędzie, ale routines bota pokrywają większość potrzeb; self-hosting to osobny projekt.","trudna",
 ["Tylko jeśli potrzebujesz wizualnych workflow.","Bot może uruchomić n8n lokalnie na swoim komputerze do testów.","Stały hosting wymaga serwera."],
 "Porównaj po polsku n8n (https://github.com/n8n-io/n8n) z Twoimi routines: co n8n robi lepiej, co Ty robisz lepiej, i czy w moim przypadku warto go stawiać.")
add("upptime/upptime","Automatyzacje","Upptime",
 "Monitor dostępności stron i strona statusu działające w całości na GitHub Actions i GitHub Pages.",
 7,"Mógłby pilnować, czy Twoje strony na GitHub Pages działają. Wymaga dodania workflow ręcznie (token bota nie ma scope 'workflow').","średnia",
 ["Tworzysz repo z szablonu Upptime.","Wpisujesz adresy swoich stron w .upptimerc.yml.","Workflow dodajesz ręcznie albo bot robi prostszą routine z curl."],
 "Na wzór Upptime (https://github.com/upptime/upptime) zrób mi routine, która raz dziennie sprawdza curl-em wszystkie moje strony z centrum dowodzenia i pisze mi tylko, gdy któraś nie działa. Najpierw pokaż mi plan routine.")
add("simonw/llm","Narzędzia CLI","llm (Simon Willison)",
 "Narzędzie CLI i biblioteka do korzystania z modeli językowych z terminala, z logowaniem do SQLite i wtyczkami.",
 5,"Przydatne w skryptach na komputerze bota, ale wymaga własnego klucza API.","średnia",
 ["Bot instaluje llm (pip).","Konfigurujesz klucz API (opcjonalnie).","Używa w skryptach wsadowych."],
 "Wyjaśnij mi, do czego mógłbym użyć narzędzia https://github.com/simonw/llm na Twoim komputerze (np. masowe streszczanie plików) i czego by wymagało. Nic nie instaluj bez mojej zgody.")
add("simonw/shot-scraper","Narzędzia CLI","shot-scraper",
 "CLI do zrzutów ekranu stron, nagrywania demo i scrapowania przez JavaScript (na Playwright).",
 8,"Automatyczne zrzuty Twoich stron w widoku iPhone'a – np. do centrum dowodzenia lub raportów.","łatwa",
 ["Bot instaluje shot-scraper na swoim komputerze.","Robi zrzuty z ustawioną szerokością.","Zapisuje je lub wysyła w raporcie."],
 "Zainstaluj na swoim komputerze shot-scraper (https://github.com/simonw/shot-scraper) i zrób zrzuty wszystkich moich stron z centrum dowodzenia w rozmiarze iPhone'a (390x844). Pokaż mi je w jednym zestawieniu.")
add("yt-dlp/yt-dlp","Narzędzia CLI","yt-dlp",
 "Rozbudowany downloader audio/wideo z tysięcy serwisów, także same napisy i metadane.",
 7,"Pobieranie napisów z lekcji gitary czy wykładów i streszczanie ich przez bota.","łatwa",
 ["Bot instaluje yt-dlp.","Pobiera napisy (--write-auto-subs --skip-download).","Streszcza lub robi notatki."],
 "Zainstaluj yt-dlp (https://github.com/yt-dlp/yt-dlp) na swoim komputerze, pobierz same napisy z filmu, który Ci podam (bez wideo), i zrób z nich notatki po polsku z najważniejszymi wskazówkami.")
add("tabler/tabler","Dashboardy HTML","Tabler",
 "Darmowy UI kit dashboardów admina: 100+ stron, tysiące ikon, komponenty i wykresy.",
 7,"Gotowe wzory układów dashboardów; ikony SVG można wbudować bez zależności.","średnia",
 ["Bot przegląda układy Tablera.","Wybiera wzór dashboardu.","Odtwarza go w czystym HTML w Twoim stylu."],
 "Przejrzyj https://github.com/tabler/tabler i na wzór jednego z jego dashboardów przebuduj mój dashboard z /workspace/(folder dashboardu) – czysty HTML bez zewnętrznych zależności, styl iOS, iPhone. Pokaż zrzut ekranu.")
add("chartjs/Chart.js","Dashboardy HTML","Chart.js",
 "Prosta biblioteka wykresów HTML5 (canvas): liniowe, słupkowe, kołowe, z animacjami.",
 7,"Najprostsza droga do ładnych wykresów w Twoich dashboardach (plik można wbudować lokalnie).","łatwa",
 ["Bot pobiera plik chart.umd.js do repo.","Dodaje wykres do strony.","Publikuje na GitHub Pages."],
 "Dodaj do mojego dashboardu z /workspace/(folder dashboardu) wykresy z Chart.js (https://github.com/chartjs/Chart.js) – plik biblioteki skopiuj do repo, bez CDN. Wykresy mają dobrze wyglądać na iPhonie i w trybie ciemnym.")

# Non-GitHub
NG = {
 "hn:48015397": dict(kat="Poradniki", nazwa="Agent Skills – Addy Osmani (HN)", url="https://addyosmani.com/blog/agent-skills/", src="Hacker News", hn="https://news.ycombinator.com/item?id=48015397", points=376, date="2026-05-04", unit="punktów HN"),
 "hn:48289950": dict(kat="Poradniki", nazwa="Claude Code jako codzienne narzędzie (HN)", url="https://arps18.github.io/posts/claude-code-mastery/", src="Hacker News", hn="https://news.ycombinator.com/item?id=48289950", points=451, date="2026-05-27", unit="punktów HN"),
 "rd:mcp-q3": dict(kat="Serwery MCP", nazwa="Lista MCP używanych w praktyce – Q3 2026 (r/mcp)", url="https://www.reddit.com/r/mcp/comments/1vsuinw/compiled_a_list_of_mcp_servers_q3_2026/", src="Reddit", points=19, date="2026-08-19", unit="punktów Reddit"),
 "rd:5skills": dict(kat="Skille", nazwa="5 skilli na start każdego projektu (r/AI_Agents)", url="https://www.reddit.com/r/AI_Agents/comments/1roe8k8/5_agent_skills_id_install_before_starting_any_new/", src="Reddit", points=123, date="2026-03-08", unit="punktów Reddit"),
}
add("hn:48015397","Poradniki","",
 "Artykuł Addy'ego Osmaniego o tym, czym są Agent Skills, jak je projektować i dlaczego progresywne ładowanie kontekstu działa lepiej niż wielkie prompty.",
 7,"Dobre wprowadzenie, jak pisać skuteczne SKILL.md dla Twojego bota.","łatwa",
 ["Bot czyta artykuł.","Streszcza zasady po polsku.","Sprawdza Twoje skille pod ich kątem."],
 "Przeczytaj artykuł https://addyosmani.com/blog/agent-skills/ i streść mi po polsku najważniejsze zasady pisania skilli. Potem sprawdź według nich swoje obecne skille i zaproponuj poprawki.")
add("hn:48289950","Poradniki","",
 "Praktyczny przewodnik: plik instrukcji, skille, subagenci, pluginy i MCP w codziennej pracy z agentem.",
 6,"Pokazuje, jak łączyć skille, subagentów i konektory – te same klocki ma Grok Bot.","łatwa",
 ["Bot czyta przewodnik.","Mapuje pojęcia na swoje funkcje.","Proponuje ulepszenia Twojej konfiguracji."],
 "Przeczytaj https://arps18.github.io/posts/claude-code-mastery/ i przełóż to na Twoje funkcje (skille, subagenci, konektory, routines). Daj mi listę 5 ulepszeń mojej konfiguracji po polsku.")
add("rd:mcp-q3","Serwery MCP","",
 "Zestawienie z Reddita serwerów MCP, których ludzie faktycznie używają (GitHub, Context7, Postgres, Playwright, Notion, Home Assistant…), a nie tylko tych z katalogów.",
 7,"Filtr „co naprawdę działa” – pomaga nie zaśmiecać bota zbędnymi konektorami.","łatwa",
 ["Bot czyta wątek.","Porównuje z Twoimi konektorami.","Proponuje 1–3 brakujące."],
 "Przeczytaj wątek https://www.reddit.com/r/mcp/comments/1vsuinw/compiled_a_list_of_mcp_servers_q3_2026/ i porównaj z konektorami, które już mam u Ciebie. Zaproponuj maksymalnie 3, które warto dodać, i powiedz dlaczego.")
add("rd:5skills","Skille","",
 "Wątek z r/AI_Agents o 5 skillach na start: prompt-engineer, skill-creator, mcp-builder, agentic-eval, openai-docs.",
 7,"Krótka lista sprawdzonych skilli – większość jest w anthropics/skills i github/awesome-copilot.","łatwa",
 ["Bot znajduje każdy skill.","Ocenia przydatność.","Adaptuje 2–3 najlepsze."],
 "Przeczytaj wątek https://www.reddit.com/r/AI_Agents/comments/1roe8k8/5_agent_skills_id_install_before_starting_any_new/, znajdź źródła wymienionych skilli (prompt-engineer, skill-creator, mcp-builder, agentic-eval) i zaadaptuj 2 najbardziej przydatne dla mnie jako Twoje skille.")

TOP = ["anthropics/skills","mvanhorn/last30days-skill","nextlevelbuilder/ui-ux-pro-max-skill","unclecode/crawl4ai","tt-a1i/archify"]
items=[]
for (key,kat,nazwa,opis,ocena,why,tr,kroki,prompt) in E:
    it=dict(id=key.replace('/','__').replace(':','_'),kategoria=kat,opis=opis,ocena=ocena,dlaczego=why,trudnosc=tr,kroki=kroki,prompt=prompt,top=key in TOP)
    if key in raw:
        g=raw[key]
        it.update(nazwa=nazwa,repo=g['full_name'],url=g['url'],zrodlo="GitHub",licencja=(g['license'] if g['license'] and g['license']!="NOASSERTION" else ("inna / niestandardowa" if g['license']=="NOASSERTION" else "brak danych")),
                  gwiazdki=g['stars'],aktywnosc=g['pushed_at'][:10],opis_oryginalny=g['desc'])
    else:
        n=NG[key]
        it.update(nazwa=n['nazwa'],repo=None,url=n['url'],zrodlo=n['src'],licencja="brak danych",gwiazdki=None,aktywnosc=n['date'],
                  popularnosc=f"{n['points']} {n['unit']}",dyskusja=n.get('hn') or n['url'])
    items.append(it)
from projekt_domu import projekt_domu_items, PD_TOP
LIC_OVERRIDE={'anthropics__skills':'mieszana: Apache-2.0 / zastrzeżona (docx, xlsx, pptx, pdf)'}
for _i in items:
    if _i['id'] in LIC_OVERRIDE: _i['licencja']=LIC_OVERRIDE[_i['id']]
items += projekt_domu_items()
assert len(items)==len({i['id'] for i in items})
data=dict(tytul="Zwiadowca Rozwiązań",data_zwiadu="2026-10-26",wygenerowano=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"),
  zrodla=["GitHub API (gh api repos/…, search/repositories)","Hacker News (Algolia API)","Reddit (wyniki wyszukiwania; API Reddita zablokowane z komputera bota)","awesome-listy: awesome-mcp-servers, modelcontextprotocol/servers, awesome-claude-skills, awesome-agent-skills, awesome-ai-agents"],
  uwagi="Pozycje z tagiem Projekt Domu dodano 26.10.2026 dla agenta projektowania domu. Gwiazdki i daty ostatniego pushu pobrane z GitHub API w dniu zwiadu. Dla pozycji spoza GitHuba podano punkty z HN/Reddita i datę publikacji.",
  top5=[i['id'] for i in items if i['top']], pozycje=items)
data['top5']=[k.replace('/','__') for k in TOP]
data['top5_projekt_domu']=PD_TOP
json.dump(data,open('data.json','w'),ensure_ascii=False,indent=1)
print(len(items))
