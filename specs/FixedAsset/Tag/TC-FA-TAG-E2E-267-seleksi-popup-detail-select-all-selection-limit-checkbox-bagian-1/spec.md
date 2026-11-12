---
id: TC-FA-TAG-E2E-267-seleksi-popup-detail-select-all-selection-limit-checkbox-bagian-1
title: "Seleksi Popup Detail: Unselect All, Checkbox Header Indeterminate, dan Selection Limit pada Seleksi Manual serta Select All (Bagian 1)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1400
  - TC-FA-TAG-1401
  - TC-FA-TAG-1402
  - TC-FA-TAG-1403
  - TC-FA-TAG-1404
coverage:
  web: automated
---

# Seleksi Popup Detail: Unselect All, Checkbox Header Indeterminate, dan Selection Limit pada Seleksi Manual serta Select All (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab Paired (tanpa suffix `{runId}`; kunci `Fixture.fixedAssetTag.pairedGrup`): grup Excavator 20 Ton / Plant A (RFID, 20 aset), Excavator 20 Ton / Plant B (RFID, 20 aset; target Popup Detail, 10 baris per halaman sehingga 2 halaman; memuat aset AST-0011 dan AST-0021), Laptop Pro 14 / HQ (NFC dan QR, 25 aset), dan Forklift Manual / Plant A (Non TAG, 10 aset).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned dalam jumlah yang dibutuhkan; pengubahan Selection Limit di Lifecycle Settings > System Limits oleh pelaku kedua lewat sesi API (nilai awal dicatat sebelum diubah); tidak ada endpoint yang dikarang di spec ini.
- Sesi API aktor: pelaku kedua (akun admin disediakan tim FE) mengubah Selection Limit dan dataset lewat login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`), tanpa asersi di sesinya.
- Selection Limit: TC-FA-TAG-1402, 1403, dan 1404 berjalan dengan Selection Limit nilai awal; Selection Limit diturunkan menjadi 5 pada langkah 20 untuk TC-FA-TAG-1400 dan 1401. Hook `after` memulihkan Selection Limit ke nilai awal, juga bila spec gagal di tengah. Suite serial mencegah spec lain membaca Selection Limit yang turun.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan melakukan aksi lewat sesi API (langkah 20).

## Test Steps

### TC-FA-TAG-1402: Unselect All membatalkan seluruh seleksi lintas halaman

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
2. Klik tombol `Select All (20 records)`
3. Verifikasi tombol berlabel `Unselect All`
4. Klik tombol `Unselect All`
5. Verifikasi Bulk Action Bar tertutup
6. Verifikasi seleksi kembali 0
7. Pindah ke halaman 2 Popup Detail
8. Verifikasi tidak ada baris tercentang di halaman 2
9. Kembali ke halaman 1 Popup Detail
10. Verifikasi tidak ada baris tercentang di halaman 1

### TC-FA-TAG-1403: uncheck satu baris dari seleksi penuh mengembalikan tombol ke Select All

11. Klik tombol `Select All (20 records)`
12. Hilangkan centang satu baris pada halaman 1
13. Verifikasi tombol berubah kembali dari `Unselect All` menjadi `Select All (20 records)`
14. Verifikasi Bulk Action Bar tetap tampil dengan jumlah terpilih 19
15. Klik ikon `×` di sisi kanan Bulk Action Bar

### TC-FA-TAG-1404: checkbox header indeterminate saat sebagian baris tercentang

16. Centang tiga baris pada halaman 1
17. Verifikasi checkbox header kolom Checkbox berstatus indeterminate (ikon strip minus)
18. Verifikasi Bulk Action Bar tampil dengan jumlah terpilih 3
19. Klik ikon `×` di sisi kanan Bulk Action Bar

### TC-FA-TAG-1400: seleksi manual berhenti di Selection Limit

20. Atur Selection Limit menjadi 5 di Lifecycle Settings > System Limits (pelaku kedua lewat sesi API) hingga tersimpan, muat ulang halaman (F5), lalu klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
21. Centang baris satu per satu sampai 5 baris
22. Arahkan kursor ke checkbox baris keenam
23. Verifikasi checkbox baris keenam Disabled (tetap tampil) dengan tooltip "You've reached the maximum selection of 5 rows."
24. Verifikasi Bulk Action Bar tetap tampil dengan jumlah terpilih 5
25. Verifikasi Bulk Action Bar dapat dipakai

### TC-FA-TAG-1401: Select All melebihi Selection Limit dipotong dengan toast error

26. Klik ikon `×` di sisi kanan Bulk Action Bar
27. Klik tombol `Select All (20 records)`
28. Verifikasi toast "Error, only the first 5 of 20 rows were selected. Narrow your filter to include the rest." tampil
29. Verifikasi Bulk Action Bar tampil dengan jumlah terpilih 5
30. Verifikasi Bulk Action Bar tetap dapat dipakai
31. Tutup Popup Detail

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1400 s.d. 1404). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1405 s.d. 1407 ada di spec 268; TC-FA-TAG-1371 s.d. 1376 ada di spec 264; TC-FA-TAG-1408 s.d. 1413 ada di spec 265 dan 266.
- Urutan TC di dalam spec: TC-FA-TAG-1402, 1403, 1404, lalu 1400 dan 1401. TC-FA-TAG-1402 sampai 1404 dijalankan dengan Selection Limit awal sehingga Select All memilih 20 baris; Selection Limit diturunkan satu kali pada langkah 20 untuk TC-FA-TAG-1400 dan 1401 (S-10).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 9 (kembali ke halaman 1); 15, 19, 26 (membatalkan seleksi lewat ikon `×` pada Bulk Action Bar); 20 (memuat Selection Limit 5 dan membuka kembali Popup Detail); 31 (menutup Popup Detail).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan melakukan aksi lewat sesi API (langkah 20).
- Temuan untuk QA:
  - TC-FA-TAG-1400 s.d. 1404 tidak menyebut teks jumlah terpilih pada Bulk Action Bar di Popup Detail (hanya "jumlah terpilih N"); spec mengasersi jumlahnya tanpa teks persis.
  - TC-FA-TAG-1400 s.d. 1404 tidak menyebut cara membatalkan seleksi antar kasus selain `Unselect All`; spec memakai ikon `×` pada Bulk Action Bar seperti pada TC-FA-TAG-1408.
  - TC-FA-TAG-1400 dan 1401 Expected "Bulk Action Bar dapat dipakai" tidak menyebut aksi yang diverifikasi; spec mengasersi bar tampil dan aksinya tidak Disabled.
  - TC-FA-TAG-1402 s.d. 1404 menyebut data Pre-setup tab Paired "lihat Data Uji" tanpa merinci aset yang dicentang; spec memakai baris halaman 1 dan halaman 2 Popup Detail.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
