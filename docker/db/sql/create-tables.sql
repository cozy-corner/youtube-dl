DROP TABLE IF EXISTS `youtube`;

create table IF not exists `youtube`
(
 `id`               INT(20) AUTO_INCREMENT,
 `videoId`          VARCHAR(20) UNIQUE,
 `title`            TEXT NOT NULL,
 `description`      TEXT NOT NULL,
 `channel_id`       VARCHAR(255) NOT NULL,
 `publishedAt`      Datetime DEFAULT NULL,
 `download_url`     TEXT DEFAULT NULL,
 `created_at`       Datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
 `updated_at`       Datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;