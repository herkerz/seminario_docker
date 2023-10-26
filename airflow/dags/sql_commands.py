SQL_DB = 'seminario'  
SQL_TABLE = 'gdp_data'


SQL_CREATE = f"""
                        CREATE TABLE IF NOT EXISTS {SQL_TABLE} ( 
                            date DATE NOT NULL
                            , value REAL
                            , pct_change REAL
                            , PRIMARY KEY (date)
                        );

"""