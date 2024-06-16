# Create a simple scene with FURY
import wgpu
from fury import window, actor


# Create a scene
scene = window.Scene()

# Create a sphere actor
sphere = actor.sphere(centers=[[0, 0, 0]], colors=[[1, 1, 1]], radii=2.5)
scene.add(sphere)

# Show the scene
window.show(scene)

# WGPU basic setup (this won't render anything yet)
adapter = wgpu.request_adapter(canvas=None)
device = adapter.request_device(extensions=[])

print("FURY and WGPU setup complete.")