def generate_career_path(best_role):

    career_paths = {

        "Data Analyst": [
            "Learn SQL",
            "Learn Statistics",
            "Become Data Analyst",
            "Move to Data Scientist",
            "Become ML Engineer"
        ],

        "Data Scientist": [
            "Improve Statistics",
            "Learn Machine Learning",
            "Work on Projects",
            "Become Data Scientist",
            "Move to AI Engineer"
        ],

        "Ml Engineer": [
            "Master ML Algorithms",
            "Learn Model Deployment",
            "Learn Cloud",
            "Become ML Engineer",
            "Move to AI Engineer"
        ],

        "Ai Engineer": [
            "Master Deep Learning",
            "Learn NLP",
            "Learn MLOps",
            "Become AI Engineer"
        ],

        "Backend Developer": [
            "Learn SQL",
            "Learn API Development",
            "Master Python",
            "Become Backend Developer",
            "Move to ML Engineer"
        ],

        "Frontend Developer": [
            "Learn React",
            "Improve UI/UX",
            "Learn JavaScript",
            "Become Frontend Developer",
            "Move to Fullstack Developer"
        ],

        "Aws Cloud Engineer": [
            "Learn EC2",
            "Learn IAM",
            "Learn VPC",
            "Become Cloud Engineer",
            "Move to DevOps Engineer"
        ]
    }

    return career_paths.get(best_role, ["Explore more skills"])
