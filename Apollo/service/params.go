package service

import (
	"../controller"
	"../repository"
)

type Params struct {
	Controller controller.BusDetailsController
}

func BuildServiceParams() (*Params, error) {
	r, err := repository.NewBusDetailsRepository()
	if err != nil {
		return nil, err
	}
	c := controller.NewBusDetailsController(r)
	return &Params{Controller: c}, nil
}