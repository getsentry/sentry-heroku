"""
sentry_heroku.plugin
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2015 by Sentry Team, see AUTHORS for more details.
:license: Apache 2.0, see LICENSE for more details.
"""
import sentry_heroku

from sentry.models import User
from sentry.plugins import ReleaseHook, ReleaseTrackingPlugin


class HerokuReleaseHook(ReleaseHook):
    def handle(self, request):
        email = request.POST['user']
        try:
            user = User.objects.get(
                email__iexact=email,
                sentry_orgmember_set__organization__project=self.project,
            )
        except User.MultipleObjectsReturned:
            user = None

        self.finish_release(
            version=request.POST['head_long'],
            url=request.POST['url'],
            owner=user,
        )


class HerokuPlugin(ReleaseTrackingPlugin):
    author = 'Sentry Team'
    author_url = 'https://github.com/getsentry'
    resource_links = (
        ('Bug Tracker', 'https://github.com/getsentry/sentry-heroku/issues'),
        ('Source', 'https://github.com/getsentry/sentry-heroku'),
    )

    title = 'Heroku'
    slug = 'heroku'
    description = 'Integrate Heroku release tracking.'
    version = sentry_heroku.VERSION

    def get_release_doc_html(self, hook_url):
        return """
        <p>Add Sentry as a deploy hook to automatically track new releases.</p>
        <pre class="clippy">heroku addons:create deployhooks:http --url={hook_url}</pre>
        """.format(hook_url=hook_url)

    def get_release_hook(self):
        return HerokuReleaseHook
