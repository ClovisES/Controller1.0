

#/****************************************************************************/
#/* PiTimer - Step 5 - Relay functions.                                      */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2015-07-04 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Class to handle the current relay states.                                */
#/****************************************************************************/


import datetime
import SystemTime


# Constants to define relay state.
RELAY_OFF = 0
RELAY_ON = 1


class Relays:

   def __init__(self):
# Instance storage for relay states.
      self.RelayState = []


#/***********************************************************/
#/* Add a relay to the relays supported by the application. */
#/***********************************************************/
   def AddRelay(self, RelayNumber, RelayState):
      self.RelayState.append([RelayNumber, RelayState])
      
   def AddRelay(self, RelayNumber, RelayState):
      self.RelayState.append([RelayNumber, RelayState])




#/*******************************************/
#/* Display a table of the current relay    */
#/* states and the date/time at that point. */
#/*******************************************/
   def DisplayRelayStates(self):
      ThisSystemTime = SystemTime.SystemTime()
      pfarint("{:=^21}".format("") + "\r")
      print("|{:^19}|".format(ThisSystemTime.SystemTimeString()) + "\r")
      print("{:=^21}".format("") + "\r")
      print("|{:^9}|{:^9}|".format("Relay", "State") + "\r")
      print("|{:-^9}|{:-^9}|".format("", "") + "\r")

      for ThisRelayState in self.RelayState:
         if ThisRelayState[0]:
            print("|{:>9}|{:^9}|".format(ThisRelayState[0], ThisRelayState[1]) + "\r")

      print("{:=^21}".format("") + "\r")
         

#/************************************************/
#/* Get the current state of the specific relay. */
#/************************************************/
   def GetRelayState(self, RelayNumber):
      Result = False
      if RelayNumber - 1 < len(self.RelayState):
         Result = self.RelayState[RelayNumber - 1][1]
      return Result


#/************************************************/
#/* Set the current state of the specific relay. */
#/************************************************/
   def SetRelayState(self, RelayNumber, NewRelayState):
      if RelayNumber - 1 < len(self.RelayState):
         self.RelayState[RelayNumber - 1][1] = NewRelayState


#/***************************************************/
#/* Toggle the current state of the specific relay. */
#/***************************************************/
   def ToggleRelayState(self, RelayNumber):
      Result = False
      if RelayNumber - 1 < len(self.RelayState):
         if self.RelayState[RelayNumber - 1][1] == RELAY_OFF:
            self.RelayState[RelayNumber - 1][1] = RELAY_ON
         else:
            self.RelayState[RelayNumber - 1][1] = RELAY_OFF
         Result = self.RelayState[RelayNumber - 1][1]
      return Result

