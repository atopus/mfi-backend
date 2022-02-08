from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from peaks.models import Peak
from peaks.serializers import PeakSerializer


class PeakViewSet(ModelViewSet):

    queryset = Peak.objects.exclude(Q(lat=0) | Q(lon=0))
    serializer_class = PeakSerializer

    def list(self, request):

        boundarie_names = ['n', 's', 'e', 'w']
        boundaries = [request.query_params.get(c) for c in boundarie_names]

        if any(boundaries):

            if not all(boundaries):
                return Response({
                    "error": "Missing data. When defining a bounding box, every coordinates must be set."
                }, status=HTTP_400_BAD_REQUEST)

            north, south, east, west = boundaries
            qs = self.get_queryset()
            result = qs.filter(
                lat__gte=south,
                lat__lte=north,
                lon__gte=west,
                lon__lte=east
            )

            # There may be a lot of peaks, which has a nasty impact on front performance.
            # Let's filter on the highests 10.
            # NOTE(pantropius): This is not so cool...
            highests = result.order_by('-altitude')
            highests_top = highests[:10]

            # TODO: change de queryset instead ?
            serialized = [PeakSerializer(res).data for res in highests_top]
            return Response(data=serialized)

        return super(PeakViewSet, self).list(request)
