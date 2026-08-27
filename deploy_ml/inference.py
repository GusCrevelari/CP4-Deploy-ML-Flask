from flask import Flask, request, jsonify
import os
import pickle
import joblib
import pandas as pd

app = Flask(__name__)


def load_model():
    """Try to load a saved model using joblib or pickle.
    Looks for commonly saved filenames and returns the loaded model.
    """
    candidates = [
        "wine_random_forest_model.pkl",
        "wine_svm_model.pkl",
        "wine_random_forest_model.joblib",
        "model.pkl",
    ]

    for fname in candidates:
        if os.path.exists(fname):
            try:
                return joblib.load(fname)
            except Exception:
                with open(fname, "rb") as f:
                    return pickle.load(f)

    raise FileNotFoundError("No model file found. Expected one of: {}".format(candidates))


def preprocess_input(data):
    """Convert incoming JSON to a DataFrame and apply minimal preprocessing.

    - Accepts either a single dict (one sample) or a list of dicts (multiple samples).
    - If a `type` categorical field is provided (e.g. 'red'/'white'), it creates
      the `type_white` column matching the training notebook (drop_first=True -> single column).
    - Raises ValueError if required numeric features are missing.
    """
    # normalize input to list of records
    if isinstance(data, dict):
        records = [data]
    elif isinstance(data, list):
        records = data
    else:
        raise ValueError("Input JSON must be an object or an array of objects")

    df = pd.DataFrame.from_records(records)

    # Handle 'type' categorical -> create 'type_white' if needed
    if "type" in df.columns and "type_white" not in df.columns:
        df["type_white"] = df["type"].apply(lambda v: 1 if str(v).lower() == "white" else 0)
        df = df.drop(columns=["type"])

    # Ensure numeric columns are numeric when possible
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass

    return df


modelo = None
try:
    modelo = load_model()
except Exception as e:
    # model will be loaded lazily on first request if not present at import time
    modelo = None
    load_error = str(e)
else:
    load_error = None


@app.route("/predict", methods=["POST"])
def predict():
    global modelo
    if modelo is None:
        try:
            modelo = load_model()
        except Exception as e:
            return jsonify({"error": "Model not available", "details": str(e)}), 500

    try:
        dados = request.get_json()
        df = preprocess_input(dados)
    except ValueError as e:
        return jsonify({"error": "Invalid input", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Failed to parse input", "details": str(e)}), 400

    try:
        pred = modelo.predict(df)
        result = {"prediction": [int(x) for x in pred.tolist()]}

        # include probabilities if available
        if hasattr(modelo, "predict_proba"):
            probs = modelo.predict_proba(df)
            result["probabilities"] = probs.tolist()

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)