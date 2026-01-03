from app.db.connection import get_db_connection


def get_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    cols = [desc[0] for desc in cursor.description]  # type: ignore
    rows = cursor.fetchall()

    users = []
    for row in rows:
        users.append(dict(zip(cols, row)))

    cursor.close()
    conn.close()

    return users


def create_user(email: str, full_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (email, full_name) VALUES (%s, %s) RETURNING *",
        (email, full_name),
    )

    cols = [desc[0] for desc in cursor.description]  # type: ignore
    row = cursor.fetchone()
    user = dict(zip(cols, row))  # type: ignore

    conn.commit()
    cursor.close()
    conn.close()

    return user


def get_user_by_id(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

    cols = [desc[0] for desc in cursor.description]  # type: ignore
    row = cursor.fetchone()

    user = None
    if row:
        user = dict(zip(cols, row))

    cursor.close()
    conn.close()

    return user


def delete_user_by_id(user_id: int):
    conn = get_db_connection()  
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = %s RETURNING *", (user_id,))

    cols = [desc[0] for desc in cursor.description]  # type: ignore
    row = cursor.fetchone()

    deleted_user = None
    if row:
        deleted_user = dict(zip(cols, row))

    conn.commit()
    cursor.close()
    conn.close()

    return deleted_user
