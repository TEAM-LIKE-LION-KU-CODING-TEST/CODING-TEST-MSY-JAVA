SELECT patient_id, patient_name, conditions
FROM Patients
-- ^DIAB1는 해당 증상으로 시작하는 이름일 경우, 왼쪽 공백이 있는 경우 (condition 내 다른 문장 존재)
WHERE REGEXP_LIKE(conditions, '^DIAB1| DIAB1')