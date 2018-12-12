sector_code
-----------
attribute(get_feature('sectors', 'name', attribute(get_feature('wall_parts', 'name', "wall_part"), 'sector')), 'name')

monument_code
-------------
attribute(get_feature('sectors', 'name', attribute(get_feature('wall_parts', 'name', "wall_part"), 'sector')), 'monument')

monument_name
-------------
attribute(get_feature('monuments', 'code', attribute(get_feature('sectors', 'name', attribute(get_feature('wall_parts', 'name', "wall_part"), 'sector')), 'monument')), 'name')

Filename
--------
@surveydate||'_'||attribute(get_feature('sectors', 'name', attribute(get_feature('wall_parts', 'name', "wall_part"), 'sector')), 'monument')||'_'||"name"||'_'||replace(@surveyname, ' ', '-')||'_DAO'

Scale_Simple
------------
(round(1.8* bounds_width( $geometry )/5))* 5

Scale_Standard
--------------
with_variable('scale_feature', (round(1.8* bounds_width( $geometry )/5))* 5 , if(@scale_feature < 5, 10, @scale_feature))

Scale_ConsideringFormat
-----------------------
if(bounds_height($geometry) / bounds_width($geometry) < 0.7, with_variable('scale_feature', (round(1.8* bounds_width( $geometry )/5))* 5 , if(@scale_feature < 10, 10, @scale_feature)), with_variable('scale_feature', (round(2.57* bounds_height( $geometry )/5))* 5 , if(@scale_feature < 10, 10, @scale_feature)))
