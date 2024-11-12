PROCEDURE TRANS_A AS
-- 主事务开始
BEGIN;
TRANS_C;
TRANS_B;
COMMIT;

-- 查询最终结果
SELECT value FROM test_table WHERE id = 1;
-- 主事务结束
END;
