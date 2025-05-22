Ez egy útmutató ahhoz, hogy hogyan csinálj saját bejelentkezési, regisztrációs és jelszóemlékeztetési felületet.


1. Töltsd le ezt a repo-t egy zip fájlban, tömörítsd ki és nyisd meg egy mappában azt a könyvtárat, ahol a manage.py is van.
2. Hozz létre egy virtuális környezetet és telepítsd a szükséges csomagokat a requirements.txt-ből
    ```ps1
    py -m virtualenv venv
    pip install -r requirements.txt
    ```
3. Nyisd meg VSCode-dal azt a mappát, ahol a manage.py is van.
4. Hozz létre egy ``.gitignore`` fájlt ezzel a tartalommal:
   ```
   db.sqlite3
   local_settings.py
   venv/
   ```
5. Érzékeny adatokról való gondoskodás: 
    1. Írd át a ``ird_at_erre_hogy_local_settings.py`` fájlt arra, hogy ``local_settings.py``.
    2. Nyisd meg a ``local_settings.py˙˙-t és töltsd ki a te adataiddal.
    3. A ``settings.py``-ban görgess le a fájl aljára és szedd ki a local_settings.py-ról szóló kommentelést. Tehát ezt:
        ```py 
        # import local_settings

        # EMAIL_HOST = local_settings.EMAIL_HOST
        # EMAIL_HOST_USER = local_settings.EMAIL_HOST_USER
        # EMAIL_HOST_PASSWORD = local_settings.EMAIL_HOST_PASSWORD
        # DEFAULT_FROM_EMAIL = local_settings.DEFAULT_FROM_EMAIL
        # EMAIL_PORT = local_settings.EMAIL_PORT
        # EMAIL_USE_TLS = local_settings.EMAIL_USE_TLS
        ```
        Cseréld ki erre: 
        ```py

        import local_settings

        EMAIL_HOST = local_settings.EMAIL_HOST
        EMAIL_HOST_USER = local_settings.EMAIL_HOST_USER
        EMAIL_HOST_PASSWORD = local_settings.EMAIL_HOST_PASSWORD
        DEFAULT_FROM_EMAIL = local_settings.DEFAULT_FROM_EMAIL
        EMAIL_PORT = local_settings.EMAIL_PORT
        EMAIL_USE_TLS = local_settings.EMAIL_USE_TLS
        ```
6. Most már létrehozhatsz egy gitrepot VSCODE-ban, és feltöltheted az adatokat GitHubra. A ``local_settings.py``-ban tárolt érzékeny adatok nem fognak felkerülni a GitHubra, mivel a ``.gitignore`` fájl tartalmazza a fájl nevét. Innentől már futtatható a projekt.
7. Most már személyre szabhatod az autentikációt a template-ek átírásával. 
    - A **regisztrációról** szóló részeket az ``app_reg/templates/registration`` mappában találod.
    - A **bejelentkezésről** és az **elfelejtett jelszóról** szóló részeket (beleértve az email tartalmát) a ``global_templates/registration/`` mappában találod.
    - A bejelentkezési és regisztrációs template-ekhez tartozó **stíluslapok** mind az  ``app_reg/static/registration/registration.css`` stílusfájlban találhatók (ami most üres.)
8. Kis segítség még: Az ``app_reg/templates/registration`` mappában találsz egy kijelentkezést tartalmazó ``kijelentkezes.html``-t, amit bármely html-template-be beilleszthetsz és kijelentkezési gombként használhatsz. Ezt bármely template-ben a következővel tudsz beimportálni:
```django
    {% include "registration/kijelentkezes.html" %}
```
vagy ha azt akarod, hogy csak akkor legyen ott, ha az illető be is van jelentkezve, 
```django
{% if request.user.is_authenticated %}
    {% include "registration/kijelentkezes.html" %}
{% endif %}
```
