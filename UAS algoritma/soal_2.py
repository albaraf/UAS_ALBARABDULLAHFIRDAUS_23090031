import pandas as pd

data = [
    ["nama", "Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    ["algoritma dan struktur data 2", 90, 50, 65],
    ["matematika numerik", 80, 60, 70]
]

df = pd.DataFrame(data).T

df.columns = df.iloc[0]
df = df.iloc[1:]

print("DataFrame:")
print(df)

rata_rata_mata_kuliah = df.iloc[:, 1:].mean()
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_mata_kuliah)

rata_rata_mahasiswa = df.iloc[1:, 1:].mean(axis=1)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(rata_rata_mahasiswa)