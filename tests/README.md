# Tests

## Tests-list

### 内部测试用例

1. test_load

这组测试用例用于检查Yuheng能否正常加载来自不同来源的osm、osh、osc文件。

They are all real data export by OSM Website or other well-known OSM editor, such as JOSM, level0. iD/RapiD 's exported `.osc` file will be supported soon.

为实现交叉验证，提供不通过Yuheng的方法来验证数目。用功能无错误的文本编辑器或IDE搜索`<bound`, `<node`, `<way`, `<relation`并分别计数，作为对应元素的数量，看Yuheng是否能正常加载。

NOTE！测试用例目录未来可能会重置，届时请注意调整目录结构！

2. test_iterator

这组测试用例用于检查循环器是否能正常迭代。通常在满足第一组测试用例的情况下是可以的。


单元测试中使用的数据由OSM导出，
所有数据均按照 [开放数据共享开放数据库许可协议 (ODbL)](https://opendatacommons.org/licenses/odbl/summary/)
进行授权
- `OSMWebsite_export.osm`: 于2021年11月18日从 [此位置](https://www.openstreetmap.org/export#map=16/37.3943/122.6981) 导出

3. test_select

这组测试用例用于检查根据查询语句能否查询到正确的结果。

### 外部测试用例

1. osmcode/osm-testdata

https://github.com/osmcode/osm-testdata/tree/master/xml/data

## 不同来源测试用例遵循的标准

1. JOSM

JOSM遵循的是 https://wiki.openstreetmap.org/wiki/JOSM_file_format 所提供的文件格式，既是服务器文件，也是Diff文件

2. 大部分文件

* https://wiki.openstreetmap.org/wiki/OSM_XML
* https://wiki.openstreetmap.org/wiki/API_v0.6

3. OverpassAPI文件

https://wiki.openstreetmap.org/wiki/Overpass_API#Simple_usage_examples

4. OSC文件

https://wiki.openstreetmap.org/wiki/OsmChange

5. OSH文件

(No demo file)
* https://wiki.openstreetmap.org/wiki/Planet.osm/full
* https://wiki.openstreetmap.org/wiki/User:MaZderMind/Reading_OSM_History_dumps

6. 其他（可以不用兼容）

https://wiki.openstreetmap.org/wiki/OpenLayers_osm_file_example

7. Geofabrik

> The OpenStreetMap data files provided on this server do not contain the user names, user IDs and changeset IDs of the OSM objects because these fields are assumed to contain personal information about the OpenStreetMap contributors and are therefore subject to data protection regulations in the European Union.
Extracts with full metadata are available to OpenStreetMap contributors only. 

http://download.geofabrik.de/
