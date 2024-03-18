import pandas as pd
class CentralTendency:
    
    def central_tendency(dataset, quan):
        
        descriptive = pd.DataFrame(columns=quan, index=["Mean","Median", "Mode"])
        for column_name in quan:
            descriptive [column_name]['Mean'] = dataset[column_name].mean()
            descriptive [column_name]['Median'] = dataset[column_name].median()
            descriptive [column_name]['Mode'] = dataset[column_name].mode()[0]   
        return descriptive