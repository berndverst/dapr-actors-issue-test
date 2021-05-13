# -*- coding: utf-8 -*-
# Copyright (c) Microsoft Corporation and Dapr Contributors.
# Licensed under the MIT License.

import datetime

from dapr.actor import Actor
from dapr.actor import ActorRuntime
from demo_actor_interface import DemoActorInterface


class DemoActor(Actor, DemoActorInterface):
    """Implements DemoActor actor service"""
    def __init__(self, ctx, actor_id):
        super(DemoActor, self).__init__(ctx, actor_id)

    async def _on_activate(self) -> None:
        """An callback which will be called whenever actor is activated."""
        print(f'Activate {self.__class__.__name__} actor!', flush=True)

    async def _on_deactivate(self) -> None:
        """An callback which will be called whenever actor is deactivated."""
        print(f'Deactivate {self.__class__.__name__} actor!', flush=True)

    async def set_timer(self) -> None:
        """Enables and disables a timer.

        Args:
            enabled (bool): the flag to enable and disable demo_timer.
        """
        print(f'set_timer called', flush=True)
        # Register 'demo_timer' timer and call timer_callback method
        await self.register_timer(
            'demo_timer',                   # timer name
            self.timer_callback,            # Callback method
            'timer_state',                  # Parameter to pass to the callback method
            datetime.timedelta(seconds=5),  # Amount of time to delay before the callback is invoked
            datetime.timedelta(seconds=20))  # Time interval between invocations
        print(f'set_timer is done: delay:5, interval:20', flush=True)
    
    async def timer_callback(self, state) -> None:
        """A callback which will be called whenever timer is triggered.

        Args:
            state (object): an object which is defined when timer is registered.
        """
        print(f'timer_callback is called - {state}', flush=True)