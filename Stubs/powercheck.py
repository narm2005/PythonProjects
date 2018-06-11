#!/usr/bin/python
def main():
  power_now = open("/sys/class/power_supply/BAT0/energy_now", "r").readline()
  power_full = open("/sys/class/power_supply/BAT0/energy_full", "r").readline()
  print float(power_now)/float(power_full) * 100 , "%"

if __name__ == "__main__":
  main()
