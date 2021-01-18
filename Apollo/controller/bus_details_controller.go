package controller

import (
	"../entities"
	"../repository"
)

type BusDetailsController interface {
	GetDetails(req *entities.Bus) (*entities.BusDetails, error)
}

func NewBusDetailsController(r repository.BusDetailsRepository) BusDetailsController {
	return &controller{r}
}

type controller struct {
	r repository.BusDetailsRepository
}

func (c controller) GetDetails(b *entities.Bus) (*entities.BusDetails, error) {
	return c.r.GetDetailsFromID(b.ID)
}
