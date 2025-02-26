import streamlit as st
import pandas as pd

def main():
    # Set page config to make it look cleaner
    st.set_page_config(
        page_title="Unit Converter",
        page_icon="🔄",
        layout="centered"
    )
    
    # Add title and description
    st.title("Unit Converter")
    st.markdown("Convert between different units of measurement")
    
    # Dictionary of conversion categories and their units
    conversion_types = {
        "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        "Mass/Weight": ["Kilogram", "Gram", "Milligram", "Metric Ton", "Pound", "Ounce"],
        "Volume": ["Liter", "Milliliter", "Cubic Meter", "Gallon", "Quart", "Pint", "Cup", "Fluid Ounce"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Area": ["Square Meter", "Square Kilometer", "Square Centimeter", "Hectare", "Square Mile", "Acre", "Square Foot", "Square Inch"],
        "Time": ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"],
        "Digital Storage": ["Bit", "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"],
        "Speed": ["Meter per second", "Kilometer per hour", "Mile per hour", "Knot", "Foot per second"]
    }
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        # Select conversion category
        category = st.selectbox("Category", list(conversion_types.keys()))
        
        # Input value
        input_value = st.number_input("Enter value", value=1.0, format="%.10f")
        
        # From unit
        from_unit = st.selectbox("From", conversion_types[category], key="from_unit")
    
    with col2:
        # Placeholder to align with category dropdown
        st.text("")
        st.text("")
        
        # Result display with background color similar to Google's result
        result_container = st.container()
        
        # To unit
        to_unit = st.selectbox("To", conversion_types[category], key="to_unit")
    
    # Calculate and display the result
    result = convert(input_value, from_unit, to_unit, category)
    
    with result_container:
        st.markdown(
            f"""
            <div style="background-color: #f1f3f4; padding: 20px; border-radius: 8px; text-align: center;">
                <h2>{result:.10g} {to_unit}</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Formula display
    st.markdown("---")
    formula = get_conversion_formula(from_unit, to_unit, category)
    st.markdown(f"**Conversion Formula:** {formula}")
    
    # Add example calculation
    if from_unit != to_unit:
        st.markdown(f"**Example:** 1 {from_unit} = {convert(1, from_unit, to_unit, category):.10g} {to_unit}")

def convert(value, from_unit, to_unit, category):
    """Convert value between units"""
    # If units are the same, return the value
    if from_unit == to_unit:
        return value
    
    # Convert to base unit first, then to target unit
    if category == "Length":
        # Convert to meters first
        meters = 0
        if from_unit == "Meter": meters = value
        elif from_unit == "Kilometer": meters = value * 1000
        elif from_unit == "Centimeter": meters = value * 0.01
        elif from_unit == "Millimeter": meters = value * 0.001
        elif from_unit == "Mile": meters = value * 1609.344
        elif from_unit == "Yard": meters = value * 0.9144
        elif from_unit == "Foot": meters = value * 0.3048
        elif from_unit == "Inch": meters = value * 0.0254
        
        # Then convert meters to target unit
        if to_unit == "Meter": return meters
        elif to_unit == "Kilometer": return meters / 1000
        elif to_unit == "Centimeter": return meters / 0.01
        elif to_unit == "Millimeter": return meters / 0.001
        elif to_unit == "Mile": return meters / 1609.344
        elif to_unit == "Yard": return meters / 0.9144
        elif to_unit == "Foot": return meters / 0.3048
        elif to_unit == "Inch": return meters / 0.0254
    
    elif category == "Mass/Weight":
        # Convert to grams first
        grams = 0
        if from_unit == "Kilogram": grams = value * 1000
        elif from_unit == "Gram": grams = value
        elif from_unit == "Milligram": grams = value * 0.001
        elif from_unit == "Metric Ton": grams = value * 1000000
        elif from_unit == "Pound": grams = value * 453.59237
        elif from_unit == "Ounce": grams = value * 28.349523125
        
        # Then convert grams to target unit
        if to_unit == "Kilogram": return grams / 1000
        elif to_unit == "Gram": return grams
        elif to_unit == "Milligram": return grams / 0.001
        elif to_unit == "Metric Ton": return grams / 1000000
        elif to_unit == "Pound": return grams / 453.59237
        elif to_unit == "Ounce": return grams / 28.349523125
    
    elif category == "Volume":
        # Convert to liters first
        liters = 0
        if from_unit == "Liter": liters = value
        elif from_unit == "Milliliter": liters = value * 0.001
        elif from_unit == "Cubic Meter": liters = value * 1000
        elif from_unit == "Gallon": liters = value * 3.78541
        elif from_unit == "Quart": liters = value * 0.946353
        elif from_unit == "Pint": liters = value * 0.473176
        elif from_unit == "Cup": liters = value * 0.236588
        elif from_unit == "Fluid Ounce": liters = value * 0.0295735
        
        # Then convert liters to target unit
        if to_unit == "Liter": return liters
        elif to_unit == "Milliliter": return liters / 0.001
        elif to_unit == "Cubic Meter": return liters / 1000
        elif to_unit == "Gallon": return liters / 3.78541
        elif to_unit == "Quart": return liters / 0.946353
        elif to_unit == "Pint": return liters / 0.473176
        elif to_unit == "Cup": return liters / 0.236588
        elif to_unit == "Fluid Ounce": return liters / 0.0295735
    
    elif category == "Temperature":
        # Temperature requires special conversion formulas
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    
    elif category == "Area":
        # Convert to square meters first
        sq_meters = 0
        if from_unit == "Square Meter": sq_meters = value
        elif from_unit == "Square Kilometer": sq_meters = value * 1000000
        elif from_unit == "Square Centimeter": sq_meters = value * 0.0001
        elif from_unit == "Hectare": sq_meters = value * 10000
        elif from_unit == "Square Mile": sq_meters = value * 2589988.11
        elif from_unit == "Acre": sq_meters = value * 4046.86
        elif from_unit == "Square Foot": sq_meters = value * 0.092903
        elif from_unit == "Square Inch": sq_meters = value * 0.00064516
        
        # Then convert square meters to target unit
        if to_unit == "Square Meter": return sq_meters
        elif to_unit == "Square Kilometer": return sq_meters / 1000000
        elif to_unit == "Square Centimeter": return sq_meters / 0.0001
        elif to_unit == "Hectare": return sq_meters / 10000
        elif to_unit == "Square Mile": return sq_meters / 2589988.11
        elif to_unit == "Acre": return sq_meters / 4046.86
        elif to_unit == "Square Foot": return sq_meters / 0.092903
        elif to_unit == "Square Inch": return sq_meters / 0.00064516
    
    elif category == "Time":
        # Convert to seconds first
        seconds = 0
        if from_unit == "Second": seconds = value
        elif from_unit == "Minute": seconds = value * 60
        elif from_unit == "Hour": seconds = value * 3600
        elif from_unit == "Day": seconds = value * 86400
        elif from_unit == "Week": seconds = value * 604800
        elif from_unit == "Month": seconds = value * 2592000  # Approximate: 30 days
        elif from_unit == "Year": seconds = value * 31536000  # Approximate: 365 days
        
        # Then convert seconds to target unit
        if to_unit == "Second": return seconds
        elif to_unit == "Minute": return seconds / 60
        elif to_unit == "Hour": return seconds / 3600
        elif to_unit == "Day": return seconds / 86400
        elif to_unit == "Week": return seconds / 604800
        elif to_unit == "Month": return seconds / 2592000
        elif to_unit == "Year": return seconds / 31536000
    
    elif category == "Digital Storage":
        # Convert to bits first
        bits = 0
        if from_unit == "Bit": bits = value
        elif from_unit == "Byte": bits = value * 8
        elif from_unit == "Kilobyte": bits = value * 8 * 1024
        elif from_unit == "Megabyte": bits = value * 8 * 1024**2
        elif from_unit == "Gigabyte": bits = value * 8 * 1024**3
        elif from_unit == "Terabyte": bits = value * 8 * 1024**4
        
        # Then convert bits to target unit
        if to_unit == "Bit": return bits
        elif to_unit == "Byte": return bits / 8
        elif to_unit == "Kilobyte": return bits / (8 * 1024)
        elif to_unit == "Megabyte": return bits / (8 * 1024**2)
        elif to_unit == "Gigabyte": return bits / (8 * 1024**3)
        elif to_unit == "Terabyte": return bits / (8 * 1024**4)
    
    elif category == "Speed":
        # Convert to meters per second first
        mps = 0
        if from_unit == "Meter per second": mps = value
        elif from_unit == "Kilometer per hour": mps = value * 0.277778
        elif from_unit == "Mile per hour": mps = value * 0.44704
        elif from_unit == "Knot": mps = value * 0.514444
        elif from_unit == "Foot per second": mps = value * 0.3048
        
        # Then convert meters per second to target unit
        if to_unit == "Meter per second": return mps
        elif to_unit == "Kilometer per hour": return mps / 0.277778
        elif to_unit == "Mile per hour": return mps / 0.44704
        elif to_unit == "Knot": return mps / 0.514444
        elif to_unit == "Foot per second": return mps / 0.3048
    
    return value  # Default return

def get_conversion_formula(from_unit, to_unit, category):
    """Return the conversion formula between units"""
    if from_unit == to_unit:
        return f"1 {from_unit} = 1 {to_unit}"
    
    formulas = {
        "Length": {
            ("Meter", "Kilometer"): "divide by 1000",
            ("Meter", "Centimeter"): "multiply by 100",
            ("Meter", "Millimeter"): "multiply by 1000",
            ("Meter", "Mile"): "divide by 1609.344",
            ("Meter", "Yard"): "multiply by 1.09361",
            ("Meter", "Foot"): "multiply by 3.28084",
            ("Meter", "Inch"): "multiply by 39.3701",
            
            ("Kilometer", "Meter"): "multiply by 1000",
            ("Kilometer", "Mile"): "multiply by 0.621371",
            
            ("Centimeter", "Meter"): "divide by 100",
            ("Centimeter", "Inch"): "multiply by 0.393701",
            
            ("Millimeter", "Meter"): "divide by 1000",
            ("Millimeter", "Inch"): "multiply by 0.0393701",
            
            ("Mile", "Meter"): "multiply by 1609.344",
            ("Mile", "Kilometer"): "multiply by 1.60934",
            
            ("Yard", "Meter"): "multiply by 0.9144",
            ("Yard", "Foot"): "multiply by 3",
            
            ("Foot", "Meter"): "multiply by 0.3048",
            ("Foot", "Inch"): "multiply by 12",
            
            ("Inch", "Centimeter"): "multiply by 2.54",
            ("Inch", "Foot"): "divide by 12"
        },
        "Temperature": {
            ("Celsius", "Fahrenheit"): "(°C × 9/5) + 32 = °F",
            ("Celsius", "Kelvin"): "°C + 273.15 = K",
            ("Fahrenheit", "Celsius"): "(°F - 32) × 5/9 = °C",
            ("Fahrenheit", "Kelvin"): "(°F - 32) × 5/9 + 273.15 = K",
            ("Kelvin", "Celsius"): "K - 273.15 = °C",
            ("Kelvin", "Fahrenheit"): "(K - 273.15) × 9/5 + 32 = °F"
        }
    }
    
    # Check if there's a specific formula for this conversion
    if category in formulas and (from_unit, to_unit) in formulas[category]:
        return formulas[category][(from_unit, to_unit)]
    
    # If we don't have a specific formula, return a generic one
    return f"Convert {from_unit} to {to_unit}"

if __name__ == "__main__":
    main()