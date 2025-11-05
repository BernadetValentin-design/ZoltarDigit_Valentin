import os
import time
from datetime import datetime

configs = [
    {
        "name": "Config 1 - Baseline",
        "STEPS": 100,
        "BATCH": 512,
        "LR": 0.02,
        "LR_DECAY": 0.9,
        "PATIENCE": 50
    },
    {
        "name": "Config 2 - Plus d'entrainement",
        "STEPS": 200,
        "BATCH": 512,
        "LR": 0.02,
        "LR_DECAY": 0.9,
        "PATIENCE": 50
    },
    {
        "name": "Config 3 - Learning rate eleve",
        "STEPS": 100,
        "BATCH": 512,
        "LR": 0.05,
        "LR_DECAY": 0.9,
        "PATIENCE": 50
    },
    {
        "name": "Config 4 - Learning rate bas",
        "STEPS": 100,
        "BATCH": 512,
        "LR": 0.01,
        "LR_DECAY": 0.9,
        "PATIENCE": 50
    },
    {
        "name": "Config 5 - Batch size petit",
        "STEPS": 100,
        "BATCH": 256,
        "LR": 0.02,
        "LR_DECAY": 0.9,
        "PATIENCE": 50
    },
    {
        "name": "Config 6 - Batch size grand",
        "STEPS": 100,
        "BATCH": 1024,
        "LR": 0.02,
        "LR_DECAY": 0.9,
        "PATIENCE": 50
    },
    {
        "name": "Config 7 - Configuration optimisee",
        "STEPS": 200,
        "BATCH": 512,
        "LR": 0.03,
        "LR_DECAY": 0.9,
        "PATIENCE": 50
    },
    {
        "name": "Config 8 - Configuration agressive",
        "STEPS": 150,
        "BATCH": 256,
        "LR": 0.05,
        "LR_DECAY": 0.8,
        "PATIENCE": 30
    }
]

print("=" * 70)
print("DEMARRAGE DES TESTS AUTOMATIQUES - CNN")
print("=" * 70)
print(f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Nombre de configurations : {len(configs)}")
print("=" * 70)
print()

log_file = "cnn_results_log.txt"
with open(log_file, "w", encoding="utf-8") as f:
    f.write("# LOG DES RESULTATS CNN\n")
    f.write(f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

results = []

for i, config in enumerate(configs, 1):
    print("\n" + "=" * 70)
    print(f"TEST {i}/{len(configs)} : {config['name']}")
    print("=" * 70)
    
    print("Parametres :")
    for key, value in config.items():
        if key != "name":
            print(f"   - {key:12} = {value}")
    print()
    
    os.environ["JIT"] = "1"
    for key, value in config.items():
        if key != "name":
            os.environ[key] = str(value)
    
    print("Entrainement en cours...")
    start_time = time.time()
    
    exit_code = os.system("python mnist_convnet.py")
    
    duration = time.time() - start_time
    
    result = {
        "config_num": i,
        "name": config["name"],
        "params": {k: v for k, v in config.items() if k != "name"},
        "duration": duration,
        "success": exit_code == 0
    }
    results.append(result)
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Config {i}: {config['name']}\n")
        f.write(f"{'='*60}\n")
        for key, value in config.items():
            if key != "name":
                f.write(f"{key}: {value}\n")
        f.write(f"Duree: {duration:.1f} secondes\n")
        f.write(f"Statut: {'Succes' if exit_code == 0 else 'Echec'}\n")
    
    if exit_code == 0:
        print(f"\nConfig {i} terminee en {duration:.1f} secondes")
    else:
        print(f"\nConfig {i} a echoue (code: {exit_code})")
    
    print("=" * 70)
    
    if i < len(configs):
        print("\nPause de 2 secondes...\n")
        time.sleep(2)

print("\n" + "=" * 70)
print("TOUS LES TESTS CNN SONT TERMINES")
print("=" * 70)
print(f"\nResume :")
print(f"   Succes : {sum(1 for r in results if r['success'])}/{len(results)}")
print(f"   Temps total : {sum(r['duration'] for r in results):.1f} secondes")
print(f"\nLes resultats detailles sont dans : {log_file}")