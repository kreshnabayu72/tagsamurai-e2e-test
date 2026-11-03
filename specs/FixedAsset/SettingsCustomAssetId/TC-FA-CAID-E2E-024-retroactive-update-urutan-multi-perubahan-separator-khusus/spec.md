---
id: TC-FA-CAID-E2E-024-retroactive-update-urutan-multi-perubahan-separator-khusus
title: "Retroactive Mass Update B: Urutan Segmen, Multi Perubahan, Space, dan None"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-80
  - TC-FA-CAID-81
  - TC-FA-CAID-82
  - TC-FA-CAID-83
coverage:
  web: automated
---

# Retroactive Mass Update B: Urutan Segmen, Multi Perubahan, Space, dan None

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 ke kondisi awal di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company).
- Data Pre-setup No 11 (Company Alpha): A1 Active `JKT/LAP/T490/0926/1` (Increment 1, Division `Human Resources`), A2 Draft `JKT/LAP/T490/0926/2` (Division `Human Resources`), A3 Waiting for Approval `JKT/LAP/T490/0000/3` (Purchase Date kosong, tanpa Division), A4 Disposed `JKT/LAP/T490/0926/4` (Division `Human Resources`), A5 Deleted dengan Increment 5 (tidak tampil di UI). Group `Jakarta Office` (`JKT`), Category `IT Equipment > Laptop` (`LAP`), Asset Name `ThinkPad T490` (`T490`), Division `Human Resources` (`HR`), Purchase Date 15/09/26 kecuali A3. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE): drag-and-drop pada drag handle baris segmen (langkah 1).
- State: spec ini menyimpan konfigurasi dan mengubah Asset ID A1 sampai A3 (Last Updated aset berubah; entri Changelog, System Log, dan Activity Log bertambah dan tidak dihapus). Pemulihan antar TC lewat langkah penghubung (langkah 9, 20, 29) dan hook `after` suite.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-80: Mengubah urutan segmen me-recompute Asset ID mengikuti urutan baru

1. Seret baris `Purchase Date (MMYY)` ke atas baris `Group Code`
2. Klik `[Save]`
3. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
4. Buka Fixed Asset > Assets > All Assets
5. Verifikasi kolom Asset ID baris A1 (Active) menjadi `0926/JKT/LAP/T490/1`
6. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `0926/JKT/LAP/T490/2`
7. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `0000/JKT/LAP/T490/3`
8. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`
9. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-81: Satu Save dengan Separator, Initial Company, dan Division sekaligus

10. Pilih Separator `- (Dash)`
11. Centang `Initial Company` dan ketik `ABC` pada input Initial Company
12. Centang `Division Code`
13. Klik `[Save]`
14. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
15. Buka Fixed Asset > Assets > All Assets
16. Verifikasi kolom Asset ID baris A1 (Active) menjadi `ABC-JKT-LAP-T490-HR-0926-1`
17. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `ABC-JKT-LAP-T490-HR-0926-2`
18. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `ABC-JKT-LAP-T490-0000-0000-3`
19. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`
20. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-82: Separator Space me-recompute Asset ID dengan spasi tunggal

21. Pilih Separator `Space`
22. Klik `[Save]`
23. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
24. Buka Fixed Asset > Assets > All Assets
25. Verifikasi kolom Asset ID baris A1 (Active) menjadi `JKT LAP T490 0926 1`
26. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `JKT LAP T490 0926 2`
27. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `JKT LAP T490 0000 3`
28. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`
29. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-83: Separator None menyambung nilai segmen dan Increment tetap unik

30. Pilih Separator `None`
31. Klik `[Save]`
32. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
33. Buka Fixed Asset > Assets > All Assets
34. Verifikasi kolom Asset ID baris A1 (Active) menjadi `JKTLAPT49009261`
35. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `JKTLAPT49009262`
36. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `JKTLAPT49000003`
37. Verifikasi nomor Increment 1, 2, dan 3 pada akhir ketiga Asset ID berbeda satu sama lain
38. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 38 langkah, di atas smell 35 langkah. Alasan: keempat blok satu topik (Retroactive Mass Update dengan aset yang sama), satu kelas harness, dan berdiri sendiri karena baseline dan aset dipulihkan lewat seed antar blok (langkah 9, 20, 29), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pola berulang per TC: ubah konfigurasi, `[Save]`, toast, buka All Assets, Asset ID A1 sampai A4 (langkah 1 sampai 8, 10 sampai 19, 21 sampai 28, 30 sampai 38).
- Langkah penghubung (tanpa `Verifikasi`): langkah 9, 20, dan 29 (pemulihan baseline B1 dan aset lewat sesi API aktor, lalu kembali ke tab Custom Asset ID); langkah 4, 15, 24, dan 33 membuka All Assets sesuai Langkah Uji TC.
- Langkah 37 memeriksa keunikan Increment sebagai `Verifikasi` sendiri (S-01) walau nilainya terlihat dari langkah 34 sampai 36, karena Expected TC-FA-CAID-83 c memuatnya sebagai klausa terpisah dari A4.
- Temuan untuk QA:
  - TC menyebut baris A1 sampai A4 berdasarkan status (Active, Draft, Waiting for Approval, Disposed) tanpa kunci baris yang tetap setelah Asset ID berubah; skrip perlu mengidentifikasi baris lewat status atau nomor Increment (tahap script).
  - Post Condition TC-FA-CAID-80 sampai TC-FA-CAID-83 kosong; tidak ada asersi tambahan.
