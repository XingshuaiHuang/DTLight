from agents.agent import SharedAgent
from agents.maxwave import WaveAgent
from configs.signal_config import signal_configs


class MAXPRESSURE(SharedAgent):
    def __init__(self, config, obs_act, map_name, thread_number):
        super().__init__(config, obs_act, map_name, thread_number)
        self.valid_acts = signal_configs[map_name]['valid_acts']
        self.agent = MaxAgent(signal_configs[map_name]['phase_pairs'])


class MaxAgent(WaveAgent):
    def act(self, observation, valid_acts=None, reverse_valid=None):
        repacked_obs = []
        for obs in observation:
            repacked_obs.append(obs[1:])
        return super().act(repacked_obs, valid_acts, reverse_valid)


class EMP(SharedAgent):
    """Epsilon-greedy version of MAXPRESSURE."""
    def __init__(self, config, obs_act, map_name, thread_number):
        super().__init__(config, obs_act, map_name, thread_number)
        self.valid_acts = signal_configs[map_name]['valid_acts']
        self.agent = MaxAgent(signal_configs[map_name]['phase_pairs'], epsilon_decay=config['epsilon_decay'])