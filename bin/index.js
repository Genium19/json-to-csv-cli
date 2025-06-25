#!/usr/bin/env node
import fs from 'fs';
import { parse } from 'json2csv';

const inputPath = process.argv[2];
const outputPath = process.argv[3] || 'output.csv';

if (!inputPath) {
  console.error('❌ Debes proporcionar un archivo JSON de entrada.');
  console.error('Ejemplo: json-to-csv archivo.json salida.csv');
  process.exit(1);
}

try {
  const jsonData = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
  const csv = parse(jsonData);
  fs.writeFileSync(outputPath, csv);
  console.log(`✅ CSV creado en: ${outputPath}`);
} catch (err) {
  console.error('❌ Error:', err.message);
  process.exit(1);
}
