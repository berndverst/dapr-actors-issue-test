# -*- coding: utf-8 -*-
# Copyright (c) Microsoft Corporation and Dapr Contributors.
# Licensed under the MIT License.

from abc import abstractproperty
from fastapi import FastAPI  # type: ignore
from dapr.ext.fastapi import DaprActor  # type: ignore
from demo_actor import DemoActor
from dapr.actor import ActorRuntime

import datetime


app = FastAPI(title=f'{DemoActor.__name__}Service')

config = ActorRuntime.get_actor_config()
config._actor_idle_timeout = datetime.timedelta(seconds=10)
ActorRuntime.set_actor_config(config)

# Add Dapr Actor Extension
actor = DaprActor(app)

@app.on_event("startup")
async def startup_event():
    # Register DemoActor
    await actor.register_actor(DemoActor)
