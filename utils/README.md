round_shape_pillars.py creates glass tube on the inrun from x1=2 to x2=18.
example usage of round_shape_pillars.py

```{bash}
python round_shape_pillars.py 64 4.03 4.08 '-110' 110 3 -1 'test_upper_glass.xml'
```

* 64 - create a ring with 64 pillars
* 4.03 4.08 - create a ring with 0.05 thickness. 4.03 is a radius of a inside tube, 4.08 is a radius outside

* -110 - radius from
* 110 - radius to. For example, to create the whole tube use radius from= -180 radius to= 180. To create only upper half use radius from=-90 radius to=90
* 3 - tube height above inrun
* -1 z offset
