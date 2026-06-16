-- DSE Study Platform - Question Bank Database Schema
-- Import this into your MySQL/MariaDB database

CREATE DATABASE IF NOT EXISTS dse_study_platform CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE dse_study_platform;

-- Questions table: stores all MC questions for all subjects
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    qid VARCHAR(20) NOT NULL UNIQUE,
    subject VARCHAR(10) NOT NULL COMMENT 'ict or chem',
    topic INT NOT NULL COMMENT 'Topic number 1-13',
    year INT NOT NULL,
    qnum INT NOT NULL COMMENT 'Question number in original paper',
    source_type VARCHAR(10) DEFAULT 'mc' COMMENT 'mc or converted',
    source_paper VARCHAR(5) DEFAULT '1A' COMMENT '1A, 1B, 2, etc.',
    difficulty ENUM('easy','medium','hard') NOT NULL DEFAULT 'medium',
    question TEXT NOT NULL COMMENT 'Question text (Chinese)',
    question_en TEXT DEFAULT NULL COMMENT 'Question text (English)',
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT DEFAULT NULL,
    option_a_en TEXT DEFAULT NULL,
    option_b_en TEXT DEFAULT NULL,
    option_c_en TEXT DEFAULT NULL,
    option_d_en TEXT DEFAULT NULL,
    answer TINYINT NOT NULL COMMENT '0=A, 1=B, 2=C, 3=D',
    explanation TEXT NOT NULL COMMENT 'Explanation (Chinese)',
    explanation_en TEXT DEFAULT NULL COMMENT 'Explanation (English)',
    marking_notes TEXT DEFAULT NULL COMMENT 'Marking scheme notes (Chinese)',
    marking_notes_en TEXT DEFAULT NULL COMMENT 'Marking scheme notes (English)',
    topic_name_en VARCHAR(100) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_subject (subject),
    INDEX idx_topic (topic),
    INDEX idx_year (year),
    INDEX idx_difficulty (difficulty),
    INDEX idx_subject_topic (subject, topic),
    INDEX idx_subject_year (subject, year)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Performance tracking per user per topic
CREATE TABLE IF NOT EXISTS user_performance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    subject VARCHAR(10) NOT NULL,
    topic INT NOT NULL,
    total_attempted INT DEFAULT 0,
    total_correct INT DEFAULT 0,
    mastery_level ENUM('new','novice','developing','proficient','advanced','master') DEFAULT 'new',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY uk_user_subject_topic (user_id, subject, topic),
    INDEX idx_user (user_id)
) ENGINE=InnoDB;

-- Answer history per user
CREATE TABLE IF NOT EXISTS answer_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    qid VARCHAR(20) NOT NULL,
    selected_option TINYINT NOT NULL,
    is_correct TINYINT(1) NOT NULL,
    answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_user_qid (user_id, qid),
    INDEX idx_answered_at (answered_at)
) ENGINE=InnoDB;

-- Users table (if not already existing)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) DEFAULT NULL,
    role ENUM('user','admin') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
