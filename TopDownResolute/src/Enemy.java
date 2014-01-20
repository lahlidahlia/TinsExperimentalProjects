import org.lwjgl.opengl.GL11;
import org.newdawn.slick.Color;


public class Enemy extends CubeletEntity{
	
	//Variables that let the entity move
	//Overriding superclass (change from bool to int to let you "queue" up movement)
	public int isMoveWest = 0;
	public int isMoveEast = 0;
	public int isMoveNorth = 0;
	public int isMoveSouth = 0;
	
	private Color enemyColor = Color.red;
	private final int maxMove = 50; //Maximum amount of movement distance if randomly chosen to move
	private final int minMove = 30; //Minimum amount of movement distance if randomly chosen to move
	public long minActionPause = 500; //Minimum time for the enemy to pause inbetween actions
	public long maxActionPause = 2000; //Maximum time for the enemy to pause inbetween actions
	public boolean readyToAct = true; //Check if the enemy is ready for an action
	public Timer timer;
	//CONSTRUCTOR
	Enemy(int x, int y, int cubeAmntWidth, int cubeAmntHeight, int cubeWidth, int cubeHeight){
		this.x = x;
		this.y = y;
		this.cubeAmntWidth = cubeAmntWidth;
		this.cubeAmntHeight = cubeAmntHeight;
		this.cubeWidth = cubeWidth;
		this.cubeHeight = cubeHeight;
		
		totalWidth  = cubeAmntWidth * cubeWidth;
		totalHeight = cubeAmntHeight * cubeHeight;
		
		//Defining Bounding boxes. TopLeft is already defined in superclass
		bBox_botRightX = x + totalWidth;
		bBox_botRightY = y + totalHeight;
		
		timer = new Timer(); //Creating a new timer
	}
	
	public void render(){
		GL11.glColor3f(enemyColor.r, enemyColor.g, enemyColor.b);
		GL11.glBegin(GL11.GL_QUADS);
			GL11.glVertex2i(x, y);
			GL11.glVertex2i(x + totalWidth, y);
			GL11.glVertex2i(x + totalWidth, y + totalHeight);
			GL11.glVertex2i(x, y + totalHeight);
		GL11.glEnd();
	}
	
	
	public void update(){
		if(timer.isTimerDone()){ //Decide which action to perform every so often
			chooseAction();
			timer.setTimer(minActionPause, maxActionPause);
			System.out.println("Action!");
		}
		updateBBox();
		checkForCollision();
		move();
	}
	
	public void chooseAction(){
		int r = (int) (Math.random() * 50000); //Get a number between 0 and given number
		int action = r % 1;//Get a random number between 0 and given number (non-inclusive)
		switch(action){ //Choosing an action, currently could only moveRandom()
		case 0:
			moveRandom();
			break;
		default:
			//Do nothing
		}
	} 
	
	public void moveRandom(){
		if(isMoveWest == 0 && isMoveEast == 0 && isMoveNorth == 0 && isMoveNorth == 0){ //To prevent movements from accumulating when there is movements queued
			while(true){ //In case you want to rechoose the direction
				int r = (int) (Math.random() * 50000); //Get a number between 0 and given number
				int dir = r % 4; //Choosing a random direction
				
				int i = r % (maxMove-minMove) + minMove; //Choosing a random amount of distance to move
				switch(dir){ //This preliminary check is so that the enemy won't spend too much time at the edge of the screen
				case 0:
					if(!canMoveWest) continue;
					else break;
				case 1:
					if(!canMoveEast) continue;
					else break;
				case 2:
					if(!canMoveNorth) continue;
					else break;
				case 3:
					if(!canMoveSouth) continue;
					else break;
				default:	
					continue;
				}
				for(; i != 0; i--){
					switch(dir){
					case 0:
						moveWest();
						break;
					case 1:
						moveEast();
						break;
					case 2:
						moveNorth();
						break;
					case 3:
						moveSouth();
						break;
					}
				}
				break; //Break out of the while loop if it executes successfully
			}
		}
	}
	

	
	
	@Override
	public void move(){ //Call move() in update() in order to move
		if(isMoveWest > 0){
			if(canMoveWest){
				x -= speed;
			}
			isMoveWest--;
		}
		if(isMoveEast > 0){
			if(canMoveEast){
				x += speed;
			}
			isMoveEast--;
		}
		if(isMoveNorth > 0){
			if(canMoveNorth){
				y -= speed;
			}
			isMoveNorth--;
		}
		if(isMoveSouth > 0){
			if(canMoveSouth){
				y += speed;
			}
			isMoveSouth--;
		}
	}
	//Setter functions for movement variables
	@Override
	public void moveWest(){
		isMoveWest++;
	}
	public void moveEast(){
		isMoveEast++;
	}
	public void moveNorth(){
		isMoveNorth++;
	}
	public void moveSouth(){
		isMoveSouth++;
	}
}


