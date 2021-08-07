import os
import logging
import json
import pandas as pd
import joblib


def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    model_path = os.path.join(
        os.getenv("AZUREML_MODEL_DIR"), "reg_model.pkl"
    )
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)


def run(raw_data):
    """
    This function is called for every invocation of the endpoint to perform the actual scoring/prediction.
    In the example we extract the data from the json input and call the scikit-learn model's predict()
    method and return the result back
    """
    logging.info("Request received")
    try:
        data = json.loads(raw_data)['data']
        test_data = {
            'gamename':  [data[0]],
            'publisher': [data[1]],
            'developer': [data[2]],
            'tag_common': [data[3]],
            'multi': [data[4]],
            'genre_common': [data[5]],
            'plat_count': [data[6]],
        }
        test_df = pd.DataFrame (test_data, columns = ['gamename','publisher','developer','tag_common','multi','genre_common','plat_count'])
        result = model.predict(test_df)
        logging.info("Request processed")
        return {'data' : result.tolist() , 'message' : "Successfully predicted!"}
    except Exception as e:
           error = str(e)
           return {'data' : str(data) + error , 'message' : 'Failed to predict...'}
