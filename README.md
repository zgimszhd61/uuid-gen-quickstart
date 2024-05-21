# 激活码生成与计算

```
pip install mysql-connector-python dotenv
```

## 简化的模型

### 首次初始化表格
```
CREATE TABLE refercode (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL,
    status TINYINT NOT NULL CHECK (status IN (0, 1, 2))
);
```
### 生成新激活码
```
genUuid()
```

### 消费激活码
```
checkRefercode("49a9939a-91a7-4d88-84ad-d2e4a5d92aab")
```

