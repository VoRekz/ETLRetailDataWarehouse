/*
SET SQL_SAFE_UPDATES = 0;

UPDATE storenames
SET Region = CASE
    WHEN State IN ('Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania', 'Rhode Island', 'Vermont') THEN 'Northeast'
    WHEN State IN ('Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin') THEN 'Midwest'
    WHEN State IN ('Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia', 'District of Columbia') THEN 'South'
    WHEN State IN ('Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Oregon', 'Utah', 'Washington', 'Wyoming') THEN 'West'
    ELSE Region -- Keeps current value if state isn't listed
END;

SET SQL_SAFE_UPDATES = 1;


*/
Select * from storenames
