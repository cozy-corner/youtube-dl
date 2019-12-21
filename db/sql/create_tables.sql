---- drop ----
DROP TABLE IF EXISTS `youtube`;

---- create ----
create table IF not exists `youtube`
(
 `id`               INT(20) AUTO_INCREMENT,
 `videoId`          VARCHAR(20) NOT NULL,
 `title`            TEXT NOT NULL,
 `description`      TEXT NOT NULL,
 `channel_id`       VARCHAR(255) NOT NULL,
 you`publishedAt`      Datetime DEFAULT NULL,
 `created_at`       Datetime DEFAULT NULL,
 `updated_at`       Datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;