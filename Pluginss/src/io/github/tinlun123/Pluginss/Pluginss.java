package io.github.tinlun123.Pluginss;


import java.util.Random;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;

public class Pluginss extends JavaPlugin {
	Random random = new Random();
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		if(cmd.getName().equalsIgnoreCase("ping")){
			sender.sendMessage("ping");
			return true;
		}
		if(cmd.getName().equalsIgnoreCase(("unleashTheDoges"))){
			Player player = (Player) sender;
			for(int i = 0; i < 200; i++)
			player.getWorld().spawnEntity(player.getLocation().add(-10 + random.nextInt(20), 0, -10 + random.nextInt(20)), EntityType.WOLF);
		}
		return false;
	}
}
