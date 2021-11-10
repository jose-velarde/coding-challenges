SELECT group_id,
  player_id
FROM (
    SELECT group_id,
      player_id,
      ROW_NUMBER() OVER (
        PARTITION BY group_id
        ORDER BY group_id
      ) AS row_number,
      SUM(score) AS total_score
    FROM (
        SELECT *,
          CASE
            WHEN players.player_id = matches.first_player THEN first_score
            WHEN players.player_id = matches.second_player THEN second_score
          END AS score
        FROM players
          LEFT JOIN matches ON players.player_id = matches.first_player
          OR players.player_id = matches.second_player
      ) players_score
    GROUP BY group_id,
      player_id
  ) etc
WHERE row_number = 1
ORDER BY group_id,
  total_score DESC,
  player_id