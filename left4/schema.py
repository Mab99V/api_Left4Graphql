import graphene
import infected.schema

class Query(infected.schema.Query, graphene.ObjectType):
    pass

class Mutation(infected.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
