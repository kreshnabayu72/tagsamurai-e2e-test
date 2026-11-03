---
id: TC-GS-NLU-E2E-062-bulk-activate-dan-deactivate-tombol-sesuai-status-collapse-single
title: "Bulk Activate dan Deactivate: Tombol Sesuai Status, Collapse Single, Dialog, dan Cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-220
  - TC-GS-NLU-221
  - TC-GS-NLU-224
  - TC-GS-NLU-448
coverage:
  web: automated
---

# Bulk Activate dan Deactivate: Tombol Sesuai Status, Collapse Single, Dialog, dan Cancel

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Division Operations, Represented By Ahmad Fauzi): `Budi Kurniawan {runId}-062` (Active), `Rina Marlina {runId}-062` (Active, Position Driver), `Joko Susilo {runId}-062` (Inactive manual), `Dedi Hari Ini {runId}-062` (Inactive, Temporary Until hari ini). Search `{runId}-062` menyaring tepat empat baris. Pengganti Budi Kurniawan, Rina Marlina, Joko Susilo, dan Dedi Hari Ini Pre-setup karena dialog dapat mengubah statusnya (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-220: Tombol Bulk Activate dan Deactivate sesuai status

1. Ketik Search `{runId}-062`, tekan Enter
2. Centang baris `Budi Kurniawan {runId}-062` dan `Rina Marlina {runId}-062` (keduanya Active)
3. Klik `Bulk Action`
4. Verifikasi `Deactivate` dan `Convert to Login User` tampil
5. Verifikasi `Activate` Hidden
6. Ganti seleksi ke `Joko Susilo {runId}-062` (Inactive) saja: hapus centang kedua baris Active lalu centang baris itu
7. Klik `Bulk Action`
8. Verifikasi `Activate` dan `Convert to Login User` tampil
9. Verifikasi `Deactivate` Hidden
10. Ganti seleksi ke `Budi Kurniawan {runId}-062` dan `Joko Susilo {runId}-062`: hapus centang yang lain lalu centang kedua baris itu
11. Klik `Bulk Action`
12. Verifikasi `Activate`, `Deactivate`, dan `Convert to Login User` tampil

### TC-GS-NLU-221: Bulk Deactivate satu baris collapse ke dialog single

13. Klik icon `(X)` untuk membatalkan seleksi
14. Centang baris `Rina Marlina {runId}-062`
15. Pilih `Bulk Action` > `Deactivate`
16. Verifikasi dialog dengan Title `Deactivate Non-Login User` (singular)
17. Verifikasi dialog memuat satu bullet `Rina Marlina {runId}-062`
18. Verifikasi dialog memuat `Are you sure you want to deactivate it?`
19. Klik `[Cancel]` untuk menutup dialog

### TC-GS-NLU-224: Cancel pada dialog Bulk Deactivate

20. Klik icon `(X)` untuk membatalkan seleksi
21. Centang baris `Budi Kurniawan {runId}-062` dan `Rina Marlina {runId}-062`
22. Pilih `Bulk Action` > `Deactivate`
23. Klik `[Cancel]`
24. Verifikasi dialog menutup
25. Verifikasi kedua baris tetap Active (switch ON)
26. Verifikasi seleksi dipertahankan (`2 Non-Login Users selected`)

### TC-GS-NLU-448: Cancel pada dialog Bulk Activate

27. Klik icon `(X)` untuk membatalkan seleksi
28. Centang baris `Joko Susilo {runId}-062` dan `Dedi Hari Ini {runId}-062`
29. Pilih `Bulk Action` > `Activate`
30. Klik `[Cancel]`
31. Verifikasi dialog menutup
32. Verifikasi kedua baris tetap Inactive (switch OFF)
33. Verifikasi seleksi dipertahankan (`2 Non-Login Users selected`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 6, 10, 13, 19, 20, 27.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- Pembagian TC lintas spec: dialog Bulk Deactivate dan Bulk Activate dengan 12 baris (TC-222, TC-223) ada di spec 132.
- Langkah 16 dan sesudahnya: dialog dibuka dari pilihan satu baris (TC-221); `[Cancel]` sesudahnya adalah langkah penghubung karena TC-221 tidak menutup dialog.
- Temuan untuk QA:
  - TC-220 Expected a sampai c hanya menyebut daftar aksi pada `Bulk Action`; tidak menyebut urutan item menu, sehingga spec hanya memverifikasi tampil atau Hidden.
  - TC-221 tidak menyebut cara menutup dialog; spec memakai `[Cancel]`.
  - TC-224 dan TC-448 Expected "seleksi dipertahankan" tidak menyebut cara mengamatinya; spec memakai counter Bulk Action Bar.
