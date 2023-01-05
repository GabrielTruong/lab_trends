# Deploy an app on deta

With this project we want to deploy an app on deta that displays the trends of two keywords using the `pytrends` library. 

## Getting Started

**Create a conda environment**
```bash
create -n ENVNAME --file requirements.txt
```

**Run locally**
```bash
python main.py
```

**Deploy on deta (need account)**
```bash
deta deploy
```

You can find the app on: 
https://vly79t.deta.dev/chart