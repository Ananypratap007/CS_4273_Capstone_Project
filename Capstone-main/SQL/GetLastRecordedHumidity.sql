SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[GetLastRecordHumidity]
AS
BEGIN
    SELECT TOP 1 Humid
    FROM dbo.weatherBox
    ORDER BY Date DESC, Time DESC;
END;
GO
