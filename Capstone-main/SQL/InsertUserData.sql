SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertUserData]
    @Temperature DECIMAL(5,2),
    @Humidity DECIMAL(5,2),
    @Lux INT
AS
BEGIN
    INSERT INTO UserData (Temperature, Humidity, Lux)
    VALUES (@Temperature, @Humidity, @Lux);
END;
GO
