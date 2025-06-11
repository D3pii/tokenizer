# Set up
1. installeer uv
2. download en ga naar deze map
3. run het volgende commando, afhankelijk van het platform:

**MacOS/ Linux**
```sh
source .venv/bin/activate
```
**Windows**
```powershell
.venv\Scripts\activate
```

4. installeer de benodigde packages doormiddel van het volgende command

```sh
uv sync
```

5. Zet het aantal rijen een toepasselijke woorden in een python dictionary formaat en zet deze in de data variabele (rij 17)

```python
    data = {"150": 10465, "250": 18038, "350": 27405}  
```

6. run de code door
```sh
uv run main.py
```

