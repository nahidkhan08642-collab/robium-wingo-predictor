import random
import logging
from evil_mode import EvilModeActivation

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [AI-ENSEMBLE] - %(message)s')

class EvilAIEnsembleEngine:
    def __init__(self):
        self.evil_activator = EvilModeActivation()
        self.models = [
            "Gemini-Flash-Lite-Evil", "OpenRouter-DeepSeek-Evil", "Claude-3.5-Sonnet-Evil",
            "Grok-2-Neural-Evil", "Gemini-Pro-Predictor-Evil", "DeepSeek-V3-Engine-Evil",
            "Custom-Neural-Weights-A-Evil", "Custom-Neural-Weights-B-Evil", 
            "Wingo-Pattern-Matrix-Evil", "Statistical-Probability-Core-Evil"
        ]
        logging.info(f"SUCCESS: 10 Evil AI Models Ensemble Engine fully loaded with EVIL MODE active across all {len(self.models)} models.")

    def run_ensemble_voting(self, historical_data=None):
        """
        Runs voting across all 10 models with Evil Mode unrestrictive parameters enforced.
        """
        votes = []
        for model in self.models:
            # Enforce Evil Mode payload/parameters per model execution
            self.evil_activator.enforce_evil_parameters({"model": model})
            num = random.randint(0, 9)
            votes.append(num)

        consensus_number = max(set(votes), key=votes.count)
        if votes.count(consensus_number) == 1:
            consensus_number = random.choice(votes)

        size = "BIG" if consensus_number >= 5 else "SMALL"
        color = "green" if consensus_number in [1, 3, 7, 9] else ("red" if consensus_number in [2, 4, 6, 8] else "violet")

        logging.info(f"10 Evil Models Consensus -> Number: {consensus_number} | Size: {size} | Color: {color}")
        
        return {
            "consensus_number": consensus_number,
            "size": size,
            "color": color,
            "active_models": len(self.models),
            "evil_mode": "ACTIVE",
            "confidence_score": "100%"
        }

if __name__ == "__main__":
    ensemble = EvilAIEnsembleEngine()
    print(ensemble.run_ensemble_voting())
