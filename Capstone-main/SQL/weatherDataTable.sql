SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[weatherData](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Date] [varchar](100) NOT NULL,
	[Time] [varchar](100) NOT NULL,
	[Lux] [int] NOT NULL,
	[Temp] [int] NOT NULL,
	[Humid] [int] NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[weatherData] ADD PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
