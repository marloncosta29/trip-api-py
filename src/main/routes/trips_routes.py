from flask import jsonify, Blueprint, request
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirm import TripConfirm
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder
from src.controllers.participant_creator import Participantcreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirm
from src.controllers.activitiy_creator import ActivityCreator


from src.models.repositories.trip_repository import TripRepository
from src.models.repositories.email_to_invite_repossitoory import EmailToInviteRepository
from src.models.repositories.link_repository import LinkRepository
from src.models.repositories.participants_repository import ParticipantRepository
from src.models.repositories.activities_repository import ActivitiesRepository




from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    email_repository = EmailToInviteRepository(conn)
    trip_creator_controller = TripCreator(trip_repository=trip_repository, email_repository=email_repository)
    response = trip_creator_controller.create(request.json)


    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def get_trip(tripId):
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    controller = TripFinder(trip_repository)

    response = controller.execute(tripId)
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["POST"])
def update_trip_status(tripId):
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    controller = TripConfirm(trip_repository)

    response = controller.execute(tripId)
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/link", methods=["POST"])
def create_link_for_trip(tripId):
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)
    controller = LinkCreator(link_repository)

    response = controller.execute(body=request.json, trip_id=tripId)

    return jsonify(response['body']), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/link", methods=["GET"])
def get_links_by_trip_id(tripId):
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)
    controller = LinkFinder(link_repository)

    response = controller.execute(trip_id=tripId)

    return jsonify(response['body']), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantRepository(conn)
    email_repository = EmailToInviteRepository(conn)
    controller = Participantcreator(participant_repository, email_repository)

    response = controller.execute(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["GET"])
def get_invites_for_trip(tripId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantRepository(conn)
    email_repository = EmailToInviteRepository(conn)
    controller = ParticipantFinder(participant_repository)

    response = controller.execute(tripId)
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites/confirm", methods=["GET"])
def confirm_invites_for_trip(tripId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantRepository(conn)
    email_repository = EmailToInviteRepository(conn)
    controller = ParticipantFinder(participant_repository)

    response = controller.execute(tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity_for_trip(tripId):
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)
    controller = ActivityCreator(activity_repository)

    response = controller.execute(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantRepository(conn)

    controller = ParticipantConfirm(participant_repository)

    response = controller.execute(participantId)
    return jsonify(response["body"]), response["status_code"]



