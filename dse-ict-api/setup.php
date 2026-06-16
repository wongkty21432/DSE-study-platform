<?php
/**
 * One-click Database Setup — run this in your browser to initialize everything.
 * After setup, DELETE this file for security.
 *
 * Usage: http://localhost:8080/dse-ict-api/setup.php
 */

$step = $_GET['step'] ?? 1;
$db_host = 'localhost';
$db_user = 'root';
$db_pass = '';
$db_name = 'dse_study_platform';

?>
<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DSE Study Platform — Database Setup</title>
<style>
  body { font-family:'Segoe UI',system-ui,sans-serif; background:#0a0f1e; color:#e8edf5; max-width:700px; margin:40px auto; padding:20px; }
  h1 { color:#38bdf8; }
  .card { background:#131b2e; border:1px solid #263048; border-radius:12px; padding:20px; margin:16px 0; }
  .ok { color:#4ade80; } .err { color:#f87171; } .info { color:#8899b4; }
  pre { background:#1c2840; padding:12px; border-radius:8px; overflow-x:auto; font-size:.8rem; }
  button, .btn { padding:10px 24px; border-radius:20px; border:none; background:#38bdf8; color:#0a0f1e; font-weight:600; cursor:pointer; font-size:.85rem; text-decoration:none; display:inline-block; }
  button:hover { background:#7dd3fc; }
  label { display:block; font-size:.8rem; color:#8899b4; margin:8px 0 4px; }
  input { width:100%; padding:8px 12px; border-radius:8px; border:1px solid #263048; background:#1c2840; color:#e8edf5; font-size:.85rem; font-family:inherit; }
</style>
</head>
<body>
<h1>🗄️ DSE Study Platform — Database Setup</h1>

<?php if ($step == 1): ?>
<div class="card">
  <h3>Step 1: Database Connection</h3>
  <p class="info">Enter your MySQL credentials (same as phpMyAdmin).</p>
  <form method="get" action="setup.php">
    <input type="hidden" name="step" value="2">
    <label>MySQL Host</label>
    <input name="host" value="localhost">
    <label>MySQL Username</label>
    <input name="user" value="root">
    <label>MySQL Password</label>
    <input name="pass" type="password" placeholder="(leave blank if none)">
    <label>Database Name</label>
    <input name="db" value="dse_study_platform">
    <br><br>
    <button type="submit">Connect & Create Database →</button>
  </form>
  <p style="margin-top:16px;font-size:.75rem;color:#8899b4;">
    ℹ️ Make sure XAMPP MySQL is running first.
  </p>
</div>

<?php elseif ($step == 2):
$db_host = $_GET['host'] ?? 'localhost';
$db_user = $_GET['user'] ?? 'root';
$db_pass = $_GET['pass'] ?? '';
$db_name = $_GET['db'] ?? 'dse_study_platform';

try {
    // Connect without database first
    $pdo = new PDO("mysql:host=$db_host;charset=utf8mb4", $db_user, $db_pass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    ]);

    // Create database
    $pdo->exec("CREATE DATABASE IF NOT EXISTS `$db_name` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");
    echo "<div class='card'><p class='ok'>✅ Database '$db_name' created/verified.</p></div>";

    // Connect to the database
    $pdo->exec("USE `$db_name`");

    // Create tables
    $tables_sql = "
    CREATE TABLE IF NOT EXISTS questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        qid VARCHAR(20) NOT NULL UNIQUE,
        subject VARCHAR(10) NOT NULL,
        topic INT NOT NULL,
        year INT NOT NULL,
        qnum INT NOT NULL,
        source_type VARCHAR(10) DEFAULT 'mc',
        source_paper VARCHAR(5) DEFAULT '1A',
        difficulty ENUM('easy','medium','hard') NOT NULL DEFAULT 'medium',
        question TEXT NOT NULL,
        question_en TEXT DEFAULT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT DEFAULT NULL,
        option_a_en TEXT DEFAULT NULL,
        option_b_en TEXT DEFAULT NULL,
        option_c_en TEXT DEFAULT NULL,
        option_d_en TEXT DEFAULT NULL,
        answer TINYINT NOT NULL,
        explanation TEXT NOT NULL,
        explanation_en TEXT DEFAULT NULL,
        marking_notes TEXT DEFAULT NULL,
        marking_notes_en TEXT DEFAULT NULL,
        topic_name_en VARCHAR(100) DEFAULT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        INDEX idx_subject (subject),
        INDEX idx_topic (topic),
        INDEX idx_year (year),
        INDEX idx_difficulty (difficulty),
        INDEX idx_subject_topic (subject, topic)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

    CREATE TABLE IF NOT EXISTS user_performance (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        subject VARCHAR(10) NOT NULL,
        topic INT NOT NULL,
        total_attempted INT DEFAULT 0,
        total_correct INT DEFAULT 0,
        mastery_level ENUM('new','novice','developing','proficient','advanced','master') DEFAULT 'new',
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY uk_user_subject_topic (user_id, subject, topic)
    ) ENGINE=InnoDB;

    CREATE TABLE IF NOT EXISTS answer_history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        qid VARCHAR(20) NOT NULL,
        selected_option TINYINT NOT NULL,
        is_correct TINYINT(1) NOT NULL,
        answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        INDEX idx_user_qid (user_id, qid)
    ) ENGINE=InnoDB;

    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        email VARCHAR(100) DEFAULT NULL,
        role ENUM('user','admin') DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB;
    ";

    $pdo->exec($tables_sql);
    echo "<div class='card'><p class='ok'>✅ All tables created.</p></div>";

    // Save config
    $config = "<?php
define('DB_HOST', '$db_host');
define('DB_NAME', '$db_name');
define('DB_USER', '$db_user');
define('DB_PASS', '$db_pass');
define('DB_CHARSET', 'utf8mb4');
define('JWT_SECRET', '" . bin2hex(random_bytes(16)) . "');
function getDB(): PDO {
    static \$pdo = null;
    if (\$pdo === null) {
        \$dsn = sprintf('mysql:host=%s;dbname=%s;charset=%s', DB_HOST, DB_NAME, DB_CHARSET);
        \$pdo = new PDO(\$dsn, DB_USER, DB_PASS, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]);
    }
    return \$pdo;
}
function verifyToken(): ?array {
    \$headers = getallheaders();
    \$auth = \$headers['Authorization'] ?? '';
    if (!preg_match('/^Bearer\s+(.+)$/', \$auth, \$m)) return null;
    \$payload = json_decode(base64_decode(\$m[1]), true);
    return (\$payload && isset(\$payload['user_id'])) ? \$payload : null;
}
function requireAuth(): array {
    \$user = verifyToken();
    if (!\$user) { http_response_code(401); echo json_encode(['error'=>'Authentication required']); exit; }
    return \$user;
}
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');
header('Content-Type: application/json; charset=utf-8');
if (\$_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(200); exit; }
";
    file_put_contents(__DIR__ . '/config.php', $config);
    echo "<div class='card'><p class='ok'>✅ config.php written with your credentials.</p></div>";

    // Step 3: import questions
    echo "<div class='card'>";
    echo "<h3>Step 2: Import Questions</h3>";
    echo "<p class='info'>Click below to import questions from JSON files into MySQL.</p>";
    echo "<a href='setup.php?step=3&host=" . urlencode($db_host) . "&user=" . urlencode($db_user) . "&pass=" . urlencode($db_pass) . "&db=" . urlencode($db_name) . "' class='btn'>Import Questions →</a>";
    echo "</div>";

} catch (PDOException $e) {
    echo "<div class='card'><p class='err'>❌ Connection failed: " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "<p class='info'>Make sure MySQL is running in XAMPP Control Panel.</p>";
    echo "<a href='setup.php' class='btn'>← Try Again</a></div>";
}

elseif ($step == 3):
$db_host = $_GET['host'] ?? 'localhost';
$db_user = $_GET['user'] ?? 'root';
$db_pass = $_GET['pass'] ?? '';
$db_name = $_GET['db'] ?? 'dse_study_platform';

try {
    $pdo = new PDO("mysql:host=$db_host;dbname=$db_name;charset=utf8mb4", $db_user, $db_pass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    ]);

    $json_files = [
        'chem' => __DIR__ . '/../chem/questions-chem.json',
        'ict'  => __DIR__ . '/../ict/questions-ict.json',
    ];

    $sql = 'INSERT INTO questions
        (qid, subject, topic, year, qnum, source_type, source_paper, difficulty,
         question, question_en, option_a, option_b, option_c, option_d,
         option_a_en, option_b_en, option_c_en, option_d_en,
         answer, explanation, explanation_en, marking_notes, marking_notes_en, topic_name_en)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON DUPLICATE KEY UPDATE
        topic=VALUES(topic), year=VALUES(year), difficulty=VALUES(difficulty),
        question=VALUES(question), question_en=VALUES(question_en),
        option_a=VALUES(option_a), option_b=VALUES(option_b),
        option_c=VALUES(option_c), option_d=VALUES(option_d),
        answer=VALUES(answer), explanation=VALUES(explanation),
        explanation_en=VALUES(explanation_en),
        marking_notes=VALUES(marking_notes), marking_notes_en=VALUES(marking_notes_en),
        topic_name_en=VALUES(topic_name_en)';

    $stmt = $pdo->prepare($sql);
    $total = 0;

    foreach ($json_files as $subject => $path) {
        if (!file_exists($path)) {
            echo "<p class='err'>⚠️ JSON not found: $path</p>";
            continue;
        }
        $questions = json_decode(file_get_contents($path), true);
        if (!$questions) {
            echo "<p class='err'>⚠️ Invalid JSON: $path</p>";
            continue;
        }

        $count = 0;
        foreach ($questions as $q) {
            $opts = $q['options'] ?? [];
            $opts_en = $q['options_en'] ?? [];
            $stmt->execute([
                $q['qid'], $subject, (int)($q['topic']??0), (int)($q['year']??0),
                (int)($q['qnum']??0), $q['sourceType']??'mc', $q['sourcePaper']??'1A',
                $q['difficulty']??'medium', $q['question']??'', $q['question_en']??null,
                $opts[0]??'', $opts[1]??'', $opts[2]??'', $opts[3]??null,
                $opts_en[0]??null, $opts_en[1]??null, $opts_en[2]??null, $opts_en[3]??null,
                (int)($q['answer']??0), $q['explanation']??'', $q['explanation_en']??null,
                $q['markingNotes']??null, $q['markingNotes_en']??null, $q['topic_name_en']??null,
            ]);
            $count++;
        }
        echo "<div class='card'><p class='ok'>✅ $subject: imported $count questions</p></div>";
        $total += $count;
    }

    echo "<div class='card' style='border-color:#4ade80;'>";
    echo "<h3 class='ok'>🎉 Setup Complete!</h3>";
    echo "<p>Total questions in database: <strong>$total</strong></p>";
    echo "<p class='info'>The quiz banks will now load questions from MySQL instead of JSON files.</p>";
    echo "<p class='err' style='margin-top:12px;'>⚠️ IMPORTANT: Delete setup.php now for security!</p>";
    echo "<a href='../index.html' class='btn'>Go to Study Platform →</a>";
    echo " <a href='get-questions.php?subject=chem' class='btn' style='background:#4ade80;'>Test API →</a>";
    echo "</div>";

} catch (PDOException $e) {
    echo "<div class='card'><p class='err'>❌ Error: " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "<a href='setup.php' class='btn'>← Try Again</a></div>";
}

endif; ?>

</body>
</html>
