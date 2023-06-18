bl_info = {
    "name": "mijo ping-pong play",
    "blender": (3, 0, 50),
    "category": "Animation",
    "author": "mijo",
    "location": "TIMELINE > left-side ",
    "description":"",
    "warning": "",
    "wiki_url":"",
    "tracker_url": "",
    "version":(0,0,2)
}

import bpy

def fuck(frame,start_f,end_f):
    if frame == end_f:
        bpy.ops.screen.animation_play(reverse=True)
        
    elif frame == start_f:
        bpy.ops.screen.animation_play()

def mijo_ping_pong_play(scene):
    
    
    scr = bpy.context.screen #get current screen
    is_Playing = scr.is_animation_playing #get play state(boolean) 
    is_scrubbing = scr.is_scrubbing
    is_temporary = scr.is_temporary
    
    # print('is_Playing:',is_Playing)
    # print('is_scrubbing:',is_scrubbing)
    # print('is_temporary:',is_temporary)
    
    pv = scene.use_preview_range
    
    frame = scene.frame_current
    
    if pv :
        start_f = scene.frame_preview_start
        end_f = scene.frame_preview_end
    else:
        start_f = scene.frame_start
        end_f = scene.frame_end
    
    print(frame)
    print('is_Playing:',is_Playing)
    print('is_scrubbing:',is_scrubbing)
    print('is_temporary:',is_temporary)
    
    if is_Playing and is_scrubbing: # scrubbing to end
        pass
    # elif not is_Playing and not is_scrubbing and not is_temporary :
        # pass
    # else:
    elif is_Playing and not is_scrubbing and not is_temporary :# playing
        fuck(frame,start_f,end_f)
        
    elif not is_Playing and not is_scrubbing and not is_temporary : # sudden at end reverse
        fuck(frame,start_f,end_f)

class mijo_pingpong_OT_button(bpy.types.Operator):
    bl_idname = "custom.button"
    bl_label = "Custom Button"
    toggle_value: bpy.props.IntProperty(default=0)
    
    def execute(self, context):
        self.toggle_value = 1 - self.toggle_value
        
        if self.toggle_value == 0:
            pass
            bpy.app.handlers.frame_change_post.append(mijo_ping_pong_play)
            # bpy.app.handlers.frame_change_pre.append(mijo_ping_pong_play)
            self.report({'WARNING'}, 'ping-pong: ON')
            pass
        
        elif self.toggle_value == 1:
            pass
            try:
                bpy.app.handlers.frame_change_post.remove(mijo_ping_pong_play)
                # bpy.app.handlers.frame_change_pre.remove(mijo_ping_pong_play)
                self.report({'WARNING'}, 'ping-pong: OFF')
            except:
                print('test: NO... mijo_ping_pong_play') 
                self.report({'WARNING'}, 'ping-pong: OFF')
            pass
        
        return {'FINISHED'}
        

def draw_func_mijo_pingpong(self, context):
    layout = self.layout
    layout.operator("custom.button",text="ping-pong",icon='ARROW_LEFTRIGHT')


def register():
    bpy.utils.register_class(mijo_pingpong_OT_button)
    bpy.types.TIME_MT_editor_menus.append(draw_func_mijo_pingpong)

def unregister():
    bpy.utils.unregister_class(mijo_pingpong_OT_button)
    bpy.types.TIME_MT_editor_menus.remove(draw_func_mijo_pingpong)
    
if __name__ == "__main__":
    register()
