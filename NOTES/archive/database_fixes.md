"""
                    webapp2.Route('/articlefix/', ArticleFix),

                    

Ran on 2017 02 22
class ArticleFix(webapp2.RequestHandler):
    """Add the goals to articles and vice versa so we can access them"""
    def get(self):
        query = LearningGoal.query()#.order(-Article.timestamp.created)
        goals = query.fetch()
        i = 0
        for goal in goals:
            """ Removes the ghosts """
            art = ndb.gql("SELECT __key__ from Article WHERE learning_goals = :1", goal.key).get()
            if art == None:
                self.response.write("Removing goal with no article: %s" % goal.goal)
                goal.key.delete()
            else:
                goal.article = art.get().key
                goal.put()

            outputString = "> %d | %s | %s <br>" % \
            (i,  goal.goal,goal.article)
            self.response.write(outputString)
            i += 1
"""
