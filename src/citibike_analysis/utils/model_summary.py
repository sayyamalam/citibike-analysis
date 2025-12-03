import numpy as np
import pandas as pd

def custom_summary(model):
    """
    Kompakte, interpretierbare Modellzusammenfassung für Poisson-GLMs.
    Zeigt nur das, was wichtig ist: Effekte, Signifikanz, Overdispersion.
    """

    params = model.params
    conf = model.conf_int()
    pvals = model.pvalues

    rows = []
    for name in params.index:
        rows.append({
            "feature": name,
            "coef": params[name],
            "exp(coef)": np.exp(params[name]),
            "p_value": pvals[name],
            "ci_2.5%": conf.loc[name, 0],
            "ci_97.5%": conf.loc[name, 1],
        })
        
    df = pd.DataFrame(rows)

    # Overdispersion
    pearson_chi2 = model.pearson_chi2
    df_resid = model.df_resid
    dispersion = pearson_chi2 / df_resid

    print("\n============================")
    print("  Kompakte Modell-Summary")
    print("============================\n")
    
    print(f"Anzahl Beobachtungen: {model.nobs}")
    print(f"Log-Likelihood:       {model.llf:.2f}")
    print(f"Overdispersion:       {dispersion:.3f}")
    print(f"(≈1 gut, 1–3 normal, >4 auffällig)\n")
    
    print(df.to_string(
        index=False,
        formatters={
            "coef": lambda x: f"{x: .3f}",
            "exp(coef)": lambda x: f"{x: .3f}",
            "p_value": lambda x: f"{x: .3g}",
            "ci_2.5%": lambda x: f"{x: .3f}",
            "ci_97.5%": lambda x: f"{x: .3f}",
        }
    ))

    return
