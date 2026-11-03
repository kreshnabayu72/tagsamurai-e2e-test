---
id: TC-FA-CAID-E2E-022-perilaku-tombol-save
title: "Perilaku Tombol Save: Spinner, Klik Ganda, dan Pristine Setelah Sukses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-73
  - TC-FA-CAID-74
  - TC-FA-CAID-75
coverage:
  web: automated
---

# Perilaku Tombol Save: Spinner, Klik Ganda, dan Pristine Setelah Sukses

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 (Pre-setup No 11) ke kondisi awal di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). Aset Pre-setup No 11 (A1 Active, A2 Draft, A3 Waiting for Approval, A4 Disposed, A5 Deleted) dipakai sebagai precondition TC, tidak diasersi. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE): intercept respons Save untuk menahan dan melepas respons (`Spectra.intercept()`), hanya untuk mengamati spinner pada langkah 2 sampai 5; pemantau jumlah request Save yang terkirim ke server (pemantauan jaringan pada sesi otomasi; langkah 12 sampai 13); kemampuan membaca jumlah baris Edit Separator `Slash` ke `Dash` pada Modal Changelog sebelum dan sesudah aksi (langkah 9, baseline, dan langkah 16).
- State: spec ini menyimpan Separator `- (Dash)` pada Company Alpha dan menambah entri Changelog (tidak dihapus). Pemulihan antar TC lewat langkah penghubung (langkah 8, 18) dan hook `after` suite.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-73: Tombol Save menampilkan spinner dan disabled selama proses simpan

1. Pilih Separator `- (Dash)`
2. Tahan respons Save lewat intercept, lalu klik `[Save]`
3. Verifikasi tombol `[Save]` menampilkan spinner selama respons ditahan
4. Verifikasi tombol `[Save]` berstatus disabled selama respons ditahan
5. Lepas tahanan respons Save
6. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
7. Verifikasi spinner pada tombol `[Save]` hilang
8. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman

### TC-FA-CAID-74: Klik ganda cepat pada Save hanya memproses satu request

9. Buka Modal Changelog: Custom Asset ID dan catat jumlah baris Edit Separator Old Value `Slash` New Value `Dash` sebagai baseline
10. Tutup Modal Changelog: Custom Asset ID
11. Pilih Separator `- (Dash)`
12. Klik `[Save]` dua kali dengan cepat
13. Verifikasi hanya satu request Save terkirim ke server
14. Tunggu aksi selesai: tombol `[Save]` kembali tidak menampilkan spinner
15. Buka Modal Changelog: Custom Asset ID
16. Verifikasi jumlah baris Edit Separator Old Value `Slash` New Value `Dash` bertambah tepat satu dari baseline (tanpa baris ganda)
17. Tutup Modal Changelog: Custom Asset ID
18. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman

### TC-FA-CAID-75: Setelah Save sukses form kembali pristine

19. Pilih Separator `- (Dash)`, lalu klik `[Save]`
20. Tunggu aksi selesai
21. Verifikasi tombol `[Save]` berstatus disabled
22. Centang `Division Code`
23. Verifikasi tombol `[Save]` berstatus aktif lagi
24. Hilangkan centang `Division Code`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penahanan respons pada langkah 2 sampai 5 hanya untuk mengamati spinner (konvensi bagian 3 prinsip 13b); bukan kelas fault injection.
- Langkah penghubung (tanpa `Verifikasi`): langkah 8 dan 18 (pemulihan baseline), langkah 14 dan 20 (Tunggu aksi selesai: tombol `[Save]` kembali tidak menampilkan spinner), langkah 9 (membuka modal dan mencatat baseline, S-12), langkah 15 (membuka modal), langkah 10 dan 17 (menutup modal), dan langkah 24 (memulihkan form yang berakhir dirty; form tidak disimpan).
- Baseline pada langkah 9 dicatat sebelum aksi pemicu; asersi langkah 16 memakai selisih terhadap baseline itu (S-12), bukan total absolut. Baseline dan pembanding dihitung atas baris Edit Separator `Slash` ke `Dash` sesuai Langkah dan Expected b TC-FA-CAID-74.
- Temuan untuk QA:
  - TC-FA-CAID-74 tidak menyebut cara menghitung request Save yang terkirim; spec mengasumsikan pemantau jumlah request disediakan tim FE.
  - Dimensi "Date Changelog = waktu aksi" tidak diasersi pada TC ini karena TC tidak memintanya.
