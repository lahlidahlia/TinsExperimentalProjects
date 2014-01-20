import java.awt.*;

import org.lwjgl.opengl.GL11;
import org.lwjgl.util.*;
import org.lwjgl.input.Keyboard;
import org.newdawn.slick.Color;

public class Player extends CubeletEntity{
	public int speed = 5;
	
	public boolean isMoveWest = false;
	public boolean isMoveEast = false;
	public boolean isMoveNorth = false;
	public boolean isMoveSouth = false;
	
	
	//Keyboard variables
	public static int KEY_MOVE_WEST = Keyboard.KEY_A;
	public static int KEY_MOVE_EAST = Keyboard.KEY_D;
	public static int KEY_MOVE_NORTH = Keyboard.KEY_W;
	public static int KEY_MOVE_SOUTH = Keyboard.KEY_S;
	

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
		if(isMoveWest){
			x -= speed;
			isMoveWest = false;
		}
		if(isMoveEast){
			x += speed;
			isMoveEast = false;
		}
		if(isMoveNorth){
			y -= speed;
			isMoveNorth = false;
		}
		if(isMoveSouth){
			y += speed;
			isMoveSouth = false;
		}
	}
	
	
	public void render(){

//		GL11.glColor4ub(playerColor.getRedByte(), playerColor.getGreenByte(), playerColor.getBlueByte(), (byte)1);//Set color
		GL11.glColor3f(playerColor.r, playerColor.g, playerColor.b);
		GL11.glBegin(GL11.GL_QUADS);
			GL11.glVertex2i(x, y);
			GL11.glVertex2i(x + totalWidth, y);
			GL11.glVertex2i(x + totalWidth, y + totalHeight);
			GL11.glVertex2i(x, y + totalHeight);
		GL11.glEnd();
	}
	
	public void moveWest(){
		isMoveWest = true;
	}
	public void moveEast(){
		isMoveEast = true;
	}
	public void moveNorth(){
		isMoveNorth = true;
	}
	public void moveSouth(){
		isMoveSouth = true;
	}

	

}