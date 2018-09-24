# Set up dev environment
Requirements
- Docker 

Step 0: Create a folder called "smart_contracts"
```
$ mkdir neo-tutorial/smart_contracts 
```

Step 1: Bring Up private net 
Run following command while you are in the smart_contracts folder
```
$ docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp -v "$(pwd)":/neo-python/smart_contracts cityofzion/neo-privatenet
```
Docker image: https://hub.docker.com/r/cityofzion/neo-privatenet/

Run `docker ps` to see if container is running
```
➜ docker ps
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                                                                        NAMES
d8c6821e7fb4        cityofzion/neo-privatenet   "/bin/bash /opt/run.…"   9 seconds ago       Up 7 seconds        0.0.0.0:20333-20336->20333-20336/tcp, 0.0.0.0:30333-30336->30333-30336/tcp   neo-privatenet
```

Step 2: ssh into container

```
➜  docker exec -it neo-privatenet /bin/bash

* Consensus nodes are running in screen sessions, check 'screen -ls'
* neo-python is installed in /neo-python, with a neo-privnet.wallet file in place
* You can use the alias 'neopy' in the shell to start neo-python's prompt.py with privnet settings
* Please report issues to https://github.com/CityOfZion/neo-privatenet-docker

root@d8c6821e7fb4:/neo-python#
```


Step 3: Open the Neo-python cli prompt with private net option
```
root@d8c6821e7fb4:/neo-python# neopy -p
Privatenet useragent '/NEO:2.7.6/', nonce: 1227527326
[I 180924 00:34:35 LevelDBBlockchain:114] Created Blockchain DB at /root/.neopython/Chains/privnet
[I 180924 00:34:35 NotificationDB:73] Created Notification DB At /root/.neopython/Chains/privnet_notif
NEO cli. Type 'help' to get started

neo>



[PrivateNet] Progress: 9403/9403

```

Step 4: Open Wallet
```
neo> open wallet neo-privnet.wallet
[password]>
```
Enter `coz` for password

Step 5: Sync wallet with the network
```
neo> wallet rebuild
```


Step 6: Compile .py contract file to .avm file and test
- neo> build /path/to/smartcontract.py/file test {input_types} {return_type} {needs_storage} {needs_dynamic_invoke} {test_param}
```
neo> build smart_contracts/domain.py test 0710 05 True False query ["bongani.com"]
neo> build smart_contracts/domain.py test 0710 05 True False register ["bongani.com","AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]
neo> build smart_contracts/domain.py test 0710 05 True False delete ["bongani.com"]
neo> build smart_contracts/domain.py test 0710 05 True False transfer ["bongani.com","AK2nJJpJr6o664CWJKi1QRXjqeic"]
```

Step 7:  Deploy contract
- import contract /path/to/smartcontract.avm/file INPUT_TYPES OUTPUT_TYPES NEEDS_STORAGE NEEDS_DYNAMIC_INVOKE
```
neo> import contract smart_contracts/domain.avm 0710 05 True False
Please fill out the following contract details:
[Contract Name] > DomainTutorial
[Contract Version] > 0.0.1
[Contract Author] > Bongani
[Contract Email] > sibandabongz@gmail.com
[Contract Description] > description
Creating smart contract....
  ......
  blah blah blah
  ......
-------------------------------------------------------------------------------------------------------------------------------------
Test deploy invoke successful
Total operations executed: 11
Results:
[<neo.Core.State.ContractState.ContractState object at 0x7feda18af780>]
Deploy Invoke TX GAS cost: 490.0
Deploy Invoke TX Fee: 0.0
-------------------------------------------------------------------------------------------------------------------------------------

Enter your password to continue and deploy this contract
[password]>
```
Enter wallet password to deploy

