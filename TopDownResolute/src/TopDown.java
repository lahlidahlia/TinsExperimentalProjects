import org.lwjgl.LWJGLException;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;
import org.lwjgl.opengl.GL11; 

public class TopDown {
	public static void main(String[] args){
		TopDown TopDown = new TopDown(); 
		TopDown.start();
		while(!Display.isCloseRequested() && !finished){
			TopDown.loop();
		}
		Display.destroy();
		System.exit(0);
	}
	
	
	public void loop(){
		GL11.glClearColor(0, 0, 0, 1);
		GL11.glClear(GL11.GL_COLOR_BUFFER_BIT);
		
		Display.update();
	}
	
	
	public void start(){
		//Setting up display
		try {
			Display.setDisplayMode(new DisplayMode(Global.SCREEN_HEIGHT, Global.SCREEN_WIDTH));
			Display.create();
		} catch (LWJGLException e) {
			System.exit(1);
		}
		
		//Setting up GL
		GL11.glMatrixMode(GL11.GL_PROJECTION);
		GL11.glLoadIdentity(); // Resets any previous projection matrices
		GL11.glOrtho(0, Display.getWidth(), Display.getHeight(), 0, 1, -1);
		GL11.glMatrixMode(GL11.GL_MODELVIEW);	
	}
	public static boolean finished = false; 
}
