#
# Copyright (c) 2019 LG Electronics, Inc.
#
# This software contains code licensed as described in LICENSE.
#

import unittest

import lgsvl
from .common import SimConnection, spawnState, cmEqual, mEqual, TestTimeout, TestException

PROBLEM = "Object reference not set to an instance of an object"

# TODO Add tests for callbacks for when NPC changes lanes, reaches stop line

class TestNPC(unittest.TestCase):

# THIS TEST RUNS FIRST
    def test_AAA_NPC_no_scene(self):
        with SimConnection(load_scene=False) as sim:
            with self.assertRaises(Exception) as e:
                state = lgsvl.AgentState()
                agent = sim.add_agent("Jeep", lgsvl.AgentType.NPC, state)
                agent.state.position
            self.assertFalse(repr(e.exception).startswith(PROBLEM))

    def test_NPC_creation(self): # Check if the different types of NPCs can be created
        with SimConnection(60) as sim:
            state = spawnState(sim)
            state.position.x += 10
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
            spawns = sim.get_spawn()
            for name in ["Sedan", "SUV", "Jeep", "HatchBack", "SchoolBus", "DeliveryTruck"]:
                agent = self.create_NPC(sim, name)
                cmEqual(self, agent.state.position, spawns[0].position, name)
                self.assertEqual(agent.name, name)

    def test_get_agents(self):
        with SimConnection() as sim:
            agentCount = 1
            state = spawnState(sim)
            state.position.x += 10
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
            for name in ["Sedan", "SUV", "Jeep", "HatchBack", "SchoolBus", "DeliveryTruck"]:
                self.create_NPC(sim, name)
                agentCount += 1
            agents = sim.get_agents()
            self.assertEqual(len(agents), agentCount)
            agentCounter = {"XE_Rigged-apollo":0, "Sedan":0, "SUV":0, "Jeep":0, "HatchBack":0, "SchoolBus":0, "DeliveryTruck":0}
            for a in agents:
                agentCounter[a.name] += 1

            expectedAgents = ["XE_Rigged-apollo", "Sedan", "SUV", "Jeep", "HatchBack", "SchoolBus", "DeliveryTruck"]
            for a in expectedAgents:
                with self.subTest(a):
                    self.assertEqual(agentCounter[a], 1)

    def test_NPC_follow_lane(self): #Check if NPC can follow lane
        with SimConnection() as sim:
            state = spawnState(sim)
            state.position.x += 10
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
            agent = self.create_NPC(sim, "Sedan")
            agent.follow_closest_lane(True, 5.6)
            sim.run(1.0)
            self.assertLess(agent.state.speed, 5.6)
            self.assertLess(agent.state.position.z - sim.get_spawn()[0].position.z, 5.6)

    def test_rotate_NPC(self): # Check if NPC can be rotated
        with SimConnection() as sim:
            state = spawnState(sim)
            state.position.x += 10
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
            agent = self.create_NPC(sim, "SUV")
            self.assertAlmostEqual(agent.state.transform.rotation.y, 269.949, places=3)
            x = agent.state
            x.transform.rotation.y = 0
            agent.state = x
            self.assertEqual(agent.state.transform.rotation.y, 0)

    def test_blank_agent(self): # Check that an exception is raised if a blank name is given
        with SimConnection() as sim:
            with self.assertRaises(Exception) as e:
                self.create_NPC(sim, "")
            self.assertFalse(repr(e.exception).startswith(PROBLEM))

    def test_int_agent(self): # Check that an exception is raised if an integer name is given
        with SimConnection() as sim:
            with self.assertRaises(TypeError):
                    self.create_NPC(sim, 1)

    def test_wrong_type_NPC(self): # Check that an exception is raised if 4 is given as the agent type
        with SimConnection() as sim:
            with self.assertRaises(TypeError):
                sim.add_agent("SUV", 4, spawnState(sim))
    
    def test_wrong_type_value(self):
        with SimConnection() as sim:
            with self.assertRaises(ValueError):
                sim.add_agent("SUV", lgsvl.AgentType(9), spawnState(sim))

    def test_upsidedown_NPC(self): # Check that an upside-down NPC keeps falling
        with SimConnection() as sim:
            state = spawnState(sim)
            state.position.x += 10
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
            state = spawnState(sim)
            state.rotation.z += 180
            agent = sim.add_agent("HatchBack", lgsvl.AgentType.NPC, state)
            initial_height = agent.state.position.y
            sim.run(1)
            final_height = agent.state.position.y
            self.assertLess(final_height, initial_height)

    def test_flying_NPC(self): # Check if an NPC created above the map falls
        with SimConnection() as sim:
            state = spawnState(sim)
            state.position.x += 10
            state.position.y += 200
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
            state = spawnState(sim)
            state.position.y += 200
            agent = sim.add_agent("HatchBack", lgsvl.AgentType.NPC, state)
            initial_height = agent.state.position.y
            sim.run(1)
            final_height = agent.state.position.y
            self.assertLess(final_height, initial_height)

    def test_underground_NPC(self): # Check if an NPC created below the map keeps falling
        with SimConnection() as sim:
            state = spawnState(sim)
            state.position.y -= 200
            agent = sim.add_agent("HatchBack", lgsvl.AgentType.NPC, state)
            initial_height = agent.state.position.y
            sim.run(1)
            final_height = agent.state.position.y
            self.assertLess(final_height, initial_height)

    def test_access_removed_NPC(self): # Check that and exception is raised when trying to access position of a removed NPC
        with SimConnection() as sim:
            state = spawnState(sim)
            agent = sim.add_agent("HatchBack", lgsvl.AgentType.NPC, state)
            self.assertAlmostEqual(agent.state.position.x, state.position.x)
            sim.remove_agent(agent)
            with self.assertRaises(Exception) as e:
                agent.state.position
            self.assertFalse(repr(e.exception).startswith(PROBLEM))

    def test_follow_waypoints(self): # Check that the NPC can follow waypoints
        with SimConnection(60) as sim:
            state = spawnState(sim)
            state.position.x += 10
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
            spawns = sim.get_spawn()
            sx = spawns[0].position.x
            sy = spawns[0].position.y
            sz = spawns[0].position.z
            agent = self.create_NPC(sim, "Sedan")
            # snake-drive
            waypointCommands = []
            waypoints = []
            z_max = 4
            x_delta = 12
            for i in range(5):
                speed = 6 if i % 2 == 0 else 12
                px = (i + 1) * x_delta
                pz = z_max * (-1 if i % 2 == 0 else 1)

                wp = lgsvl.DriveWaypoint(lgsvl.Vector(sx - px, sy, sz - pz), speed)
                waypointCommands.append(wp)
                waypoints.append(lgsvl.Vector(sx - px, sy, sz - pz))

            def on_waypoint(agent, index):
                msg = "Waypoint " + str(index)
                mEqual(self, agent.state.position, waypoints[index], msg)
                if index == len(waypoints)-1:
                    sim.stop()

            agent.on_waypoint_reached(on_waypoint)

            agent.follow(waypointCommands)

            sim.run()

    def test_high_waypoint(self): # Check that a NPC will drive to under a high waypoint
        try:
            with SimConnection(15) as sim:
                state = spawnState(sim)
                state.position.x += 10
                sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
                spawns = sim.get_spawn()
                sx = spawns[0].position.x
                sy = spawns[0].position.y
                sz = spawns[0].position.z
                agent = self.create_NPC(sim, "Sedan")

                px = 12
                pz = 4
                py = 5
                speed = 6
                wp = [lgsvl.DriveWaypoint(lgsvl.Vector(sx-px, sy+py, sz-pz), speed)]

                def on_waypoint(agent,index):
                    raise TestException("Waypoint reached?")
                agent.on_waypoint_reached(on_waypoint)
                agent.follow(wp)
                sim.run(10)
        except TestException as e:
            self.assertNotIn("Waypoint reached?", repr(e.exception))

    def test_npc_different_directions(self): # Check that specified velocities match the NPC's movement
        with SimConnection() as sim:
            state = spawnState(sim)
            state.position.x += 10
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
            state = spawnState(sim)
            state.velocity = lgsvl.Vector(-10,0,0)
            npc = sim.add_agent("SUV", lgsvl.AgentType.NPC, state)
            sim.run(1)
            self.assertNotAlmostEqual(state.position.x, npc.state.position.x, delta=0.2)
            self.assertAlmostEqual(state.position.y, npc.state.position.y, delta=0.2)
            self.assertAlmostEqual(state.position.z, npc.state.position.z, delta=0.2)
            sim.remove_agent(npc)
            state.velocity = lgsvl.Vector(0,10,0)
            npc = sim.add_agent("SUV", lgsvl.AgentType.NPC, state)
            sim.run(1)
            self.assertNotAlmostEqual(state.position.y, npc.state.position.y, delta=0.2)
            self.assertAlmostEqual(state.position.x, npc.state.position.x, delta=0.2)
            self.assertAlmostEqual(state.position.z, npc.state.position.z, delta=0.2)
            sim.remove_agent(npc)
            state.velocity = lgsvl.Vector(0,0,-10)
            npc = sim.add_agent("SUV", lgsvl.AgentType.NPC, state)
            sim.run(1)
            self.assertNotAlmostEqual(state.position.z, npc.state.position.z, delta=0.2)
            self.assertAlmostEqual(state.position.y, npc.state.position.y, delta=0.2)
            self.assertAlmostEqual(state.position.x, npc.state.position.x, delta=0.2)

    def test_stopline_callback(self):
        with self.assertRaises(TestException) as e:
            with SimConnection(60) as sim:
                state = lgsvl.AgentState()
                point = lgsvl.Vector(-39, 10.7,50)
                state.transform = sim.map_point_on_lane(point)
                #npc = sim.add_agent("SUV", lgsvl.AgentType.NPC, state)
                npc = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)

                def on_stop_line(agent):
                    raise TestException("Waypoint reached")

                npc.follow_closest_lane(True, 10)
                npc.on_stop_line(on_stop_line)

                state.transform = sim.map_point_on_lane(lgsvl.Vector(-39,10.7,60))
                sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, state)
                sim.run(60)
        self.assertIn("Waypoint reached", repr(e.exception))

    def test_remove_npc_with_callback(self):
        with SimConnection() as sim:
            npc = sim.add_agent("Sedan", lgsvl.AgentType.NPC, spawnState(sim))

            def on_stop_line(agent):
                pass

            npc.follow_closest_lane(True, 10)
            npc.on_stop_line(on_stop_line)

            sim.run(1)
            sim.remove_agent(npc)
            with self.assertRaises(Exception):
                npc.state.position
            with self.assertRaises(KeyError):
                sim.callbacks[npc]

    def test_spawn_speed(self):
        with SimConnection() as sim:
            sim.add_agent("XE_Rigged-apollo", lgsvl.AgentType.EGO, spawnState(sim, 1))
            npc = sim.add_agent("Sedan", lgsvl.AgentType.NPC, spawnState(sim))

            self.assertEqual(npc.state.speed,0)
            sim.run(1)
            self.assertEqual(npc.state.speed,0)


    def create_NPC(self, sim, name): # Create the specified NPC
        return sim.add_agent(name, lgsvl.AgentType.NPC, spawnState(sim))
