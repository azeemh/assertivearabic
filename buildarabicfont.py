import sys
import os
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables.C_P_A_L_ import table_C_P_A_L_, Color
from fontTools.ttLib.tables.C_O_L_R_ import LayerRecord, table_C_O_L_R_

def compile_assertive_font(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"[!] Error: Target file '{input_path}' not found.")
        sys.exit(1)
        
    print(f"[*] Parsing font structures inside: {input_path}")
    font = TTFont(input_path)
    
    # Initialize CPAL table
    cpal = table_C_P_A_L_()
    cpal.version = 0
    
    # FIX: Define colors using fontTools Color objects, NOT raw tuples
    solid_black = Color(blue=0, green=0, red=0, alpha=255)
    faded_black = Color(blue=0, green=0, red=0, alpha=35)
    
    cpal.palettes = [[solid_black, faded_black]]
    cpal.numPaletteEntries = 2
    font['CPAL'] = cpal

    # Isolate Unicode points for short vowel diacritics
    tashkeel_unicodes = set(range(0x064B, 0x0653))
    cmap = font.getBestCmap()
    glyf_table = font['glyf']
    
    vowel_glyphs = {name for code, name in cmap.items() if code in tashkeel_unicodes}

    # Construct the OpenType Layer Mapping Table (COLR)
    colr = table_C_O_L_R_()
    colr.version = 0
    colr.ColorLayers = {}

    print("[*] Splitting consonants and diacritics into distinct visual layers...")
    for glyph_name in glyf_table.keys():
        layer = LayerRecord()
        layer.name = glyph_name
        # Map diacritics to entry 1 (faded) and consonants to entry 0 (solid)
        layer.colorID = 1 if glyph_name in vowel_glyphs else 0
        colr.ColorLayers[glyph_name] = [layer]

    font['COLR'] = colr

    # Save compiled binary
    font.save(output_path)
    print(f"[+] Success! Native Assertive Arabic Font compiled at: {output_path}")

# Execute using CLI arguments
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 buildarabicfont.py <input_font.ttf> <output_font.ttf>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    compile_assertive_font(input_file, output_file)
