public abstract class CubeletEntity extends Entity {
	/*Class defining entities that are made up of cubelets*/
	/*
	Inherits:
	
	public int totalHeight;
	public int totalWidth;
	public int x, y;
	
	protected abstract void render();
	protected abstract void update(); 
	*/	
	public int cubeAmntWidth;  //Amount of cube in the player width  wise
	public int cubeAmntHeight; //Amount of cube in the player height wise
	public int cubeWidth;      //Width  of individual cube
	public int cubeHeight;     //Height of individual cube
	public int speed = 5;
	
	//Variables that let the entity move
	public boolean isMoveWest = false;
	public boolean isMoveEast = false;
	public boolean isMoveNorth = false;
	public boolean isMoveSouth = false;
	
	public void move(){ //Call move() in update() in order to move
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
	
	//Setter functions for movement variables
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

