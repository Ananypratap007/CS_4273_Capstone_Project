SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[UserData](
	[Date] [date] NULL,
	[Time] [time](7) NULL,
	[Temp] [int] NULL,
	[Humid] [int] NULL,
	[Lux] [int] NULL
) ON [PRIMARY]
GO
