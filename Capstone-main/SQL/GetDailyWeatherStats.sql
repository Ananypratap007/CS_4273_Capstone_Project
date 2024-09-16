CREATE PROCEDURE GetDailyWeatherStats
AS
BEGIN
    SELECT 
        Date,
        AVG(dBl) AS average_dBl,
        MAX(dBl) AS max_dBl,
        MIN(dBl) AS min_dBl,
        AVG(Lux) AS average_Lux,
        MAX(Lux) AS max_Lux,
        MIN(Lux) AS min_Lux,
        AVG(Temp) AS average_Temp,
        MAX(Temp) AS max_Temp,
        MIN(Temp) AS min_Temp,
        AVG(Humid) AS average_Humid,
        MAX(Humid) AS max_Humid,
        MIN(Humid) AS min_Humid
    FROM 
        dbo.weatherArchive
    GROUP BY 
        Date
    ORDER BY 
        CAST(Date AS DATETIME);
END;