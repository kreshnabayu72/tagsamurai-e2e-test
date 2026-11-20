---
id: TC-FA-BORROW-E2E-100-foto-dihapus-di-file-manager-rujukan-borrow-dikosongkan
title: "Foto Handover dan Return yang dihapus di File Manager tampil kosong di Borrow tanpa mengubah status baris"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceRules: ["BORROW-LOGIC-23j", "EC-BRW-186", "BORROW-LOGIC-23i", "BORROW-LOGIC-23a", "BORROW-LOGIC-23k"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-23j": [6, 10, 34, 35, 36, 39, 46]
  "EC-BRW-186": [6, 34, 35, 36, 39, 46, 47]
  "BORROW-LOGIC-23i": 7
  "BORROW-LOGIC-23a": 16
  "BORROW-LOGIC-23k": [45, 47]
anchor: []
coverage:
  web: automated
---

# Foto Handover dan Return yang dihapus di File Manager tampil kosong di Borrow tanpa mengubah status baris

## Prerequisites
- Mode: FE+BE (backend nyata; Delete File Manager mengosongkan rujukan foto pada record sumber secara atomik).
- Aktor: `Wulan Anggraini {runId}`, Total Control dengan akses Delete pada File Manager FAMS dan akses Borrow.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-100-1: BRW `Returned` Group `Head Office`, Borrower `Hendra Kusuma {runId}-100`, berisi satu baris aset DU-100-2 berstatus `Returned`.
  - DU-100-2: aset `Kamera Canon EOS {runId}-100`, TAG `NFC`, Group `Head Office`, dengan Handover Photo `handover-kamera-{runId}-100.jpg` dan Return Photo `return-kamera-{runId}-100.jpg` tersimpan di File Manager FAMS.
  - DU-100-3: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}-100`, berisi satu baris aset DU-100-4 berstatus `Borrowed`.
  - DU-100-4: aset `Speaker JBL {runId}-100`, TAG `RFID`, Group `Head Office`, dengan Handover Photo `handover-speaker-{runId}-100.jpg` tersimpan di File Manager FAMS.
  - Asset ID dan Transaction ID dibentuk sistem dan menjadi milik entri masing-masing.

## Test Steps
### Foto tersimpan tampil di Borrow dan tidak dapat diubah dari baris tersimpan
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Klik tab `History`
4. Ketik Search `Hendra Kusuma {runId}-100`, tekan Enter
5. Buka Borrow Detail BRW milik DU-100-1 dari tabel History
6. Verifikasi baris aset DU-100-2 menampilkan thumbnail Handover Photo dan thumbnail Return Photo
7. Verifikasi thumbnail Handover Photo dan Return Photo baris DU-100-2 tampil tanpa ikon Edit dan Delete karena foto sekali-kirim
8. Klik menu ⋯ pada baris aset DU-100-2
9. Klik `Borrow Log`
10. Verifikasi node `Returned` Borrow Log memuat foto Handover dan foto Return berdampingan
11. Tutup dialog Borrow Log

### Admin men-Delete foto Handover dan foto Return di File Manager
12. Klik `Settings` pada sidebar
13. Klik `File Manager`
14. Klik tab `Files`
15. Ketik Search `handover-kamera-{runId}-100.jpg`, tekan Enter
16. Verifikasi baris file `handover-kamera-{runId}-100.jpg` menampilkan Source `Handover Photo`
17. Klik menu ⋯ pada baris file `handover-kamera-{runId}-100.jpg`
18. Klik `Delete`
19. Verifikasi dialog `Delete File` tampil
20. Klik `[Delete]`
21. Verifikasi toast `Success, handover-kamera-{runId}-100.jpg has been deleted.` tampil
22. Klik `(←)` pada kotak Search
23. Ketik Search `handover-speaker-{runId}-100.jpg`, tekan Enter
24. Klik menu ⋯ pada baris file `handover-speaker-{runId}-100.jpg`
25. Klik `Delete`
26. Verifikasi dialog `Delete File` tampil
27. Klik `[Delete]`
28. Verifikasi toast `Success, handover-speaker-{runId}-100.jpg has been deleted.` tampil

### Rujukan foto dikosongkan pada baris Returned dan status baris tidak berubah
29. Klik `Transactions` pada sidebar
30. Klik `Borrow`
31. Klik tab `History`
32. Ketik Search `Hendra Kusuma {runId}-100`, tekan Enter
33. Buka Borrow Detail BRW milik DU-100-1 dari tabel History
34. Verifikasi kolom Handover Photo baris DU-100-2 menampilkan `—`
35. Verifikasi kolom Return Photo baris DU-100-2 tetap menampilkan thumbnail foto Return
36. Verifikasi baris DU-100-2 tetap berstatus `Returned` dengan penanda dan hasil baris yang sama
37. Klik menu ⋯ pada baris aset DU-100-2
38. Klik `Borrow Log`
39. Verifikasi node `Returned` Borrow Log menampilkan `—` untuk Handover Photo dan tetap menampilkan foto Return
40. Tutup dialog Borrow Log

### Baris Borrowed dengan foto Handover dihapus tetap valid dan tidak memicu validasi
41. Klik `Transactions` pada sidebar
42. Klik `Borrow`
43. Ketik Search `Hendra Kusuma {runId}-100`, tekan Enter
44. Buka Borrow Detail BRW milik DU-100-3 dari tabel Transactions
45. Verifikasi halaman Borrow Detail terbuka tanpa pesan validasi atau error
46. Verifikasi kolom Handover Photo baris DU-100-4 menampilkan `—`
47. Verifikasi baris DU-100-4 tetap berstatus `Borrowed`

## Notes
- Mode: FE+BE. Sumber: PRD `fixed-asset/borrow/PRD/borrow.md` (`BORROW-LOGIC-23`, `V-BRW-47`, `T-BRW-33`, `EC-BRW-180` sampai `EC-BRW-186`) dan `fixed-asset/file-manager/PRD/file-manager.md`. Belum ada TestCase untuk aturan ini; spec dikutip langsung dari ID aturan PRD.
- Spec memakai dua aset: baris `Returned` (foto Handover dihapus, foto Return tetap) untuk menguji pasangan foto dan node `Returned` Borrow Log, dan baris `Borrowed` (foto Handover dihapus) untuk menguji bahwa kewajiban foto tidak divalidasi saat membaca record (`BORROW-LOGIC-23k`).
- Teks dialog `Delete File` dan toast sukses mengikuti `file-manager.md` (`D-01`, `T-01`); pratinjau foto pada baris yang fotonya dihapus tidak diasersi karena PRD hanya menetapkan nilai kosong `—` pada kolom, tampilan berdampingan, dan node Log.
- Di atas smell 35 langkah: sebelum dan sesudah Delete harus diasersi pada record yang sama, dan dua Delete di File Manager berbagi satu kunjungan; memecahnya menggandakan seeding dua BRW. Alasan P-1 (state berat).
- Ikon Edit dan Delete foto pada baris tersimpan diasersi sebagai tidak tampil dengan anchor positif thumbnail foto pada langkah yang sama (`BORROW-LOGIC-23i`).
