
public class Timer {
	/*Static class timer that requires a timer that is used to check against the system time, so make your own 
	long timer*/
	private long timer = 0;
	public void setTimer(long time/*in Ms*/){
		//Set a timer. Remember to check the timer, because it's not going to go off on its own.
		timer = System.currentTimeMillis() + time;
	}
	public void setTimer(long minTimer, long maxTimer){
		//Set the timer with a random value between minTimer and maxTimer
		long r = (long) (Math.random() * maxTimer) + (maxTimer - minTimer);
		long time = r % maxTimer + minTimer;
		timer = System.currentTimeMillis() + time;
	}
	public boolean isTimerDone(){
		return System.currentTimeMillis() > timer;
	}
}
