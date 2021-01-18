package repository

import (
	"../entities"
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

const (
	dbUser    = "root"
	dbPass    = "root"
	dbDriver  = "mysql"
	dbPort    = "3307"
	localhost = "127.0.0.1"
)

type BusDetailsRepository interface {
	GetDetailsFromID(id int32) (*entities.BusDetails, error)
}

type busDetailRepository struct {
	db *sql.DB
}

func (b busDetailRepository) GetDetailsFromID(id int32) (*entities.BusDetails, error) {
	query := fmt.Sprintf(
		"SELECT d.id, b.number, d.standing_people_capacity, d.sitting_people_capacity, d.disabled_people_capacity, d.average_people_count \nFROM details d JOIN bus_to_number b ON d.id=b.bus_id \nWHERE d.id=%d;", id)

	row, err := b.db.Query(query)
	if err != nil {
		return nil, err
	}
	if !row.Next() {
		return nil, fmt.Errorf("no data found in the database for the given bus")
	}
	result := entities.BusDetails{}
	err = row.Scan(
		&result.ID,
		&result.Number,
		&result.StandingPeopleCapacity,
		&result.SittingPeopleCapacity,
		&result.DisabledPeopleCapacity,
		&result.AveragePeopleCount,
		)

	if err != nil {
		return nil, err
	}

	return &result, nil
}

func NewBusDetailsRepository() (BusDetailsRepository, error)  {
	db, err := sql.Open(dbDriver, composeDataSourceName())
	if err != nil {
		return nil, err
	}
	return &busDetailRepository{
		db: db,
	}, nil
}

func composeDataSourceName() string {
	return fmt.Sprintf("%s:%s@tcp(%s:%s)/apollo_db", dbUser, dbPass, localhost, dbPort)
}
