import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Keep house_price_model.pkl in the same folder as this app.py file.
MODEL_PATH = Path(__file__).parent / "house_price_model.pkl"

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

st.title("🏠 House Price Predictor")
st.write(
    "Enter the property details below to estimate its price using your "
    "trained Linear Regression pipeline."
)

try:
    model = load_model()
except FileNotFoundError:
    st.error(
        "Model file not found. Put 'house_price_model.pkl' in the same "
        "folder as app.py, then restart the app."
    )
    st.stop()
except Exception as exc:
    st.error(f"Could not load the model: {exc}")
    st.stop()

st.info(
    "The inputs below are generated from the features stored in your "
    "saved scikit-learn pipeline. Check that the values and categories "
    "match the data used to train your model."
)

# Read the original training feature names from the saved pipeline.
try:
    preprocessor = model.named_steps["preprocessor"]
    transformers = preprocessor.transformers_
except Exception:
    st.error(
        "This app expects the saved Pipeline to contain a "
        "'preprocessor' step, as in your training code."
    )
    st.stop()

numeric_features = []
categorical_features = []
categorical_choices = {}

for name, transformer, columns in transformers:
    if name == "num" and columns is not None:
        numeric_features = list(columns)
    elif name == "cat" and columns is not None:
        categorical_features = list(columns)
        try:
            encoder = transformer
            categorical_choices = {
                col: [str(v) for v in values]
                for col, values in zip(categorical_features, encoder.categories_)
            }
        except Exception:
            categorical_choices = {}

# Create one input control for every feature, retaining training column names.
user_values = {}
with st.form("house_details"):
    st.subheader("Property Details")
    for feature in numeric_features:
        user_values[feature] = st.number_input(
            feature.replace("_", " ").title(),
            value=0.0,
            step=1.0,
            format="%.2f",
            help=f"Enter a value for the '{feature}' feature."
        )

    for feature in categorical_features:
        options = categorical_choices.get(feature, [])
        if options:
            user_values[feature] = st.selectbox(
                feature.replace("_", " ").title(),
                options=options
            )
        else:
            user_values[feature] = st.text_input(
                feature.replace("_", " ").title()
            )

    submitted = st.form_submit_button("Predict House Price", type="primary")

if submitted:
    # Use exactly the same feature names/order as the training data.
    feature_order = numeric_features + categorical_features
    input_df = pd.DataFrame(
        [{feature: user_values[feature] for feature in feature_order}],
        columns=feature_order
    )

    try:
        predicted_price = float(model.predict(input_df)[0])
        st.subheader("Estimated House Price")
        st.success(f"{predicted_price:,.2f}")
        st.caption(
            "This is a model estimate, not a guaranteed market price. "
            "The result uses the currency/units of the target 'price' "
            "column in your training dataset."
        )
        with st.expander("View input sent to the model"):
            st.dataframe(input_df, use_container_width=True)
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
        st.write(
            "Check that the model file was created from the same training "
            "code and that all required input features are available."
        )
