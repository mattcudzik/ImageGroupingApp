import ExampleMetric
import abc

class IMetric:

    def get_Values(self, paths, choosen):
        metric = ExampleMetric.ExampleMetric()

        metricArray = []
        for path in paths:
            metricArray.append(metric.Compare(path, paths))  # wybor metryki

        return metricArray

