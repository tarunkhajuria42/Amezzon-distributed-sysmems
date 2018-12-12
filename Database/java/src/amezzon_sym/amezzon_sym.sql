DELETE
FROM syn_trigger_router;
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

INSERT INTO sym_channel(channel_id, processinorder, max_batch_size, enabled, description)
VALUES ('amezzon', 1, 100000, 1, 'Amezzon Database instance replication');

INSERT INTO sym_node_group (node_group_id)
VALUES ('amezzon1');
INSERT INTO sym_node_group (node_group_id)
VALUES ('amezzon2');
INSERT INTO sym_node_group (node_group_id)
VALUES ('amezzon3');

INSERT INTO sym_node_group_link (source_node_group_id, target_node_group_id, data_event_action)
VALUES ('amezzon1', 'amezzon2', 'P');
INSERT INTO sym_node_group_link (source_node_group_id, target_node_group_id, data_event_action)
VALUES ('amezzon1', 'amezzon3', 'P');
