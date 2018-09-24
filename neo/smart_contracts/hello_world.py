from boa.interop.Neo.Runtime import CheckWitness


def main():
    owner = b"031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf4a"

    # return true if the owner of the contract is the one calling it

    if CheckWitness(owner):
        print("He is the owner")
        return True

    return False
