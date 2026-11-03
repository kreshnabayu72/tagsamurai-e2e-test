---
id: TC-FA-CAID-E2E-035-dialog-unsaved-changes-d01-navigasi
title: "Dialog D-01 Unsaved Changes: Judul, Cancel, Leave, Breadcrumb, dan Sidebar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-104
  - TC-FA-CAID-105
  - TC-FA-CAID-106
  - TC-FA-CAID-107
  - TC-FA-CAID-108
coverage:
  web: automated
---

# Dialog D-01 Unsaved Changes: Judul, Cancel, Leave, Breadcrumb, dan Sidebar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11), dipulihkan oleh hook `beforeEach` suite. Tidak ada data Dinamis.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: tidak ada; perubahan form tidak pernah disimpan dan spec berakhir dengan form pristine setelah `[Leave]`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-104: Judul, isi, dan tombol dialog D-01

1. Centang `Division Code` tanpa menekan `[Save]`
2. Klik tab `Asset Name`
3. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning) tampil
4. Verifikasi halaman tidak berpindah selama dialog terbuka (tab `Custom Asset ID` tetap aktif)

### TC-FA-CAID-105: Cancel membatalkan navigasi dan mempertahankan perubahan

5. Klik `[Cancel]` pada dialog
6. Verifikasi dialog tertutup
7. Verifikasi pengguna tetap di tab `Custom Asset ID`
8. Verifikasi checkbox `Division Code` tetap tercentang
9. Verifikasi tombol `[Save]` tetap aktif

### TC-FA-CAID-107: D-01 muncul saat klik segmen Breadcrumb

10. Klik segmen `Asset Master` pada Breadcrumb
11. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning) tampil
12. Verifikasi pengguna tetap di tab `Custom Asset ID` sampai memilih tombol dialog
13. Klik `[Leave]` pada dialog `Unsaved Changes`
14. Verifikasi halaman berpindah ke tujuan yang diklik sebelum dialog muncul, yaitu `Asset Master`

### TC-FA-CAID-108: D-01 muncul saat klik menu sidebar

15. Klik tab `Custom Asset ID` pada Tabs Bar
16. Centang `Division Code` tanpa menekan `[Save]`
17. Klik menu `Assets` pada sidebar navigasi
18. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning) tampil
19. Verifikasi pengguna tetap di tab `Custom Asset ID` sampai memilih tombol dialog
20. Klik `[Leave]` pada dialog `Unsaved Changes`
21. Verifikasi halaman berpindah ke tujuan yang diklik sebelum dialog muncul, yaitu menu `Assets`

### TC-FA-CAID-106: Leave pindah ke tab tujuan dan membuang perubahan

22. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
23. Centang `Division Code` tanpa menekan `[Save]`
24. Klik tab `Asset Name`
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`
27. Verifikasi tab `Asset Name` terbuka
28. Klik tab `Custom Asset ID`
29. Verifikasi checkbox `Division Code` tidak tercentang (nilai tersimpan)
30. Verifikasi tombol `[Save]` disabled

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: TC-FA-CAID-104, TC-FA-CAID-105, TC-FA-CAID-107, TC-FA-CAID-108, TC-FA-CAID-106. Form dirty dari langkah 1 dipakai ulang oleh TC-FA-CAID-104, 105, dan 107 karena aksi pembuka tiap TC identik (centang `Division Code` tanpa Save) dan dialog dipakai ulang. `[Leave]` pada TC-FA-CAID-107 (langkah 13) membuang perubahan dan memindahkan halaman, sehingga TC-FA-CAID-108 dan TC-FA-CAID-106 kembali ke tab `Custom Asset ID` dan mengulang aksi pembuka sendiri (langkah 15 dan 16, 22 dan 23). TC-FA-CAID-106 tetap di akhir karena `[Leave]` menutup form (S-09, S-10).
- Langkah penghubung: langkah 5 (`[Cancel]` menutup dialog sebelum TC-FA-CAID-107), langkah 15 dan 22 (kembali ke tab `Custom Asset ID` setelah `[Leave]` memindahkan halaman), langkah 16 dan 23 (mengulang aksi pembuka karena `[Leave]` membuang perubahan); `Verifikasi` dialog pada langkah 25 mengikuti S-08.
- Pembagian TC lintas spec: TC-FA-CAID-109 sampai 115 ada di spec 036.
- Temuan untuk QA:
  - Post Condition TC-FA-CAID-104 sampai 108 tidak diasersi karena TC tidak memberi langkah observasinya.
