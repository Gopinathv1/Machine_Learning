import gradio as gr
import numpy as np

# ---------------------------------------------------------
# Mock prediction function
# Replace this with your actual model inference logic
# ---------------------------------------------------------
def predict_digit(image_dict):
    """
    image_dict contains 'background', 'layers', 'composite'
    'composite' is a numpy array of shape (H, W, 4) for RGBA
    """
    # Extract the image array from the dictionary that Gradio's new ImageEditor returns
    if image_dict is None or "composite" not in image_dict:
        return "No image drawn"
        
    image = image_dict["composite"]
    
    # In a real scenario, you would preprocess the image here.
    # For MNIST, you typically want a 28x28 grayscale image.
    # The Gradio canvas usually gives RGBA, so you'd extract the alpha channel
    # or convert to grayscale, then resize to 28x28.
    # 
    # Example preprocessing (pseudo-code):
    # import cv2
    # gray = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
    # resized = cv2.resize(gray, (28, 28))
    # tensor = resized.reshape(1, 28, 28, 1) / 255.0
    # prediction = model.predict(tensor)
    # return str(np.argmax(prediction))
    
    # For now, return a random digit for demonstration
    predicted_digit = np.random.randint(0, 10)
    
    # You can return a dictionary of confidences for a more visual output:
    # return {str(i): float(i == predicted_digit) for i in range(10)}
    return str(predicted_digit)


# Create the Gradio Interface
with gr.Blocks(title="MNIST Digit Recognizer") as demo:
    gr.Markdown("# 🎨 MNIST Digit Recognizer")
    gr.Markdown("Draw a single digit (0-9) on the canvas below and click **Predict**.")
    
    with gr.Row():
        with gr.Column():
            # Gradio 4.x uses ImageEditor for drawing
            sketchpad = gr.ImageEditor(
                type="numpy",
                image_mode="RGBA",
                crop_size=(280, 280),
                label="Draw here",
                brush=gr.Brush(colors=["#FFFFFF"], default_size=15), # White brush on transparent/black
            )
            predict_btn = gr.Button("Predict", variant="primary")
            
        with gr.Column():
            output_label = gr.Label(label="Prediction", num_top_classes=3)
            
    # Link the button to the prediction function
    predict_btn.click(
        fn=predict_digit,
        inputs=sketchpad,
        outputs=output_label
    )

if __name__ == "__main__":
    # Launch the Gradio app
    # Set share=True to create a public link to deploy temporarily
    demo.launch(share=False)
