---
id: TC-FA-CAID-E2E-019-segmen-checkbox-dan-live-preview
title: "Daftar Segmen: Asset Increment Terkunci, Centang Segmen, dan Live Preview"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-61
  - TC-FA-CAID-62
  - TC-FA-CAID-63
  - TC-FA-CAID-64
coverage:
  web: automated
---

# Daftar Segmen: Asset Increment Terkunci, Centang Segmen, dan Live Preview

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 di `beforeEach` dan `after` lewat sesi API aktor.
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company), hanya dibaca. Contoh Live Preview memakai Code master Pre-setup No 11 (Group `Jakarta Office` `JKT`, Category `IT Equipment > Laptop` `LAP`, Asset Name `ThinkPad T490` `T490`, Purchase Date 15/09/26). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Spec hanya mengklik dan mengamati: tidak menekan `[Save]`, tidak membuat data, tidak mengubah state global. Satu pembukaan form dipakai untuk seluruh TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-61: Checkbox Asset Increment terkunci tercentang

1. Klik checkbox pada baris `Asset Increment`
2. Verifikasi checkbox `Asset Increment` tetap tercentang
3. Verifikasi checkbox `Asset Increment` berstatus disabled
4. Verifikasi Live Preview tetap `JKT/LAP/T490/0926/1`
5. Verifikasi tombol `[Save]` tetap disabled

### TC-FA-CAID-62: Mencentang dan meng-uncheck segmen default tercentang

6. Hilangkan centang `Group Code`
7. Verifikasi Live Preview menampilkan `LAP/T490/0926/1`
8. Centang kembali `Group Code`
9. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0926/1`
10. Hilangkan centang `Category Code`
11. Verifikasi Live Preview menampilkan `JKT/T490/0926/1`
12. Centang kembali `Category Code`
13. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0926/1`
14. Hilangkan centang `Asset Name Code`
15. Verifikasi Live Preview menampilkan `JKT/LAP/0926/1`
16. Centang kembali `Asset Name Code`
17. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0926/1`
18. Hilangkan centang `Purchase Date (MMYY)`
19. Verifikasi Live Preview menampilkan `JKT/LAP/T490/1`
20. Centang kembali `Purchase Date (MMYY)`
21. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0926/1`

### TC-FA-CAID-63: Segmen default tidak tercentang menampilkan 0000

22. Centang `Division Code`
23. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0000/0926/1`
24. Verifikasi sub-contoh baris `Division Code` bernilai `0000`
25. Hilangkan centang `Division Code`
26. Centang `Account Code`
27. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0000/0926/1`
28. Verifikasi sub-contoh baris `Account Code` bernilai `0000`
29. Centang juga `Division Code`
30. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0000/0000/0926/1`

### TC-FA-CAID-64: Kedelapan segmen tercentang dengan Initial Company ABC

31. Hilangkan centang `Division Code` dan `Account Code`, lalu centang `Initial Company` dan ketik `ABC` pada input Initial Company
32. Centang `Division Code`
33. Centang `Account Code`
34. Verifikasi Live Preview menampilkan `ABC/JKT/LAP/T490/0000/0000/0926/1` dengan delapan token berurutan sesuai urutan baris
35. Kosongkan input Initial Company, lalu hilangkan centang `Initial Company`, `Division Code`, dan `Account Code`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 25 (menghilangkan centang `Division Code` sesuai Langkah Uji TC-FA-CAID-63), langkah 31 (bagian "Hilangkan centang `Division Code` dan `Account Code`" menyiapkan keadaan awal TC-FA-CAID-64; bagian berikutnya adalah Langkah Uji TC-FA-CAID-64), dan langkah 35 (memulihkan form yang berakhir dirty; form tidak pernah disimpan).
- Langkah 8, 12, 16, dan 20 (centang kembali) adalah bagian Langkah Uji TC-FA-CAID-62 ("lalu centang kembali"); keadaan Live Preview sesudahnya diasersi pada langkah 9, 13, 17, dan 21.
- Pola berulang per segmen pada TC-FA-CAID-62: langkah 6 sampai 9, 10 sampai 13, 14 sampai 17, dan 18 sampai 21.
- Temuan untuk QA:
  - G-11 di catatan TC: teks dan format Sub-Labels Live Preview tidak didefinisikan PRD; spec hanya mengasersi sub-contoh `0000` yang disebut Expected TC-FA-CAID-63 dan tidak mengasersi sub-label lain.
  - Post Condition TC-FA-CAID-61 sampai TC-FA-CAID-64 kosong; tidak ada asersi tambahan.
