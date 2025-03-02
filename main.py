from Flight import Flight, Vertex, Graph, FlightAgency
import streamlit as st

# The airports as vertices

airportE = Vertex("E", [])
airportD = Vertex("D", [airportE])
airportB = Vertex("B", [airportD, airportE])
airportC = Vertex("C", [airportB, airportD])
airportA = Vertex("A", [airportC, airportB, airportE])


def run():
    # List the flights for airports

    flights = [
        Flight('FN-101', airportA, airportB, 6, 2),
        Flight('FN-102', airportA, airportC, 8, 2),
        Flight('FN-103', airportB, airportD, 13, 12),
        Flight('FN-104', airportB, airportE, 17, 11),
        Flight('FN-105', airportC, airportB, 10, 9),
        Flight('FN-106', airportC, airportD, 20, 8),
        Flight('FN-107', airportC, airportD, 10, 6, ),
        Flight('FN-108', airportD, airportE, 14, 13),
        Flight('FN-109', airportA, airportE, 24, 21),
    ]
    st.set_page_config(layout="wide")
    st.title("Amrita International Airservices")

    c1, c2 = st.columns(2)

    with c1:
        st.success("Currently Available Flights are")
        st.info("Airport A to Airport B | Dept Time: 2AM   | Arrival Time: 6AM ")
        st.info("Airport A to Airport C | Dept Time: 2AM   | Arrival Time: 8AM ")
        st.info("Airport B to Airport D | Dept Time: 12PM  | Arrival Time: 13PM")
        st.info("Airport B to Airport E | Dept Time: 11AM  | Arrival Time: 17PM")

    with c2:
        st.info("Airport C to Airport B | Dept Time: 9AM   | Arrival Time: 10AM")
        st.info("Airport C to Airport D | Dept Time: 6AM   | Arrival Time: 10AM")
        st.info("Airport C to Airport D | Dept Time: 8AM   | Arrival Time: 20PM")
        st.info("Airport D to Airport E | Dept Time: 13PM  | Arrival Time: 14PM")
        st.info("Airport A to Airport E | Dept Time: 21PM  | Arrival Time: 24PM")

    # print("Available Flights Currently are: ")
    # print("Airport A to Airport B | Dept Time: 2AM   | Arrival Time: 6AM ")
    # print("Airport A to Airport C | Dept Time: 2AM   | Arrival Time: 8AM ")
    # print("Airport B to Airport D | Dept Time: 12PM  | Arrival Time: 13PM ")
    # print("Airport B to Airport E | Dept Time: 11AM  | Arrival Time: 17PM ")
    # print("Airport C to Airport B | Dept Time: 9AM   | Arrival Time: 10AM ")
    # print("Airport C to Airport D | Dept Time: 6AM   | Arrival Time: 10AM ")
    # print("Airport C to Airport D | Dept Time: 8AM   | Arrival Time: 20PM ")
    # print("Airport D to Airport E | Dept Time: 13PM  | Arrival Time: 14PM ")
    # print("Airport A to Airport E | Dept Time: 21PM  | Arrival Time: 24PM ")
    # print(flights)

    # Graph with airports as vertices
    graph = Graph([airportA, airportB, airportC, airportD, airportE])
    airport_dict = {"airportA": airportA, "airportB": airportB, "airportC": airportC, "airportD": airportD,
                    "airportE": airportE}

    with c1:
        s_vertex = st.selectbox("Origin Airport", ["airportA", "airportB", "airportC", "airportD", "airportE"])

        Origin_Airport = airport_dict[s_vertex]

    with c1:
        e_vertex = st.selectbox("Destination Airport", ["airportA", "airportB", "airportC", "airportD", "airportE"])

        Destination_Airport = airport_dict[e_vertex]

    with c1:
        s_time = st.text_input("Starting Time ")

        Start_Time = s_time

    if st.button("Check Flight Availability"):

        earliestArrivalTime = FlightAgency(flights, graph, Origin_Airport, Destination_Airport, int(Start_Time))
        if (earliestArrivalTime != float("inf")):
            st.success(
                f'\nThe Earliest Arrival Time for the Airport {Destination_Airport} From Airport {Origin_Airport} is {earliestArrivalTime}:00.')
        else:
            st.error(
                f'\nNo Flight from Airport {Origin_Airport} to Airport {Destination_Airport} after {Start_Time}:00.')


run()

