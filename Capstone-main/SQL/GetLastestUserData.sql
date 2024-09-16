SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[GetLatestUserData]
AS
BEGIN
    SELECT TOP 1 Temperature, Humidity, Lux
    FROM UserData
    ORDER BY ID DESC;  -- Retrieves the latest entry based on the highest ID
END;
GO
