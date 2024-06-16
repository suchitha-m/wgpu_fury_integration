import wgpu.backends.auto  # Automatically select the appropriate backend
import wgpu.gui.glfw  # Use GLFW for GUI integration
from fury import window, actor

# Create a scene
scene = window.Scene()

# Create a sphere actor
sphere = actor.sphere(centers=[[0, 0, 0]], colors=[[1, 1, 1]], radii=2.5)
scene.add(sphere)

# Create a simple interactive window
show_manager = window.ShowManager(scene, size=(800, 600), reset_camera=True)

# WGPU setup
async def setup_wgpu():
    adapter = await wgpu.request_adapter(canvas=None)
    device = await adapter.request_device()

    # Print statements to ensure setup completion
    print("FURY and WGPU setup complete.")

# Start the rendering loop
show_manager.initialize()
show_manager.start()

# Run the WGPU setup
import asyncio
asyncio.run(setup_wgpu())
