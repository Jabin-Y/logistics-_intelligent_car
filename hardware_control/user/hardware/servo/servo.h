#ifndef SERVO_H
#define SERVO_H
#include "main.h"
#include "timer.h"


#define S1  TIM5->CCR4     //A×ó
#define S2  TIM5->CCR3     //BÓÒ
#define S3  TIM5->CCR2     //CÉÏ
#define S4  TIM5->CCR1
#define S5  TIM4->CCR4
#define S6  TIM4->CCR3
#define S7  TIM4->CCR2
#define S8  TIM4->CCR1

typedef enum
{
	
	servo1 = 0,  
	servo2 = 1,  
	servo3 = 2,  
	servo4 = 3,
	servo5 = 4,
	servo6 = 5,
	servo7 = 6,
	servo8 = 7,
} Servo;


void TIM5_Servo(int16_t s1,int16_t s2,int16_t s3);

/********************************************************************************/
void servo(int16_t s1,int16_t s2,int16_t s3,int16_t s4,int16_t s5,int16_t s6);
void AirPump(int16_t s7,int16_t s8);

void Servo_Action_Init(void);
void Servo_Action_Catch(void);
void Servo_Action_Get(void);
void AirPump_Inhale(void);
void AirPump_Hold(void);
void AirPump_Release(void);
void AirPump_Stop(void);
/*******************************************************************************/

void Servo_Init(void);
void Normal(void);
void Normal2(void);

void Nor(void);
void Raise(void);
void Raise2(void);

void Get(void);

void Place1(void);
void Place2(void);
void Place3(void);
void Place222(void);
void Place333(void);

void Place11(void);
void Place21(void);
void Place22(void);
void Place31(void);
void Place32(void);

void Placec1(void);
void Placec2(void);
void Placec3(void);
void Placec4(void);



void Servo_Ramp(Servo servo ,float x);

#endif
