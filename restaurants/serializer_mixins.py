from slugify import slugify



class AddCreateMethodMixin:
    """ Provides create() and update() methods ... """

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        print(instance.__dict__)
        if hasattr(instance, 'slug'):
            instance.slug = slugify(validated_data.get('title'))
        instance.save()
        return instance


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if hasattr(instance, 'slug'):
            instance.slug = slugify(validated_data.get('title', instance.slug))
        instance.save()
        return instance