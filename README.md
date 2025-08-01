# 🧩 JSON to CSV CLI (sin instalación)

Convierte cualquier archivo `.json` a `.csv` desde la terminal usando **Docker**, sin necesidad de instalar Node.js, Python ni dependencias.

---

## ✅ Requisitos

- Tener instalado [Docker Desktop](https://www.docker.com/products/docker-desktop)

---

## 🚀 Cómo usar

### 1. Coloca tu archivo `data.json` en una carpeta local

Ejemplo de contenido (`data.json`):

```json
[
  { "name": "Alice", "age": 30, "email": "alice@example.com" },
  { "name": "Bob", "age": 25, "email": "bob@example.com" },
  { "name": "Charlie", "age": 35, "email": "charlie@example.com" }
]
```

---

### 2. Ejecuta el siguiente comando según tu sistema

#### 🐧 Linux / macOS:

```bash
docker run --rm -v "$(pwd)":/data json-to-csv data.json resultado.csv
```

#### 🪟 Windows PowerShell:

```powershell
docker run --rm -v "${PWD}:/data" json-to-csv data.json resultado.csv
```

#### 🪟 Windows CMD:

```cmd
docker run --rm -v "%cd%:/data" json-to-csv data.json resultado.csv
```

---

## 🔨 ¿Cómo se construye la imagen?

(Este paso lo haces solo una vez)

```bash
docker build -t json-to-csv .
```

---

## 📦 ¿Qué hace?

- Lee el archivo `data.json`
- Convierte el contenido a CSV
- Genera `resultado.csv` en la misma carpeta

---

## 💡 Nota

Este conversor funciona si el JSON es un arreglo de objetos, como:

```json
[
  { "clave": "valor1" },
  { "clave": "valor2" }
]
```

---

## 📃 Licencia

MIT