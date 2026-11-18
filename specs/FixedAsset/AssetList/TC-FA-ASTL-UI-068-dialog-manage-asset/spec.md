---
id: TC-FA-ASTL-UI-068-dialog-manage-asset
title: "Dialog Manage Asset"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-15h", "FI-12", "FI-13", "T-09", "T-10", "T-24", "D-03", "FLD-39", "§6#r9", "EB-FB-1@manage-asset", "EB-FB-2@manage-asset", "EB-FRM-1@manage-asset", "EB-ERR-1@manage-asset"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-15h": [6, 17, 18, 51, 52]
  "FI-12": [17, 18, 20]
  "FI-13": [8, 21]
  "T-09": [14, 29, 37]
  "T-10": 45
  "T-24": 33
  "D-03": [2, 3, 4, 12, 16, 20]
  "FLD-39": [4, 5, 8, 10, 18]
  "§6#r9": [33, 41]
  "EB-FB-1@manage-asset": [14, 29, 33]
  "EB-FB-2@manage-asset": 49
  "EB-FRM-1@manage-asset": [24, 25, 27, 30]
  "EB-ERR-1@manage-asset": [34, 35, 38, 41, 42]
anchor: [48]
coverage:
  web: automated
---

# Dialog Manage Asset

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Manage Asset
- Data:
  - DU-068-1: Aset `Kamera Mirrorless - 1`, Asset ID `AST-0070`, Unmanaged, di group `Cabang Bandung`.
  - DU-068-2: Aset `Kamera Mirrorless - 2`, Asset ID `AST-0073`, Unmanaged, di group `Cabang Bandung`.
  - DU-068-3: Lisensi group `Cabang Bandung` dengan Available license `5`.
  - DU-068-4: Lisensi group `Cabang Bandung` dengan Available license `1`.
  - DU-068-5: Lisensi group `Cabang Bandung` dengan Available license `2`.
  - Teks yang diharapkan untuk dua aset: `2 assets will be managed in Cabang Bandung.`, dari jumlah aset 2 dan group `Cabang Bandung`.
  - Teks yang diharapkan untuk satu aset: `1 asset will be managed in Cabang Bandung.`, dari jumlah aset 1 dan group `Cabang Bandung`.
  - Teks yang diharapkan untuk Available license: `Available license in Cabang Bandung: 5` dari DU-068-3 dan `Available license in Cabang Bandung: 1` dari DU-068-4.
- Kondisi:
  - K1: seleksi berisi DU-068-1 dan DU-068-2; Available license mengikuti DU-068-3.
  - K2: seleksi berisi DU-068-1 dan DU-068-2; Available license mengikuti DU-068-4.
  - K3: seleksi berisi DU-068-1; Available license mengikuti DU-068-3; simpan berhasil.
  - K4: seleksi berisi DU-068-1 dan DU-068-2; Available license mengikuti DU-068-3; simpan berhasil setelah respons tertunda.
  - K5: seleksi berisi DU-068-1 dan DU-068-2; Available license mengikuti DU-068-3; simpan pertama gagal karena error server, simpan berikutnya berhasil.
  - K6: seleksi berisi DU-068-1 dan DU-068-2; Available license mengikuti DU-068-3; simpan gagal karena timeout atau jaringan terputus.
  - K7: seleksi berisi DU-068-1 dan DU-068-2; Available license saat dialog dibuka mengikuti DU-068-5, lalu kuota group terpakai pihak lain sehingga tinggal 1 slot; simpan ditolak karena kuota group terlampaui.
  - K8: seleksi berisi DU-068-1 dan DU-068-2; Available license mengikuti DU-068-5 (sama dengan jumlah aset).

## Test Steps

