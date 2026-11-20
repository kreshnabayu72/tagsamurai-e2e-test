---
id: TC-FA-BORROW-E2E-099-return-storage-penuh-submit
title: "Submit Return berfoto ditolak seluruhnya saat Storage penuh, termasuk Return Photo wajib karena I Can't Scan the TAG"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceRules: ["BORROW-LOGIC-23d", "BORROW-LOGIC-23b", "BORROW-LOGIC-23f", "BORROW-LOGIC-23e", "V-BRW-47", "T-BRW-33", "EC-BRW-182", "BORROW-LOGIC-23g", "BORROW-LOGIC-23h"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-23d": [20, 21, 22]
  "BORROW-LOGIC-23b": 23
  "BORROW-LOGIC-23f": [23, 32]
  "BORROW-LOGIC-23e": [24, 26]
  "V-BRW-47": 24
  "T-BRW-33": [24, 26]
  "EC-BRW-182": [24, 32, 41]
  "BORROW-LOGIC-23g": 32
  "BORROW-LOGIC-23h": [33, 34, 39, 40, 41, 44]
anchor: []
coverage:
  web: automated
---

# Submit Return berfoto ditolak seluruhnya saat Storage penuh, termasuk Return Photo wajib karena I Can't Scan the TAG

## Prerequisites
- Mode: FE+BE (backend nyata; cek Storage dijalankan server saat `[Submit]`; keadaan Storage diatur lewat fixture BE).
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-099-1: BRW Group `Head Office`, Borrower `Dewi Lestari {runId}-099`, Photo at end ON, berisi baris `Borrowed` aset DU-099-2 dan DU-099-3.
  - DU-099-2: aset `Laptop Lenovo T14 {runId}-099`, TAG `RFID`, Group `Head Office`.
  - DU-099-3: aset `Kamera Fuji X-T4 {runId}-099`, TAG `QR`, Group `Head Office`.
  - DU-099-4: BRW Group `Head Office`, Borrower `Dewi Lestari {runId}-099`, Photo at end OFF, berisi baris `Borrowed` aset DU-099-5.
  - DU-099-5: aset `Pompa Air Portable {runId}-099`, TAG `QR` yang tidak dapat dipindai, Group `Head Office`; Note laporan TAG yang dicoba `Label TAG rusak terkena air`.
  - DU-099-6: Client Aktor dengan kuota Storage `50.0 GB` dan usage ledger `50.0 GB` (usage di atau di atas kuota) pada awal spec; fixture BE menaikkan kuota di atas usage pada langkah yang menyebutnya.
  - Asset ID tiap aset dibentuk sistem dan menjadi milik entri aset itu.
- Jeda: langkah 25 menunggu 10 detik tanpa menutup toast agar kepersistenan toast teramati; jeda melampaui durasi tampil toast biasa dan jauh di bawah 30 detik.

## Test Steps
### Return berfoto ditolak seluruhnya saat Storage penuh
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Klik tab `Borrowed Assets`
4. Ketik Search `Laptop Lenovo T14 {runId}-099`, tekan Enter
5. Klik menu ⋯ pada baris aset DU-099-2
6. Klik `Return`
7. Klik `[+ Asset]`
8. Pilih aset DU-099-3 pada dialog Select Asset
9. Klik `[Select]`
10. Klik `[+ Asset]`
11. Pilih aset DU-099-5 pada dialog Select Asset
12. Klik `[Select]`
13. Scan TAG aset DU-099-2 lewat `[Verify Asset]`
14. Scan TAG aset DU-099-3 lewat `[Verify Asset]`
15. Klik menu ⋯ pada baris DU-099-5
16. Klik `I Can't Scan the TAG`
17. Isi Note laporan dengan `Label TAG rusak terkena air`
18. Klik tombol kirim laporan pada dialog Report TAG
19. Verifikasi baris DU-099-5 menampilkan Verification `TAG Reported`
20. Ambil foto pada kolom Return Photo baris DU-099-2
21. Ambil foto pada kolom Return Photo baris DU-099-3
22. Ambil foto pada kolom Return Photo baris DU-099-5, wajib karena `I Can't Scan the TAG` walau Photo at end OFF
23. Klik `[Submit]`
24. Verifikasi toast Error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
25. Tunggu 10 detik tanpa menutup toast
26. Verifikasi toast Error Storage penuh masih tampil (persisten, tidak hilang otomatis)
27. Tutup toast Error secara manual

### Semua baris tetap Borrowed dan pengiriman ulang berhasil setelah kuota ditambah
28. Klik `Transactions` pada sidebar
29. Klik `Borrow`
30. Klik tab `Borrowed Assets`
31. Ketik Search `{runId}-099`, tekan Enter
32. Verifikasi baris DU-099-2, DU-099-3, dan DU-099-5 semuanya berstatus `Borrowed` dan tidak ada yang sebagian Returned
33. Kuota Storage Client dinaikkan menjadi lebih besar dari usage ledger lewat fixture BE
34. Klik menu ⋯ pada baris aset DU-099-2, lalu klik `Return`
35. Klik `[+ Asset]`, pilih aset DU-099-3 pada dialog Select Asset, lalu klik `[Select]`
36. Klik `[+ Asset]`, pilih aset DU-099-5 pada dialog Select Asset, lalu klik `[Select]`
37. Scan TAG aset DU-099-2 dan DU-099-3 lewat `[Verify Asset]`
38. Klik menu ⋯ pada baris DU-099-5, klik `I Can't Scan the TAG`, isi Note laporan dengan `Label TAG rusak terkena air`, lalu klik tombol kirim laporan pada dialog Report TAG
39. Ambil ulang foto pada kolom Return Photo baris DU-099-2, DU-099-3, dan DU-099-5
40. Klik `[Submit]`
41. Verifikasi toast `Success, 3 assets have been returned.` tampil
42. Klik tab `History`
43. Ketik Search `{runId}-099`, tekan Enter
44. Verifikasi baris DU-099-2, DU-099-3, dan DU-099-5 berstatus `Returned`

## Notes
- Mode: FE+BE. Sumber: PRD `fixed-asset/borrow/PRD/borrow.md` (`BORROW-LOGIC-23`, `V-BRW-47`, `T-BRW-33`, `EC-BRW-180` sampai `EC-BRW-186`) dan `fixed-asset/file-manager/PRD/file-manager.md`. Belum ada TestCase untuk aturan ini; spec dikutip langsung dari ID aturan PRD.
- Langkah penghubung (bukan klausa aturan): langkah 1 sampai 19 (navigasi, pemilihan aset, scan, dan laporan TAG sesuai alur halaman Return), langkah 25 (jeda 10 detik agar kepersistenan toast teramati), langkah 27 (menutup toast persisten), dan langkah 28 sampai 31 (navigasi verifikasi).
- Di atas smell 35 langkah: dua percobaan Return atas data yang sama (ditolak lalu berhasil setelah kuota ditambah) tidak bermakna bila dipisah, karena percobaan kedua bergantung pada keadaan baris sesudah penolakan. Alasan P-1 (state berat).
- Nilai `50.0 GB` pada Client dan toast adalah nilai data uji (format Size T-FAFM-01; contoh PRD `50.0 GB of 50.0 GB`); keadaan Storage dan kenaikan kuota diatur lewat fixture BE.
- Klausa absence EC-BRW-182 (tidak ada Damage Report dan notifikasi `borrow_returned` dari Return yang ditolak) tidak diasersi di spec UI ini; diasersi dengan baseline jumlah di `TC-FA-BORROW-BE-097-storage-penuh-blokir-foto-transaksi-aturan-server`.
- Toast sukses `Success, 3 assets have been returned.` mengikuti pola jamak katalog yang dipakai `TC-FA-BORROW-E2E-023-return-scan-verifikasi-sebagian` (`Success, 2 assets have been returned.`); bentuk kalimat PRD T-BRW-08 diikuti pada tahap script.
- Temuan untuk PM: PRD tidak menetapkan apakah meninggalkan halaman Return lewat sidebar sesudah penolakan memunculkan dialog perubahan belum tersimpan; spec berpindah halaman lewat sidebar tanpa asersi dialog.
