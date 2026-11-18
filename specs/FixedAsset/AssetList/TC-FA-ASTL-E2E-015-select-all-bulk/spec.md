---
id: TC-FA-ASTL-E2E-015-select-all-bulk
title: "Seleksi baris dan Select All"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-20g", "ASTL-LOGIC-20h", "EC-35", "§4.4#b4", "EB-BLK-2@tabel-all-assets", "EB-EDG-2"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-20g": [8, 17]
  "ASTL-LOGIC-20h": 21
  "EC-35": 21
  "§4.4#b4": 11
  "EB-BLK-2@tabel-all-assets": [5, 6, 8, 9, 14, 15]
  "EB-EDG-2": [3, 26, 27]
anchor: [2]
coverage:
  web: automated
---
# Seleksi baris dan Select All

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-015-1: aset Active ber-Custody `Available`, bukan Unmanaged, Asset Name `Kursi Lipat 1 {runId}`, tampil `Kursi Lipat 1 {runId} - 1`, Brand `Chitose`, Model/Type `Lipat Standar`, Category `Furniture`, Group `Kantor Pusat {runId}`, Status `Available`, ada di entitas aktor.
  - DU-015-2: 10 aset Active dengan nilai yang sama seperti DU-015-1, Asset Name `Kursi Lipat {n} {runId}` dengan n dari 2 sampai 11, sehingga bersama DU-015-1 dan DU-015-3 Search dengan kata kunci runId menghasilkan 12 baris.
  - DU-015-3: 1 aset Asset Name `Rak Arsip {runId}`, tampil `Rak Arsip {runId} - 1`, Brand `Chitose`, Model/Type `Rak Besi`, Category `Furniture`, Group `Kantor Pusat {runId}`, Status `Available`.
  - DU-015-4: Group `Kantor Pusat {runId}`, ada di entitas aktor.
  - DU-015-5: aset ke-13 Asset Name `Kursi Lipat 12 {runId}`, tampil `Kursi Lipat 12 {runId} - 1`, didaftarkan aktor lain selama spec berjalan.
- Kondisi:
  - Ukuran halaman tabel bernilai 10 (bawaan).

## Test Steps

### Bar Bulk tidak tampil tanpa seleksi
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Kursi Lipat 1 {runId} - 1` tampil pada tabel
3. Verifikasi Bar Bulk dan tombol `Select All (12 records)` tidak tampil karena belum ada baris terpilih

### Select All memilih seluruh hasil filter lintas halaman
4. Klik checkbox di header kolom Checkbox
5. Verifikasi Bar Bulk menampilkan `10 assets selected`
6. Verifikasi tombol `Select All (12 records)` tampil
7. Klik `Select All (12 records)`
8. Verifikasi Bar Bulk menampilkan `12 assets selected`
9. Verifikasi tombol berubah menjadi `Unselect All`
10. Pindah ke halaman `2`
11. Verifikasi seluruh baris data uji pada halaman `2` tercentang

### Uncheck satu baris mengembalikan tombol Select All
12. Pindah ke halaman `1`
13. Batalkan centang baris `Kursi Lipat 1 {runId} - 1`
14. Verifikasi tombol kembali menjadi `Select All (12 records)` dengan total tetap 12
15. Verifikasi Bar Bulk menampilkan `11 assets selected`

### Select All memakai snapshot saat diklik
16. Klik `Select All (12 records)`
17. Verifikasi Bar Bulk menampilkan `12 assets selected`
18. Aktor lain mendaftarkan aset baru `Kursi Lipat 12 {runId}` yang cocok dengan Search yang aktif
19. Klik `Bulk Action`
20. Pilih `Print Label`
21. Verifikasi dialog `Print Label` memuat `Selected asset: 12 assets`, tanpa aset baru
22. Klik `[Cancel]`
23. Klik `×` pada Bar Bulk

### Satu aset memakai bentuk tunggal
24. Centang baris `Kursi Lipat 1 {runId} - 1` dan `Kursi Lipat 2 {runId} - 1`
25. Ganti isi kotak search dengan `Rak Arsip {runId}`, tekan Enter
26. Verifikasi Bar Bulk tetap menampilkan `2 assets selected` karena seleksi tidak direset oleh Search
27. Verifikasi tombol `Select All (1 record)` tampil karena hasil Search 1 baris dan baris itu belum terpilih
