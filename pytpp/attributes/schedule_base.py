from pytpp.attributes._helper import IterableMeta, Attribute


class ScheduleBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Schedule Base"
	blackout = Attribute('Blackout')
	days_of_month = Attribute('Days Of Month')
	days_of_week = Attribute('Days Of Week')
	days_of_year = Attribute('Days Of Year')
	hour = Attribute('Hour')
	minute = Attribute('Minute')
	priority = Attribute('Priority')
	reschedule = Attribute('Reschedule')
	start_time = Attribute('Start Time')
	stop_time = Attribute('Stop Time')
	timezone = Attribute('Timezone', min_version='21.2')
	utc = Attribute('UTC')
