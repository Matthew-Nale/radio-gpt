from .extensions import mysql

def is_whitelisted(discord_id, username):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT * FROM WhitelistedUsers
        WHERE discord_id = %s
        AND username = %s
        """,
        (discord_id, username)
    )

    result = cur.fetchone()
    cur.close()

    return bool(result)


def store_discord_tokens(id, username, avatar_url, access_token, refresh_token, expires_in):
    return 0