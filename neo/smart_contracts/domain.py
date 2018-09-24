# Can find all functions you can import here:
# https://github.com/neo-project/docs/tree/master/en-us/sc/reference/fw/dotnet/neo

from boa.builtins import concat
from boa.interop.Neo.Runtime import CheckWitness
from boa.interop.Neo.Runtime import Notify
from boa.interop.Neo.Storage import Get, Put, GetContext, Delete


def main(operation, args):
    """ Main entry for smart contract.

    Args:
        operation(str): a function your want to invoke
        args(list): list of arguments
            :args[0] domain name
            :args[1] address
    """
    nargs = len(args)
    if nargs == 0:
        print("No domain name supplied")
        return 0

    if operation == 'query':
        domain_name = args[0]
        return query_domain(domain_name)

    elif operation == 'delete':
        domain_name = args[0]
        return delete_domain(domain_name)

    elif operation == 'register':
        if nargs < 2:
            print("required arguments: [domain_name] [owner]")
            return 0
        domain_name = args[0]
        owner = args[1]
        return register_domain(domain_name, owner)

    elif operation == 'transfer':
        if nargs < 2:
            print("required arguments: [domain_name] [to_address]")
            return 0
        domain_name = args[0]
        to_address = args[1]
        return transfer_domain(domain_name, to_address)


def query_domain(domain_name):
    msg = concat("QueryDomain: ", domain_name)
    Notify(msg)

    context = GetContext()  # Used to interact with the correct storage
    owner = Get(context, domain_name)
    if not owner:
        Notify("Domain is not yet registered")
        return False

    Notify(owner)
    return owner


def register_domain(domain_name, owner):
    msg = concat("RegisterDomain: ", domain_name)
    Notify(msg)

    if not CheckWitness(owner):
        Notify("Owner argument is not the same as the sender")
        return False

    context = GetContext()
    exists = Get(context, domain_name)
    if exists:
        Notify("Domain is already registered")
        return False

    Put(context, domain_name, owner)
    return True


def transfer_domain(domain_name, to_address):
    msg = concat("TransferDomain: ", domain_name)
    Notify(msg)

    context = GetContext()
    # check if domain exist
    owner = Get(context, domain_name)
    if not owner:
        Notify("Domain is not yet registered")
        return False

    # check if the owner is the person who invoked the function
    if not CheckWitness(owner):
        Notify("Sender is not the owner, cannot transfer")
        return False

    # validate the new address
    if not len(to_address) != 34:
        Notify("Invalid new owner address. Must be exactly 34 characters")
        return False

    # replace previous address with new address
    Put(context, domain_name, to_address)
    return True


def delete_domain(domain_name):
    msg = concat("DeleteDomain: ", domain_name)
    Notify(msg)

    context = GetContext()
    owner = Get(context, domain_name)
    # check if domain exist
    if not owner:
        Notify("Domain is not yet registered")
        return False

    # check if the owner is the person invoked
    if not CheckWitness(owner):
        Notify("Sender is not the owner, cannot delete")
        return False

    Delete(context, domain_name)
    return True
