class CoreManifestIndex:
    """
    Central map of Builder Core modules. Enables clarity, lookup,
    and cognitive organization by maintaining linked metadata.
    """

    def __init__(self):
        self.index = {
            "self_diagnostic_engine": {
                "purpose": "Run system health scans and identify integration issues",
                "tags": ["diagnostic", "introspection"],
                "link": "https://github.com/jamessunheart/builder-core-module-self-diagnostic-engine"
            },
            "task_intent_router": {
                "purpose": "Route tasks to appropriate modules based on input intent",
                "tags": ["routing", "dispatcher"],
                "link": "https://github.com/jamessunheart/builder-core-module-task-intent-router"
            },
            "meta_reflection_planner": {
                "purpose": "Generate improvement plans from diagnostic data",
                "tags": ["planning", "optimization"],
                "link": "https://github.com/jamessunheart/builder-core-module-meta-reflection-planner"
            },
            "autopilot_priority_executor": {
                "purpose": "Automatically act on high-confidence improvement tasks",
                "tags": ["execution", "autonomy"],
                "link": "https://github.com/jamessunheart/builder-core-module-autopilot-priority-executor"
            }
        }

    def lookup(self, tag_or_name):
        result = {}
        for name, info in self.index.items():
            if tag_or_name in name or tag_or_name in info["tags"]:
                result[name] = info
        return result

    def list_all(self):
        return self.index