import sys
import pandas as pd
import json

if len(sys.argv) < 2:
    print("❌ Debes proporcionar el archivo JSON de entrada.")
    print("Uso: docker run --rm -v $(pwd):/data json-to-csv input.json output.csv")
    sys.exit(1)

input_file = f"/data/{sys.argv[1]}"
output_file = f"/data/{sys.argv[2]}" if len(sys.argv) > 2 else "/data/output.csv"

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    df.to_csv(output_file, index=False)
    print(f"✅ CSV creado en: {output_file}")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
