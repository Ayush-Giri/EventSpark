from rest_framework import serializers
from event.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 1

    def to_internal_value(self, data):
        data = data.copy()
        is_online = data.get("is_online")
        if is_online == True:
            is_venue_link_valid = data.get("venue_address").startswith("www")
            if is_venue_link_valid:
                return super().to_internal_value(data)
            else:
                raise serializers.ValidationError("oops link is not valid")
        else:
            return super().to_internal_value(data)
            
        

