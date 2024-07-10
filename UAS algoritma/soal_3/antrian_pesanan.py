class AntrianPesanan:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f" Pesanan {pesanan} telah ditambahkan ke antrian.")

    def dequeue(self):
        if len(self.antrian) == 0:
            print("Antrian kosong. Tidak ada pesanan untuk dihapus.")
        else:
            pesanan = self.antrian.pop(0)
            print(f" Pesanan {pesanan} telah dihapus dari antrian.")

    def display_antrian(self):
        print("Antrian Pesanan:")
        for i, pesanan in enumerate(self.antrian):
            print(f"{i+1}. {pesanan}")