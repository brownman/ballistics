from ballistics.linearmath import Vector3, Transform, Quaternion
from ballistics.linearmath.motion_state import DefaultMotionState
from ballistics.collision.broadphase import DbvtBroadphase
from ballistics.collision.dispatch import DefaultCollisionConfiguration, \
        CollisionDispatcher
from ballistics.collision.shapes import StaticPlaneShape, SphereShape
from ballistics.dynamics.world import DiscreteDynamicsWorld
from ballistics.dynamics.constraintsolver import SequentialImpulseConstraintSolver
from ballistics.dynamics.rigid_body import RigidBody, RigidBodyConstructionInfo


def test_hello_world():
    """
    Reproduce the hello world example from the tutorial.
    """
    # Setup world
    broadphase = DbvtBroadphase()
    collision_config = DefaultCollisionConfiguration()
    dispatcher = CollisionDispatcher(collision_config)
    solver = SequentialImpulseConstraintSolver()
    world = DiscreteDynamicsWorld(dispatcher, broadphase, solver,
            collision_config)
    world.setGravity(Vector3(0, -9.8, 0))
    # Create collision shapes
    ground_shape = StaticPlaneShape(Vector3(0, 1, 0), 1)
    ball_shape = SphereShape(1)
    # Create ground rigid body
    ground_motion_state = DefaultMotionState(
            Transform(Quaternion(0, 0, 0, 1), Vector3(0, -1, 0)))
    ground_rigid_body_ci = RigidBodyConstructionInfo(0, ground_motion_state,
            ground_shape, Vector3(0, 0, 0))
    ground_rigid_body = RigidBody(ground_rigid_body_ci)
    world.addRigidBody(ground_rigid_body)
    # Create ball rigid body
    ball_motion_state = DefaultMotionState(
            Transform(Quaternion(0, 0, 0, 1), Vector3(0,50,0)))
    mass = 1
    ball_inertia = ball_shape.calculateLocalInertia(mass)
    ball_rigid_body_ci = RigidBodyConstructionInfo(mass, ball_motion_state,
            ball_shape, ball_inertia)
    ball_rigid_body = RigidBody(ball_rigid_body_ci)
    world.addRigidBody(ball_rigid_body)
    # Simulate 300 frames, printing ball height    
    for i in range(300):
        world.stepSimulation(1.0 / 60.0, 10)
        trans = ball_rigid_body.motionState.worldTransform
        print "sphere height:", trans.origin.y
