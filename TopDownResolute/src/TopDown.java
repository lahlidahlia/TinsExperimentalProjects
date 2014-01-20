import java.awt.Font;

import org.lwjgl.LWJGLException;
import org.lwjgl.input.Keyboard;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;
import org.lwjgl.opengl.GL11; 
import org.newdawn.slick.Color;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.TrueTypeFont;
import org.newdawn.slick.UnicodeFont;

public class TopDown {
	public static boolean finished = false;
	public FPSCounter FPS;
	public Player mainPlayer;
	 //Font used for FPS counter
	public TrueTypeFont fpsFont;
	
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
		Font awtFont = new Font("Serif", Font.PLAIN, 24);
		fpsFont = new TrueTypeFont(awtFont, false);
		FPS = new FPSCounter();
		mainPlayer = new Player(100, 100, 4, 4, 16, 16);
		
	}
	
	////////////
	//MAIN LOOP
	////////////
	public void loop(){
		while(!Display.isCloseRequested() && !finished){
			
			GL11.glClearColor(Global.BG_Color.r, Global.BG_Color.g, Global.BG_Color.b ,1);
			GL11.glClear(GL11.GL_COLOR_BUFFER_BIT);
			
			drawFPS();
			pollInput();
			if(mainPlayer != null){
				mainPlayer.update();
				mainPlayer.render();
			}
			
			FPS.tick();
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
			if(Keyboard.isKeyDown(Player.KEY_MOVE_WEST)){
				mainPlayer.moveWest();
			}
			if(Keyboard.isKeyDown(Player.KEY_MOVE_EAST)){
				mainPlayer.moveEast();
			}
			if(Keyboard.isKeyDown(Player.KEY_MOVE_NORTH)){
				mainPlayer.moveNorth();
			}
			if(Keyboard.isKeyDown(Player.KEY_MOVE_SOUTH)){
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
		
//		//Setting up GL
		GL11.glMatrixMode(GL11.GL_PROJECTION);
		GL11.glLoadIdentity(); // Resets any previous projection matrices
		GL11.glOrtho(0, Display.getWidth(), Display.getHeight(), 0, 1, -1);
		GL11.glMatrixMode(GL11.GL_MODELVIEW);	
		
	}
	
	public void cleanUp(){
		Display.destroy();
		System.exit(0);
	}
	
	
	
	public void drawFPS(){
		GL11.glEnable(GL11.GL_BLEND);
		GL11.glBlendFunc(GL11.GL_SRC_ALPHA, GL11.GL_ONE_MINUS_SRC_ALPHA);
		fpsFont.drawString(4, 0, FPS.getFPS(), Color.black);
		GL11.glDisable(GL11.GL_BLEND);
	}
}
