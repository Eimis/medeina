from django_states.machine import StateDefinition, StateMachine, \
    StateTransition


class IssueStates(StateMachine):

    ##########
    # States #
    ##########
    class open(StateDefinition):
        description = 'Issue is open'
        initial = True

    class solved(StateDefinition):
        description = 'Issue is solved'

    ###############
    # Transitions #
    ###############
    class mark_as_solved(StateTransition):
        from_states = ['open']
        to_state = 'solved'
        description = 'Mark Issue as solved'

        def has_permission(cls, instance, user):
            # Only allow to mark issues as solved for Superusers
            return user.is_superuser

        def handler(transition, instance, user):
            # some custom actions during transition can be added here
            pass
