from antrian_pesanan import AntrianPesanan

antrian = AntrianPesanan()

antrian.display_antrian()

antrian.enqueue("Nasi Goreng")
antrian.enqueue("Mie Ayam")
antrian.enqueue("Sate")

antrian.display_antrian()

antrian.dequeue()

antrian.display_antrian()

antrian.dequeue()

antrian.display_antrian()