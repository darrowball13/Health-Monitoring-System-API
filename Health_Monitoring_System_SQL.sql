CREATE TABLE `users` (
  `id` integer PRIMARY KEY,
  `first_name` varchar(255),
  `last_name` varchar(255),
  `ssn` varchar(255),
  `username` varchar(255),
  `password` varchar(255),
  `time_added` timestamp
);

CREATE TABLE `devices` (
  `id` integer PRIMARY KEY,
  `type` varchar(255),
  `added_on` timestamp
);

CREATE TABLE `user_roles` (
  `id` integer PRIMARY KEY,
  `user_id` integer,
  `role` varchar(255)
);

CREATE TABLE `user_devices` (
  `id` integer PRIMARY KEY,
  `assigner_id` integer,
  `patient_id` integer,
  `device_id` integer,
  `date_assigned` timestamp
);

CREATE TABLE `devices_data` (
  `id` integer PRIMARY KEY,
  `device_id` integer,
  `user_id` integer,
  `data_collected` varchar(255),
  `time_collected` timestamp
);

CREATE TABLE `appointment_history` (
  `id` integer PRIMARY KEY,
  `scheduler_id` integer,
  `doctor_id` integer,
  `patient_id` integer,
  `date_appoint` timestamp,
  `duration` time,
  `notes` text COMMENT 'Any comments from appointment',
  `time_created` timestamp
);

CREATE TABLE `patient_med_information` (
  `id` integer PRIMARY KEY,
  `entrant_id` integer,
  `user_id` integer,
  `data` varchar(255) COMMENT 'manual information input',
  `note` text COMMENT 'info regarding data added',
  `time_added` timestamp
);

CREATE TABLE `messages` (
  `id` integer PRIMARY KEY,
  `user_id` integer,
  `message` text COMMENT 'message to doctor',
  `file` file COMMENT 'any file patient uploaded with message',
  `time_added` timestamp
);

ALTER TABLE `patient_med_information` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `patient_med_information` ADD FOREIGN KEY (`entrant_id`) REFERENCES `users` (`id`);

ALTER TABLE `user_roles` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

CREATE TABLE `user_devices_devices` (
  `user_devices_device_id` integer,
  `devices_id` integer,
  PRIMARY KEY (`user_devices_device_id`, `devices_id`)
);

ALTER TABLE `user_devices_devices` ADD FOREIGN KEY (`user_devices_device_id`) REFERENCES `user_devices` (`device_id`);

ALTER TABLE `user_devices_devices` ADD FOREIGN KEY (`devices_id`) REFERENCES `devices` (`id`);


CREATE TABLE `user_devices_users` (
  `user_devices_assigner_id` integer,
  `users_id` integer,
  PRIMARY KEY (`user_devices_assigner_id`, `users_id`)
);

ALTER TABLE `user_devices_users` ADD FOREIGN KEY (`user_devices_assigner_id`) REFERENCES `user_devices` (`assigner_id`);

ALTER TABLE `user_devices_users` ADD FOREIGN KEY (`users_id`) REFERENCES `users` (`id`);


CREATE TABLE `user_devices_users(1)` (
  `user_devices_patient_id` integer,
  `users_id` integer,
  PRIMARY KEY (`user_devices_patient_id`, `users_id`)
);

ALTER TABLE `user_devices_users(1)` ADD FOREIGN KEY (`user_devices_patient_id`) REFERENCES `user_devices` (`patient_id`);

ALTER TABLE `user_devices_users(1)` ADD FOREIGN KEY (`users_id`) REFERENCES `users` (`id`);


ALTER TABLE `devices_data` ADD FOREIGN KEY (`device_id`) REFERENCES `devices` (`id`);

ALTER TABLE `devices_data` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `appointment_history` ADD FOREIGN KEY (`scheduler_id`) REFERENCES `users` (`id`);

ALTER TABLE `appointment_history` ADD FOREIGN KEY (`doctor_id`) REFERENCES `users` (`id`);

ALTER TABLE `appointment_history` ADD FOREIGN KEY (`patient_id`) REFERENCES `users` (`id`);

ALTER TABLE `messages` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
