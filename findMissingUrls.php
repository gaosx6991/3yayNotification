<?php

class AlbumProcessor
{
    /**
     * 处理相册图片，返回用户最新的相册图片数组
     * @param array $adminArray 管理员审核后的相册数组
     * @param array $userArray 用户提交的相册数组
     * @return array 处理后的相册数组
     */
    public function processAlbumImages(array $adminArray, array $userArray): array
    {
        // 提取管理员审核过的图片路径
        $adminPaths = array_map(function($item) {
            return $this->normalizePath($item['url']);
        }, $adminArray);

        // 处理用户提交的图片路径
        $userPaths = array_map(function($url) {
            return $this->normalizePath($url);
        }, $userArray);

        // 构建结果数组
        $result = [];
        foreach ($userArray as $userUrl) {
            $normalizedPath = $this->normalizePath($userUrl);
            
            // 构建新的完整URL
            $newUrl = getProtocol() . '://' . getHost() . $normalizedPath;
            
            // 如果这张图片不在管理员审核过的数组中，标记为已删除
            if (!in_array($normalizedPath, $adminPaths)) {
                $newUrl .= '?deleted=1';
            }
            
            $result[] = $newUrl;
        }

        return $result;
    }

    /**
     * 标准化路径，去除域名部分和查询参数
     * @param string $url URL或路径
     * @return string 标准化后的路径
     */
    private function normalizePath(string $url): string
    {
        // 如果包含完整URL，解析并只保留路径部分
        if (strpos($url, 'http') === 0) {
            $parsedUrl = parse_url($url);
            $path = $parsedUrl['path'] ?? '';
        } else {
            $path = $url;
        }

        // 移除查询参数（如 ?cover=1）
        $path = preg_replace('/\?.*$/', '', $path);

        return $path;
    }
}

// 初始化处理器
$processor = new AlbumProcessor();

// 管理员审核过的相册
$adminArray = [
    array(
        'url' => '/uploads/20241217/image1.jpeg?cover=1'
    ),
    array(
        'url' => '/uploads/20241217/image3.jpeg'
    )
];

// 用户提交的相册
$userArray = [
    'http://hookupapps.net:8019/uploads/20241217/image1.jpeg',
    'http://hookupapps.net:8019/uploads/20241217/image2.jpeg',
    'http://hookupapps.net:8019/uploads/20241217/image3.jpeg'
];

$result = $processor->processAlbumImages($adminArray, $userArray);

/* 
结果将是：
[
    'https://example.com/uploads/20241217/image1.jpeg',
    'https://example.com/uploads/20241217/image2.jpeg?deleted=1',
    'https://example.com/uploads/20241217/image3.jpeg'
]
*/