PROCEDURE TRANS_A AS
-- 主事务开始
BEGIN;
TRANS_C;
TRANS_B;
COMMIT;

-- 查询最终结果
SELECT value FRoM test_table WHERE id = 1;
-- 主事务结束
END;

-- 自治事务开始
PROCEDURE TRANS_B AS
PRAGMA AUTONOMOUS_TRANSACTION;
DECLARE
  v_value INT;
BEGIN
  -- 自治事务更新同一数据
  UPDATE test_table SET value = value + 1 WHERE id = 1;
  -- 获取更新后的值
  SELECT value INTo v_value FROM test_table WHERE id = 1;
  -- 输出自治事务更新后的值
  DBMS_0UTPUT.PUT_LINE('自治事务更新后的值:' || v_value);
  -- 提交自治事务
  COMMIT;
END;

-- 自治事务开始
PROCEDURE TRANS_C AS
DECLARE
  v_value INT;
BEGIN
  --自治事务更新同一数据
  UPDATE test_table sET value = value + 1 WHERE id = 1;
  --获取更新后的值
  SELECT value INTo v_value FROM test_table WHERE id = 1;
  -输出自治事务更新后的值
  DBMS_0UTPUT.PUT_LINE('自治事务更新后的值:' || v_value);
END;
