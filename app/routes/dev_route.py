from app.controllers.dev_controller import (
    get_devs,
    create_dev,
    remove_dev,
    get_by_gmail,
    update_dev,
)


def dev_route(app):
    @app.get("/devs")
    def retrieve():
        return get_devs()

    @app.get("/filter-devs")
    def filter_devs():
        return get_by_gmail()

    @app.post("/devs")
    def create():
        return create_dev()

    @app.delete("/devs/<dev_id>")
    def delete(dev_id):
        return remove_dev(dev_id)

    @app.patch("/devs/<dev_id>")
    def update(dev_id):
        return update_dev(dev_id)
