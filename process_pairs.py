def convert_to_php_pairs():
    # 用于存储已处理的对，避免重复
    processed_pairs = set()
    current_group = None
    current_file = None
    current_array = None
    
    with open('test.md', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
        
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 检查是否是分组标题
        if line.endswith('：'):
            if current_array and current_file:
                # 写入之前的分组
                current_array += "];"
                with open(f"{current_file}.php", 'w', encoding='utf-8') as f:
                    f.write(current_array)
            
            # 设置新的分组
            current_group = line
            current_file = line.rstrip('：')
            current_array = "[\n"
            i += 1
            continue
        
        # 确保有足够的行来处理一对
        if i + 1 >= len(lines):
            break
            
        title = lines[i]
        content = lines[i + 1]
        
        # 创建pair元组用于检查重复
        pair = (title, content)
        
        if pair not in processed_pairs and current_array is not None:
            # 转义单引号
            escaped_title = title.replace("'", "\\'")
            escaped_content = content.replace("'", "\\'")
            
            # 添加到PHP数组
            current_array += "\tarray(\n"
            current_array += f"\t\t'title' => '{escaped_title}',\n"
            current_array += f"\t\t'content' => '{escaped_content}'\n"
            current_array += "\t),\n"
            
            # 记录已处理的对
            processed_pairs.add(pair)
        
        i += 2
    
    # 写入最后一个分组
    if current_array and current_file:
        current_array += "];"
        with open(f"{current_file}.php", 'w', encoding='utf-8') as f:
            f.write(current_array)

# 执行转换
if __name__ == "__main__":
    convert_to_php_pairs() 