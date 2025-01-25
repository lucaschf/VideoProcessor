from injector import Binder, Injector

from src.application.di.modules import ExternalServiceModule


def configure_injector(binder: Binder) -> None:  # noqa: ARG001
    """Configures the injector by installing the Modules."""
    binder.install(ExternalServiceModule())


dependency_injector = Injector([configure_injector])

__all__ = ["dependency_injector"]

