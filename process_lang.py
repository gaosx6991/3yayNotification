def convert_to_php_array():
    # 用于存储已处理的行,避免重复
    processed_lines = set()
    
    # 存储最终的PHP数组字符串
    php_array = "array(\n"
    
    with open('test.md', 'r', encoding='utf-8') as file:
        for line in file:
            # 跳过空行
            if not line.strip():
                continue
            
            # 清理行末换行符
            line = line.strip()
            
            # 如果这行已经处理过，就跳过
            if line in processed_lines:
                continue
                
            # 将单引号转义
            escaped_line = line.replace("'", "\\'")
            
            # 添加到PHP数组格式
            php_array += f"\t'{escaped_line}' => array(\n"
            php_array += f"\t\t'en' => '{escaped_line}',\n"
            php_array += "\t),\n"
            
            # 记录已处理的行
            processed_lines.add(line)
    
    php_array += ");"
    
    return php_array

# 执行转换并打印结果
if __name__ == "__main__":
    result = convert_to_php_array()
    with open('result.php', 'w', encoding='utf-8') as file:
        file.write(result)
