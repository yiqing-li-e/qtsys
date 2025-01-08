INSERT INTO QTMNG.device_status (status_code, status) VALUES ('0', 'QT TESTING');
INSERT INTO QTMNG.device_status (status_code, status) VALUES ('2', 'LOAN');
INSERT INTO QTMNG.device_status (status_code, status) VALUES ('9', 'LOST');
INSERT INTO QTMNG.device_status (status_code, status) VALUES ('10', 'STOCKED');
INSERT INTO QTMNG.device_status (status_code, status) VALUES ('11', 'RETURNED TO HQ');

SELECT T.*,T.rowid FROM QTMNG.device_status T;



INSERT INTO QTMNG.device_battery (ID, status) VALUES ('00', 'NO');
INSERT INTO QTMNG.device_battery (ID, status) VALUES ('01', 'YES');
INSERT INTO QTMNG.device_battery (ID, status) VALUES ('10', 'BUILT-IN');
INSERT INTO QTMNG.device_battery (ID, status) VALUES ('99', 'UNKNOWN');
SELECT T.*, T.ROWID FROM QTMNG.device_battery T;

INSERT INTO QTMNG.device_category (ID, type) VALUES ('1', 'Reference Devices');
INSERT INTO QTMNG.device_category (ID, type) VALUES ('11', 'SD card');
INSERT INTO QTMNG.device_category (ID, type) VALUES ('10', 'Bluetooth devices');
INSERT INTO QTMNG.device_category (ID, type) VALUES ('13', 'N/A');
SELECT T.*, T.ROWID FROM QTMNG.device_category T;

INSERT INTO QTMNG.reimbursement_status (status) VALUES ('QT Dept Approval');
INSERT INTO QTMNG.reimbursement_status (status) VALUES ('Finance Dept Approval');
INSERT INTO QTMNG.reimbursement_status (status) VALUES ('Paid');
SELECT T.*, T.ROWID FROM QTMNG.reimbursement_status T;

