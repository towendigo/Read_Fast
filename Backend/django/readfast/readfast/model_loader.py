from django.apps import apps as loader

def Single_Loader(app_name, model_name, err_code=False):

    try:
        App = loader.get_app_config(app_name)
        return App.get_model(model_name)
    except LookupError as er:
        if err_code:
            return 'Error on app : %s' %er
        else :
            return None


def Multi_Loader(app_name, model_names, err_code = False):

    try:
        App = loader.get_app_config(app_name)
        Models = {}
        for model_name in model_names:
            try : 
                Models[model_name] = App.get_model(model_name)
            except LookupError as er:
                if err_code:
                    Models[model_name] = 'Error on model : %s' %er
                else :
                    pass       

        return Models

    except LookupError as er:
        if err_code:
            return 'Error on app : %s' %er
        else :
            return None


def Multi_Loader_List(app_name, model_names, err_code = False):

    try:
        App = loader.get_app_config(app_name)
        Models = []
        for model_name in model_names:
            try : 
                Models.append(App.get_model(model_name))
            except LookupError as er:
                if err_code:
                    Models.append('Error on model : %s' %er)
                else :
                    pass       

        return Models
        
    except LookupError as er:
        if err_code:
            return 'Error on app : %s' %er
        else :
            return None