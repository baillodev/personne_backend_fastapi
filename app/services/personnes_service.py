from app.core.database import get_db

def create_personne(data):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO personne (nom, prenom, age, photo) VALUES (%s, %s, %s, %s)",
        (data.nom, data.prenom, data.age, data.photo),
    )
    db.commit()
    cursor.close()
    db.close()

def fetch_personnes():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM personne")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def update_personne(personne_id: int, data):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        UPDATE personne
        SET nom=%s, prenom=%s, age=%s, photo=%s
        WHERE id=%s
        """,
        (data.nom, data.prenom, data.age, data.photo, personne_id),
    )
    db.commit()
    cursor.close()
    db.close()

def remove_personne(personne_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM personne WHERE id=%s", (personne_id,))
    db.commit()
    cursor.close()
    db.close()
