-- 自治事务开始
PROCEDURE TRANS_B AS
PRAGMA AUTONOMOUS_TRANSACTION;
DECLARE
  v_value INT;
BEGIN
  -- 自治事务更新同一数据
  UPDATE test_table SET value = value + 1 WHERE id = 1;
  -- 获取更新后的值
  SELECT value INTO v_value FROM test_table WHERE id = 1;
  -- 输出自治事务更新后的值
  DBMS_OUTPUT.PUT_LINE('自治事务更新后的值:' || v_value);
  -- 提交自治事务
  COMMIT;
END;
