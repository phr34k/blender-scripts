def clear_file():    
    for bpy_data_iter in (
            bpy.data.collections,
            bpy.data.objects,        
            bpy.data.lights,    
            bpy.data.meshes,            
            bpy.data.materials,                    
            bpy.data.images,                            
            bpy.data.brushes,                                    
            bpy.data.cameras,                                            
            ):
        for id_data in bpy_data_iter:
            bpy_data_iter.remove(id_data)

    
def link_file(filepath, name):
    with bpy.data.libraries.load(filepath) as (data_from, data_to):
        data_to.collections = ["Collection"]
    for collection in data_to.collections:
        collection.name = name    
        

clear_file()        
link_file( 'D:/SDK/dds2/geometry/Houses/SPR_House_01.blend', "SPR_House_01" )
bpy.ops.object.collection_instance_add(name='SPR_House_01', location=(0.0, 0.0, -0.0))    
bpy.ops.object.collection_instance_add(name='SPR_House_01', location=(10.0, 5.0, -0.0))    
