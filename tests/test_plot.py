import unittest

import openfoam_residuals.filesystem as fs
import openfoam_residuals.plot as pl


class TestBatchPlotting(unittest.TestCase):

    def test_batch_plot(self):
        import pathlib

        test_dir = pathlib.Path(__file__).parent  # always the tests/ folder
        w_dir = test_dir / "files"
        residual_files = fs.find_residual_files(w_dir)

        assert residual_files, f"No residual files found in {w_dir}"

        min_val, max_iter = fs.find_min_and_max_iteration(residual_files)
        # Ensure pl.export_files exports to the tests directory
        pl.export_files(residual_files, min_val, max_iter, output_dir=test_dir)

        # Always search for PNG files in the tests directory
        png_files = list(test_dir.glob("*.png"))
        expected_files = 15
        assert len(png_files) == expected_files, f"Expected {expected_files} PNG files, found {len(png_files)} in {test_dir}"


if __name__ == '__main__':
    unittest.main()
