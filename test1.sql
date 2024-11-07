CREATE PROCEDURE Procedure1  
    @ID INT,  
    @NewValue NVARCHAR(50)  
AS  
BEGIN  
    -- 开启事务  
    BEGIN TRANSACTION;  
  
    -- 更新数据，这里我们假设ID=1的行是我们要更新的目标  
    UPDATE TestTable  
    SET Value = @NewValue  
    WHERE ID = 1;  
  
    -- 模拟长时间运行的操作（例如，等待用户输入或其他操作）  
    -- 在实际应用中，这可能是网络延迟、I/O操作或其他任何事情  
    WAITFOR DELAY '00:00:05';  -- 等待5秒  
  
    -- 尝试更新另一行数据，这将与Procedure2产生冲突  
    UPDATE TestTable  
    SET Value = @NewValue + '_extra'  
    WHERE ID = 2;  
  
    -- 提交事务  
    COMMIT TRANSACTION;  
END;  
GO  
  
CREATE PROCEDURE Procedure2  
    @ID INT,  
    @NewValue NVARCHAR(50)  
AS  
BEGIN  
    -- 开启事务  
    BEGIN TRANSACTION;  
  
    -- 更新数据，这里我们同样假设ID=2的行是我们要更新的目标  
    UPDATE TestTable  
    SET Value = @NewValue  
    WHERE ID = 2;  
  
    -- 模拟长时间运行的操作  
    WAITFOR DELAY '00:00:05';  -- 等待5秒  
  
    -- 尝试更新第一行数据，这将与Procedure1产生冲突  
    UPDATE TestTable  
    SET Value = @NewValue + '_extra'  
    WHERE ID = 1;  
  
    -- 提交事务  
    COMMIT TRANSACTION;  
END;  
GO
