#include "servo.h"
#include "motor_ctrl.h"
#include "chassis_task.h"
#include "stm32f4xx.h"

#include "FreeRTOSConfig.h"
#include "FreeRTOS.h"
#include "task.h"

extern int i;
uint8_t inhaled=0;
extern Flag flag;
fp32 Servo_Real[8]={0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0};
fp32 Servo_Target[8]={0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0};

void Servo_Init()
{
	S1=7.4*120+500; //140
	S2=7.4*120+500; //180
	S3=7.4*120+500;	//180
	S4=7.4*115+500;
}

void servo(int16_t s1,int16_t s2,int16_t s3,int16_t s4,int16_t s5,int16_t s6)//0°-180°   舵机
{
	/* chassis_feedback_update(Cloud_Angle_Measure_Yaw); */
	static fp32 servo_time;
	S1=7.4*s1+500;
	S2=7.4*s2+500;
	S3=7.4*s3+500;	
	S4=7.4*s4+500;
	S5=7.4*s5+500;
	S6=7.4*s6+500;	
	if(Servo_Real[0] == Servo_Target[0] && Servo_Real[1] == Servo_Target[1] && Servo_Real[2] == Servo_Target[2]&&
	Servo_Real[3] == Servo_Target[3] && Servo_Real[4] == Servo_Target[4] && Servo_Real[5] == Servo_Target[5])
	//判断机械臂是否移动到指定位置
	{
		servo_time++;
		if(servo_time > 200)
		{
			flag.get = TRUE;
			flag.back = TRUE;
			flag.posi_go = TRUE;
			flag.turn = TRUE;
			flag.arm = FALSE;//机械臂标志位
			servo_time = 0;//机械臂运行时间统计
		  i++;
		}
	}
	else
	{
	  flag.get = FALSE;
	  flag.turn = FALSE;
	}
}

void AirPump(int16_t s7,int16_t s8)
{
	static fp32 airpump_time;
	S7=7.4*s7+500;
	S8=7.4*s8+500;
	if(Servo_Real[7] == Servo_Target[7] && Servo_Real[6] == Servo_Target[6])
	{
		airpump_time++;
		if(airpump_time > 200)
		{
			flag.get = TRUE;
			flag.back = TRUE;
			flag.posi_go = TRUE;
			flag.turn = TRUE;
			flag.arm = FALSE;
			airpump_time = 0;
			i++;
		}
	}
	else
	{
		flag.get = FALSE;
	  	flag.turn = FALSE;
	}
}

void Servo_Action_Init(void)
{
	if(flag.arm == TRUE)
	{
		Servo_Target[0]=120;//140
		Servo_Target[1]=120;//180
		Servo_Target[2]=120;//180
		Servo_Target[3]=115;
		Servo_Ramp(servo1,5);
		Servo_Ramp(servo2,5);
		Servo_Ramp(servo3,5);
		Servo_Ramp(servo4,5);
		servo(Servo_Real[0],Servo_Real[1],Servo_Real[2],Servo_Real[3],Servo_Real[4],Servo_Real[5]);
	}
}

void Servo_Action_Catch(void)
{
	if(flag.arm == TRUE)
	{
		Servo_Target[0]=70;
		Servo_Target[1]=120;
		Servo_Target[2]=60;
		Servo_Target[3]=115;
		Servo_Ramp(servo1,5);
		Servo_Ramp(servo2,5);
		Servo_Ramp(servo3,5);
		Servo_Ramp(servo4,5);
		servo(Servo_Real[0],Servo_Real[1],Servo_Real[2],Servo_Real[3],Servo_Real[4],Servo_Real[5]);
	}
}

void Servo_Action_Get(void)
{
//	if(flag.arm == TRUE)
//	{
//		Servo_Target[0]=120;
//		Servo_Target[1]=120;
//		Servo_Target[2]=120;
//		Servo_Target[3]=115;
//		Servo_Ramp(servo1,5);
//		Servo_Ramp(servo2,5);
//		Servo_Ramp(servo3,5);
//		Servo_Ramp(servo4,5);
//		servo(Servo_Real[0],Servo_Real[1],Servo_Real[2],Servo_Real[3],Servo_Real[4],Servo_Real[5]);
//	}
}

void AirPump_Inhale(void)
{
	if(flag.arm == TRUE)
	{
		Servo_Target[7]=180;
		Servo_Ramp(servo8,5);
		AirPump(Servo_Real[6],Servo_Real[7]);
	}
}

void AirPump_Hold(void)
{
	if(flag.arm == TRUE)
	{
		Servo_Target[6]=180;
		
		Servo_Ramp(servo7,5);
		AirPump(Servo_Real[6],Servo_Real[7]);
	}
}

void AirPump_Stop(void)
{
	
	if(flag.arm == TRUE)
	{
		Servo_Target[6]=0;
		
		Servo_Ramp(servo7,5);
		AirPump(Servo_Real[6],Servo_Real[7]);
	}
}

void AirPump_Release(void)
{
	if(flag.arm == TRUE)
	{
		
		Servo_Target[7]=0;
		Servo_Ramp(servo8,5);
		AirPump(Servo_Real[6],Servo_Real[7]);
	}
}

// void Placec4(void) //取环
// {
// 	if(flag.arm == TRUE)
// 	{
// 		Servo_Target[0] = 10;
// 		Servo_Target[1] = 92;
// 		Servo_Target[2] = 22;
// 		Servo_Ramp(servo1,5);
// 		Servo_Ramp(servo2,5);
// 		Servo_Ramp(servo3,10);
// 		//servo(Servo_Real[0],Servo_Real[1],Servo_Real[2]);
// 	}
// }


/**
  * @brief  舵机输出斜坡函数
  * @param  void
  * @retval void
  * @attention 
  */
void Servo_Ramp(Servo servo ,float x)
{
	if (Servo_Real[servo] < Servo_Target[servo])
	{
		Servo_Real[servo] += x;
		if(Servo_Real[servo] > Servo_Target[servo])
		{
			Servo_Real[servo] = Servo_Target[servo];
		}
	}
	else if (Servo_Real[servo] > Servo_Target[servo])
	{
		Servo_Real[servo] -= x;
	}
	
	if (Servo_Real[servo] < 0)
	{
		Servo_Real[servo] = 0;
	}
}


