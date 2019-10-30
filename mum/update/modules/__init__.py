"""Manage update modules"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod
from pkg_resources import iter_entry_points
from typing import Optional, Dict, Type, Mapping


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
    __slots__ = ('module_name', 'enabled',)

    def __init__(self, module=None, enabled=True, **kwargs):
        self.enabled = enabled
        self.module_name = module
        super().__init__(**kwargs)

    def needs_update(self, state: Mapping):
        """Check if the update module should run.

        Subclasses may override this method to check if new files are
        available before running their update process.
        """
        return True

    @abstractmethod
    def update(self, state: Mapping):
        """Perform the update"""
        pass


class NullUpdateModule(UpdateModule):
    """Update module not installed"""
    __slots__ = ()

    def __init__(self, module=None, enabled=True, **kwargs):
        # Swallow all kwargs from config file
        super().__init__(module=module, enabled=enabled)

    def update(self, state):
        raise NotImplementedError(
            f"Update Module '{self.module_name}' not found"
        )
