import pandas as pd

ser = pd.Series(
            data=[7.19, 7.16, 7.04],
            index=pd.to_datetime(['03-Jan-2020', '01-Feb-2020', '01-Apr-2020'])
            )

# List of lists
tsla_dat_ll = [ ['2010-06-29',4.78,93831500],
             ['2010-06-30',4.77,85935500],
             ['2010-07-01',4.39,41094000],
             ['2010-07-02',3.84,25699000],
             ['2010-07-06',3.22,34334500],
           ]

# Dictionary of lists
dates = ['2010-06-29', '2010-06-30', '2010-07-01', '2010-07-02', '2010-07-06']
tsla_prcs = [ 4.78, 4.77, 4.39, 3.84, 3.22]
tsla_vols = [ 93831500, 85935500, 41094000, 25699000, 34334500]
tsla_dat_dl = { 'adj_prce': tsla_prcs, 'volume': tsla_vols}

# List of dictionaries
tsla_dat_ld = [ 
    {'date': '2010-06-29', 'adj-price': 4.78, 'volume': 93831500},
    {'date': '2010-06-30', 'adj-price': 4.77, 'volume': 85935500},
    {'date': '2010-07-01', 'adj-price': 4.39, 'volume': 41094000},
    {'date': '2010-07-02', 'adj-price': 3.84, 'volume': 25699000},
    {'date': '2010-07-06', 'adj-price': 3.22, 'volume': 34334500},
    ]

dates_index = pd.to_datetime(dates)
tsla_prcs_ser = pd.Series(data=[4.78, 4.77, 4.39, 3.84, 3.22], index=dates_index)
tsla_vols_ser = pd.Series(data=[93831500, 85935500, 41094000, 25699000, 34334500], index=dates_index)


# Dictionary of series
price_partial = [4.78, 4.77, 4.39]
price_dates_partial = pd.to_datetime(['2010-06-29', '2010-06-30', '2010-07-01'])

volume_partial = [34334500, 25699000, 41094000 ]
volume_dates_partial = pd.to_datetime(['2010-07-02', '2010-07-01', '2010-06-30', ])

tsla_prcs_partial_ser = pd.Series(data=price_partial, index=price_dates_partial)
tsla_vols_partial_ser = pd.Series(data=volume_partial, index=volume_dates_partial)


# Selection demo
tsla_df = pd.DataFrame({'adj_price': tsla_prcs_ser, 'volume': tsla_vols_ser})

