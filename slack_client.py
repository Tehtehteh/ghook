import slackclient
import logging

slack_logger = logging.getLogger('slack')


class GitSlackBot:

    def __init__(self, *, slack_token=None):
        slack_logger.info('Connecting slack bot...')
        self.sc = None
        self._channels = None
        self._users = []
        if not slack_token:
            slack_logger.warning('No slack token provided. Raising error')
            raise NotImplementedError('Please provide token')
        else:
            try:
                self.sc = slackclient.SlackClient(token=slack_token)
                slack_logger.info('Successfully connected to slack. Getting users list')
                users = self.do('users.list')
                self._users = users.get('members')
                channels = self.do('channels.list')
                self._channels = channels['channels']
                slack_logger.info(f'Got users from API: {channels}')
            except Exception as e:
                slack_logger.error(f'Error connecting to slack: {e}')

    def do(self, *args, **kwargs):
        result = self.sc.api_call(*args, **kwargs)
        if result.get('ok', False):
            return result
        else:
            slack_logger.error(f'Error executing {result.get("req_method", "API method")}. Error: {result["error"]}')
            raise Exception

    @property
    def status(self):
        return self.sc.server

    @property
    def users(self):
        return self._users

    @property
    def channels(self):
        return self._channels

    def dispatch(self, event):
        # todo implement pub-sub
        pass
