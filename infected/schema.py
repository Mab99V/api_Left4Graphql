import graphene
from graphene_django import DjangoObjectType

from .models import sick

class sickType(DjangoObjectType):
    class Meta:
        model = sick

class Query(graphene.ObjectType):
    infected = graphene.List(sickType)

    def resolve_infected(self,info, **kwargs):
        return sick.objects.all()

class CreateInf(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    ability = graphene.String()

    class Arguments:
        name = graphene.String()
        ability = graphene.String()

    def mutate(self, info, name, ability):
        s = sick(name=name,ability=ability)
        s.save()

        return CreateInf(
            id=s.id,
            name=s.name,
            ability=s.ability,
        )

class Mutation(graphene.ObjectType):
    create_infected = CreateInf.Field()
