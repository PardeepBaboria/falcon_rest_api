import falcon
import source.routes as routes

# Create the Falcon application object
app = falcon.App()

# Add a route to serve the resource
routes.add(app, '/api/v1/')