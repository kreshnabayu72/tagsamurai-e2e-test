---
id: TC-FA-ASTL-UI-067-dialog-remove-label
title: "Dialog Remove Label"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-16", "S-04", "T-02", "T-23", "D-18", "FLD-37", "§4.1f#b2", "§6#r9", "EB-FB-1@remove-label", "EB-FB-2@remove-label", "EB-FRM-1@remove-label", "EB-ERR-1@remove-label"]
smoke: []
dependsOn: []
trace:
  "FI-16": [11, 13]
  "S-04": 13
  "T-02": [22, 31]
  "T-23": 27
  "D-18": [2, 3, 6]
  "FLD-37": [3, 4, 6, 9]
  "§4.1f#b2": [6, 7, 13]
  "§6#r9": [27, 36]
  "EB-FB-1@remove-label": [22, 27, 31]
  "EB-FB-2@remove-label": 41
  "EB-FRM-1@remove-label": [17, 18, 20, 23]
  "EB-ERR-1@remove-label": [28, 29, 32, 36, 37]
anchor: [40]
coverage:
  web: automated
---

# Dialog Remove Label

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Remove Label
- Data:
  - DU-067-1: Label manual `Kritis`, terpasang pada aset terpilih.
  - DU-067-2: Label manual `Audit Q4`, terpasang pada aset terpilih.
  - DU-067-3: Label bawaan template Asset Name `Laptop Utama`, terpasang pada aset terpilih.
- Kondisi:
  - K1: seleksi memuat DU-067-1 sampai DU-067-3; simpan berhasil.
  - K2: seleksi tidak memiliki label manual, hanya DU-067-3.
  - K3: seleksi memuat DU-067-1 sampai DU-067-3; simpan pertama gagal karena error server, simpan berikutnya berhasil.
  - K4: seleksi memuat DU-067-1 sampai DU-067-3; simpan berhasil setelah respons tertunda.
  - K5: seleksi memuat DU-067-1 sampai DU-067-3; simpan gagal karena timeout atau jaringan terputus.

## Test Steps

### Isi dialog menawarkan label manual saja
1. Tampilkan Dialog Remove Label dengan kondisi K1
2. Verifikasi dialog berjudul `Remove Label` tampil dengan kontrol pilihan label ber-placeholder `Select label`, keterangan `Only manual labels can be removed here.`, tombol `[Cancel]`, dan tombol `[Apply]`
3. Verifikasi kontrol pilihan label ditandai wajib
4. Verifikasi `[Apply]` Disabled karena belum ada label dipilih
5. Klik kontrol pilihan label
6. Verifikasi opsi `Kritis` dan `Audit Q4` tampil sebagai label manual seleksi
7. Verifikasi opsi `Laptop Utama` tidak tampil
8. Pilih `Kritis`
9. Verifikasi `[Apply]` aktif

### Tanpa label manual Apply Disabled beralasan
10. Tampilkan Dialog Remove Label dengan kondisi K2
11. Verifikasi `[Apply]` Disabled
12. Arahkan kursor ke `[Apply]`
13. Verifikasi alasan `The selected assets have no manual labels to remove.` tersampaikan pada tombol `[Apply]` yang Disabled

### Apply menyimpan satu kali dan toast sukses
14. Tampilkan Dialog Remove Label dengan kondisi K4
15. Pilih `Kritis`
16. Klik `[Apply]`
17. Verifikasi `[Apply]` tidak bisa diklik selama permintaan berjalan
18. Verifikasi kontrol pilihan label, tombol `[Cancel]`, dan tombol tutup `✕` Disabled selama permintaan berjalan
19. Klik `[Apply]` sekali lagi saat permintaan masih berjalan
20. Verifikasi permintaan simpan hanya terkirim satu kali
21. Respons simpan berhasil diterima
22. Verifikasi toast `Success, label has been removed.` tampil
23. Verifikasi dialog `Remove Label` tertutup

### Kegagalan server mempertahankan dialog
24. Tampilkan Dialog Remove Label dengan kondisi K3
25. Pilih `Kritis`
26. Klik `[Apply]`
27. Verifikasi toast `Error, failed to remove label.` tampil
28. Verifikasi dialog `Remove Label` tetap terbuka dengan `Kritis` masih terpilih dan `[Apply]` aktif kembali
29. Verifikasi toast `Error, failed to remove label.` tidak memiliki tombol aksi seperti `[Try Again]`
30. Klik `[Apply]`
31. Verifikasi toast `Success, label has been removed.` tampil
32. Verifikasi dialog `Remove Label` tertutup dan simpan berhasil tepat satu kali

### Timeout mempertahankan dialog
33. Tampilkan Dialog Remove Label dengan kondisi K5
34. Pilih `Kritis`
35. Klik `[Apply]`
36. Verifikasi toast `Connection problem. Please try again.` tampil
37. Verifikasi dialog `Remove Label` tetap terbuka dengan `Kritis` masih terpilih dan `[Apply]` aktif kembali

### Cancel menutup dialog tanpa toast
38. Tampilkan Dialog Remove Label dengan kondisi K1
39. Klik `[Cancel]`
40. Verifikasi dialog `Remove Label` tertutup
41. Verifikasi tidak ada toast yang tampil dan tidak ada permintaan simpan yang terkirim
