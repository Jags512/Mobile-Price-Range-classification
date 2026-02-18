import pandas as pd
import cloudpickle
import gradio as gr

# Load model safely
try:
    with open("mobile_price_model (1).pkl", "rb") as f:
        model = cloudpickle.load(f)
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")


def predict_price(*inputs):
    columns = [
        "battery_power","blue","clock_speed","dual_sim","fc","four_g",
        "int_memory","m_dep","mobile_wt","n_cores","pc",
        "px_height","px_width","ram","sc_h","sc_w",
        "talk_time","three_g","touch_screen","wifi"
    ]

    data = pd.DataFrame([inputs], columns=columns)

    # Type casting
    data = data.astype({
        "blue": int,
        "dual_sim": int,
        "four_g": int,
        "three_g": int,
        "touch_screen": int,
        "wifi": int,
        "n_cores": int,
    })

    prediction = model.predict(data)[0]

    labels = {
        0: "Low Cost",
        1: "Medium Cost",
        2: "High Cost",
        3: "Very High Cost",
    }

    return labels.get(prediction, "Unknown")


inputs = [
    gr.Number(label="Battery Power"),
    gr.Radio([0, 1], label="Blue"),
    gr.Number(label="Clock Speed"),
    gr.Radio([0, 1], label="Dual SIM"),
    gr.Number(label="Front Camera"),
    gr.Radio([0, 1], label="4G"),
    gr.Number(label="Internal Memory"),
    gr.Number(label="Mobile Depth"),
    gr.Number(label="Mobile Weight"),
    gr.Number(label="Number of Cores"),
    gr.Number(label="Primary Camera"),
    gr.Number(label="Pixel Height"),
    gr.Number(label="Pixel Width"),
    gr.Number(label="RAM"),
    gr.Number(label="Screen Height"),
    gr.Number(label="Screen Width"),
    gr.Number(label="Talk Time"),
    gr.Radio([0, 1], label="3G"),
    gr.Radio([0, 1], label="Touch Screen"),
    gr.Radio([0, 1], label="WiFi"),
]

demo = gr.Interface(
    fn=predict_price,
    inputs=inputs,
    outputs=gr.Textbox(label="Predicted Price Range"),
    title="📱 Mobile Price Prediction",
    description="Predict the price range of a mobile phone based on its specifications.",
    examples=[
        [1000,1,2.2,1,5,1,32,0.5,150,4,12,800,1200,3000,15,7,20,1,1,1]
    ]
)

demo.launch()

