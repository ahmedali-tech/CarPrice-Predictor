import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def Model(Year, Present_Price, Kms_Driven, Owner, Car_Name_Activa3g, Car_Name_Activa4g, Car_Name_BajajAvenger150,	Car_Name_scross, Car_Name_swift, Car_Name_sx4, Car_Name_verna, Car_Name_vitarabrezza, Car_Name_wagonr, Car_Name_xcent	, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual):
    df = pd.read_csv("car data.csv")
    df = pd.get_dummies(df, columns=[
                        'Car_Name', "Fuel_Type", "Seller_Type", "Transmission"], drop_first=True)
    xtrain, xtest, ytrain, ytest = train_test_split(df[["Year", "Present_Price", "Kms_Driven", "Owner", "Car_Name_Activa 3g", "Car_Name_Activa 4g", "Car_Name_Bajaj Avenger 150", "Car_Name_s cross", "Car_Name_swift",
                                                    "Car_Name_sx4", "Car_Name_verna", "Car_Name_vitara brezza", "Car_Name_wagon r", "Car_Name_xcent", "Fuel_Type_Diesel", "Fuel_Type_Petrol", "Seller_Type_Individual"]], df["Selling_Price"])

    model = LinearRegression()
    model.fit(xtrain, ytrain)
    array = np.reshape([int(Year), int(Present_Price), int(Kms_Driven), Owner, Car_Name_Activa3g, Car_Name_Activa4g, Car_Name_BajajAvenger150,	Car_Name_scross, Car_Name_swift,
                       Car_Name_sx4, Car_Name_verna, Car_Name_vitarabrezza, Car_Name_wagonr, Car_Name_xcent	, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual], (1, -1))
    return model.predict(array)[0]