You can do a contract search
```
neo> contract search DomainTutorial
Found 1 results for DomainTutorial
{
    "version": 0,
    "code": {
        "hash": "0x4ff46372121d101ec66724c1459f8da62c39da14",
        "script": "011cc56b6a00527ac46a51527ac46a51c3c06a52527ac46a52c3009c643000174e6f20646f6d61696e206e616d6520737570706c696564680f4e656f2e52756e74696d652e4c6f67006c7566616a00c30571756572799c6416006a51c300c36a53527ac46a53c36535056c7566616a00c30664656c6574659c6416006a51c300c36a53527ac46a53c36504016c7566616a00c30872656769737465729c646c006a52c3529f64420029726571756972656420617267756d656e74733a205b646f6d61696e5f6e616d655d205b6f776e65725d680f4e656f2e52756e74696d652e4c6f67006c7566616a51c300c36a53527ac46a51c351c36a54527ac46a53c36a54c37c6558036c7566616a00c3087472616e736665729c6471006a52c3529f6447002e726571756972656420617267756d656e74733a205b646f6d61696e5f6e616d655d205b746f5f616464726573735d680f4e656f2e52756e74696d652e4c6f67006c7566616a51c300c36a53527ac46a51c351c36a55527ac46a53c36a55c37c653e016c756661006c75665fc56b6a00527ac40e44656c657465446f6d61696e3a206a00c37e6a51527ac46a51c368124e656f2e52756e74696d652e4e6f746966796168164e656f2e53746f726167652e476574436f6e74657874616a52527ac46a52c36a00c37c680f4e656f2e53746f726167652e476574616a53527ac46a53c36339001c446f6d61696e206973206e6f7420796574207265676973746572656468124e656f2e52756e74696d652e4e6f7469667961006c7566616a53c368184e656f2e52756e74696d652e436865636b5769746e657373616343002653656e646572206973206e6f7420746865206f776e65722c2063616e6e6f742064656c65746568124e656f2e52756e74696d652e4e6f7469667961006c7566616a52c36a00c37c68124e656f2e53746f726167652e44656c65746561516c75660113c56b6a00527ac46a51527ac4105472616e73666572446f6d61696e3a206a00c37e6a52527ac46a52c368124e656f2e52756e74696d652e4e6f746966796168164e656f2e53746f726167652e476574436f6e74657874616a53527ac46a53c36a00c37c680f4e656f2e53746f726167652e476574616a54527ac46a54c36339001c446f6d61696e206973206e6f7420796574207265676973746572656468124e656f2e52756e74696d652e4e6f7469667961006c7566616a54c368184e656f2e52756e74696d652e436865636b5769746e657373616345002853656e646572206973206e6f7420746865206f776e65722c2063616e6e6f74207472616e7366657268124e656f2e52756e74696d652e4e6f7469667961006c7566616a51c3c001229e63550038496e76616c6964206e6577206f776e657220616464726573732e204d7573742062652065786163746c79203334206368617261637465727368124e656f2e52756e74696d652e4e6f7469667961006c7566616a53c36a00c36a51c35272680f4e656f2e53746f726167652e50757461516c756660c56b6a00527ac46a51527ac4105265676973746572446f6d61696e3a206a00c37e6a52527ac46a52c368124e656f2e52756e74696d652e4e6f74696679616a51c368184e656f2e52756e74696d652e436865636b5769746e657373616349002c4f776e657220617267756d656e74206973206e6f74207468652073616d65206173207468652073656e64657268124e656f2e52756e74696d652e4e6f7469667961006c75666168164e656f2e53746f726167652e476574436f6e74657874616a53527ac46a53c36a00c37c680f4e656f2e53746f726167652e476574616a54527ac46a54c36439001c446f6d61696e20697320616c7265616479207265676973746572656468124e656f2e52756e74696d652e4e6f7469667961006c7566616a53c36a00c36a51c35272680f4e656f2e53746f726167652e50757461516c75665cc56b6a00527ac40d5175657279446f6d61696e3a206a00c37e6a51527ac46a51c368124e656f2e52756e74696d652e4e6f746966796168164e656f2e53746f726167652e476574436f6e74657874616a52527ac46a52c36a00c37c680f4e656f2e53746f726167652e476574616a53527ac46a53c36339001c446f6d61696e206973206e6f7420796574207265676973746572656468124e656f2e52756e74696d652e4e6f7469667961006c7566616a53c368124e656f2e52756e74696d652e4e6f74696679616a53c36c75665ec56b6a00527ac46a51527ac46a51c36a00c3946a52527ac46a52c3c56a53527ac4006a54527ac46a00c36a55527ac461616a00c36a51c39f6433006a54c36a55c3936a56527ac46a56c36a53c36a54c37bc46a54c351936a54527ac46a55c36a54c3936a00527ac462c8ff6161616a53c36c7566",
        "parameters": "0710",
        "returntype": 5
    },
    "name": "DomainTutorial",
    "code_version": "0.0.1",
    "author": "Bongani",
    "email": "sibandabongz@gmail.com",
    "description": "description",
    "properties": {
        "storage": true,
        "dynamic_invoke": false
    }
}
```

Step 8: Invoke Contract
```
neo> testinvoke 0x4ff46372121d101ec66724c1459f8da62c39da14 query ["bongani.com"]
neo> testinvoke 0x4ff46372121d101ec66724c1459f8da62c39da14 register ["bongani.com","AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]
neo> testinvoke 0x4ff46372121d101ec66724c1459f8da62c39da14 delete ["bongani.com"]
neo> testinvoke 0x4ff46372121d101ec66724c1459f8da62c39da14 transfer ["bongani.com","AZ9Bmz6qmboZ4ry1z8p2KF3ftyA2ckJAym"]
```
Example output:

```
neo> testinvoke 0x4ff46372121d101ec66724c1459f8da62c39da14 query ["bongani.com"]
[I 180924 11:35:18 EventHub:71] [test_mode][SmartContract.Storage.Get] [4ff46372121d101ec66724c1459f8da62c39da14] ["b'bongani.com' -> bytearray(b'')"]
[I 180924 11:35:18 EventHub:71] [test_mode][SmartContract.Runtime.Notify] [4ff46372121d101ec66724c1459f8da62c39da14] [b'QueryDomain: bongani.com']
[I 180924 11:35:18 EventHub:71] [test_mode][SmartContract.Runtime.Notify] [4ff46372121d101ec66724c1459f8da62c39da14] [b'Domain is not yet registered']
[I 180924 11:35:18 EventHub:71] [test_mode][SmartContract.Execution.Success] [4ff46372121d101ec66724c1459f8da62c39da14] [b'']
Used 0.178 Gas

-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 113
Results ['']
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
-------------------------------------------------------------------------------------------------------------------------------------

Enter your password to continue and invoke on the network

[password]>
```



