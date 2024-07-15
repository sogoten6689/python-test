-- Insert subscriptions
INSERT INTO user_subscription (user_id, keyword_id, subscription_type, start_time, end_time) VALUES
(1, 1, 'hourly', '2024-01-01 00:00:00', '2024-03-31 23:59:59'),
(1, 2, 'daily', '2024-01-01 00:00:00', '2024-03-31 23:59:59'),
(2, 1, 'daily', '2024-01-15 00:00:00', '2024-02-15 23:59:59'),
(2, 2, 'hourly', '2024-02-01 00:00:00', '2024-02-28 23:59:59');
