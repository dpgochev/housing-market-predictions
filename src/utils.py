def correct_nan(df):
    df.loc[df.Alley.isnull(),'Alley']='NoAlley'
    df.loc[df.BsmtQual .isnull(),'BsmtQual']='NoBasement'
    df.loc[df.BsmtCond .isnull(),'BsmtCond']='NoBasement'
    df.loc[df.BsmtExposure .isnull(),'BsmtExposure']='NoBasement'
    df.loc[df.BsmtFinType1 .isnull(),'BsmtFinType1']='NoBasement'
    df.loc[df.BsmtFinType2 .isnull(),'BsmtFinType2']='NoBasement'
    df.loc[df.FireplaceQu .isnull(),'FireplaceQu']='NoFireplace'
    df.loc[df.GarageType .isnull(),'GarageType']='NoGarage'
    df.loc[df.GarageFinish .isnull(),'GarageType']='NoGarage'
    df.loc[df.GarageQual .isnull(),'GarageQual']='NoGarage'
    df.loc[df.GarageCond .isnull(),'GarageCond']='NoGarage'
    df.loc[df.PoolQC .isnull(),'PoolQC']='NoPool'
    df.loc[df.Fence .isnull(),'Fence']='NoFence'
    df.loc[df.MiscFeature .isnull(),'MiscFeature']='NoMisc'
    return df