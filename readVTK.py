import numpy as np
import sys
import vtk
from vtk import vtkStructuredPointsReader
from vtk.util import numpy_support as VN
import meshio

# https://stackoverflow.com/questions/58713448/reading-the-position-coordinates-of-nodes-cells-points-from-vtk-files

fnm=r'F:\yzx-2\neural-flow-style-FORK\neural-flow-style\data\dambreak2d\vtk\ParticleData_Fluid_1.vtk'

# reader = vtk.vtkGenericDataObjectReader()
# reader.SetFileName(fnm)
# reader.Update()

# points = np.array( reader.GetOutput().GetPoints().GetData() )
# print(points.shape)
# print(points)

print('-----------------------------t2')

from vtk.util.numpy_support import vtk_to_numpy


reader = vtk.vtkUnstructuredGridReader()
reader.SetFileName( fnm )
reader.Update()
field_array = reader.GetOutput().GetPointData().GetArray( "density" )
print(np.array(field_array))
print( vtk_to_numpy(field_array).shape)
field_array = reader.GetOutput().GetPointData().GetArray( "id" )
print(np.array(field_array))


pc0 = reader.GetOutput().GetPointData()



pc=                reader.GetOutput().GetPoints().GetData().GetTuple(0)
print(pc)


point_cordinates = meshio.read(fnm).points
print(point_cordinates[:,0:2])
print(point_cordinates.shape)

# Point_cordinates = reader.GetOutput().GetPoints().GetData()
# numpy_coordinates = vtk_to_numpy(Point_cordinates)
# print(numpy_coordinates)
