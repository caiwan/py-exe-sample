import sys
from setuptools import setup, find_namespace_packages


try:
    from cx_Freeze import Executable
except ImportError:
    import pip

    pip.main(["install", "cx_Freeze"])

    from cx_Freeze import Executable

target_name = "sample_qt_app"
entry_point = "src/sample_qt_app/app.py"
additional_modules = ["sample_qt_app"]

executable = Executable(
    script=entry_point,
    base="Win32GUI" if sys.platform == "win32" else None,
    target_name=target_name,
    icon=None,
)

options = {
    "build_exe": {
        "packages": [],  # Additional packages to include
        "includes": additional_modules,
        "excludes": [
            "tkinter",
            "tcl",
            "tk",
            "unittest",
            "test",
        ],  # Modules to exclude
        "optimize": 2,  # Optimization level
    }
}


def main():
    # Note: pip calls [egg_info, (develop|install)]

    extra_options = {}
    if len(sys.argv) >= 2 and sys.argv[1] == "build_exe":
        extra_options = {
            "options": options,
            "executables": [executable],
        }

    setup(
        name="sample-qt-app",
        version="1.0",
        author="Your Name",
        description="Sample Qt App",
        long_description=open("README.md").read(),
        install_requires=[
            "PyQt5",
        ],
        package_dir={"": "src"},
        packages=find_namespace_packages(
            where="src",
            exclude=[
                "tests",
                "*.tests",
                "tests.*",
                "*.tests.*",
            ],
        ),
        entry_points={
            "console_scripts": [
                "sample-qt-app=sample_qt_app.app:main",
            ]
        },
        extras_require={
            "test": [
                "pytest",
                "flake8",
            ],
        },
        flake8={
            "ignore": "E203, E266, E501, W503, F403, F401",
            "max-line-length": "120",
            "max-complexity": "24",
            "select": "B,C,E,F,W,T4,B9",
        },
        black={
            "line-length": "120",
        },
        **extra_options,
    )


if __name__ == "__main__":
    main()
