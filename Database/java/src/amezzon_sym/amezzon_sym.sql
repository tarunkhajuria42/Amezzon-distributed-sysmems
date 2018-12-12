DELETE
FROM sym_trigger_router;
DELETE
FROM sym_trigger;
DELETE
FROM sym_channel
WHERE channel_id IN ('amezzon');
DELETE
FROM sym_node_group_link;
DELETE
FROM sym_node_group;
DELETE
FROM sym_node_host;
DELETE
FROM sym_node_identity;
DELETE
FROM sym_node_security;
DELETE
FROM sym_node;

INSERT INTO sym_channel(channel_id, processing_order, max_batch_size, enabled, description)
VALUES ('amezzon', 1, 100000, 1, 'Amezzon Database instance replication');

INSERT INTO sym_node_group (node_group_id)
VALUES ('amezzon1');
INSERT INTO sym_node_group (node_group_id)
VALUES ('amezzon2');
INSERT INTO sym_node_group (node_group_id)
VALUES ('amezzon3');

INSERT INTO sym_node_group_link (source_node_group_id, target_node_group_id, data_event_action)
VALUES
  ('amezzon1', 'amezzon2', 'P'),
  ('amezzon1', 'amezzon3', 'P');
INSERT INTO sym_node_group_link (source_node_group_id, target_node_group_id, data_event_action)
VALUES
  ('amezzon2', 'amezzon1', 'P'),
  ('amezzon2', 'amezzon3', 'P');
INSERT INTO sym_node_group_link (source_node_group_id, target_node_group_id, data_event_action)
VALUES
  ('amezzon3', 'amezzon1', 'P'),
  ('amezzon3', 'amezzon2', 'P');

INSERT INTO sym_trigger (trigger_id, source_table_name, channel_id, last_update_time, create_time)
VALUES
  ('person', 'person', 'amezzon', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  ('product', 'product', 'amezzon', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  ('product_history', 'product_history', 'amezzon', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  ('product_type', 'product_type', 'amezzon', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  ('transaction', 'transaction', 'amezzon', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  ('transaction_type', 'transaction_type', 'amezzon', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO sym_router (router_id, source_node_group_id, target_node_group_id, router_type, create_time,
                        last_update_time)
VALUES
('amezzon1-to-amezzon2', 'amezzon1', 'amezzon2', 'default', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('amezzon1-to-amezzon3', 'amezzon1', 'amezzon3', 'default', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('amezzon2-to-amezzon1', 'amezzon2', 'amezzon1', 'default', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('amezzon2-to-amezzon3', 'amezzon2', 'amezzon3', 'default', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('amezzon3-to-amezzon1', 'amezzon3', 'amezzon1', 'default', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('amezzon3-to-amezzon2', 'amezzon3', 'amezzon2', 'default', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO sym_trigger_router (trigger_id, router_id, initial_load_order, last_update_time, create_time)
VALUES
('person', 'amezzon1-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('person', 'amezzon1-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('person', 'amezzon2-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('person', 'amezzon2-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('person', 'amezzon3-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('person', 'amezzon3-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product', 'amezzon1-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product', 'amezzon1-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product', 'amezzon2-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product', 'amezzon2-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product', 'amezzon3-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product', 'amezzon3-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_history', 'amezzon1-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_history', 'amezzon1-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_history', 'amezzon2-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_history', 'amezzon2-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_history', 'amezzon3-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_history', 'amezzon3-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_type', 'amezzon1-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_type', 'amezzon1-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_type', 'amezzon2-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_type', 'amezzon2-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_type', 'amezzon3-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('product_type', 'amezzon3-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction', 'amezzon1-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction', 'amezzon1-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction', 'amezzon2-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction', 'amezzon2-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction', 'amezzon3-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction', 'amezzon3-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction_type', 'amezzon1-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction_type', 'amezzon1-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction_type', 'amezzon2-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction_type', 'amezzon2-to-amezzon3', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction_type', 'amezzon3-to-amezzon1', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('transaction_type', 'amezzon3-to-amezzon2', 100, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO sym_node (node_id, node_group_id, external_id, sync_enabled, sync_url, schema_version, symmetric_version,
                      database_type, database_version, heartbeat_time, timezone_offset, batch_to_send_count,
                      batch_in_error_count, created_at_node_id)
VALUES
('001', 'amezzon1', '001', 1, NULL, NULL, NULL, NULL, NULL, CURRENT_TIMESTAMP, NULL, 0, 0, '001'),
('002', 'amezzon2', '002', 1, NULL, NULL, NULL, NULL, NULL, CURRENT_TIMESTAMP, NULL, 0, 0, '001'),
('003', 'amezzon3', '003', 1, NULL, NULL, NULL, NULL, NULL, CURRENT_TIMESTAMP, NULL, 0, 0, '001');

INSERT INTO sym_node_security (node_id, node_password, registration_enabled, registration_time, initial_load_enabled,
                               initial_load_time, created_at_node_id)
VALUES
('001', '5d1c92bbacbe2edb9e1ca5dvv0e481', 0, CURRENT_TIMESTAMP, 0, CURRENT_TIMESTAMP, '001'),
('002', '5d1c92bbacbe2edb9e1ca5dvv0e481', 1, NULL, 1, NULL, '001'),
('003', '5d1c92bbacbe2edb9e1ca5dvv0e481', 1, NULL, 1, NULL, '001');
