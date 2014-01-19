
public class Player extends Entity{
	private int cubeAmntWidth;  //Amount of cube in the player width  wise
	private int cubeAmntHeight; //Amount of cube in the player height wise
	private int cubeWidth;      //Width  of individual cube
	private int cubeHeight;     //Height of individual cube
	
	//CONSTRUCTOR
	Player(int cubeAmntWidth, int cubeAmntHeight, int cubeWidth, int cubeHeight){
		this.cubeAmntWidth = cubeAmntWidth;
		this.cubeAmntHeight = cubeAmntHeight;
		this.cubeWidth = cubeWidth;
		this.cubeHeight = cubeHeight;
		
		totalWidth  = cubeAmntWidth * cubeWidth;
		totalHeight = cubeAmntHeight * cubeHeight;
		
	}
	
	
	
	public void update(){
		
	}
	
	
	public void render(){
		//GL11.
	}
}
