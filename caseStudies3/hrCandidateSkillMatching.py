# ==================================================
# Case Study 9: HR Candidate Skill-Matching Analyzer
# ==================================================


# ==================================================
# Task 1: Job Requirements
# ==================================================

jobRequirements = {
    "Python",
    "SQL",
    "Git",
    "Docker"
}


# ==================================================
# Task 2: Candidate Profiles
# ==================================================

candidateProfiles = {

    "Reyaz": {
        "Python",
        "SQL",
        "Git",
        "Docker"
    },

    "Tufail": {
        "Python",
        "SQL",
        "Git"
    },

    "Burhan": {
        "Python",
        "Git"
    },

    "Hazim": {
        "Python",
        "SQL",
        "Docker"
    }
}


# ==================================================
# Task 3 & Task 4: Analyze Candidate
# ==================================================

def analyzeCandidate(candidateName, candidateSkills, jobRequirements):

    matchedSkills = candidateSkills.intersection(jobRequirements)

    missingSkills = jobRequirements.difference(candidateSkills)

    matchPercentage = (
        len(matchedSkills) / len(jobRequirements)
    ) * 100

    return matchedSkills, missingSkills, matchPercentage


# ==================================================
# Task 5: Generate Recruitment Report
# ==================================================

def generateReport(candidateProfiles, jobRequirements):

    candidateResults = []

    for candidateName, candidateSkills in candidateProfiles.items():

        matchedSkills, missingSkills, matchPercentage = analyzeCandidate(
            candidateName,
            candidateSkills,
            jobRequirements
        )

        candidateResults.append(
            (
                candidateName,
                matchedSkills,
                missingSkills,
                matchPercentage
            )
        )

    # Sort candidates by match percentage
    candidateResults.sort(
        key=lambda candidate: candidate[3],
        reverse=True
    )

    print("\n")

    print("=" * 70)
    print("       HR RECRUITMENT SKILL COMPATIBILITY REPORT")
    print("=" * 70)

    print(
        f"{'Rank':<6}"
        f"{'Candidate':<15}"
        f"{'Matched Skills':<20}"
        f"{'Missing Skills':<20}"
        f"{'Match %':<10}"
    )

    print("-" * 70)

    for rank, candidate in enumerate(candidateResults, start=1):

        candidateName = candidate[0]
        matchedSkills = candidate[1]
        missingSkills = candidate[2]
        matchPercentage = candidate[3]

        matchedText = ", ".join(sorted(matchedSkills))
        missingText = ", ".join(sorted(missingSkills))

        print(
            f"{rank:<6}"
            f"{candidateName:<15}"
            f"{matchedText:<20}"
            f"{missingText:<20}"
            f"{matchPercentage:.1f}%"
        )

    print("-" * 70)

    print("Required Skills:", ", ".join(sorted(jobRequirements)))

    print("=" * 70)


# ==================================================
# Main Program
# ==================================================

generateReport(candidateProfiles, jobRequirements)