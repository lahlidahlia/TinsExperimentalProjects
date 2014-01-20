import org.newdawn.slick.TrueTypeFont;

public class FPSCounter {
    public int currentFPS = 0;
    public int FPS = 0;
    public long start = 0;
    
    public void tick() {
        currentFPS++;
        if(System.currentTimeMillis() - start >= 1000) {
            FPS = currentFPS;
            currentFPS = 0;
            start = System.currentTimeMillis();
        }
    }
    
    public String getFPS() {
        return String.valueOf(FPS);
    }
}