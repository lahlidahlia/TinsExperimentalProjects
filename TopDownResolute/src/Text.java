import java.awt.Font;

import org.lwjgl.opengl.GL11;
import org.newdawn.slick.Color;
import org.newdawn.slick.TrueTypeFont;


public class Text {
	public static Font awtFont = new Font("Serif", Font.PLAIN, 24);
	public static TrueTypeFont fpsFont = new TrueTypeFont(awtFont, false);
	
	public static void drawText(String string){
		GL11.glEnable(GL11.GL_BLEND);
		GL11.glBlendFunc(GL11.GL_SRC_ALPHA, GL11.GL_ONE_MINUS_SRC_ALPHA);
		fpsFont.drawString(4, 0, string, Color.black);
		GL11.glDisable(GL11.GL_BLEND);
	}
}
