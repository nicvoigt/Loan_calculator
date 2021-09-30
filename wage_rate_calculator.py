import pandas as pd

tax_rates = pd.read_csv("/content/drive/MyDrive/lohnsteuer.txt", sep = "\t")


tax_rates_preprocessed = pd.DataFrame( columns = ["Gehalt", "I", "II", "III", "V", "VI"])
for i in range(len(df.index )-1):
  try:
    to_append = pd.DataFrame([df.iloc[i][0].split()],index = [0], columns = tax_rates_preprocessed.columns)
    # print(i)
    tax_rates_preprocessed = tax_rates_preprocessed.append(to_append, ignore_index=True)
  except:
    pass
    
for column in range(len(tax_rates_preprocessed.columns)):
  for row in tax_rates_preprocessed.index:
    tax_rates_preprocessed.iloc[row,column] = float(tax_rates_preprocessed.iloc[row, column].replace(".","").replace(",","."))
    
sorted_list = (tax_rates_preprocessed["Gehalt"].sort_values(ascending=False)).sort_values()


def naechsten_wert_suchen(liste,wert):
  naehester_wert = 9e99
  liste = liste.tolist()
  for i in range(len(liste)):
    if abs(liste[i]-wert)< abs(wert - naehester_wert):
      naehester_wert = liste[i]
      speicher_index =i
  return speicher_index, naehester_wert
                           
Bruttogehalt = 2000
Stundenanzahl = 160
Zielstundenlohn = 17
for i in range(100):

  steuerindex, Bruttogehalt = naechsten_wert_suchen(sorted_list,Bruttogehalt)

  netto = Bruttogehalt * (1-(0.075+ 0.012+ 0.093 + 0.012 + 0.0165)) - new_df.iloc[steuerindex,1]
  stundenlohn = netto / Stundenanzahl
  if stundenlohn < Zielstundenlohn:
    Bruttogehalt+=100
  elif stundenlohn >= Zielstundenlohn:
    break
    
