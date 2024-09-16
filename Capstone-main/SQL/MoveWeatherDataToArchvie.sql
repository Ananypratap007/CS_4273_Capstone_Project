SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[MoveWeatherDataToArchive]
AS
BEGIN
    -- Transaction ensures both operations complete successfully or none do
    BEGIN TRANSACTION;
    
    -- Step 1: Copy data from weatherBox to weatherArchive
    INSERT INTO [dbo].[weatherArchive] ([Date], [Time], [dBl], [Lux], [Temp], [Humid])
    SELECT [Date], [Time], [dBl], [Lux], [Temp], [Humid]
    FROM [dbo].[weatherBox];
    
    -- Step 2: Check if the insert was successful before deleting
    IF @@ROWCOUNT > 0
    BEGIN
        -- Delete all data from weatherBox
        DELETE FROM [dbo].[weatherBox];
        
        -- Commit the transaction if everything is correct
        COMMIT TRANSACTION;
    END
    ELSE
    BEGIN
        -- If no rows were copied, rollback the transaction
        ROLLBACK TRANSACTION;
    END
END;
GO
