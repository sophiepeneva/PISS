package entities

//Bus represents only the identifying data about the entity
type Bus struct {
	ID     int32
	Number int32
}

//BusDetails represents identifying data and details about the entity
type BusDetails struct {
	ID                     int32
	Number                 int32
	StandingPeopleCapacity int32
	SittingPeopleCapacity  int32
	DisabledPeopleCapacity int32
	AveragePeopleCount     float32
}
