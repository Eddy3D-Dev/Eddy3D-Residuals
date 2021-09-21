from importlib.machinery import ModuleSpec, SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec
import os.path
import types
import unittest


def import_from_source(name: str, file_path: str) -> types.ModuleType:
    loader: SourceFileLoader = SourceFileLoader(name, file_path)
    spec: ModuleSpec = spec_from_loader(loader.name, loader)
    module: types.ModuleType = module_from_spec(spec)
    loader.exec_module(module)
    return module


script_path: str = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "plot.py",
    )
)

plot: types.ModuleType = import_from_source("plot", script_path)


class PlotTestCase(unittest.TestCase):
    def plotCandy(self: "PlotTestCase") -> None:
        self.assertEqual(plot.plot(), "plot")


if __name__ == '__main__':
    unittest.main()
