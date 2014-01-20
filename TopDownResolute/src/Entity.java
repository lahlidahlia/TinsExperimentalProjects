
public abstract class Entity {
	/*Class defining entities, which are quad shape things that can be drawn and update*/
	public int totalHeight;
	public int totalWidth;
	public int x, y;
	
	protected abstract void render();
	protected abstract void update();	
}
