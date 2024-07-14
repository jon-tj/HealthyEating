# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:49:24 2024
@author: Jon:)
@about: 
"""

import pandas as pd

def in_standard_units(amount,unit):
    """ Returns amount in kJ, mg or L. """
    if unit=="kg": return amount*1e+6 # mg
    if unit=="g": return amount*1e+3 # mg
    if unit=="mg": return amount # mg
    if unit=="µg": return amount*1e-3 # mg
    if unit=="mcg": return amount*1e-3 # mg
    if unit=="L": return amount # L
    if unit=="dL": return amount*1e-1 # L
    if unit=="cL": return amount*1e-2 # L
    if unit=="kcal": return amount*4.184 # kj
    if unit=="kJ": return amount # kJ
    if unit=="IU": return None # SKIP!!
    print("Unrecognized unit:",unit)
    return amount


class db_connection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.compiled = pd.read_csv(db_path+"compiled.csv")
        # Remove 'Unnamed' columns
        self.compiled = self.compiled.loc[:, ~self.compiled.columns.str.contains('^Unnamed')]

        self.food = pd.read_csv(db_path+"food.csv")
        self.foodcat = pd.read_csv(db_path+"foodcats.csv")
        self.nutr = pd.read_csv(db_path+"nutr.csv")
        self.rel = pd.read_csv(db_path+"food_nutr_rel.csv")
    
    def query(self, name, cat=None, verbose=False, must_start_with=True):
        original_query = name
        name = name.lower()
        ignore=[]
        if "/" in name:
            # Things we do NOT want to have in name
            name, ignore = name.split("/")
            ignore = [i.strip() for i in ignore.split(",")]
        name = [n.strip() for n in name.split(" ")]
            
        def is_ignored(name_i):
            if must_start_with and not name_i.startswith(name[0]):
                return True
            ignored=False
            for n in name:
                if n not in name_i:
                    ignored=True
                    break
            if ignored:
                return True
            ignored=False
            for ign in ignore:
                if ign in name_i:
                    ignored=True
                    break
            return ignored
        
        for i in range(len(self.compiled)):
            name_i = self.compiled.loc[i, "Name"]
            cat_i = self.compiled.loc[i, "Category"]
            #if not name_i.lower().startswith(name):
            #    continue
            if is_ignored(name_i.lower()): continue
            if cat!=None and cat not in cat_i.lower():
                continue
            if verbose:
                print(f"Matching '{name}' with '{name_i}'({cat_i})")
            return self.compiled.loc[i]
        
        for i in range(len(self.food)):
            name_i = self.food.loc[i, "Long_Desc"]
            cat_i = self.get_cat(self.food.loc[i, "FdGrp_Cd"])
            #if not name_i.lower().startswith(name):
            #    continue
            if is_ignored(name_i.lower()): continue
            if cat!=None and cat not in cat_i.lower():
                continue 
            food_id = self.food.loc[i, "NDB_No"]
            if verbose:
                print(f"Matching '{name}' with '{name_i}'({cat_i})")
            return self.db_lookup(
                food_id,
                cat_i,
                name_i)
        if must_start_with:
            return self.query(" ".join(name),cat,verbose,False)
        print(f"Warning! Could not find '{original_query}'")
        return None
            
    def db_lookup(self, food_id, food_cat, food_name, update_compiled=True):
        # Should be optimized to use binary search and
        # stop reading when nid changes. Can only be done
        # on sorted database. :)
        n={}
        n["Category"] = food_cat
        n["Name"] = food_name
        
        for i in range(len(self.rel)):
            if self.rel.loc[i, "NDB_No"] != food_id:
                continue
            nid = self.rel.loc[i, "Nutr_No"]
            nutr_name, unit = self.get_nid(nid)
            amount = self.rel.loc[i, "Nutr_Val"]
            amount = in_standard_units(amount, unit)
            if amount != None: # Skipping IU
                n[nutr_name] = amount
        
        df = {name:n[name] if name in n else 0 for name in self.compiled.columns}
        df = pd.DataFrame([df])
        if update_compiled:
            # For retracability, we dont want to remove the compiled
            # nutrients from the relation, just write to compiled.
            self.compiled = pd.concat([self.compiled, df], ignore_index=True)
            
        return df
    
    def get_cat(self, food_cat):
        for i in range(len(self.foodcat)):
            if self.foodcat.loc[i, "FdGrp_Cd"] == food_cat:
                return self.foodcat.loc[i, "FdGrp_desc"]
        return None
    
    def get_nid(self, nutr_id):
        for i in range(len(self.nutr)):
            if self.nutr.loc[i, "Nutr_no"] == nutr_id:
                return self.nutr.loc[i, "NutrDesc"], self.nutr.loc[i, "Units"]
        return None
            
        
    def save_compiled(self):
        self.compiled.to_csv(self.db_path+"compiled.csv")

if __name__=="__main__":
    db = db_connection()
    print(db.query("Cheese"))
    print(db.query("Mayo"))
    db.save_compiled()