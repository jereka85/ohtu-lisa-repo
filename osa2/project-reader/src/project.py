class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, python, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.dependencies.append(f"python{python}")
        self.license = license
        self.authors = [a["name"] for a in authors]

    def _stringify_dependencies(self, dependencies):
        alku = "\n-  ".join(dependencies) if len(dependencies) > 0 else "-"
        return "\n-  " + alku + "\n"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense:  {self.license}"
            f"\n"
            f"\nAuthors: {self._stringify_dependencies(self.authors)}" 
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}" 
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )