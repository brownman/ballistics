from ballistics.collision.broadphase.dispatcher cimport btDispatcher, Dispatcher
from ballistics.collision.dispatch.config cimport btCollisionConfiguration


cdef extern from "BulletCollision/CollisionDispatch/btCollisionDispatcher.h":

    cdef cppclass btCollisionDispatcher:
        btCollisionDispatcher(btCollisionConfiguration* collisionConfiguration)


cdef class CollisionDispatcher(Dispatcher):

    cdef object config
