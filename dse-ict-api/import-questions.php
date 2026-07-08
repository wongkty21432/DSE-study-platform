<?php
/**
 * DSE Study Platform - Import Questions from JSON to MySQL
 *
 * Usage:
 *   php import-questions.php          # imports both subjects
 *   php import-questions.php chem     # imports only chemistry
 *   php import-questions.php ict      # imports only ICT
 *
 * Place the JSON files in the same directory or update paths below.
 */

require_once __DIR__ . '/config.php';

$json_files = [
    'chem' => __DIR__ . '/../chem/questions-chem.json',
    'ict'  => __DIR__ . '/../ict/questions-ict.json',
];

// Allow filtering by subject
$target = $argv[1] ?? null;
if ($target && isset($json_files[$target])) {
    $json_files = [$target => $json_files[$target]];
}

$db = getDB();
$imported = 0;
$skipped = 0;
$errors = 0;

foreach ($json_files as $subject => $path) {
    if (!file_exists($path)) {
        echo "SKIP: JSON file not found: $path\n";
        continue;
    }

    echo "Reading $subject questions from: $path\n";
    $json = file_get_contents($path);
    $questions = json_decode($json, true);

    if (!$questions) {
        echo "ERROR: Invalid JSON in $path\n";
        $errors++;
        continue;
    }

    echo "Found " . count($questions) . " questions for $subject\n";

    $sql = 'INSERT INTO questions
        (qid, subject, topic, year, qnum, source_type, source_paper, difficulty,
         question, question_en,
         option_a, option_b, option_c, option_d,
         option_a_en, option_b_en, option_c_en, option_d_en,
         answer, explanation, explanation_en,
         marking_notes, marking_notes_en, topic_name_en)
        VALUES
        (:qid, :subject, :topic, :year, :qnum, :source_type, :source_paper, :difficulty,
         :question, :question_en,
         :option_a, :option_b, :option_c, :option_d,
         :option_a_en, :option_b_en, :option_c_en, :option_d_en,
         :answer, :explanation, :explanation_en,
         :marking_notes, :marking_notes_en, :topic_name_en)
        ON DUPLICATE KEY UPDATE
        topic=VALUES(topic), year=VALUES(year), difficulty=VALUES(difficulty),
        question=VALUES(question), question_en=VALUES(question_en),
        option_a=VALUES(option_a), option_b=VALUES(option_b),
        option_c=VALUES(option_c), option_d=VALUES(option_d),
        option_a_en=VALUES(option_a_en), option_b_en=VALUES(option_b_en),
        option_c_en=VALUES(option_c_en), option_d_en=VALUES(option_d_en),
        answer=VALUES(answer), explanation=VALUES(explanation),
        explanation_en=VALUES(explanation_en),
        marking_notes=VALUES(marking_notes), marking_notes_en=VALUES(marking_notes_en),
        topic_name_en=VALUES(topic_name_en)';

    $stmt = $db->prepare($sql);

    foreach ($questions as $q) {
        $options = $q['options'] ?? [];
        $options_en = $q['options_en'] ?? [];

        try {
            $stmt->execute([
                'qid' => $q['qid'],
                'subject' => $subject,
                'topic' => (int)($q['topic'] ?? 0),
                'year' => (int)($q['year'] ?? 0),
                'qnum' => (int)($q['qnum'] ?? 0),
                'source_type' => $q['sourceType'] ?? 'mc',
                'source_paper' => $q['sourcePaper'] ?? '1A',
                'difficulty' => $q['difficulty'] ?? 'medium',
                'question' => $q['question'] ?? '',
                'question_en' => $q['question_en'] ?? null,
                'option_a' => $options[0] ?? '',
                'option_b' => $options[1] ?? '',
                'option_c' => $options[2] ?? '',
                'option_d' => $options[3] ?? null,
                'option_a_en' => $options_en[0] ?? null,
                'option_b_en' => $options_en[1] ?? null,
                'option_c_en' => $options_en[2] ?? null,
                'option_d_en' => $options_en[3] ?? null,
                'answer' => (int)($q['answer'] ?? 0),
                'explanation' => $q['explanation'] ?? '',
                'explanation_en' => $q['explanation_en'] ?? null,
                'marking_notes' => $q['markingNotes'] ?? null,
                'marking_notes_en' => $q['markingNotes_en'] ?? null,
                'topic_name_en' => $q['topic_name_en'] ?? null,
            ]);
            $imported++;
        } catch (PDOException $e) {
            echo "ERROR on {$q['qid']}: " . $e->getMessage() . "\n";
            $errors++;
        }
    }

    echo "Done: $subject — imported $imported questions, $errors errors\n";
}

echo "\n=== Import Summary ===\n";
echo "Total imported/updated: $imported\n";
echo "Total errors: $errors\n";

// Update count
$stmt = $db->query('SELECT subject, COUNT(*) as cnt FROM questions GROUP BY subject');
echo "\nQuestions in database:\n";
while ($row = $stmt->fetch()) {
    echo "  {$row['subject']}: {$row['cnt']} questions\n";
}
