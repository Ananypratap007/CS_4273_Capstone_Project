SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertWeatherBox]
    @Date  VARCHAR(100),
    @Time  VARCHAR(100),
    @dBl   INT,
    @Lux   INT,
    @Temp  INT,
    @Humid INT
AS
BEGIN
    INSERT INTO dbo.weatherBox ([Date], [Time], [dBl], [Lux], [Temp], [Humid])
    VALUES (@Date, @Time, @dBl, @Lux, @Temp, @Humid);
END;
GO