### Tampilan awal saat Available license mencukupi
1. Tampilkan Dialog Manage Asset dengan kondisi K1
2. Verifikasi dialog berjudul `Manage Asset` tampil dengan teks `2 assets will be managed in Cabang Bandung.`
3. Verifikasi teks `Available license in Cabang Bandung: 5` tampil
4. Verifikasi pilihan sumber `Available quota` dan `Switch with a managed asset` tampil, bersama tombol `[Cancel]` dan `[Manage]`
5. Verifikasi sumber `Available quota` terpilih
6. Verifikasi sumber `Available quota` dapat dipilih (tidak Disabled)
7. Pilih sumber `Switch with a managed asset`
8. Verifikasi tombol berlabel `[Next]`
9. Pilih sumber `Available quota`
10. Verifikasi tombol berlabel `[Manage]`

### Satu aset berhasil di-Manage
11. Tampilkan Dialog Manage Asset dengan kondisi K3
12. Verifikasi teks `1 asset will be managed in Cabang Bandung.` tampil
13. Klik `[Manage]`
14. Verifikasi toast `Success, asset has been sent to be managed.` tampil

### Available license kurang dari jumlah aset
15. Tampilkan Dialog Manage Asset dengan kondisi K2
16. Verifikasi teks `Available license in Cabang Bandung: 1` tampil
17. Verifikasi sumber `Available quota` Disabled
18. Verifikasi sumber `Switch with a managed asset` terpilih
19. Arahkan kursor ke sumber `Available quota`
20. Verifikasi alasan `Not enough available license in this group.` tersampaikan pada sumber `Available quota` yang Disabled
21. Verifikasi tombol berlabel `[Next]`

### Manage menyimpan satu kali
22. Tampilkan Dialog Manage Asset dengan kondisi K4
23. Klik `[Manage]`
24. Verifikasi `[Manage]` tidak bisa diklik selama permintaan berjalan
25. Verifikasi pilihan sumber, tombol `[Cancel]`, dan tombol tutup `✕` Disabled selama permintaan berjalan
26. Klik `[Manage]` sekali lagi saat permintaan masih berjalan
27. Verifikasi permintaan simpan hanya terkirim satu kali
28. Respons simpan berhasil diterima
29. Verifikasi toast `Success, assets have been sent to be managed.` tampil
30. Verifikasi dialog `Manage Asset` tertutup

### Kegagalan server mempertahankan dialog
31. Tampilkan Dialog Manage Asset dengan kondisi K5
32. Klik `[Manage]`
33. Verifikasi toast `Error, failed to manage asset.` tampil
34. Verifikasi dialog `Manage Asset` tetap terbuka dengan sumber `Available quota` masih terpilih dan `[Manage]` aktif kembali
35. Verifikasi toast `Error, failed to manage asset.` tidak memiliki tombol aksi seperti `[Try Again]`
36. Klik `[Manage]`
37. Verifikasi toast `Success, assets have been sent to be managed.` tampil
38. Verifikasi dialog `Manage Asset` tertutup dan simpan berhasil tepat satu kali

### Timeout mempertahankan dialog
39. Tampilkan Dialog Manage Asset dengan kondisi K6
40. Klik `[Manage]`
41. Verifikasi toast `Connection problem. Please try again.` tampil
42. Verifikasi dialog `Manage Asset` tetap terbuka dengan sumber `Available quota` masih terpilih dan `[Manage]` aktif kembali

### Kuota ditolak server
43. Tampilkan Dialog Manage Asset dengan kondisi K7
44. Klik `[Manage]`
45. Verifikasi toast `Group quota exceeded. Available slots: 1. Please contact administrator to increase quota.` tampil

### Cancel menutup dialog tanpa toast
46. Tampilkan Dialog Manage Asset dengan kondisi K1
47. Klik `[Cancel]`
48. Verifikasi dialog `Manage Asset` tertutup
49. Verifikasi tidak ada toast yang tampil dan tidak ada permintaan simpan yang terkirim

### Available license tepat sama dengan jumlah aset
50. Tampilkan Dialog Manage Asset dengan kondisi K8
51. Verifikasi sumber `Available quota` dapat dipilih (tidak Disabled)
52. Verifikasi sumber `Available quota` terpilih
