from db.run_sql import run_sql
from models.human import Human
from models.biting import Biting
import repositories.zombie_repository as zombie_repository
import repositories.human_repository as human_repository


def save(biting):
    sql = "INSERT INTO bitings ( zombie_id, human_id ) VALUES ( %s, %s) RETURNING id"
    values = [biting.zombie.id, biting.human.id]
    results = run_sql( sql, values )
    biting.id = results[0]['id']
    return biting

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)

    for result in results:
        human = human_repository.select(result['human_id'])
        zombie = zombie_repository.select(result['zombie_id'])
        biting = Biting(human, zombie, result['id'])
        bitings.append(biting)
    return bitings

def select(id):
    biting = None 
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        human = human_repository.select(result['human_id'])
        zombie = zombie_repository.select(result['zombie_id'])
        biting = Biting(human, zombie, result["id"])
    return biting

def update(biting):
    sql = "UPDATE bitings SET (zombie_id, human_id) = (%s, %s) WHERE id = %s"
    values = [biting.zombie.id, biting.human.id, biting.id]
    run_sql(sql, values)