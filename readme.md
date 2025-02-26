# Vietnamese Poem Generation with GPT-2

This Streamlit application allows users to generate Vietnamese poems using a pre-trained GPT-2 model. The model is fine-tuned on a dataset of Vietnamese poems and is capable of generating creative and contextually relevant verses.

## Features

*   **Interactive Interface:** A user-friendly Streamlit interface for easy interaction.
*   **Customizable Generation:** Users can provide a starting phrase or sentence and adjust various generation parameters like temperature, top-k, top-p, and repetition penalty.
*   **Parameter Tuning:** Fine-tune the generation process by adjusting `temperature`, `top-k`, `top-p`, and `repetition_penalty` to achieve desired results.
*   **Clear Output:** Displays the generated poem in a readable format, line by line.
*   **Error Handling:** Includes error handling to gracefully manage exceptions during poem generation.
*   **Footer Attribution:** Clear attribution to AI Vietnam and the original developer with a link to the GitHub repository.
*   **Instructional Expander:** Provides helpful instructions on how to use the application effectively.

## Usage

1.  **Input Prompt:** Enter a few words or a sentence as a starting point for the poem in the text area.
2.  **Adjust Parameters:**
    *   **Max Output Tokens:** Set the maximum length of the generated poem.
    *   **Temperature:** Control the randomness of the generated text. Higher values lead to more diverse and unexpected results.
    *   **Top-k:** Limit the number of most likely next words considered at each step.
    *   **Top-p:**  Set a probability threshold, selecting the smallest set of words whose cumulative probability exceeds the threshold.
    *   **Repetition Penalty:**  Penalize repeated words to encourage more diverse text.
3.  **Generate Poem:** Click the "Sinh thơ" (Generate Poem) button to generate the poem based on the provided input and parameters.
4.  **View and Download:** The generated poem will be displayed on the screen.

## Model

*   The application uses the `thangduong0509/gpt2_viet_poem_generation` GPT-2 model, which has been trained specifically for generating Vietnamese poetry.

## Setup

1.  **Install Dependencies:**

    ```bash
    pip install streamlit transformers
    ```

2.  **Run the Application:**

    ```bash
    streamlit run app.py
    ```

## Credits

*   Developed by [Koii2k3(https://github.com/Koii2k3/Poem-Generation) for AI Vietnam.
*   GPT-2 Model: `thangduong0509/gpt2_viet_poem_generation`