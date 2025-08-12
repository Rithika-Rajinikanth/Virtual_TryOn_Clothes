import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

# --- Configuration Paths ---
# IMPORTANT: Adjust these paths if your project structure changes
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Points to VITON-HD/
DATASETS_DIR = os.path.join(BASE_DIR, 'datasets')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

TEST_PAIRS_FILE = os.path.join(DATASETS_DIR, 'test_pairs.txt') # Corrected path

@app.route('/')
def index():
    image_pairs = []
    try:
        with open(TEST_PAIRS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    person_img_name = parts[0]
                    cloth_img_name = parts[1]

                    # Assuming generated image name is person_image_name_0.jpg (e.g., 00000_0.jpg)
                    # Adjust this logic if your generated image names differ
                    generated_img_name = person_img_name.replace('.jpg', '_0.jpg')

                    # Construct URLs for static assets
                    person_img_url = url_for('static', filename=f'images/people/{person_img_name}')
                    cloth_img_url = url_for('static', filename=f'images/clothes/{cloth_img_name}')
                    generated_img_url = url_for('static', filename=f'images/generated/{generated_img_name}')

                    # Check if generated image exists before adding to list
                    # This prevents broken images if results are incomplete
                    if os.path.exists(os.path.join(RESULTS_DIR, generated_img_name)):
                        image_pairs.append({
                            'person_img': person_img_url,
                            'cloth_img': cloth_img_url,
                            'generated_img': generated_img_url,
                            'id': person_img_name.replace('.jpg', '') # Unique ID for JS targeting
                        })
                    else:
                        print(f"Warning: Generated image not found for {person_img_name} -> {generated_img_name}")

    except FileNotFoundError:
        print(f"Error: {TEST_PAIRS_FILE} not found. Please ensure it exists.")
        return "Error: test_pairs.txt not found. Check server logs."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An internal server error occurred."

    return render_template('index.html', image_pairs=image_pairs)

if __name__ == '__main__':
    # You can change the port if needed, e.g., port=8000
    app.run(debug=True, port=5000)