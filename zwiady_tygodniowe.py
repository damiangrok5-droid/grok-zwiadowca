# Znaleziska z cotygodniowych zwiadów. Dane GitHub (gwiazdki, licencja, ostatni push) pobierane na żywo z gh api.
import json, subprocess
def gh(repo):
    d=json.loads(subprocess.run(['gh','api','repos/'+repo],capture_output=True,text=True,check=True).stdout)
    lic=(d.get('license') or {}).get('spdx_id')
    return dict(repo=d['full_name'],gwiazdki=d['stargazers_count'],aktywnosc=d['pushed_at'][:10],
                licencja=lic if lic and lic!="NOASSERTION" else ("inna / niestandardowa" if lic=="NOASSERTION" else "brak danych"),
                opis_oryginalny=d['description'],url=d['html_url'])
W = {"2026-11-02": [
 dict(repo="heydamir/unslop", kategoria="Skille", nazwa="unslop – z „wyglądu AI” do zaprojektowanego UI", ocena=9, trudnosc="łatwa",
  opis="Skill (SKILL.md), który najpierw wypisuje oznaki „AI-slopu” w interfejsie (fioletowe gradienty, poświaty, emoji w etykietach, krzykliwe teksty, nierówne odstępy), proponuje kierunek, a potem poprawia odstępy, kolory, ikony, teksty, typografię i układ. Opcjonalnie robi krótkie wideo „przed i po” (Playwright + ffmpeg). Repo z 29.10.2026, bardzo szybko rośnie.",
  dlaczego="Twoje strony (zwiadowca, centrum dowodzenia, Projekt Domu) są robione przez agentów – ten skill daje gotową listę kontrolną, żeby nie wyglądały „jak z generatora”. Licencja CC BY 4.0 pozwala adaptować, z podaniem autora.",
  kroki=["Bot czyta skills/unslop/SKILL.md i referencje.","Adaptuje go jako własny skill (z atrybucją autora, CC BY 4.0) albo dopisuje zasady do skilla projektowanie-stron.","Robi audyt jednej Twojej strony i pokazuje zrzuty przed i po."],
  prompt="Przeczytaj skill https://github.com/heydamir/unslop (skills/unslop/SKILL.md i references). Licencja to CC BY 4.0, więc przy adaptacji podaj autora (Damir Sokolovsky) i link do repo. Dopisz najlepsze zasady do mojego skilla projektowanie-stron, zachowując styl iOS/glass. Potem zrób audyt strony https://damiangrok5-droid.github.io/grok-zwiadowca/: wypisz po polsku oznaki „wyglądu AI”, zaproponuj kierunek i pokaż zrzuty z iPhone'a przed i po. Nie publikuj zmian bez mojej zgody."),
 dict(repo="enmerasoftware/ai-design-check", kategoria="Narzędzia CLI", nazwa="ai-design-check – automatyczny przegląd designu", ocena=8, trudnosc="łatwa",
  opis="87 zasad projektowania i checker bez zależności i bez klucza API (npx @enmera/ai-design-check): wskazuje plik i linię z problemem (dostępność, skala fontów, kontrast, dekoracyjne wersaliki). Ma też tryb „narrow” sprawdzający, co psuje się na telefonie, oraz skill do naprawy ekranu.",
  dlaczego="Daje mierzalny wynik „przed i po” zamiast oceny na oko, a tryb narrow testuje dokładnie to, na czym Ci zależy: widok na iPhonie.",
  kroki=["Bot uruchamia checker na swoim komputerze na pliku index.html.","Tryb narrow sprawdza wąski ekran.","Bot poprawia błędy i pokazuje liczbę problemów przed i po."],
  prompt="Na swoim komputerze uruchom npx @enmera/ai-design-check (https://github.com/enmerasoftware/ai-design-check, MIT) dla /workspace/grok-zwiadowca/template.html, a potem tryb narrow dla index.html. Pokaż mi po polsku listę błędów i ostrzeżeń, popraw te z dostępności i czytelności na iPhonie i podaj liczbę problemów przed i po. Nie publikuj bez mojej zgody."),
 dict(repo="emanuele-em/kanzo", kategoria="Workflow multi-agent", nazwa="Kanzo – tablica kanban dla Ciebie i agentów (MCP)", ocena=7, trudnosc="średnia",
  opis="Tablica kanban w przeglądarce i serwer MCP w jednym programie (4,5 MB, bez konta i bez bazy). Agenci biorą zadania, przesuwają karty i komentują przez MCP, a Ty widzisz to na tablicy. Licencja AGPL-3.0.",
  dlaczego="Masz kilku agentów (Zwiadowca, Projekt Domu, Trading, Trener) – wspólna tablica zadań pokazałaby, kto co robi. Uwaga: to narzędzie lokalne na komputerze bota, Grok Bot nie podłączy go jako konektora bez publicznego adresu.",
  kroki=["Bot uruchamia kanzo lokalnie na swoim komputerze.","Agenci dodają i przesuwają karty przez polecenie kanzo (CLI).","Bot co tydzień eksportuje stan tablicy do centrum dowodzenia."],
  prompt="Przeczytaj https://github.com/emanuele-em/kanzo (AGPL-3.0) i oceń po polsku, czy da się go użyć na Twoim komputerze jako wspólnej tablicy zadań dla moich agentów: uruchom go lokalnie bez wystawiania do internetu, dodaj 3 przykładowe karty przez polecenie kanzo i powiedz, jak inni agenci mogliby z niego korzystać. Niczego nie podłączaj do moich kont."),
 dict(repo="caru-ini/stack-diagram", kategoria="Skille", nazwa="stack-diagram – schemat architektury z jednego zdania", ocena=7, trudnosc="łatwa",
  opis="Skill, który z opisu typu „Next.js na Vercel, Postgres na Neon, płatności Stripe” rysuje schemat architektury z oficjalnymi logo, w trybie jasnym i ciemnym, jako jeden samodzielny plik HTML (albo PNG). Kod MIT, fonty OFL. Repo z 1.11.2026.",
  dlaczego="Ładny, gotowy do wklejenia na stronę schemat Twojego systemu agentów (Grok Bot, GitHub Pages, routines, konektory) – dobry do centrum dowodzenia. Uwaga: po narysowaniu proponuje publikację w publicznej galerii – trzeba odmówić (prywatność).",
  kroki=["Bot czyta SKILL.md i adaptuje go jako własny skill.","Opisujesz swój układ agentów jednym zdaniem.","Bot zapisuje schemat HTML i dodaje go do centrum dowodzenia – bez publikacji w galerii."],
  prompt="Przeczytaj skill https://github.com/caru-ini/stack-diagram (MIT) i według niego narysuj schemat mojego systemu: Grok Bot z agentami Zwiadowca Rozwiązań, Projekt Domu i Trading, routines, GitHub Pages i konektory GitHub i X. Zapisz jako jeden plik HTML w trybie jasnym i ciemnym i pokaż mi zrzut. NIE publikuj niczego w galerii stacks.caru.moe ani nigdzie indziej bez mojej zgody."),
 dict(repo="KrushnaVardhanReddy/PaperPilot", licencja_stala="Apache-2.0 (wg pliku LICENSE; GitHub API: niestandardowa)", kategoria="Serwery MCP", nazwa="PaperPilot – narzędzia PDF jako MCP i CLI (lokalnie)", ocena=7, trudnosc="średnia",
  opis="Silnik PDF w Ruście działający lokalnie: łączenie, dzielenie, OCR, kompresja i ekstrakcja tekstu. Ten sam silnik działa jako serwer MCP, CLI, lokalne REST API i wersja w przeglądarce (WASM). Był na Hacker News (236 punktów, 26.10.2026).",
  dlaczego="Przydaje się Projektowi Domu i każdemu agentowi pracującemu z PDF-ami (oferty wykonawców, kosztorysy). Pliki nie opuszczają komputera, co pasuje do Twoich zasad prywatności.",
  kroki=["Bot pobiera wydanie CLI z Releases na swój komputer.","Testuje łączenie, kompresję i ekstrakcję tekstu na przykładowym PDF.","Jeśli działa dobrze, zapisuje skill „obróbka PDF” korzystający z CLI."],
  prompt="Pobierz na swój komputer CLI PaperPilot z https://github.com/KrushnaVardhanReddy/PaperPilot/releases (Apache-2.0). Na przykładowym PDF bez danych osobowych przetestuj: połączenie dwóch plików, kompresję i wyciągnięcie tekstu. Porównaj wynik z poppler-utils i powiedz po polsku, czy warto zrobić z tego skill do obróbki PDF dla Projektu Domu."),
 dict(repo="YTruman/better-skill", kategoria="Skille", nazwa="better-skill – „lekarz” do audytu skilli", ocena=7, trudnosc="łatwa",
  opis="Standard i skill do oceny innych skilli: tryby tworzenia, audytu (raport z numerami linii i priorytetami P0/P1/P2), poprawek (minimalne łatki) i porównania dwóch skilli na pięciu skalach (m.in. trafność uruchamiania i zużycie tokenów). Dokumentacja po chińsku i angielsku. MIT.",
  dlaczego="Masz już kilka własnych skilli (projektowanie-stron, tworzenie-skilli, pdf-dla-wykonawcy…). To gotowa metoda, żeby sprawdzić, czy uruchamiają się wtedy, kiedy trzeba, i czy nie są przegadane.",
  kroki=["Bot czyta README.en.md i pliki standardu.","Robi audyt 2–3 Twoich skilli.","Proponuje małe poprawki i czeka na Twoją zgodę."],
  prompt="Przeczytaj https://github.com/YTruman/better-skill (README.en.md i pliki standardu, MIT). Według tej metody zrób audyt moich skilli projektowanie-stron, tworzenie-skilli i pdf-dla-wykonawcy: raport po polsku z priorytetami P0/P1/P2 i proponowanymi minimalnymi poprawkami. Niczego nie zmieniaj bez mojej zgody."),
 dict(repo="Moh4696/open-3d-skills", kategoria="Skille", nazwa="Open 3D Skills – sceny three.js i animowane strony", ocena=7, trudnosc="średnia",
  opis="Osiem skilli do stron 3D: sceny three.js budowane z kodu (bez plików modeli), filmy przewijane scrollem, przezroczyste wideo działające w Safari, widok rozłożony (exploded view) i inne. MIT.",
  dlaczego="Dla Projektu Domu (spacer 3D, model GLB) i dla efektownych stron działających na iPhonie – wskazówki pod Safari są tu kluczowe.",
  kroki=["Bot czyta skill threejs-scene i ten o wideo w Safari.","Porównuje z obecnym spacerem 3D Projektu Domu.","Proponuje 3 ulepszenia i testuje je w widoku iPhone'a."],
  prompt="Przeczytaj skille z https://github.com/Moh4696/open-3d-skills (MIT), zwłaszcza threejs-scene. Porównaj ich metody z tym, jak zbudowany jest spacer 3D w Projekcie Domu, i zaproponuj po polsku 3 konkretne ulepszenia (wydajność i wygląd na iPhonie w Safari). Niczego nie zmieniaj bez mojej zgody."),
]}
def weekly_items():
    out=[]
    for data,lst in W.items():
        for e in lst:
            g=gh(e['repo']); it=dict(e); it.update(g)
            if e.get('licencja_stala'): it['licencja']=e['licencja_stala']
            it.pop('licencja_stala',None)
            it['id']="w__"+e['repo'].replace('/','__'); it['tagi']=["Nowe "+data[8:10]+"."+data[5:7]]; it['dodano']=data
            it['zrodlo']="GitHub"; it['top']=False
            out.append(it)
    return out
