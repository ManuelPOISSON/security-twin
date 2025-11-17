query_select_adgroup_members_recursive = """
WITH RECURSIVE GroupHierarchy AS (
    -- Base case: Direct members of the group
    SELECT member_of AS group_id, member AS member_id
    FROM ADgroup_member_ADgroup
    WHERE member_of = '<adgroup_id>'
    UNION ALL
    -- Recursive case: Members of nested groups
    SELECT gm.member_of, gm.member
    FROM ADgroup_member_ADgroup gm
    INNER JOIN GroupHierarchy gh ON gm.member_of = gh.member_id
)
SELECT adu.id AS aduser_id, GROUP_CONCAT(adu.name) AS member_name
FROM ADgroup_member_ADuser gmu
JOIN ADuser adu ON gmu.member = adu.id
WHERE gmu.member_of IN (SELECT member_id FROM GroupHierarchy)
GROUP BY adu.id
UNION
SELECT adu.id AS aduser_id, adu.name AS member_name
FROM ADgroup_member_ADuser gmu
JOIN ADuser adu ON gmu.member = adu.id
WHERE gmu.member_of = '<adgroup_id>'
""".strip()

query_select_users_can_runas = """SELECT rc.id_machine, 
            COALESCE(u2.name, adu2.name) AS impersonator, 
            COALESCE(u2.id, adu2.id) AS impersonator_id, 
            COALESCE(u.name, adu.name) AS impersonated_name,
            COALESCE(u.id, adu.id) AS impersonated_id
            FROM runas_impersonated ri
            JOIN runas_creds rc ON ri.runas_id = rc.id
            LEFT JOIN user u ON ri.user_loc = u.id
            LEFT JOIN ADuser adu ON ri.user_AD = adu.id
            LEFT JOIN user u2 ON rc.can_runas_local = u2.id
            LEFT JOIN ADuser adu2 ON rc.can_runas_AD = adu2.id
        """.strip()

query_select_gpo_result = """
    SELECT GPOresult.id_machine, GPOresult.policy, sp_data.name, sp_data.id_sp
FROM GPOresult
JOIN (
    SELECT name, id AS id_sp
    FROM user
    UNION
    SELECT name, id
    FROM ADuser
    UNION
    SELECT name, id
    FROM `group`
    UNION
    SELECT name, id
    FROM ADgroup
) AS sp_data
ON GPOresult.id_sp = sp_data.id_sp
""".strip()
