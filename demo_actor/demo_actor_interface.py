# -*- coding: utf-8 -*-
# Copyright (c) Microsoft Corporation and Dapr Contributors.
# Licensed under the MIT License.

from dapr.actor import ActorInterface, actormethod


class DemoActorInterface(ActorInterface):

    @actormethod(name="SetTimer")
    async def set_timer(self) -> None:
        ...
