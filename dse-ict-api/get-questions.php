<?php
/**
 * DSE Study Platform - Get Questions API
 *
 * GET /dse-ict-api/get-questions.php?subject=chem
 * GET /dse-ict-api/get-questions.php?subject=ict&topic=1&year=2023&difficulty=medium
 *
 * Returns all questions for a subject, with optional filters.
 * Questions are fetched from MySQL database.
 */
require_once __DIR__ . '/config.php';

$subject = $_GET['subject'] ?? 'ict';
$topic   = $_GET['topic'] ?? null;
$year    = $_GET['year'] ?? null;
$difficulty = $_GET['difficulty'] ?? null;

// Validate subject
$allowed_subjects = ['ict', 'chem'];
if (!in_array($subject, $allowed_subjects)) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid subject. Allowed: ict, chem']);
    exit;
}

try {
    $db = getDB();

    $sql = 'SELECT qid, subject, topic, year, qnum, source_type, source_paper, difficulty,
                   question, question_en,
                   option_a, option_b, option_c, option_d,
                   option_a_en, option_b_en, option_c_en, option_d_en,
                   answer, explanation, explanation_en,
                   marking_notes, marking_notes_en, topic_name_en
            FROM questions
            WHERE subject = :subject';
    $params = ['subject' => $subject];

    if ($topic !== null) {
        $sql .= ' AND topic = :topic';
        $params['topic'] = (int)$topic;
    }
    if ($year !== null) {
        $sql .= ' AND year = :year';
        $params['year'] = (int)$year;
    }
    if ($difficulty !== null && in_array($difficulty, ['easy','medium','hard'])) {
        $sql .= ' AND difficulty = :difficulty';
        $params['difficulty'] = $difficulty;
    }

    $sql .= ' ORDER BY topic, year, qnum';

    $stmt = $db->prepare($sql);
    $stmt->execute($params);
    $questions = $stmt->fetchAll();

    // Convert to frontend-friendly format
    $result = array_map(function($q) {
        $options = [$q['option_a'], $q['option_b'], $q['option_c']];
        if ($q['option_d'] !== null) $options[] = $q['option_d'];

        $options_en = null;
        if ($q['option_a_en'] !== null) {
            $options_en = [$q['option_a_en'], $q['option_b_en'], $q['option_c_en']];
            if ($q['option_d_en'] !== null) $options_en[] = $q['option_d_en'];
        }

        return [
            'qid' => $q['qid'],
            'topic' => (int)$q['topic'],
            'year' => (int)$q['year'],
            'qnum' => (int)$q['qnum'],
            'sourceType' => $q['source_type'],
            'sourcePaper' => $q['source_paper'],
            'difficulty' => $q['difficulty'],
            'question' => $q['question'],
            'question_en' => $q['question_en'],
            'options' => $options,
            'options_en' => $options_en,
            'answer' => (int)$q['answer'],
            'explanation' => $q['explanation'],
            'explanation_en' => $q['explanation_en'],
            'markingNotes' => $q['marking_notes'],
            'markingNotes_en' => $q['marking_notes_en'],
            'topic_name_en' => $q['topic_name_en'],
        ];
    }, $questions);

    echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);

} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['error' => 'Database error: ' . $e->getMessage()]);
}
