---
id: TC-FA-ASTL-UI-066-dialog-add-label
title: "Dialog Add Label"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["V-02", "T-01", "T-22", "D-17", "FLD-36", "§4.1f#b1", "§4.4#b8", "§6#r9", "§9.9#p3", "EB-FB-1@add-label", "EB-FB-2@add-label", "EB-FB-4", "EB-FRM-1@add-label", "EB-ERR-1@add-label"]
smoke: []
dependsOn: []
trace:
  "V-02": [4, 10, 13]
  "T-01": [22, 37]
  "T-22": 29
  "D-17": [2, 3]
  "FLD-36": [3, 4, 6]
  "§4.1f#b1": [2, 6, 9]
  "§4.4#b8": [17, 20]
  "§6#r9": [29, 42]
  "§9.9#p3": 7
  "EB-FB-1@add-label": [22, 29, 37]
  "EB-FB-2@add-label": 47
  "EB-FB-4": [25, 33, 35]
  "EB-FRM-1@add-label": [17, 18, 20, 23]
  "EB-ERR-1@add-label": [30, 31, 38, 42, 43]
anchor: [46]
coverage:
  web: automated
---

# Dialog Add Label

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Add Label
- Data:
  - DU-066-1: Label `Kritis`, ada di katalog label.
  - DU-066-2: Label `Audit Q4`, ada di katalog label.
  - DU-066-3: Label `Garansi`, ada di katalog label.
- Kondisi:
  - K1: katalog label berisi DU-066-1 sampai DU-066-3; simpan berhasil.
  - K2: katalog label berisi DU-066-1 sampai DU-066-3; simpan pertama gagal karena error server, simpan berikutnya berhasil.
  - K3: katalog label berisi DU-066-1 sampai DU-066-3; simpan gagal karena timeout atau jaringan terputus.
  - K4: katalog label berisi DU-066-1 sampai DU-066-3; simpan berhasil setelah respons tertunda.

## Test Steps

### Isi dialog dan tombol Apply menunggu pilihan
1. Tampilkan Dialog Add Label dengan kondisi K1
2. Verifikasi dialog berjudul `Add Label` tampil dengan kontrol pilihan label ber-placeholder `Select label`, tombol `[Cancel]`, dan tombol `[Apply]`
3. Verifikasi kontrol pilihan label ditandai wajib
4. Verifikasi `[Apply]` Disabled karena belum ada label dipilih
5. Klik kontrol pilihan label
6. Verifikasi opsi `Kritis`, `Audit Q4`, dan `Garansi` tampil sebagai seluruh katalog label, dan kontrol pilihan label tidak berisi pilihan sebelum dipilih
7. Verifikasi kontrol pilihan label tampil dan tidak ada field isian teks bebas di dalam dialog
8. Pilih `Kritis` dan `Audit Q4`
9. Verifikasi `Kritis` dan `Audit Q4` tampil sebagai pratinjau chip pilihan
10. Verifikasi `[Apply]` aktif
11. Hapus chip `Audit Q4` dengan (✕) pada chip itu
12. Hapus chip `Kritis` dengan (✕) pada chip itu
13. Verifikasi `[Apply]` Disabled kembali dan placeholder `Select label` tampil lagi

### Apply menyimpan satu kali dan toast sukses hilang sendiri
14. Tampilkan Dialog Add Label dengan kondisi K4
15. Pilih `Kritis` dan `Garansi`
16. Klik `[Apply]`
17. Verifikasi `[Apply]` tidak bisa diklik selama permintaan berjalan
18. Verifikasi kontrol pilihan label, tombol `[Cancel]`, dan tombol tutup `✕` Disabled selama permintaan berjalan
19. Klik `[Apply]` sekali lagi saat permintaan masih berjalan
20. Verifikasi permintaan simpan hanya terkirim satu kali
21. Respons simpan berhasil diterima
22. Verifikasi toast `Success, label has been added.` tampil
23. Verifikasi dialog `Add Label` tertutup
24. Waktu berlalu sampai 4 detik sejak toast tampil
25. Verifikasi toast `Success, label has been added.` hilang sendiri

### Kegagalan server mempertahankan dialog dan toast error bertahan
26. Tampilkan Dialog Add Label dengan kondisi K2
27. Pilih `Kritis`
28. Klik `[Apply]`
29. Verifikasi toast `Error, failed to add label.` tampil
30. Verifikasi dialog `Add Label` tetap terbuka dengan `Kritis` masih terpilih
31. Verifikasi toast `Error, failed to add label.` tidak memiliki tombol aksi seperti `[Try Again]`
32. Waktu berlalu sampai 10 detik sejak toast tampil
33. Verifikasi toast `Error, failed to add label.` masih tampil
34. Klik tombol tutup pada toast `Error, failed to add label.`
35. Verifikasi toast `Error, failed to add label.` tidak tampil lagi
36. Klik `[Apply]`
37. Verifikasi toast `Success, label has been added.` tampil
38. Verifikasi dialog `Add Label` tertutup dan simpan berhasil tepat satu kali

### Timeout mempertahankan dialog
39. Tampilkan Dialog Add Label dengan kondisi K3
40. Pilih `Kritis`
41. Klik `[Apply]`
42. Verifikasi toast `Connection problem. Please try again.` tampil
43. Verifikasi dialog `Add Label` tetap terbuka dengan `Kritis` masih terpilih dan `[Apply]` aktif kembali

### Cancel menutup dialog tanpa toast
44. Tampilkan Dialog Add Label dengan kondisi K1
45. Klik `[Cancel]`
46. Verifikasi dialog `Add Label` tertutup
47. Verifikasi tidak ada toast yang tampil dan tidak ada permintaan simpan yang terkirim
