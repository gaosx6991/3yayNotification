# Message Notification System

一个用于处理多语言消息通知的系统，支持访客提醒、点赞通知、评论提醒等多种社交互动场景。

## 功能特性

### 消息类型
- 访客提醒 (Visitor Alerts)
- CrushNote 提醒 (CrushNote Notifications)
- 个人资料点赞提醒 (Profile Like Notifications)
- 帖子点赞提醒 (Post Like Notifications)
- 帖子评论提醒 (Post Comment Notifications)
- 内容审核提醒 (Content Moderation Notifications)
  - 头像审核
  - 相册照片审核
  - 帖子图片审核
  - 帖子内容审核
  - 个人简介审核

### 技术特性
- 多语言支持 (中英文)
- 表情符号丰富的通知内容
- 模块化的消息模板系统
- 灵活的消息处理机制

## 项目结构

```
├── message/ # 消息模板目录
│ ├── 访客提醒.php # 访客相关通知
│ ├── 收到CrushNote提醒.php # CrushNote通知
│ ├── 收到Profile Like提醒.php # 个人资料点赞通知
│ ├── 收到Post Like提醒.php # 帖子点赞通知
│ ├── 收到Post Comment提醒.php # 帖子评论通知
│ ├── 头像被拒.php # 头像审核通知
│ ├── 相册照片被拒.php # 相册审核通知
│ └── Post整体被拒.php # 帖子审核通知
├── lang.php # 语言配置文件
└── findMissingUrls.php # 图片处理工具类
```

## 图片处理功能

系统包含了一个 `AlbumProcessor` 类，用于处理相册图片：

- 标准化图片路径
- 处理已删除的图片
- 维护图片状态
- URL 规范化处理

### 使用示例

```php
$processor = new AlbumProcessor();

// 管理员审核过的相册
$adminArray = [
    ['url' => '/uploads/20241217/image1.jpeg'],
    ['url' => '/uploads/20241217/image3.jpeg']
];

// 用户提交的相册
$userArray = [
    'http://example.com/uploads/20241217/image1.jpeg',
    'http://example.com/uploads/20241217/image2.jpeg',
    'http://example.com/uploads/20241217/image3.jpeg'
];

$result = $processor->processAlbumImages($adminArray, $userArray);
```

## 消息模板

每个通知类型都包含多个变体，以保持通知的新鲜感和趣味性。每个通知包含：

- 标题 (title)
- 内容 (content)
- 相关表情符号

### 示例模板

```php
array(
    'title' => '💌 CrushNote Alert! 😘',
    'content' => 'Someone's got a crush on you! Check out the note they sent!💬'
)
```

## 开发工具

项目包含两个 Python 处理脚本：

- `process_pairs.py`: 用于处理和生成消息对
- `process_lang.py`: 用于处理语言文件

## 注意事项

- 确保服务器支持 UTF-8 编码以正确显示表情符号
- 在添加新的消息模板时，需要同时更新语言文件
- 图片处理时注意路径的规范化和安全性检查

## 贡献指南

1. Fork 该项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request
