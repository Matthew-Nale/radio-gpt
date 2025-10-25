USE RadioGPT;


DROP TABLE IF EXISTS `ChatHistory`;
CREATE TABLE `ChatHistory` (
  `chat_id` int AUTO_INCREMENT PRIMARY KEY,
  `user_id` varchar(100) NOT NULL,
  `title` tinytext NOT NULL,
  `conversation` mediumtext NOT NULL
);


DROP TABLE IF EXISTS `WhitelistedUsers`;
CREATE TABLE `WhitelistedUsers` (
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `discord_id` bigint UNIQUE,
  `username` varchar(100) NOT NULL
);


DROP TABLE IF EXISTS `Users`;
CREATE TABLE Users (
    `id` int AUTO_INCREMENT PRIMARY KEY,
    `discord_id` bigint UNIQUE,
    `username` varchar(100),
    `avatar_url` varchar(255),
    `access_token` text,
    `refresh_token` text,
    `token_expires_at` DATETIME,
    `last_login` DATETIME DEFAULT CURRENT_TIMESTAMP
);


DROP TABLE IF EXISTS `UserSettings`;
CREATE TABLE `UserSettings` (
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `username` varchar(32) NOT NULL
);
