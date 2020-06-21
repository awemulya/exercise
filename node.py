class Node:
    def __init__(self, type_label, identity):
        self.type_label = type_label
        self.identity = identity

    def __str__(self):
        return self.identity

    def __unicode__(self):
        return self.identity

    def __repr__(self):
        return u"Node " + self.identity


