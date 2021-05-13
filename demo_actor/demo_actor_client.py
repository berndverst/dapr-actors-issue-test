# -*- coding: utf-8 -*-
# Copyright (c) Microsoft Corporation and Dapr Contributors.
# Licensed under the MIT License.

import asyncio
import datetime

from dapr.actor import ActorProxy, ActorId
from dapr.actor import ActorRuntime
from demo_actor_interface import DemoActorInterface


async def main():
    # Create proxy client
    proxy = ActorProxy.create('DemoActor', ActorId('1'), DemoActorInterface)

    print("Register timer", flush=True)
    await proxy.SetTimer(True)

asyncio.run(main())
