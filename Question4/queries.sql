-- Question 4.1
SELECT SUM(balance) as "Total Sum", policy_type 
FROM policy 
GROUP BY policy_type;

-- Question 4.2
SELECT SUM(amount) as "Total of Sum", tran_type_id, id 
FROM acc_tran 
GROUP BY tran_type_id, id 
ORDER BY id;

-- Question 4.3
SELECT a.name, p.balance AS "Policy Balance" 
FROM account AS a
JOIN policy AS p 
ON a.id = p.account_id
GROUP BY a.name, p.balance;

-- Question 4.4
SELECT a.name, p.balance 
FROM account AS a
JOIN policy AS p ON a.id = p.account_id
JOIN acc_tran AS t ON p.id = t.policy_id
WHERE p.balance <> SUM(t.amount)
GROUP BY a.name, p.balance
ORDER BY a.name DESC;


