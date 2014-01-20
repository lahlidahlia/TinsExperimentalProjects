import org.lwjgl.opengl.GL11;
import org.lwjgl.input.Keyboard;
import org.newdawn.slick.Color;

public class Player extends CubeletEntity{
	
	//Keyboard variables, for easy keyboard switch
	public static int KEY_MOVE_WEST = Keyboard.KEY_A;
	public static int KEY_MOVE_EAST = Keyboard.KEY_D;
	public static int KEY_MOVE_NORTH = Keyboard.KEY_W;
	public static int KEY_MOVE_SOUTH = Keyboard.KEY_S;
	
	//The color that the player will be drawn in
	private Color playerColor = Color.green;
	
	//CONSTRUCTOR
	Player(int x, int y, int cubeAmntWidth, int cubeAmntHeight, int cubeWidth, int cubeHeight){
		this.x = x;
		this.y = y;
		this.cubeAmntWidth = cubeAmntWidth;
		this.cubeAmntHeight = cubeAmntHeight;
		this.cubeWidth = cubeWidth;
		this.cubeHeight = cubeHeight;
		
		totalWidth  = cubeAmntWidth * cubeWidth;
		totalHeight = cubeAmntHeight * cubeHeight;
	}
	
	
	
	public void update(){
		updateBBox();
		checkForCollision();
		move();
		System.out.println("X: " + x + " Y: " + y);
	}
	
	
	public void render(){
		GL11.glColor3f(playerColor.r, playerColor.g, playerColor.b);
		GL11.glBegin(GL11.GL_QUADS);
			GL11.glVertex2i(x, y);
			GL11.glVertex2i(x + totalWidth, y);
			GL11.glVertex2i(x + totalWidth, y + totalHeight);
			GL11.glVertex2i(x, y + totalHeight);
		GL11.glEnd();
	}
	

	

}
