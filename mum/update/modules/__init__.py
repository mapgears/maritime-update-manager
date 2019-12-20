"""Manage update modules"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod
from pkg_resources import iter_entry_points
from typing import Optional, Dict, Type, MutableMapping


_update_modules: Optional[Dict[str, Type[UpdateModule]]] = None


def get_update_module(module_name: str) -> Type[UpdateModule]:
    global _update_modules
    if _update_modules is None:
        _update_modules = {
            e.name: e.load()
            for e in iter_entry_points('mum.update_module')
        }

    return _update_modules.get(module_name, NullUpdateModule)


class UpdateModule(metaclass=ABCMeta):
    """Base class for an Update Module"""
    __slots__ = ('module_name', 'enabled', 'id', 'tag',)

    def __init__(self, module=None, enabled=True, tag='', **kwargs):
        self.enabled = enabled
        self.module_name = module
        self.tag = tag
        super().__init__(**kwargs)

    def needs_update(
        self,
        state: MutableMapping,
        transient_state: MutableMapping
    ) -> bool:
        """Check if the update module should run.

        Subclasses may override this method to check if new files are
        available before running their update process.

        :param state: State object that is persisted across runs. Update
            modules are encouraged to use their tag in some way when accessing
            this object to avoid collisions. The primary purpose of this state
            is for modules to remember what they need to determine if they
            should run.
        :param transient_state: State object to communicate across modules.
            This state is not saved after each run and is mainly intended for
            modules to pass along information to later modules via well-known
            keys.
        """
        return True

    @abstractmethod
    def update(self, state: MutableMapping, transient_state: MutableMapping):
        """Perform the update"""
        pass


class NullUpdateModule(UpdateModule):
    """Update module not installed"""
    __slots__ = ()

    def __init__(self, module=None, enabled=True, **kwargs):
        # Swallow all kwargs from config file
        super().__init__(module=module, enabled=enabled)

    def update(self, state, transient_state):
        raise NotImplementedError(
            f"Update Module '{self.module_name}' not found"
        )
