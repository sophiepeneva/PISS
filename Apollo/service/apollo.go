package service

import (
	"../gen"
	"fmt"
	"google.golang.org/grpc"
	"log"
	"net"
)

func RunApolloService(params Params) {
	fmt.Println("Starting Apollo Service...")

	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", 9000))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := gen.NewServer(params.Controller)

	grpcServer := grpc.NewServer()

	gen.RegisterApolloServer(grpcServer, s)

	fmt.Println("RUNNING")

	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %s", err)
	}
}