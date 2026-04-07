import pandas as pd

def main():

    # -----------------------------
    # 1. LOAD DATA (CSV VERSION)
    # -----------------------------
    df = pd.read_csv("data_center_sites.csv")

    # -----------------------------
    # 2. CATEGORY CALCULATIONS
    # -----------------------------

    # Hydrological & Regulatory Risk
    df["Hydro_Reg"] = df[
        ["Baseline Water Stress", "Annual Precipitation", "Recycled Water Infrastructure"]
    ].mean(axis=1)

    # Climate & Operational Physics
    df["Climate_Op"] = df[
        ["Cooling Degree Days", "Annual Mean Humidity", "Grid Carbon Intensity", "Renewable Energy Mix"]
    ].mean(axis=1)

    # Economic & Social Impact
    df["Econ_Social"] = df[
        ["Industrial Electricity Rate", "Water & Sewer Cost", "Environmental Justice Index"]
    ].mean(axis=1)

    # Natural Hazards Risk
    df["Hazards"] = df[
        ["Flood Risk", "Tornado Frequency", "Wildlife Hazard", "Winter Weather Disruption", "Seismic Hazard"]
    ].mean(axis=1)

    # Biodiversity Risk
    df["Biodiversity"] = df["Protected Area Proximity"]

    # -----------------------------
    # 3. USER-DEFINED WEIGHTS
    # -----------------------------
    print("Enter weights for each category (they should sum to 1.0):")

    weights = {
        "Hydro_Reg": float(input("Hydrological & Regulatory Risk weight: ")),
        "Climate_Op": float(input("Climate & Operational Physics weight: ")),
        "Econ_Social": float(input("Economic & Social Impact weight: ")),
        "Hazards": float(input("Natural Hazards Risk weight: ")),
        "Biodiversity": float(input("Biodiversity Risk weight: "))
    }

    # Normalize weights
    total_weight = sum(weights.values())
    weights = {k: v / total_weight for k, v in weights.items()}

    # -----------------------------
    # 4. TOTAL SCORE
    # -----------------------------
    df["Total Score"] = (
        df["Hydro_Reg"] * weights["Hydro_Reg"] +
        df["Climate_Op"] * weights["Climate_Op"] +
        df["Econ_Social"] * weights["Econ_Social"] +
        df["Hazards"] * weights["Hazards"] +
        df["Biodiversity"] * weights["Biodiversity"]
    )

    # -----------------------------
    # 5. RANKING
    # -----------------------------
    df["Rank"] = df["Total Score"].rank(ascending=False)
    df_sorted = df.sort_values(by="Total Score", ascending=False)

    # -----------------------------
    # 6. OUTPUT
    # -----------------------------
    print("\nFinal Rankings:")
    print(df_sorted[["City", "Total Score", "Rank"]])


if __name__ == "__main__":
    main()
