---
id: TC-FA-RP-E2E-325-auto-revert-role-transaksi-turun-dan-naik-tangga-dari-popup-assign
title: "Auto-Revert Role Transaksi: Turun dan Naik Tangga dari Popup Assign"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1152
  - TC-FA-RP-1153
coverage:
  web: automated
---

# Auto-Revert Role Transaksi: Turun dan Naik Tangga dari Popup Assign

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, Total Control; baris pola Asset Admin dan Approver), #12 (Maya Anggraeni, Read Only; baris pola Monitoring & Report), #18 (pohon group: `IT Infrastructure`), #19 (seed Role Transaksi sub-tab `Disposal`; Rina Wulandari belum ada di Monitoring & Report dan Maya Anggraeni belum ada di Asset Admin).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: pada TC-FA-RP-1152 (langkah 15) Rina Wulandari ditugaskan di Monitoring & Report dan tingkat akses Total Control Rina lepas; pada TC-FA-RP-1153 (langkah 28) Maya Anggraeni ditugaskan di Asset Admin dan tingkat akses Read Only Maya lepas. Hook `after` memulihkan Pre-setup #3, #12, dan #19 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
3. Catat jumlah pada header section Monitoring & Report sebagai baseline

### TC-FA-RP-1152: Turun tangga pada target Total Control dari popup Assign, satu dialog auto-revert D-04, D-13 tidak tampil

4. Klik `[+ Assign]` pada section Monitoring & Report
5. Centang Rina Wulandari
6. Klik `[Assign]`
7. Verifikasi dialog hanya memuat blok auto-revert: Title `Remove Total Control`; Body `• Rina W` lalu `This change will remove this user's Total Control access level. Their other role assignments will remain as they are.`, ditutup `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
8. Verifikasi tidak ada bullet `(currently ...)` dan tidak ada kalimat `This will change their role for ...` pada dialog (D-13 tidak tampil untuk target TC/RO)
9. Klik `[Cancel]`
10. Verifikasi tidak ada toast
11. Verifikasi jumlah pada header section Monitoring & Report sama dengan baseline langkah 3 (tidak ada penugasan tersimpan)
12. Klik `[+ Assign]` pada section Monitoring & Report
13. Centang Rina Wulandari
14. Klik `[Assign]`
15. Klik `[Remove]` pada dialog
16. Verifikasi toast sukses `Success, Monitoring & Report has been assigned. Rina Wulandari is no longer Total Control.`
17. Verifikasi Rina Wulandari tampil di section Monitoring & Report pada node itu
18. Verifikasi penugasan lain tidak direset: baris Rina Wulandari di section Asset Admin pada node itu tetap ada
19. Klik Tab `Total Control`
20. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
21. Verifikasi Rina Wulandari tidak lagi ada di Tab `Total Control`

### TC-FA-RP-1153: Naik tangga pada target Read Only dari popup Assign, satu dialog auto-revert D-04 dan lepas tier

22. Klik Tab `Transaction Role`
23. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
24. Klik `[+ Assign]` pada section Asset Admin
25. Centang Maya Anggraeni
26. Klik `[Assign]`
27. Verifikasi dialog Title `Remove Read Only`; Body `• Maya A` lalu `This change will remove this user's Read Only access level. Their other role assignments will remain as they are.`, ditutup `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
28. Klik `[Remove]` pada dialog
29. Verifikasi toast sukses `Success, Asset Admin has been assigned. Maya Anggraeni is no longer Read Only.`
30. Verifikasi Maya Anggraeni tampil di section Asset Admin
31. Verifikasi section Monitoring & Report Maya Anggraeni diganti sesuai tangga (`FARP-LOGIC-18d`)
32. Klik Tab `Read Only`
33. Verifikasi sedikitnya satu baris Read Only lain tampil di Tab `Read Only`
34. Verifikasi Maya Anggraeni tidak lagi ada di Tab `Read Only`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini memuat 34 langkah.
- Urutan TC sumber dipertahankan (1152, lalu 1153); keduanya melepas tier target yang berbeda sehingga tidak saling bergantung.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 22 (buka Tab `Transaction Role`), langkah 3 (baseline header), langkah 19 dan 32 (buka Tab tingkat akses). Langkah 20 dan 33 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 21 dan 34 (bagian 8b butir 2). Langkah 10 (tidak ada toast) dan langkah 11 (tidak ada penugasan tersimpan) memakai dialog langkah 7 sebagai anchor positif; langkah 8 (D-13 tidak tampil) memakai dialog langkah 7 sebagai anchor positif.
- Klausa "naik tangga memicu dialog padahal target Standard tidak" pada TC-FA-RP-1153 Expected a adalah pembanding terhadap target Standard; yang diasersi adalah dialog D-04 tampil untuk target Read Only (langkah 27). Perilaku target Standard diasersi di spec 326.
- Post Condition TC-FA-RP-1152 dan TC-FA-RP-1153 (log `Assign` dan `Auto-Revert` bermodifier admin pengedit, notifikasi in-app ke target) tidak punya langkah observasi di TC ini; tidak diasersi.
- Temuan untuk QA:
  - Copy dialog dan toast bertanda "copy usulan, perlu persetujuan PM (PRD 12 #1)" di TC sumber; spec memakai teks TC apa adanya.
  - TC-FA-RP-1152 langkah 5 ("ulangi langkah 2 sampai 3") tidak menyatakan keadaan popup Assign setelah `[Cancel]` pada dialog (tertutup atau tetap terbuka dengan Rina tercentang); spec mengikuti TC dengan membuka `[+ Assign]` lagi dan memilih Rina lagi (langkah 12 sampai 14).
  - TC-FA-RP-1152 Expected b ("tidak ada penugasan tersimpan") tidak memberi cara observasi; spec memakai baseline jumlah pada header section Monitoring & Report (langkah 3 dan 11).
  - TC-FA-RP-1152 Expected d ("penugasan lain tidak direset") tidak menyebut penugasan yang dimaksud; spec memakai baris Asset Admin Rina pada node itu (langkah 18).
  - TC-FA-RP-1153 Expected c ("Monitoring & Report diganti sesuai tangga, `FARP-LOGIC-18d`") tidak menyebut keadaan akhir Monitoring & Report Maya secara konkret, sehingga langkah 31 tidak dapat dibuat lebih presisi; perlu klarifikasi QA.
  - TC-FA-RP-1153 hanya menguji `[Remove]`; jalur `[Cancel]` pada naik tangga tidak punya TC.
