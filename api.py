"""
bs2 Python API (bs2/api.R)
Author: Peak AI
Tenant: Default
Created: 2019-01-22
Template Version: 1
"""
import json


def predict(body: str) -> str:
    """
    A function to be exposed via a Peak API.

    Parameters
    ----------
    body: str
        A string containing the body of the request. Typically JSON-formatted.

    Returns
    -------
    out: str or bytes
        A string containing the response. Must be JSON formatted.

    Notes
    -----
    sagemaker deployment:
        If deploying via Peak's SageMaker deployment workflow, the structure of the 'body' argument
        is modified to look like:
        {
            "request": <user-request>,
            "parameters": {
                "apikey": <tenant-api-key>,
                "apiendpoint": <tenant-api-endpoint>
            }
        }
        Where <user-request> is the _original_ request sent, <tenant-api-key> is the tenant's API
        key, and <tenant-api-endpoint> is the API endpoint for the tenant.

    """
    data = json.loads(body)
    for key, value in data.items():
        totalsum = sum(data.values())
    output = json.dumps(totalsum)
    return output 



    


#def index(**kwargs):
    #request = kwargs.get('request')
    #totalsum = sum(request.values())
    #return {"summary": totalsum}


#def adder(**numbers):
    #for key, value in numbers.items():
        #totalsum = sum(numbers.values())
    #print(totalsum)

#data = json.loads(body)
#return json.dumps(dict(output=sum(data.values())))

