from satellite.controller import (
    apply_request_schema,
    apply_response_schema,
    BaseHandler,
)
from satellite.service import route_manager
from satellite.schemas.route import (
    CreateRouteSchema,
    RouteSchema,
    UpdateRouteSchema,
)


class RoutesHandler(BaseHandler):

    @apply_response_schema(RouteSchema, many=True)
    def get(self):
        return route_manager.get_all()

    @apply_request_schema(CreateRouteSchema)
    @apply_response_schema(RouteSchema)
    def post(self, validated_data: dict):
        return route_manager.create(validated_data['data']['attributes'])


class RouteHandler(BaseHandler):

    @apply_response_schema(RouteSchema)
    def get(self, route_id):
        return route_manager.get(route_id)

    @apply_request_schema(UpdateRouteSchema)
    @apply_response_schema(RouteSchema)
    def put(self, route_id, validated_data):
        try:
            return route_manager.update(
                route_id,
                validated_data['data']['attributes'],
            )
        except route_manager.EntityNotFound as exc:
            self.set_status(404)
            self.finish(str(exc))

    def delete(self, route_id):
        route_manager.delete(route_id)
        self.write('OK')
