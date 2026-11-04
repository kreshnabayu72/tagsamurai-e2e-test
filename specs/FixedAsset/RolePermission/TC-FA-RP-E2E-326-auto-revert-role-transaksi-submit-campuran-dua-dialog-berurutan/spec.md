---
id: TC-FA-RP-E2E-326-auto-revert-role-transaksi-submit-campuran-dua-dialog-berurutan
title: "Auto-Revert Role Transaksi: Submit Campuran Dua Dialog Berurutan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1154
coverage:
  web: automated
---

# Auto-Revert Role Transaksi: Submit Campuran Dua Dialog Berurutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, Total Control; baris pola Asset Admin dan Approver), #18 (pohon group: `IT Infrastructure`), #19 (seed Role Transaksi sub-tab `Disposal`: Nadia Putri di Asset Admin; Nadia Putri dan Rina Wulandari belum ada di Monitoring & Report).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: pada langkah 23 Nadia Putri dan Rina Wulandari ditugaskan di Monitoring & Report, Nadia berpindah dari Asset Admin, dan tingkat akses Total Control Rina lepas. Hook `after` memulihkan Pre-setup #3 dan #19 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
3. Catat jumlah pada header section Monitoring & Report sebagai baseline

### TC-FA-RP-1154: Submit campuran target Total Control dan target Standard turun tangga, dua dialog berurutan (D-13 dulu, lalu D-04), Cancel pada dialog pertama membatalkan seluruh Submit

4. Klik `[+ Assign]` pada section Monitoring & Report
5. Centang Nadia Putri
6. Centang Rina Wulandari
7. Klik `[Assign]`
8. Verifikasi dialog pertama severity warning (`D-13`): Title `Change Transaction Role`; bullet `• Nadia P (currently Asset Admin)`, `This will change their role for Disposal to Monitoring & Report in IT Infrastructure.`, lalu `Are you sure you want to change it?`; tombol `[Cancel]` dan `[Change]`
9. Verifikasi dialog pertama hanya mendaftar target Standard: Rina tidak didaftar pada bullet `(currently ...)` dan tidak ada blok `These users will also lose Total Control access:`
10. Klik `[Cancel]`
11. Verifikasi dialog kedua tidak tampil
12. Verifikasi tidak ada toast
13. Verifikasi jumlah pada header section Monitoring & Report sama dengan baseline langkah 3 (tidak ada penugasan tersimpan sama sekali)
14. Klik `[+ Assign]` pada section Monitoring & Report
15. Centang Nadia Putri
16. Centang Rina Wulandari
17. Klik `[Assign]`
18. Klik `[Change]` pada dialog pertama
19. Verifikasi dialog kedua tampil terpisah dan tidak digabung dengan dialog pertama
20. Verifikasi jumlah pada header section Monitoring & Report masih sama dengan baseline langkah 3 (belum ada penugasan tersimpan selama dialog kedua terbuka)
21. Verifikasi dialog kedua severity danger: Title `Remove Total Control`; Body `• Rina W` lalu `This change will remove this user's Total Control access level. Their other role assignments will remain as they are.`, ditutup `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
22. Verifikasi dialog kedua hanya memuat target Total Control/Read Only (Nadia Putri tidak didaftar)
23. Klik `[Remove]`
24. Verifikasi seluruh penugasan tersimpan dalam satu transaksi: jumlah pada header section Monitoring & Report bertambah dua dari baseline langkah 3
25. Verifikasi Nadia Putri tampil di section Monitoring & Report
26. Verifikasi Rina Wulandari tampil di section Monitoring & Report
27. Klik Tab `Total Control`
28. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
29. Verifikasi Rina Wulandari tidak lagi ada di Tab `Total Control`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini memuat 29 langkah.
- Pembagian TC lintas spec: TC-FA-RP-1168 (Cancel pada dialog kedua) ada di spec 342; masing-masing TC tepat satu spec. Spec ini destruktif (melepas tier Rina), jalur batal ada di spec 342.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (buka Tab `Transaction Role`), langkah 3 (baseline header), langkah 27 (buka Tab `Total Control`). Langkah 28 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 29 (bagian 8b butir 2). Langkah 11, 12, dan 13 (dialog kedua, toast, dan penugasan tersimpan tidak ada setelah `[Cancel]`) memakai dialog pertama langkah 8 sebagai anchor positif.
- S-05 dan P-1: klausa Expected "tidak ada penugasan tersimpan" setelah `[Cancel]` ditulis sebagai `Verifikasi` berbaseline UI (jumlah pada header section, langkah 13 dan 20), bukan spec absence, karena state dialog dibangun langkah sebelumnya di spec ini.
- Post Condition TC-FA-RP-1154 (log `Remove`/`Assign` per penugasan, `Auto-Revert` untuk Rina, satu notifikasi ke Rina) tidak punya langkah observasi di TC ini; tidak diasersi.
- Temuan untuk QA:
  - Copy dialog bertanda "copy usulan, perlu persetujuan PM (PRD 12 #1)" di TC sumber; spec memakai teks TC apa adanya. Tombol `[Change]` pada dialog pertama juga bertanda copy usulan.
  - TC-FA-RP-1154 Expected d ("seluruh penugasan tersimpan dalam satu transaksi") tidak memberi cara mengamati atomisitas di UI; spec memakai hasil gabungan pada header section (kenaikan dua dari baseline) dan baris kedua user (langkah 24 sampai 26).
  - TC-FA-RP-1154 langkah 5 ("ulangi langkah 2 sampai 4") tidak menyatakan keadaan popup Assign setelah `[Cancel]`; spec membuka `[+ Assign]` lagi dan memilih kedua user lagi (langkah 14 sampai 16).
  - Penurunan Nadia Putri dari Asset Admin ke Monitoring & Report tidak diasersi pada section Asset Admin karena TC tidak memintanya.
