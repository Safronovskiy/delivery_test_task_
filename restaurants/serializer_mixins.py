from slugify import slugify



class AddCreateUpdateMethodsMixin:
    """
    Provides create() and update() methods for restaurants app serializers
    """

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        if hasattr(instance, 'slug'):
            instance.slug = slugify(validated_data.get('title'))
        instance.save()
        return instance


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if hasattr(instance, 'slug'):
            instance.slug = slugify(validated_data.get('title', instance.slug))
        # update for m2m
        instance.save()
        return instance