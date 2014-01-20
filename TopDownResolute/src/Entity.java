public abstract class Entity {
	public int totalHeight;
	public int totalWidth;
	public int x, y;
	
	protected abstract void render();
	protected abstract void update();
}

