---
id: TC-FA-CAID-E2E-023-retroactive-update-separator-division-account-initial
title: "Retroactive Mass Update A: Separator, Division, Account, dan Initial Company"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-76
  - TC-FA-CAID-77
  - TC-FA-CAID-78
  - TC-FA-CAID-79
coverage:
  web: automated
---

# Retroactive Mass Update A: Separator, Division, Account, dan Initial Company

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 ke kondisi awal di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company).
- Data Pre-setup No 11 (Company Alpha): A1 Active `JKT/LAP/T490/0926/1` (Increment 1, Division `Human Resources`), A2 Draft `JKT/LAP/T490/0926/2` (Division `Human Resources`), A3 Waiting for Approval `JKT/LAP/T490/0000/3` (Purchase Date kosong, tanpa Division), A4 Disposed `JKT/LAP/T490/0926/4` (Division `Human Resources`), A5 Deleted dengan Increment 5 (tidak tampil di UI). Group `Jakarta Office` (`JKT`), Category `IT Equipment > Laptop` (`LAP`), Asset Name `ThinkPad T490` (`T490`), Division `Human Resources` (`HR`), Purchase Date 15/09/26 kecuali A3. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- State: spec ini menyimpan konfigurasi dan mengubah Asset ID A1 sampai A3 (Last Updated aset berubah; entri Changelog, System Log, dan Activity Log bertambah dan tidak dihapus). Pemulihan antar TC lewat langkah penghubung (langkah 9, 18, 27) dan hook `after` suite.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-76: Ganti Separator menjadi Dash me-recompute Asset ID secara retroaktif

1. Pilih Separator `- (Dash)`
2. Klik `[Save]`
3. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
4. Buka Fixed Asset > Assets > All Assets
5. Verifikasi kolom Asset ID baris A1 (Active) menjadi `JKT-LAP-T490-0926-1` dengan nomor Increment 1 tidak berubah
6. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `JKT-LAP-T490-0926-2` dengan nomor Increment 2 tidak berubah
7. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `JKT-LAP-T490-0000-3` dengan nomor Increment 3 tidak berubah
8. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`
9. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-77: Mencentang Division Code me-recompute Asset ID dengan kode Division atau 0000

10. Centang `Division Code`
11. Klik `[Save]`
12. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
13. Buka Fixed Asset > Assets > All Assets
14. Verifikasi kolom Asset ID baris A1 (Division `Human Resources`) menjadi `JKT/LAP/T490/HR/0926/1`
15. Verifikasi kolom Asset ID baris A2 (Division `Human Resources`) menjadi `JKT/LAP/T490/HR/0926/2`
16. Verifikasi kolom Asset ID baris A3 (tanpa Division) menjadi `JKT/LAP/T490/0000/0000/3` dengan segmen Division `0000`
17. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`
18. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-78: Mencentang Account Code menghasilkan segmen 0000 untuk seluruh aset

19. Centang `Account Code`
20. Klik `[Save]`
21. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
22. Buka Fixed Asset > Assets > All Assets
23. Verifikasi kolom Asset ID baris A1 (Active) menjadi `JKT/LAP/T490/0000/0926/1`
24. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `JKT/LAP/T490/0000/0926/2`
25. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `JKT/LAP/T490/0000/0000/3`
26. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`
27. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-79: Menambah Initial Company ABC me-recompute Asset ID dengan prefix

28. Centang `Initial Company` dan ketik `ABC` pada input Initial Company
29. Klik `[Save]`
30. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
31. Buka Fixed Asset > Assets > All Assets
32. Verifikasi kolom Asset ID baris A1 (Active) menjadi `ABC/JKT/LAP/T490/0926/1`
33. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `ABC/JKT/LAP/T490/0926/2`
34. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `ABC/JKT/LAP/T490/0000/3`
35. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 9, 18, dan 27 (pemulihan baseline B1 dan aset lewat sesi API aktor, lalu kembali ke tab Custom Asset ID); langkah 4, 13, 22, dan 31 membuka All Assets sesuai Langkah Uji TC.
- Expected TC-FA-CAID-78 c ("penyimpanan tidak diblokir walau fallback `0000` dipakai") dipenuhi toast sukses langkah 21 dan nilai Asset ID langkah 23 sampai 25; tidak ada langkah tambahan.
- Expected TC-FA-CAID-76 b ("nomor Increment 1, 2, dan 3 tidak berubah") diasersi pada akhiran Asset ID di langkah 5 sampai 7.
- Pola berulang per TC: ubah konfigurasi, `[Save]`, toast, buka All Assets, Asset ID A1 sampai A4 (langkah 1 sampai 8, 10 sampai 17, 19 sampai 26, 28 sampai 35).
- Spec ini 35 langkah.
- Temuan untuk QA:
  - Post Condition TC-FA-CAID-76 sampai TC-FA-CAID-79 kosong; tidak ada asersi tambahan pada log (pencatatan ada di spec pencatatan log).
  - TC menyebut baris A1 sampai A4 berdasarkan status (Active, Draft, Waiting for Approval, Disposed) tanpa kunci baris yang tetap setelah Asset ID berubah; skrip perlu mengidentifikasi baris lewat status atau nomor Increment (tahap script).
