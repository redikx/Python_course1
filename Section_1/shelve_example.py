import shelve

recipes={
	"tort" : ["jajko", "maka", "biszkopt", "cukier"],
	"spaghetti" : ["pasta", "pomidory", "czosnek"],
	"mielone" : ["mieso", "groszek", "marchewka"]
}

# Create shelve and insert recipes
recshelve = shelve.open("recshelve")
recshelve["recipes"]=recipes

val_int = 666
recshelve["diablo"]=666

val_int2 = recshelve["diablo"]
print(val_int2)
