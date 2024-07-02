# Epicsmash - Prioritize Anything

Epicsmash is an interactive tool designed to help you prioritize anything, from product epics to tasks or ideas, using a merge sort algorithm with a human-in-the-loop approach for comparisons. Built with Streamlit, this application allows you to input a list of items and manually compare them to determine their relative importance.

## Features

- **Interactive Comparison**: Manually compare pairs of items to decide which is more important.
- **Merge Sort Algorithm**: Utilizes a merge sort algorithm to efficiently sort items based on your inputs.
- **Caching**: Avoid redundant comparisons by caching previous decisions.
- **Detailed Logs**: View logs of the sorting process to understand the decisions made at each step.

## Installation

To run Epicsmash locally, you'll need to have Python and Streamlit installed. Follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/epicsmash.git
    cd epicsmash
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Streamlit**:
    ```bash
    pip install streamlit
    ```

4. **Run the application**:
    ```bash
    streamlit run epicsmash.py
    ```

## Usage

1. **Enter your items**: Input your items in the text area provided, with each item on a new line.
2. **Begin the process**: Click the "Begin" button to start the sorting process.
3. **Compare items**: For each step, choose which item is more important from the pair shown.
4. **View results**: Once all comparisons are complete, view the sorted list of items and the log of decisions.

## Example

After starting the application and entering your items, you will be prompted to compare pairs of items. The app will guide you through each comparison, caching your decisions to optimize the process. Once all comparisons are made, you will see a sorted list of your items based on your inputs.

## Contributing

We welcome contributions to improve Epicsmash! Please fork the repository and submit pull requests.

1. Fork the repo.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the Streamlit team for providing an excellent framework for building interactive web applications with Python.

---

Feel free to reach out if you have any questions or need further assistance!

