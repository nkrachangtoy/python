# Define dictionary
facts = {
    'Jason': 'Can fly an airplane',
    'Jeff': 'Is affraid of clowns',
    'David': 'Plays the piano'
}
# Display facts


def display_facts(facts):
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
    print()


display_facts(facts)

facts['Jeff'] = 'Is afraid of heights'
facts['Jill'] = 'Can hula dance'

display_facts(facts)
