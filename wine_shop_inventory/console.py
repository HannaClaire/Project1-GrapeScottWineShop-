import pdb
from models.wine import Wine
from models.producer import Producer

import repositories.wine_repository as wine_repo
import repositories.producer_repository as producer_repo

# wine_repo.delete_all()
# producer_repo.delete_all()

producer1 = Producer("FancyPants")
producer_repo.save(producer1)

wine1 = Wine("Pinot Gris", "White - medium/full-bodied, Notes & flavours: delicate/floral aromatics; round feel, nutty/spicy, pears/melon on palette.", 6, 15, 18, producer1.id)  
wine_repo.save(wine1)

wine2 = Wine("Pinot Noir", "Red - light/medium-bodied, Notes & flavours: red fruits/spicey aromas, red fruits, clove, hibiscus, umami on palette.", 15, 13, 17, producer1.id)
wine_repo.save(wine2)

wine3 = Wine("Pinot Blanc", "White - medium/full-bodies, Notes & flavours: floral aromas, round feel, peaches/pears/almonds and slight minerality on the palette.", 0, 18, 21, producer1.id)
wine_repo.save(wine3)