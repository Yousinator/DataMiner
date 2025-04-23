<br/>
<p align="center">

  <h1 align="center">DataMiner</h1>

  <p align="center">
    A Data Mining application that lets you explore and visualize student bios and certifications through two AI-powered assistants: TextMiner  and GraphMiner for using Streamlit for UI.
    <br/>
    <br/>
    <a href="https://github.com/Yousinator/DataMiner/issues">Report Bug</a>
    .
    <a href="https://github.com/Yousinator/DataMiner/issues">Request Feature</a>
  </p>
</p>
<p align="center">
  <a href="">
<img src="https://img.shields.io/github/downloads/Yousinator/DataMiner/total"> <img src ="https://img.shields.io/github/contributors/Yousinator/DataMiner?color=dark-green"> <img src ="https://img.shields.io/github/forks/Yousinator/DataMiner?style=social"> <img src ="https://img.shields.io/github/stars/Yousinator/DataMiner?style=social"> <img src ="https://img.shields.io/github/license/Yousinator/DataMiner">
  </a>
</p>

## Table Of Contents

- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## About The Project

This tool allows users to:

- 💬 **Chat with the TextMiner** to semantically search student bios using NLP.
- 📊 **Chat with the GraphMiner** to generate interactive graphs of relationships based on either student names or certifications.

It's designed for educators, administrators, and data explorers who want to interactively analyze educational data.

## Built With

This tech stack powers the dynamic chat interface and graph-based exploration in the project. Streamlit and st-chat provide an intuitive chat UI, while Pandas and NetworkX handle the data and visualization logic.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/Streamlit-E04E39?style=for-the-badge&logo=streamlit&logoColor=white" /> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" /> <img src="https://img.shields.io/badge/NetworkX-000000?style=for-the-badge&logo=networkx&logoColor=white" /> <img src="https://img.shields.io/badge/Poetry-8C52FF?style=for-the-badge&logo=python" />  </p>

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/) (recommended for managing dependencies)

### Installation

1. Clone the repo

```bash
   git clone https://github.com/Yousinator/DataMiner
   cd DataMiner
```

2. **Install Poetry (if you haven’t)**

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -

   ```

3. **Install Dependencies**

   ```bash
   poetry install

   ```

4. **Activate the Virtual Environment**

   ```bash
   poetry shell

   ```

5. **Run the App**

   ```bash
   poetry run streamlit run main.py

   ```

## Usage

- Launch the app using `poetry run streamlit run main.py`.
- Use the sidebar to switch between TextMiner Chat and GraphMiner Chat.
- Ask questions about student bios or generate graphs by entering a name or certificate.
- Chat history clears when switching pages for a clean user experience.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

- If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/Yousinator/DataMiner/issues/new) to discuss it, or directly create a pull request after you edit the _README.md_ file with necessary changes.
- Please make sure you check your spelling and grammar.
- Create individual PR for each suggestion.
- Please also read through the [Code Of Conduct](https://github.com/Yousinator/DataMiner/blob/main/CODEOFCONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the `Apache 2.0` License. See [LICENSE](https://github.com/Yousinator/DataMiner/blob/main/LICENSE) for more information.

## Authors

- **Yousinator** - [Yousinator](https://github.com/Yousinator/)

### Notes:

1. **About the Project**: Elaborate on the purpose, features, and functionalities of your project.
2. **Built With**: List all significant technologies and frameworks used in the project.
3. **Getting Started**: Provide detailed instructions on setting up the project locally. Adjust paths and commands to match your project's structure.
4. **Usage**: Describe how to use the application, including any important commands.
5. **Contributing**: Encourage other developers to contribute to your project.
6. **License**: Specify the license under which the project is released.
7. **Authors**: Credit yourself and any other contributors.
8. **Acknowledgements**: Acknowledge any individual, institution, or resource that helped you in your project.

Feel free to modify and expand each section to suit your project’s specifics.
