<?php
define('DB_HOST', 'localhost');
define('DB_NAME', 'dse_study_platform');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_CHARSET', 'utf8mb4');
define('JWT_SECRET', '51c43320b939bbaee60ac37ae8a98989');
function getDB(): PDO {
    static $pdo = null;
    if ($pdo === null) {
        $dsn = sprintf('mysql:host=%s;dbname=%s;charset=%s', DB_HOST, DB_NAME, DB_CHARSET);
        $pdo = new PDO($dsn, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]);
    }
    return $pdo;
}
function verifyToken(): ?array {
    $headers = getallheaders();
    $auth = $headers['Authorization'] ?? '';
    if (!preg_match('/^Bearer\s+(.+)$/', $auth, $m)) return null;
    $payload = json_decode(base64_decode($m[1]), true);
    return ($payload && isset($payload['user_id'])) ? $payload : null;
}
function requireAuth(): array {
    $user = verifyToken();
    if (!$user) { http_response_code(401); echo json_encode(['error'=>'Authentication required']); exit; }
    return $user;
}
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');
header('Content-Type: application/json; charset=utf-8');
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(200); exit; }
