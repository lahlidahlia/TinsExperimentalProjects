import java.util.ArrayList;


public class Group {
	public static ArrayList<Entity> Collidables = new ArrayList<Entity>(); //Things that can be collided
	public static ArrayList<Entity> Renderables = new ArrayList<Entity>(); //Things that can be rendered
	public static ArrayList<Entity> Updatables = new ArrayList<Entity>();  //Things that can be updated
	
	public static void render(){ //Render everything that can be rendered
		for(Entity entity : Renderables){
			entity.render();
		}
	}
	
	public static void update(){ //Update everything that can be updated
		for(Entity entity : Updatables){
			entity.update();
		}
	}
	
	
	
	
	
}
