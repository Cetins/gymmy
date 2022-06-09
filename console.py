import pdb
from models.member import Member
import repositories.member_repository as member_repository

member_1 = Member("Charlie", False, True)
member_repository.save(member_1)


pdb.set_trace()