In order to update all libraries in this project after clone the project is necessary to execute the follows:

- DOWNLOAD
pip install -r requirements.txt

- UPDATE (If you add any new library is necessary first delete the file requirements.txt and after to execute the follow command)
pip freeze > requirements.txt


- HIGHLIGHTS NOTES
By default all endpoints is setted as without permissions needed so remember to use the annotation  **@permission_classes([permissions.IsAuthenticated])** when the user should be authenticated to reach the endpoint such as informations of a user for example.

