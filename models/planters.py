import cadquery as cq
import cadquery.exporters

def generate_planter(filename, d1=120, d2=100, h=150, t=4):
    outer = cq.Workplane("XY").circle(d1/2).workplane(offset=h).circle(d2/2).loft()
    inner = cq.Workplane("XY").circle((d1 - 2*t)/2).workplane(offset=h - t).circle((d2 - 2*t)/2).loft()
    result = outer.cut(inner)
    cq.exporters.export(result, filename)
