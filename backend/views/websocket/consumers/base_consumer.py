import pysnooper
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ConsumerException(Exception):
    """Consumer的Exception"""
    pass


class BaseJsonConsumer(AsyncJsonWebsocketConsumer):
    namespace = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.consumer_id = id(self)
        self.user = None
        self.room_group_name = None
        self.action_map = {}

    async def send_data(self, content, mutation=None, action=None, namespace=None):
        """
         为VueNativeWebSocket添加namespace等并发送

        指定action或者mutation其中一个
        :param dict or list content:
        :param str mutation:
        :param str action:
        :param str namespace:
        :return:
        """
        with pysnooper.snoop():
            namespace = self.namespace if namespace is None else namespace
            send_data = {
                'namespace': namespace
            }
            if mutation and action:
                raise ConsumerException('mutation and action is only one.')

            if (not mutation) and (not action):
                raise ConsumerException('mutation or action must be set.')

            if mutation:
                send_data['mutation'] = mutation
            if action:
                send_data['action'] = action
            if not isinstance(content, dict):
                content = {
                    'data': content,
                }
            content.update(send_data)
            await self.send_json(content)

    async def receive_json(self, content, **kwargs):
        """
        根据类型调用和执行action
        :param dict content:
        :param kwargs:
        :return:
        """
        action = self.action_map.get(content['type'])
        if not action:
            raise ConsumerException('{} is not a valid action_type'.format(content['type']))
        await action(content)

    async def group_add(self, group_name, channel_name):
        """
        加入group
        """
        await self.channel_layer.group_add(
            group_name,
            channel_name
        )

    async def group_send(self, group_name, body):
        """
        在组里发信息
        """
        await self.channel_layer.group_send(
            group_name,
            body
        )
