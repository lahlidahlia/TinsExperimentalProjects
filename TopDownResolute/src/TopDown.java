import org.lwjgl.LWJGLException;
import org.lwjgl.input.Keyboard;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;
import org.lwjgl.opengl.GL11; 

public class TopDown {
	public static boolean finished = false;
	public Player mainPlayer;
	
	////////////
	//VOID MAIN
	////////////
	public static void main(String[] args){
		TopDown TopDown = new TopDown(); 
		TopDown.start();
		TopDown.loop();
		TopDown.cleanUp();
	}
	
	///////////////
	//GENERAL INIT
	///////////////
	public void start(){
		init();
		mainPlayer = new Player(100, 100, 4, 4, 16, 16);
		
	}
	
	////////////
	//MAIN LOOP
	////////////
	public void loop(){
		while(!Display.isCloseRequested() && !finished){
			
			GL11.glClearColor(1, 1, 1, 1);
			GL11.glClear(GL11.GL_COLOR_BUFFER_BIT);
			
			pollInput();
			if(mainPlayer != null){
				mainPlayer.update();
				mainPlayer.render();
			}
			
			Display.update();
			Display.sync(Global.FPS);
		}
	}
	
	////////////////
	//INPUT POLLING
	////////////////
	public void pollInput(){
		//Player manipulation key input
		if(mainPlayer != null){
			if(Keyboard.isKeyDown(mainPlayer.KEY_MOVE_WEST)){
				mainPlayer.moveWest();
			}
			if(Keyboard.isKeyDown(mainPlayer.KEY_MOVE_EAST)){
				mainPlayer.moveEast();
			}
			if(Keyboard.isKeyDown(mainPlayer.KEY_MOVE_NORTH)){
				mainPlayer.moveNorth();
			}
			if(Keyboard.isKeyDown(mainPlayer.KEY_MOVE_SOUTH)){
				mainPlayer.moveSouth();
			}
			
		}
		while(Keyboard.next()){
			if(Keyboard.getEventKey() == Keyboard.KEY_ESCAPE){
				if(Keyboard.getEventKeyState()){
					finished = true;
				}
			}
		}
	}
	
	/////////////
	//LWJGL INIT
	/////////////
	public void init(){
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
	
	public void cleanUp(){
		Display.destroy();
		System.exit(0);
	}
}
