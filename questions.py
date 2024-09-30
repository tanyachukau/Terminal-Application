import requests


questions_by_category = {
    "Planets": [
        {"question": "What is the closest planet to the Sun?", "answer": "Mercury", "options": ["Mercury", "Venus", "Earth", "Uranus"]},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars", "options": ["Saturn", "Pluto", "Mars", "Venus"]},
        {"question": "Which planet is the largest in our solar system?", "answer": "Jupiter", "options": ["Uranus", "Jupiter", "Mercury", "Mars"]},
        {"question": "Which planet is known for its beautiful rings?", "answer": "Saturn", "options": ["Saturn", "Venus", "Mars", "Jupiter"]},
        {"question": "Which planet has the highest mountain in the solar system, Olympus Mons?", "answer": "Mars", "options": ["Mars", "Venus", "Earth", "Pluto"]},
        {"question": "What is the only planet in our solar system that rotates on its side?", "answer": "Uranus", "options": ["Jupiter", "Uranus", "Saturn", "Mars"]},
        {"question": "Which planet is known for having a strong magnetic field and numerous moons, including the largest, Ganymede?", "answer": "Jupiter", "options": ["Venus", "Mars", "Earth", "Jupiter"]},
        {"question": "What is the main component of Venus's atmosphere?", "answer": "Carbon dioxide", "options": ["Oxygen", "Carbon dioxide", "Helium", "Water"]},
        {"question": "Which planet has the longest day, taking about 243 Earth days to complete one rotation?", "answer": "Venus", "options": ["Mercury", "Venus", "Uranus", "Saturn"]},
        {"question": "Which planet is known for having a day longer than its year?", "answer": "Venus", "options": ["Pluto", "Venus", "Earth", "Mercury"]},
    ],
    "Stars": [
        {"question": "Which star is closest to Earth?", "answer": "Proxima Centauri", "options": ["Proxima Centauri", "Betelgeuse", "Polaris", "Sirius"]},
        {"question": "Which type of star is the Sun classified as?", "answer": "G-type", "options": ["Vega", "G-type", "Capella", "Procyon"]},
        {"question": "What is the term for a star that is in the process of forming?", "answer": "Protostar", "options": ["Proxima Centauri", "Dark Matter", "Quasar", "Protostar"]},
        {"question": "What is the name of the brightest star in the night sky?", "answer": "Sirius", "options": ["Vega", "Alpha Centauri", "Arcturus", "Sirius"]},
        {"question": "What is the life cycle stage of a star that follows the main sequence?", "answer": "Red giant", "options": ["Red giant", "Canopus", "Arcturus", "Capella"]},
        {"question": "What phenomenon occurs when a massive star exhausts its nuclear fuel and collapses under its own gravity?", "answer": "Supernova", "options": ["Supernova", "Alpha Centauri", "Exoplanet", "Sirius"]},
        {"question": "What is the term for the apparent brightness of a star as seen from Earth?", "answer": "Apparent magnitude", "options": ["Vega", "Apparent magnitude", "Procyon", "Cosmic Microwave Background"]},
        {"question": "Which type of star is known for having a regular and predictable change in brightness?", "answer": "Cepheid variable star", "options": ["Rigel", "Alpha Centauri", "Cepheid variable star", "Quasar"]},
        {"question": "What do astronomers use to classify stars based on their temperatures and brightness?", "answer": "Hertzsprung-Russell diagram", "options": ["Helium", "Hertzsprung-Russell diagram", "Betelgeuse", "Capella"]},
        {"question": "What is the name of the region of space around a black hole beyond which nothing can escape?", "answer": "Event horizon", "options": ["Polaris", "Alpha Centauri", "Arcturus", "Event horizon"]},
    ],
    "Space Missions": [
        {"question": "Which space mission first landed humans on the Moon?", "answer": "Apollo 11", "options": ["Apollo 11", "Hubble Space Telescope", "Voyager 1 and 2", "International Space Station (ISS)"]},
        {"question": "What was the name of the first satellite sent into space?", "answer": "Sputnik", "options": ["Landsat Satellites", "Alpha Centauri", "Sputnik", "GPS (Global Positioning System) Satellites"]},
        {"question": "What was the first human-made object to reach the Moon?", "answer": "Space Shuttle Columbia", "options": ["Space Shuttle Columbia", "Alpha Centauri", "Apollo 17 Lunar Module (Challenger)", "Event horizon"]},
        {"question": "What was the name of the Mars rover that successfully landed in 2012 and conducted extensive research on the planet's surface?", "answer": "Curiosity", "options": ["Curiosity", "Cosmic Microwave Background", "Rigel", "Exoplanet"]},
        {"question": "Which NASA mission launched in 1990 has provided some of the most detailed images of distant galaxies?", "answer": "Hubble Space Telescope", "options": ["Polaris", "Hubble Space Telescope", "Helium", "Capella"]},
        {"question": "Which mission was the first to send humans into orbit around the Earth?", "answer": "Vostok 1", "options": ["Polaris", "Alpha Centauri", "Arcturus", "Vostok 1"]},
        {"question": "What was the first spacecraft to land on the surface of Venus?", "answer": "Venera 7", "options": ["Hubble Space Telescope", "Landsat Satellites", "Venera 7", "Apollo 17 Lunar Module (Challenger)"]},
        {"question": "Which space mission aims to collect samples from an asteroid and return them to Earth?", "answer": "OSIRIS-REx", "options": ["International Space Station (ISS)", "OSIRIS-REx", "Arcturus", "Procyon"]},
        {"question": "What was the name of the international collaboration that built and operates the International Space Station (ISS)?", "answer": "International Space Station Program", "options": ["International Space Station Program", "Apparent magnitude", "Rigel", "Vostok 1"]},
        {"question": "Which mission was launched to study the Sun and its effect on space weather?", "answer": "Solar and Heliospheric Observatory", "options": ["Space Shuttle Columbia", "Cepheid variable star", "Curiosity", "Solar and Heliospheric Observatory"]},
    ],
    "Black Holes": [
        {"question": "What is the boundary surrounding a black hole called?", "answer": "Event Horizon", "options": ["Hertzsprung-Russell diagram", "Event Horizon", "Apparent magnitude", "Vostok 1"]},
        {"question": "Which type of black hole is formed by the collapse of a star?", "answer": "Stellar Black Hole", "options": ["Voyager 1 and 2", "Stellar Black Hole", "Quasar", "Red giant"]},
        {"question": "What is the term for a black hole millions of times the mass of the Sun?", "answer": "Supermassive", "options": ["Supermassive", "Curiosity", "Venera 7", "OSIRIS-REx"]},
        {"question": "Who proposed Hawking radiation?", "answer": "Hawking", "options": ["Hawking", "Sputnik", "Interstellar", "Heliosphere"]},
        {"question": "What is the center of a galaxy often home to?", "answer": "Supermassive Black Hole", "options": ["Canopus", "Dark Matter", "Supermassive Black Hole", "Space Shuttle Columbia"]},
        {"question": "What phenomenon causes black holes to emit radiation?", "answer": "Quantum Effects", "options": ["Exoplanet", "Apollo 11", "Kinematics", "Quantum Effects"]},
        {"question": "What is the theory that describes black holes?", "answer": "General Relativity", "options": ["General Relativity", "Galaxy", "Interstellar", "Asteroid"]},
        {"question": "What is the process called where matter falls into a black hole?", "answer": "Accretion", "options": ["Photon", "Dark Energy", "Accretion", "Meteor"]},
        {"question": "What is the phenomenon when a black hole pulls in nearby matter?", "answer": "Tidal Forces", "options": ["Tidal Forces", "Heliosphere", "Arcturus", "Ionization"]},
        {"question": "What kind of waves can black holes generate when they merge?", "answer": "Gravitational Waves", "options": ["Dark Energy", "Gravitational Waves", "Galaxy", "Supernova"]},
    ],
    "Galaxies": [
        {"question": "What galaxy do we live in?", "answer": "The Milky Way", "options": ["Hawking", "The Milky Way", "Arcturus", "Capella"]},
        {"question": "What is the largest galaxy in our Local Group?", "answer": "Andromeda", "options": ["Solar System", "Apollo 11", "Andromeda", "Supernova"]},
        {"question": "What type of galaxy is the Milky Way classified as?", "answer": "Spiral", "options": ["Spiral", "Cosmos", "Nebula", "Galaxy"]},
        {"question": "What is the phenomenon where galaxies collide and merge?", "answer": "Galactic Merger", "options": ["Interstellar", "Galactic Merger", "Kinematics", "Asteroid"]},
        {"question": "What is the process by which galaxies can lose their gas and dust?", "answer": "Strangulation", "options": ["Photon", "Gravity Well", "Strangulation", "Ionization"]},
        {"question": "What is the estimated number of galaxies in the observable universe?", "answer": "Two Trillion", "options": ["Two Trillion", "Apollo 11", "Five billion ", "12 Million"]},
        {"question": "What cosmic event can lead to the formation of a new galaxy?", "answer": "Galaxy Merger", "options": ["Solar System", "Radiation", "Galaxy", "Galaxy Merger"]},
        {"question": "Which telescope has provided valuable images and data about distant galaxies?", "answer": "Hubble", "options": ["Spacecraft", "Wormhole", "Hubble", "Gravity Well"]},
        {"question": "What is the name of the effect that makes galaxies appear to be moving away from us?", "answer": "Redshift", "options": ["Hawking", "Redshift", "Kinematics", "Meteor"]},
        {"question": "Which galaxy is known for its bright central bulge and elongated shape?", "answer": "Elliptical Galaxy", "options": ["Nebula", "Elliptical Galaxy", "Ionization", "Cosmos"]},
    ]
}


def fetch_trivia_questions(amount=10):
    url = "https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=multiple"
    params = {
        "amount": amount,
        "category": 17, 
        "difficulty": "medium",
        "type": "multiple"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Failed to fetch questions: {response.status_code}")
        return []

def get_all_questions(category=None, amount=10):
    # Fetch trivia questions from the API
    api_questions = fetch_trivia_questions(amount)

    api_questions_transformed = [
        {
            "question": item["question"],
            "answer": item["correct_answer"],
            "choices": item["incorrect_answers"] + [item["correct_answer"]],  
            "category": category or "API"  
        }
        for item in api_questions
    ]

    manual_questions = questions_by_category.get(category, [])

    return manual_questions + api_questions_transformed
 


