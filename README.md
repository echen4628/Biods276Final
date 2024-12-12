# Biods276Final

## Steps to running code
1. Download the dataset from https://openi.nlm.nih.gov/faq#collection. Only the PNG and Reports are neccessary. The DICOM images are huge and not used in this project.

2. Extract the datasets if needed.

3. Clone this repository.

4. Put the reports in a folder called `ecgen-radiology/` and images in a folder called `images/` at the base level of this repository.

5. Run the `select_samples.py` script, which will copy 300 frontal X-rays from the dataset.

6. Go through the `Main_Code_for_CheXagent+BiomedParse.ipynb` notebook. The code is designed to run in Google Colab and it will require the A100 GPU due to CheXagent being an 8 Billion parameter model. You will also need to upload the sampled images and reports into Google Colab.
