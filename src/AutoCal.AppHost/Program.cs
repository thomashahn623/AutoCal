var builder = DistributedApplication.CreateBuilder(args);

// Use the docker-radicale container
var calDavServer = builder.AddContainer("radicale", "docker.io/tomsquest/docker-radicale")
    .WithHttpEndpoint(port: 5232, targetPort: 5232, name: "radicale");

builder.Build().Run();
