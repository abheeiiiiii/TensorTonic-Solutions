import numpy as np

def value_iteration_step(values, transitions, rewards, gamma):

    num_states = len(values)
    num_actions = len(rewards[0])

    V_new = np.zeros(num_states)

    for s in range(num_states):

        action_values = []

        for a in range(num_actions):

            expected_value = 0

            for s_next in range(num_states):

                expected_value += (
                    transitions[s][a][s_next] * values[s_next]
                )

            q_value = (
                rewards[s][a] +
                gamma * expected_value
            )

            action_values.append(q_value)

        V_new[s] = max(action_values)

    return V_new.tolist()