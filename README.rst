Wifi Testbed Module Repository
========================

The highest level APIs for wifi testbed.

Example
-------

.. code:: python

    import testbed
    # Use wifi nodes CC3200
    c = testbed.WiFi() 

    # Choose wifi sniffer project
    if c.conf.change_instance('sniffer') :
        # Set channel to 2
        c.radio.set_channel('2')
    else:
        print 'Change library failed!'

    # in another process start all the nodes and get data
    ret = c.conf.start('dc1', 'all')

    if ret == 'OK':

        consumer = c.conf.get_data('dc1', 'all')
        for message in consumer:
            if message is not None:
            print message.value
    else:
        print 'Some nodes can't be started'

    

`Learn more <http://www.onewrt.com/armhf-docker-swarm-cluster-with-consulregistrator>`_.
