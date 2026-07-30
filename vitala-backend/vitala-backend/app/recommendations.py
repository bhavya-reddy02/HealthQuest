"""Health recommendations engine based on BMI and chronic conditions."""

def get_recommendations(height_cm: float | None, weight_kg: float | None, conditions: list[str]) -> dict:
    """Generate custom recommendations and category labels based on height, weight, and chronic conditions."""
    if not height_cm or not weight_kg:
        bmi = None
        bmi_cat = "Unknown"
        bmi_color = "var(--muted)"
    else:
        h = height_cm / 100.0
        bmi = round(weight_kg / (h * h), 1)
        if bmi < 18.5:
            bmi_cat = "Underweight"
            bmi_color = "var(--azure)"
        elif bmi < 25.0:
            bmi_cat = "Healthy range"
            bmi_color = "var(--vital)"
        elif bmi < 30.0:
            bmi_cat = "Overweight"
            bmi_color = "var(--gold)"
        else:
            bmi_cat = "Obesity range"
            bmi_color = "var(--flame)"

    tips = []

    # 1. Condition-specific recommendations
    has_any_condition = False
    for cond in conditions:
        c_lower = cond.lower()
        if c_lower in ("diabetes", "diabetic"):
            has_any_condition = True
            tips.append({
                "category": "🩺 Diabetes Management",
                "text": "Prioritize complex carbohydrates (oats, brown rice) and fiber to help regulate blood glucose levels. Engage in moderate aerobic exercise (like brisk walking) for at least 30 minutes daily to enhance insulin sensitivity."
            })
        elif c_lower in ("hypertension", "bp", "high blood pressure"):
            has_any_condition = True
            tips.append({
                "category": "❤️ Blood Pressure Control",
                "text": "Adopt a low-sodium diet rich in potassium, calcium, and magnesium (DASH diet). Incorporate stress management activities such as guided deep breathing or mindfulness meditation to support blood vessels."
            })
        elif c_lower in ("heart_disease", "heart disease", "cardiovascular"):
            has_any_condition = True
            tips.append({
                "category": "🫀 Heart Health",
                "text": "Incorporate heart-healthy fats (extra virgin olive oil, nuts, avocados) and omega-3 fatty acids. Maintain moderate, steady-state physical activities and avoid high-strain weight lifting without medical approval."
            })
        elif c_lower in ("thyroid", "thyroid issue"):
            has_any_condition = True
            tips.append({
                "category": "🦋 Thyroid Care",
                "text": "For hypothyroidism, support your metabolic rate with lean protein and regular strength exercises. For hyperthyroidism, ensure adequate calorie intake with nutrient-dense foods to prevent muscle loss."
            })
        elif c_lower in ("asthma", "respiratory"):
            has_any_condition = True
            tips.append({
                "category": "🫁 Asthma & Breathing",
                "text": "Prefer indoor exercise on high-pollen or freezing cold days. Incorporate deep-breathing exercises (like diaphragmatic breathing) to expand lung capacity and always keep your rescue inhaler handy."
            })

    # 2. BMI-specific recommendations
    if bmi is not None:
        if bmi < 18.5:
            tips.append({
                "category": "⚖️ Weight Gain Advice",
                "text": "Aim for a slight calorie surplus with nutrient-dense, calorie-dense foods (e.g., seeds, nut butters, whole grains). Focus on resistance training to build healthy muscle mass."
            })
        elif bmi >= 25.0:
            tips.append({
                "category": "⚖️ Weight Management Advice",
                "text": "Focus on a sustainable calorie deficit (e.g. 500 kcal/day reduction) by eating high-protein, high-fiber meals. Mix aerobic cardio with strength training to preserve muscle while losing fat."
            })
        elif not has_any_condition:
            tips.append({
                "category": "✨ General Wellness",
                "text": "Your BMI is in a healthy range! Keep up the good work by eating a balanced diet, staying hydrated throughout the day, and mixing cardiorespiratory exercises with strength training."
            })

    # Fallback tip if no conditions and no BMI
    if not tips:
        tips.append({
            "category": "🌱 General Wellness",
            "text": "Focus on building daily habits: stay hydrated, ensure you sleep 7-8 hours, and choose active transport (walking, biking) when possible."
        })

    return {
        "bmi": bmi,
        "category": bmi_cat,
        "color": bmi_color,
        "tips": tips
    }
