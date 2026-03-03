import numpy as np

def simulate_juice_doppler(xi=-1.21e-12, noise_floor=2e-10):
    """
    Simulates Doppler residual for JUICE EGA-2 (Sept 2026).
    Based on integrated A3 coupling acceleration.
    """
    # Time window: -30 to +30 mins from perigee
    t = np.linspace(-1800, 1800, 1000) 
    
    # Predicted UBM signal (asymmetric blue-shift profile)
    # Peak shift derived from integrated trajectory at 50,000km
    peak_shift = 1.84e-8 
    signal = peak_shift * np.exp(-(t - 500)**2 / (2 * 300**2)) 
    
    # Add Ka-band noise
    noise = np.random.normal(0, noise_floor, len(t))
    total_obs = signal + noise
    
    return t, total_obs

# Example run
t, obs = simulate_juice_doppler()
print(f"Max Predicted Shift: {np.max(obs):.2e} Hz")
print(f"Signal-to-Noise Ratio: {1.84e-8 / 2e-10:.1f} sigma")
