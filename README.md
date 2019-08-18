### Description

this TA brings a command | mkuuid which creates a random uuid/guid in like

"04ec1964-b286-405f-a11c-c7d7872e36ba"

### Usage

- add a guid 
```
index=_internal | head 20 | mkuuid
```

- add a guid per event
```
index=_internal | head 20 | mkuuid perevent=t
```

There is one parameters:

* perevent: defines if a guid should be created per Events

