# Znaleziska dla agenta „Projekt Domu” (zwiad 2026-10-26). Dane GitHub pobierane na żywo z gh api.
import json, subprocess
def gh(repo):
    d = json.loads(subprocess.run(['gh','api','repos/'+repo],capture_output=True,text=True,check=True).stdout)
    lic = (d.get('license') or {}).get('spdx_id')
    return dict(repo=d['full_name'], gwiazdki=d['stargazers_count'], aktywnosc=d['pushed_at'][:10],
                licencja=lic if lic and lic!="NOASSERTION" else ("inna / niestandardowa" if lic=="NOASSERTION" else "brak danych"),
                opis_oryginalny=d['description'], url=d['html_url'])
PD = [
 dict(repo="google/model-viewer", kategoria="Dashboardy HTML", nazwa="model-viewer – interaktywny 3D i AR na stronie", ocena=9, trudnosc="łatwa",
  opis="Web component od Google: jeden tag <model-viewer> pokazuje model GLB z obracaniem, zoomem i trybem AR (na iPhonie przez Quick Look).",
  dlaczego="Projekt Domu ma już model parteru GLB (3d/parter-g2-v2.glb) – można go obracać na stronie, a na iPhonie postawić w AR.",
  kroki=["Agent kopiuje plik model-viewer.min.js do repo strony (bez CDN).","Dodaje zakładkę „Model 3D” z plikiem GLB.","Dla AR na iPhonie eksportuje też wersję USDZ."],
  prompt="Na stronie Projektu Domu dodaj zakładkę „Model 3D”, która pokazuje model z projekt-domu/3d/parter-g2-v2.glb przez <model-viewer> (https://github.com/google/model-viewer). Plik biblioteki skopiuj do repo, bez CDN. Ma działać na iPhonie: obracanie palcem i przycisk AR (Quick Look, wersja USDZ). Pokaż mi zrzut z widoku iPhone'a."),
 dict(repo="anthropics/skills", url="https://github.com/anthropics/skills/tree/main/skills/xlsx", licencja_stala="zastrzeżona (All rights reserved) – tylko jako wzór, nie kopiować", kategoria="Skille", nazwa="Anthropic: skille xlsx + pdf – tylko jako wzór", ocena=5, trudnosc="łatwa",
  opis="Skille Anthropic do arkuszy Excel (xlsx) i plików PDF (pdf). Ich LICENSE.txt mówi: „© 2025 Anthropic, PBC. All rights reserved.”, więc nie wolno ich kopiować ani zapisywać jako własnych skilli. Można je tylko czytać jako wzór metody.",
  dlaczego="Pokazują dobre praktyki, np. formuły zamiast wpisanych na sztywno sum i sprawdzanie przeliczenia arkusza. Własny skill do kosztorysów trzeba napisać od zera na wolnych bibliotekach (np. openpyxl, MIT).",
  kroki=["Agent czyta SKILL.md tylko jako inspirację, niczego nie kopiuje.","Pisze własny skill na openpyxl (MIT) i np. reportlab (BSD).","Przerabia wycenę z CSV na arkusz z formułami."],
  prompt="Przeczytaj skille xlsx i pdf z https://github.com/anthropics/skills tylko jako inspirację: mają licencję zastrzeżoną (All rights reserved), więc nie kopiuj z nich tekstu ani skryptów. Napisz własne podejście od zera na openpyxl (MIT): zrób z pliku projekt-domu/02-wycena-budowy.csv arkusz Excel z formułami (sumy etapów, wariant min/średni/max, rezerwa 10%) i sprawdź, czy formuły się przeliczają."),
 dict(repo="frappe/gantt", kategoria="Dashboardy HTML", nazwa="Frappe Gantt – harmonogram budowy", ocena=8, trudnosc="łatwa",
  opis="Lekka biblioteka JavaScript do wykresów Gantta: zadania, zależności, postęp, przeciąganie terminów.",
  dlaczego="Etapy z wyceny (stan zerowy, SSO, SSZ, instalacje, wykończenie) można pokazać jako harmonogram z zależnościami i postępem.",
  kroki=["Agent kopiuje pliki frappe-gantt do repo strony.","Buduje harmonogram.json z etapów wyceny.","Dodaje zakładkę „Harmonogram”, czytelną na iPhonie."],
  prompt="Na podstawie etapów z projekt-domu/02-wycena-budowy.csv zrób harmonogram budowy (harmonogram.json: etap, start, koniec, zależności, % postępu) i dodaj na stronę Projektu Domu zakładkę „Harmonogram” z wykresem Frappe Gantt (https://github.com/frappe/gantt). Pliki biblioteki skopiuj do repo. Ma się dobrze przewijać na iPhonie. Terminy oznacz jako szacunkowe."),
 dict(repo="akseolabs-seo/interior-design-master", kategoria="Skille", nazwa="Interior Design Master – z rzutu do 3D wnętrza", ocena=8, trudnosc="średnia",
  opis="Skill, który z rzutu i zdjęć inspiracji robi edytowalną przeglądarkę 3D mieszkania: rendery koncepcyjne, prawdziwe wymiary mebli, linki zakupowe, kilka widoków kamery i test przejścia (spacer).",
  dlaczego="Robi prawie dokładnie to co Projekt Domu (rzuty, style, zakupy), ale dochodzi spacer 3D z prawdziwymi meblami. Repo jest młode i ma mało gwiazdek, więc lepiej traktować je jako wzór metody.",
  kroki=["Agent czyta SKILL.md i kontrakty JSON z repo.","Porównuje je z pomieszczenia.json i zakupy/*.csv.","Przenosi dobre pomysły (wymiary mebli, linki, kontrola przejść) do własnego workflow."],
  prompt="Przeczytaj skill https://github.com/akseolabs-seo/interior-design-master (SKILL.md, kontrakty JSON, scripts). Porównaj jego metodę z tym, jak pracujesz w projekt-domu (pomieszczenia.json, zakupy, wizualizacje). Wypisz po polsku 5 rzeczy, które warto przejąć, np. sprawdzanie wymiarów mebli i przejść. Niczego nie zmieniaj bez mojej zgody."),
 dict(repo="mozman/ezdxf", kategoria="Narzędzia CLI", nazwa="ezdxf – rzuty w formacie DXF (CAD)", ocena=8, trudnosc="średnia",
  opis="Biblioteka Pythona do czytania i zapisywania plików DXF, czyli formatu AutoCAD-a i innych programów CAD.",
  dlaczego="Rzuty są dziś w SVG/PDF. Eksport do DXF pozwala wysłać je architektowi lub stolarzowi, a jeśli architekt da plik DXF, można odczytać dokładne wymiary zamiast z niewyraźnych skanów.",
  kroki=["Agent instaluje ezdxf w Pythonie na swoim komputerze.","Dopisuje eksport DXF do skryptu rzutów (rzuty-2d).","Zapisuje warstwy: ściany, drzwi, okna, meble, wymiary."],
  prompt="Użyj biblioteki ezdxf (https://github.com/mozman/ezdxf), żeby z modelu rzutów w projekt-domu/rzuty-2d wyeksportować rzut parteru i poddasza do DXF z warstwami: ściany, otwory, meble, wymiary, opisy. Sprawdź wynik, renderując DXF z powrotem do PNG. Nie zmieniaj istniejących plików SVG/PDF."),
 dict(repo="ahujasid/mcp-for-blender", kategoria="Serwery MCP", nazwa="Blender MCP", ocena=8, trudnosc="trudna",
  opis="Wtyczka społeczności, przez którą agent steruje Blenderem: tworzy i zmienia obiekty, materiały, światło i kamery, a potem renderuje.",
  dlaczego="Pozwala robić fotorealistyczne, powtarzalne rendery z prawdziwego modelu 3D zamiast obrazów generowanych przez AI, które zmieniają się przy każdej próbie.",
  kroki=["Blender trzeba zainstalować na komputerze bota (na Linuksie: także tryb bez okna, z bpy).","Wtyczka MCP działa w Blenderze z interfejsem, więc dodanie jej jako konektora to osobny krok.","Prostsza droga: agent pisze skrypty bpy i renderuje GLB bez okna."],
  prompt="Oceń, czy na Twoim komputerze da się uruchomić Blendera (najlepiej bez okna, przez bpy) i wyrenderować salon z projekt-domu/3d/parter-g2-v2.glb z kamerą jak w wizualizacji v1. Opisz, co dałby Blender MCP (https://github.com/ahujasid/mcp-for-blender) w porównaniu ze skryptami bpy. Nic nie instaluj, dopóki nie zatwierdzę planu."),
 dict(repo="EL4CTEO/blender-skills", kategoria="Skille", nazwa="Blender Skills (Blender 5.2)", ocena=7, trudnosc="średnia",
  opis="Zestaw skilli z profesjonalnymi workflow Blendera: modelowanie, materiały, oświetlenie i renderowanie.",
  dlaczego="Uzupełnia Blender MCP: agent wie, jak ustawić światło dzienne, materiały PBR i kamerę, żeby rendery wnętrz wyglądały realistycznie.",
  kroki=["Agent czyta skille o oświetleniu, materiałach i renderze.","Wybiera te dotyczące wnętrz.","Stosuje je w skryptach renderujących."],
  prompt="Przejrzyj https://github.com/EL4CTEO/blender-skills i wybierz skille przydatne do renderów wnętrz: światło dzienne, materiały PBR (drewno, płytki, tkaniny), kamera we wnętrzu. Streść mi je po polsku i zaproponuj, jak użyć ich przy wizualizacjach Projektu Domu."),
 dict(repo="grimashevich/sweethome3d-mcp-server", kategoria="Serwery MCP", nazwa="Sweet Home 3D MCP", ocena=7, trudnosc="trudna",
  opis="Wtyczka do Sweet Home 3D (darmowy program do projektowania wnętrz) z wbudowanym serwerem MCP: ściany, meble, wymiary, rendery zdjęć.",
  dlaczego="Sweet Home 3D to standard amatorskiego projektowania wnętrz, z biblioteką mebli i eksportem do OBJ. Agent mógłby budować w nim dom pokój po pokoju. Repo ma jednak mało gwiazdek.",
  kroki=["Sweet Home 3D (Java) i wtyczkę instaluje się na komputerze bota, który ma pulpit.","Agent łączy się z http://127.0.0.1:9877/mcp.","Na start buduje jeden pokój z pomieszczenia.json."],
  prompt="Oceń, czy można uruchomić Sweet Home 3D z wtyczką https://github.com/grimashevich/sweethome3d-mcp-server na Twoim komputerze (Linux z pulpitem) i zbudować w nim pokój 2-06 z projekt-domu/pomieszczenia.json. Najpierw pokaż mi plan i ryzyka, nic jeszcze nie instaluj."),
 dict(repo="datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR", kategoria="Dane", nazwa="DDC CWICR – otwarta baza kosztów budowlanych", ocena=6, trudnosc="średnia",
  opis="Wielojęzyczna baza kosztów budowlanych dla agentów AI: ponad 55 tys. pozycji robót i 27 tys. zasobów, z API. Wśród kolekcji językowych jest wersja polska (Warszawa).",
  dlaczego="Daje drugie źródło stawek do sprawdzenia wyceny. Trzeba jednak zweryfikować, skąd pochodzą stawki dla Polski, i licencję danych (osobna licencja DDC).",
  kroki=["Agent czyta README i DATA_DICTIONARY.","Sprawdza polską kolekcję i licencję danych.","Porównuje kilka pozycji z wyceną (np. ławy, ściany)."],
  prompt="Przeczytaj https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR (README, DATA_DICTIONARY, polska kolekcja). Sprawdź licencję danych i skąd pochodzą stawki dla Polski. Potem porównaj 5 pozycji z projekt-domu/02-wycena-budowy.csv (ławy, ściany Porotherm, strop, tynki, wylewki) i pokaż różnice w tabeli."),
 dict(repo="neka-nat/freecad-mcp", kategoria="Serwery MCP", nazwa="FreeCAD MCP", ocena=5, trudnosc="trudna",
  opis="Serwer MCP do FreeCAD-a, darmowego parametrycznego programu CAD: agent tworzy i edytuje bryły 3D i odczytuje ich wymiary.",
  dlaczego="Przydatny do precyzyjnych elementów na wymiar, np. schodów, zabudowy szafy czy mebli kuchennych. Do całego domu prostsze będą Blender albo Sweet Home 3D.",
  kroki=["FreeCAD i dodatek MCP instaluje się na komputerze bota.","Agent modeluje jeden element na wymiar.","Eksportuje do STEP/DXF dla stolarza."],
  prompt="Oceń, czy przy pomocy FreeCAD MCP (https://github.com/neka-nat/freecad-mcp) lub skryptów FreeCAD w Pythonie na Twoim komputerze możesz zaprojektować na wymiar zabudowę garderoby 2/04 z Projektu Domu i wyeksportować rysunek dla stolarza. Pokaż plan, nic jeszcze nie instaluj."),

 dict(repo="donmccurdy/glTF-Transform", kategoria="Narzędzia CLI", nazwa="glTF-Transform – kompresja GLB do spaceru", ocena=9, trudnosc="łatwa",
  opis="Biblioteka i CLI do obróbki plików glTF/GLB: optymalizacja, kompresja geometrii (meshopt, Draco) i tekstur (KTX2, WebP), usuwanie duplikatów.",
  dlaczego="Model z wypieczonym światłem jest ciężki. Jedna komenda optimize zmniejsza go wielokrotnie, więc spacer szybciej się ładuje na iPhonie.",
  kroki=["Agent uruchamia CLI przez npx na swoim komputerze.","Kompresuje GLB (meshopt + KTX2 lub WebP).","Porównuje rozmiar i wygląd przed i po."],
  prompt="Użyj glTF-Transform (https://github.com/donmccurdy/glTF-Transform), żeby zoptymalizować GLB spaceru: npx @gltf-transform/cli optimize wejscie.glb wyjscie.glb --compress meshopt --texture-compress ktx2 (bez narzędzia ktx użyj webp). Pokaż tabelę rozmiarów przed i po oraz zrzut z three.js, żeby sprawdzić, czy lightmapy nie straciły jakości. W three.js dodaj MeshoptDecoder i KTX2Loader."),
 dict(repo="mistic100/Photo-Sphere-Viewer", kategoria="Dashboardy HTML", nazwa="Photo Sphere Viewer – panoramy 360 z hotspotami", ocena=9, trudnosc="łatwa",
  opis="Biblioteka JS do panoram 360 z wtyczkami: Virtual Tour (przejścia między punktami), Markers (hotspoty), Gyroscope, Map i Plan.",
  dlaczego="Panoramy z Cycles zamienia w spacer od pokoju do pokoju z hotspotami i żyroskopem na iPhonie. Działa na statycznej stronie.",
  kroki=["Agent kopiuje pliki biblioteki do repo (bez CDN).","Opisuje w JSON punkty: panorama, połączenia, hotspoty.","Testuje na widoku iPhone'a."],
  prompt="Zbuduj tour panoram 360 na Photo Sphere Viewer (https://github.com/mistic100/Photo-Sphere-Viewer) z wtyczkami virtual-tour, markers i gyroscope. Pliki biblioteki skopiuj do repo strony, bez CDN. Punkty i przejścia między pokojami opisz w tour.json, a na każdej panoramie dodaj hotspoty z nazwą materiału. Sprawdź na iPhonie 390×844."),
 dict(repo="sparkjsdev/spark", kategoria="Dashboardy HTML", nazwa="Spark – Gaussian splatting w three.js", ocena=7, trudnosc="trudna",
  opis="Renderer Gaussian splattingu dla three.js: wyświetla fotorealistyczne sceny ze splatów (.ply, .spz, .splat) razem ze zwykłymi obiektami 3D.",
  dlaczego="Daje fotorealizm, którego nie da zwykły GLB. Splat trzeba jednak najpierw wytrenować z wielu renderów (np. gsplat na GPU NVIDIA).",
  kroki=["Agent sprawdza, czy ma GPU do treningu splatów.","Na początek testuje Spark z przykładowym splatem.","Ocenia płynność i wagę pliku na iPhonie."],
  prompt="Oceń Spark (https://github.com/sparkjsdev/spark) do spaceru po domu: zrób testową stronę three.js z przykładowym splatem z repo i joystickiem, a potem zmierz FPS i rozmiar pliku w widoku iPhone'a. Opisz, jak z renderów Cycles z wielu kamer zrobić własny splat (np. gsplat, Apache-2.0, wymaga GPU NVIDIA) i czy da się to zrobić na Twoim komputerze."),
 dict(repo="gkjohnson/three-mesh-bvh", kategoria="Narzędzia CLI", nazwa="three-mesh-bvh – kolizje do chodzenia FPS", ocena=8, trudnosc="średnia",
  opis="Szybki raycasting i kolizje dla three.js (BVH). W repo jest przykład characterMovement z kapsułą gracza.",
  dlaczego="Dzięki niemu chodzenie joystickiem nie przechodzi przez ściany i meble, a działa płynnie na telefonie. Dobrze łączy się z joystickiem nipplejs (MIT).",
  kroki=["Agent czyta przykład characterMovement.","Dodaje kolizje kapsuły z modelem domu.","Łączy je z joystickiem nipplejs."],
  prompt="Na podstawie przykładu characterMovement z https://github.com/gkjohnson/three-mesh-bvh dodaj do spaceru three.js kolizje kapsuły gracza (wysokość oczu 1,65 m) ze ścianami i meblami. Do chodzenia użyj joysticka nipplejs (https://github.com/yoannmoinet/nipplejs, MIT), a do rozglądania przeciągania prawą stroną ekranu. Bibliotek nie ładuj z CDN, a całość przetestuj w widoku iPhone'a."),
]
def projekt_domu_items():
    out=[]
    for e in PD:
        g=gh(e['repo']); url=e.get('url') or g['url']
        it=dict(e); it.update(g); it['url']=url
        if e.get('licencja_stala'): it['licencja']=e['licencja_stala']
        it.pop('licencja_stala',None)
        it['id']="pd__"+e['repo'].replace('/','__'); it['tagi']=["Projekt Domu"]; it['zrodlo']="GitHub"; it['top']=False
        out.append(it)
    return out
PD_TOP=["pd__google__model-viewer","pd__donmccurdy__glTF-Transform","pd__mistic100__Photo-Sphere-Viewer","pd__frappe__gantt","pd__mozman__ezdxf"]
