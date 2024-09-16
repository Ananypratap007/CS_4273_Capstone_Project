SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertWeatherData]
    @Date  VARCHAR(100),
    @Time  VARCHAR(100),
    @Lux   INT,
    @Temp  INT,
    @Humid INT
AS
BEGIN
    INSERT INTO weatherData ([Date], [Time], [Lux], [Temp], [Humid])
    VALUES (@Date, @Time, @Lux, @Temp, @Humid);
END;
GO
