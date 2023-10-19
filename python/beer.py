from typing import NamedTuple
import csv


class Beer(NamedTuple):
    """Represents the expected values for common American style brews."""
    name: str
    abv_: float
    abv: float
    ibu_: int
    ibu: int
    og_: float
    og: float
    tg_: float
    tg: float
    srm_: float
    srm: float

store = {}
for key, beer in enumerate(map(Beer._make, csv.reader(open("beer.csv", "r")))):
    if beer.name != "style":
        store[key-1] = beer._replace(**{k: float(getattr(beer, k)) for k in
            ["abv_", "abv", "og_", "og", "tg_", "tg", "srm_", "srm"]})._replace(
            **{k: int(getattr(beer, k)) for k in ["ibu", "ibu_"]})


if __name__ == "__main__":
    print([(key, store[key].name) for key in store.keys()])
    key = int(input("What is the brew?"))
    abv = float(input("What is the ABV?"))
    b = store[key]
    v = (abv - b.abv_) / (b.abv - b.abv_)
    ibu = (v * (b.ibu - b.ibu_) + b.ibu_ + 0.5) // 1
    og = ((v * (b.og - b.og_) + b.og_) * 1e3 + 0.5) // 1 / 1e3
    tg = ((v * (b.tg - b.tg_) + b.tg_) * 1e3 + 0.5) // 1 / 1e3
    srm = (v * (b.srm - b.srm_) + b.srm_ + 0.5) // 1
    print("{:} -> ibu = {:}, og = {:}, tg = {:}, srm = {:}".format(v, ibu, og, tg, srm))
