---
id: TC-GS-NLU-E2E-063-bulk-activate-kelompok-di-skip-sebagian-gagal-seluruh-gagal
title: "Bulk Activate: Kelompok Di-skip, Sebagian Gagal, dan Seluruh Gagal"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-225
  - TC-GS-NLU-226
  - TC-GS-NLU-229
  - TC-GS-NLU-230
  - TC-GS-NLU-476
coverage:
  web: automated
---

# Bulk Activate: Kelompok Di-skip, Sebagian Gagal, dan Seluruh Gagal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, semua Inactive, Division Operations, Represented By Ahmad Fauzi): `Joko Susilo {runId}-063` (Inactive manual), `Agus Salim {runId}-063` dan `Reaktif Tiga {runId}-063` (Temporary-expired), `Hendra Empat {runId}-063` dan `Hendra Lima {runId}-063`, `Joko Susilo Dua {runId}-063` dan `Hendra Tujuh {runId}-063` (Inactive manual), `Campur Inaktif {runId}-063` (Inactive manual), `Campur Expired {runId}-063` (Temporary-expired). Search `{runId}-063` menyaring sembilan baris pada satu halaman. Joko Susilo Dua dipakai TC-230 karena `Joko Susilo {runId}-063` sudah Active sesudah TC-225.
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- Sesi API aktor (lihat `suite.md`, bagian Hook suite: Sesi API aktor): pelaku kedua (admin lain) yang hanya memicu perubahan state memakai sesi API akun Total Control yang sama; tidak ada sesi UI kedua. Kemampuan hapus, Convert, nonaktifkan, dan buat Login User lewat sesi itu disediakan tim FE/BE (TC tidak menyebut endpoint).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-226: Bulk Activate disembunyikan untuk seleksi Temporary-expired

1. Ketik Search `{runId}-063`, tekan Enter
2. Centang baris `Agus Salim {runId}-063` dan `Reaktif Tiga {runId}-063`
3. Klik `Bulk Action`
4. Verifikasi `Convert to Login User` tetap tampil
5. Verifikasi `Activate` tidak tampil di daftar aksi
6. Verifikasi `Deactivate` tidak tampil

### TC-GS-NLU-225: Bulk Activate memuat baris Temporary-expired

7. Ganti seleksi ke `Joko Susilo {runId}-063` dan `Agus Salim {runId}-063`: hapus centang `Reaktif Tiga {runId}-063` lalu centang `Joko Susilo {runId}-063`
8. Pilih `Bulk Action` > `Activate`
9. Verifikasi dialog dengan dua kelompok bullet: `The following will be activated:` (`Joko Susilo {runId}-063`) dan `The following will be skipped (already active or temporary period ended):` (`Agus Salim {runId}-063`), ditutup `Are you sure you want to continue?` dengan tombol `[Cancel]` dan `[Continue]`
10. Klik `[Continue]`
11. Verifikasi toast sukses varian skip: `Success, non-login user has been activated. Some users were skipped.`
12. Verifikasi `Joko Susilo {runId}-063` menjadi ON
13. Verifikasi `Agus Salim {runId}-063` tetap OFF
14. Verifikasi tidak ada dialog Extend period atau Make permanent

### TC-GS-NLU-476: Bulk Activate campuran di-skip dan baris gagal tanpa baris berhasil

15. Centang baris `Campur Inaktif {runId}-063` dan `Campur Expired {runId}-063`
16. Pilih `Bulk Action` > `Activate`
17. Di sesi API aktor (dialog dua kelompok sudah terbuka), hapus `Campur Inaktif {runId}-063` hingga penghapusan tersimpan
18. Klik `[Continue]` pada dialog dua kelompok bullet
19. Verifikasi toast error: `Error, failed to activate non-login user.` (bukan toast sukses varian skip)
20. Verifikasi `Campur Expired {runId}-063` tetap Inactive
21. Verifikasi tidak ada dialog Extend period atau Make permanent

### TC-GS-NLU-229: Bulk Activate seluruh baris gagal

22. Centang baris `Hendra Empat {runId}-063` dan `Hendra Lima {runId}-063`
23. Pilih `Bulk Action` > `Activate`
24. Di sesi API aktor (dialog sudah terbuka), hapus `Hendra Empat {runId}-063` dan `Hendra Lima {runId}-063` hingga penghapusan tersimpan
25. Klik `[Activate]`
26. Verifikasi toast error: `Error, failed to activate non-login user.` (bukan toast sukses)

### TC-GS-NLU-230: Bulk Activate sebagian baris gagal

27. Centang baris `Joko Susilo Dua {runId}-063` dan `Hendra Tujuh {runId}-063`
28. Pilih `Bulk Action` > `Activate`
29. Di sesi API aktor (dialog sudah terbuka), hapus `Hendra Tujuh {runId}-063` hingga penghapusan tersimpan
30. Klik `[Activate]`
31. Verifikasi `Joko Susilo Dua {runId}-063` diaktifkan (switch ON)
32. Verifikasi toast sukses partial: `Success, non-login user has been activated. Some users failed.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 7.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- Urutan: TC-226 (tombol disembunyikan) diletakkan sebelum TC-225 karena memakai `Agus Salim {runId}-063` dan `Reaktif Tiga {runId}-063` sebelum aksi yang mengubah status; aksi gagal berbasis hapus di sesi API ada di akhir (S-10).
- Pembagian TC lintas spec: Bulk Deactivate (TC-227, TC-228, TC-470, TC-474, TC-475) ada di spec 064.
- Temuan untuk QA:
  - TC-476 Langkah 4 menyebut dialog dua kelompok sebagai langkah (bukan Expected); spec tidak menambah asersi dialog dan hanya mengklik `[Continue]`.
  - TC-229 dan TC-230 Langkah Uji tidak menyebut cara menutup dialog atau seleksi bila ada sisa; seleksi tidak dibersihkan secara eksplisit karena TC tidak menyebutnya.
  - Bulk Activate TC-229 menyatakan toast error "bukan toast sukses"; kalimat itu dipenuhi oleh asersi teks toast error persis.
