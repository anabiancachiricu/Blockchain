import datetime
import hashlib

#definim o clasa block pentru blocurile din blockchain
class Block():
    #fiecare bloc contine index, timpul cand a fost creat, informatia pe care o detine si hash-ul blocului anterior
    def __init__(self, index, timestamp, data, previoushash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previoushash = previoushash
        self.hash = self.hashblock()

    #defimim o functie de hash pentru a salva has-ul specific fiecarui bloc
    def hashblock(self):
        #flosim functia de sha256 din hashlib
        block_encryption = hashlib.sha256()
        #semnatura blocului este obtinuta din adunarea indexului, timestampului, informatiei si hashului anterior
        block_encryption.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previoushash).encode('utf-8'))
        return block_encryption.hexdigest()

    #definim o metoda pentru primul bloc
    #acesta este initializat diferit pentru ca nu are bloc anterior de care sa se lege
    @staticmethod
    def genesisblock():
        #prevhash=h.sha256()
        #prevhash.update(str("0"))
        #consideram ca primul bloc are indexul 0 si nu are hash anterior
        return Block(0, datetime.datetime.now(), "genesis block transaction", " ")  # return the genesis block

    #definim o functie pentru a adauga un nou bloc in blochain
    #acesta se creaza in functie de blocul precedent primit drept parametru
    #prevoiushash primeste hash-ul blocului precedent
    def newblock(lastblock):
        index = lastblock.index + 1
        timestamp = datetime.datetime.now()
        previoushash= lastblock.hash
        data = "Transaction " + str(index)
        return Block(index, timestamp, data, previoushash)

#initializam blockchain-ul ca o lista de blocuri pornind de la primul bloc
blockchain=[Block.genesisblock()]
#consideram primul bloc drept bloc precedent pentru urmatorul
prevblock = blockchain[0]

#afisam toate informatiile despre primul bloc
print("Block ID ", prevblock.index)
print("Timestamp", prevblock.timestamp)
print("Hash of the block:", prevblock.hash)
print("Previous Block Hash:", prevblock.previoushash)
print("data:", prevblock.data)
print("\n")

#adaugam mai multe blocuri in blockchain
for i in range(0,3):
    #folosim functia de newblock pentru a adauga mai multe blocuri
    blocnou = Block.newblock(prevblock)
    #adaugam blocul nou creat la blockchain
    blockchain.append(blocnou)
    #actualizam blocul anterior pentru a ne lega corect in moemntul adaugarii altui bloc
    prevblock = blocnou

    #afisam blocul adaugat
    print("Block ID ", blocnou.index)
    print("Timestamp:", blocnou.timestamp)
    print("Hash of the block:",blocnou.hash)
    print("Previous Block Hash:",blocnou.previoushash)
    print("data:", blocnou.data)
    print("\n")