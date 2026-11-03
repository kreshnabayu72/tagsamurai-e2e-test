---
id: TC-FA-CAID-E2E-025-retroactive-update-increment-polos-dan-urutan-unchecked
title: "Retroactive Mass Update C: Hanya Asset Increment, Urutan Segmen Unchecked, dan Toggle ke ON"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-84
  - TC-FA-CAID-85
  - TC-FA-CAID-99
coverage:
  web: automated
---

# Retroactive Mass Update C: Hanya Asset Increment, Urutan Segmen Unchecked, dan Toggle ke ON

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 ke kondisi awal di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). TC-FA-CAID-99 memakai baseline B1 dengan Master Switch OFF dan Asset ID A1, A2, A3 berupa nomor Increment polos `1`, `2`, `3`, di-seed lewat sesi API aktor pada langkah 27.
- Data Pre-setup No 11 (Company Alpha): A1 Active `JKT/LAP/T490/0926/1` (Increment 1, Division `Human Resources`), A2 Draft `JKT/LAP/T490/0926/2` (Division `Human Resources`), A3 Waiting for Approval `JKT/LAP/T490/0000/3` (Purchase Date kosong, tanpa Division), A4 Disposed `JKT/LAP/T490/0926/4` (Division `Human Resources`), A5 Deleted dengan Increment 5 (tidak tampil di UI). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): drag-and-drop pada drag handle baris segmen (langkah 12); kemampuan membaca jumlah entri Histori Aset aset A1, A2, dan A3 sebelum aksi sebagai baseline (langkah 11).
- State: spec ini menyimpan konfigurasi dan mengubah Asset ID A1 sampai A3 (Last Updated aset berubah; entri Changelog, System Log, Activity Log, dan Histori Aset bertambah dan tidak dihapus). Pemulihan antar TC lewat langkah penghubung (langkah 10, 27) dan hook `after` suite.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-84: Hanya Asset Increment tercentang menghasilkan nomor Increment polos

1. Hilangkan centang `Group Code`, `Category Code`, `Asset Name Code`, dan `Purchase Date (MMYY)`
2. Verifikasi Live Preview menampilkan `1`
3. Klik `[Save]`
4. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
5. Buka Fixed Asset > Assets > All Assets
6. Verifikasi kolom Asset ID baris A1 (Active) menjadi `1` tanpa padding nol
7. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `2` tanpa padding nol
8. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `3` tanpa padding nol
9. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`
10. Pulihkan konfigurasi Company Alpha ke baseline B1 dan aset A1 sampai A5 ke kondisi awal lewat sesi API aktor hingga tersimpan, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-85: Perubahan urutan yang hanya melibatkan segmen unchecked tetap perubahan riil

11. Catat jumlah entri tab `Histori Aset` pada Detail A1, A2, dan A3 sebagai baseline
12. Seret baris `Division Code` ke atas baris `Initial Company`
13. Verifikasi tombol `[Save]` aktif
14. Klik `[Save]`
15. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
16. Verifikasi toast netral `No changes to save.` tidak tampil
17. Buka Fixed Asset > Assets > All Assets
18. Verifikasi kolom Asset ID baris A1 (Active) tetap `JKT/LAP/T490/0926/1`
19. Verifikasi kolom Asset ID baris A2 (Draft) tetap `JKT/LAP/T490/0926/2`
20. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) tetap `JKT/LAP/T490/0000/3`
21. Buka Detail A1 > tab `Histori Aset`
22. Verifikasi jumlah entri riwayat Asset ID A1 sama dengan baseline
23. Buka Detail A2 > tab `Histori Aset`
24. Verifikasi jumlah entri riwayat Asset ID A2 sama dengan baseline
25. Buka Detail A3 > tab `Histori Aset`
26. Verifikasi jumlah entri riwayat Asset ID A3 sama dengan baseline

### TC-FA-CAID-99: Toggle ke ON tanpa dialog konfirmasi me-reformat aset ke format lengkap

27. Setel konfigurasi Company Alpha ke baseline B1 dengan Master Switch OFF dan Asset ID A1, A2, A3 menjadi nomor Increment polos `1`, `2`, `3` lewat sesi API aktor hingga tersimpan, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID
28. Geser Master Switch ke ON
29. Verifikasi tidak ada dialog konfirmasi
30. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
31. Verifikasi Master Switch berada pada posisi ON
32. Buka Fixed Asset > Assets > All Assets
33. Verifikasi kolom Asset ID baris A1 (Active) menjadi `JKT/LAP/T490/0926/1`
34. Verifikasi kolom Asset ID baris A2 (Draft) menjadi `JKT/LAP/T490/0926/2`
35. Verifikasi kolom Asset ID baris A3 (Waiting for Approval) menjadi `JKT/LAP/T490/0000/3`
36. Verifikasi kolom Asset ID baris A4 (Disposed) tetap `JKT/LAP/T490/0926/4`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 36 langkah, di atas smell 35 langkah. Alasan: ketiga blok satu topik (Retroactive Mass Update dengan aset yang sama), satu kelas harness, dan berdiri sendiri karena baseline dan aset dipulihkan lewat seed antar blok (langkah 10 dan 27), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 10 dan 27 (pemulihan atau penyetelan baseline lewat sesi API aktor, lalu kembali ke tab Custom Asset ID), langkah 11 (pencatatan baseline Histori Aset sebelum aksi pemicu, S-12), dan langkah 5, 17, serta 32 (membuka All Assets sesuai Langkah Uji TC).
- Langkah 22, 24, dan 26 mengasersi jumlah entri riwayat Asset ID sama dengan baseline (bukan absence mutlak), sesuai Expected TC-FA-CAID-85 c ("tidak ada entri riwayat Asset ID baru").
- Temuan untuk QA:
  - TC-FA-CAID-85 menyebut Asset ID A4 pada Langkah Uji tetapi Expected c hanya memuat A1, A2, dan A3; spec tidak mengasersi A4 pada TC ini.
  - TC-FA-CAID-99 menyebut Asset ID A1 sampai A3 berupa nomor Increment polos sebagai precondition tanpa cara pembentukannya; spec membentuknya lewat seed (kemampuan disediakan tim FE/BE).
  - HINT kelas g pada indeks TC-FA-CAID-85 dan TC-FA-CAID-99 tidak dipakai: Expected keduanya mengasersi perubahan dan jumlah, bukan absence log.
