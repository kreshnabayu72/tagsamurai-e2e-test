---
id: TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target
title: "User Detail: Reset Authenticator (Screening Enrolled dan Not enrolled yet, Guard Default User dan Akun Sendiri, Dialog, Cancel, Reset Berhasil, dan Holder Update-Only)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-325
  - TC-GS-USER-326
  - TC-GS-USER-327
  - TC-GS-USER-328
  - TC-GS-USER-329
  - TC-GS-USER-332
  - TC-GS-USER-333
  - TC-GS-USER-334
coverage:
  web: automated
---

# User Detail: Reset Authenticator (Screening Enrolled dan Not enrolled yet, Guard Default User dan Akun Sendiri, Dialog, Cancel, Reset Berhasil, dan Holder Update-Only)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk menahan respons Reset Authenticator pada TC-GS-USER-328).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor pertama: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`. Akun kedua (ganti akun eksplisit di TC-GS-USER-334): Manage user and role Update-Only (Bayu Saputra) `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` (No. 6; kredensial `Spectra.env.GS_UPDATE_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_UPDATE_PASSWORD`, keduanya didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup (hanya dibaca, tidak diubah): John Doe (No. 18, Activated, MFA Enrolled) untuk TC-GS-USER-325, 327, dan 329 (dialog dibatalkan, tidak ada perubahan); Dewi Lestari (No. 12, belum enroll MFA) untuk TC-GS-USER-326; Hendra Gunawan (No. 1, Default User, MFA Enrolled) untuk TC-GS-USER-332; akun aktor Siti Nurhaliza sendiri (No. 2) untuk TC-GS-USER-333.
- Data Dinamis, di-seed lewat API di hook `before` (HK1), semuanya Activated, MFA Enrolled, Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - `John Doe {runId}-058`, Email `johndoe+{runId}-058@qwertysystem.net` (target TC-GS-USER-328).
  - `Dewi Lestari {runId}-058`, Email `dewilestari+{runId}-058@qwertysystem.net` (target TC-GS-USER-334).
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD):
  - Seeding status MFA Enrolled pada user seed lewat API.
  - Intercept (`Spectra.intercept()`) menahan respons Reset Authenticator pada TC-GS-USER-328; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD). Intercept dilepas segera setelah state loading diamati.
- State global yang diubah: enrollment authenticator dua user seed di atas. Hook `after` melepas semua intercept dan mengembalikan sesi ke akun default suite.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-325: Screening sub-section Authenticator untuk user Enrolled

3. Klik Name `John Doe` di User List
4. Verifikasi sub-section Authenticator menampilkan Badge `Enrolled` (success) dan Button `Reset Authenticator` (secondary)

### TC-GS-USER-326: Sub-section Authenticator user belum enroll tanpa tombol Reset

5. Kembali ke User List dengan klik Back
6. Klik Name `Dewi Lestari` di User List
7. Verifikasi sub-section Authenticator menampilkan teks muted `Not enrolled yet`
8. Verifikasi Button `Reset Authenticator` Hidden

### TC-GS-USER-332: Reset Authenticator target Default User disabled untuk Total Control

9. Kembali ke User List dengan klik Back
10. Klik Name `Hendra Gunawan` di User List
11. Hover `Reset Authenticator`
12. Verifikasi tombol `Reset Authenticator` tampil dan disabled
13. Verifikasi tooltip `"Default User cannot be modified."`

### TC-GS-USER-333: Reset Authenticator akun sendiri disabled

14. Kembali ke User List dengan klik Back
15. Klik Name `Siti Nurhaliza` di User List
16. Hover `Reset Authenticator`
17. Verifikasi tombol `Reset Authenticator` tampil dan disabled
18. Verifikasi tooltip `"Ask another admin to reset your authenticator."`

### TC-GS-USER-327 dan TC-GS-USER-329: Screening dialog Reset Authenticator dan [Cancel] tidak mengubah status

19. Kembali ke User List dengan klik Back
20. Klik Name `John Doe` di User List
21. Klik `Reset Authenticator`
22. Verifikasi Title dialog `Reset Authenticator`
23. Verifikasi body dialog bullet `John Doe`, `This will remove this user's current authenticator enrollment.`, `They will need to set up their authenticator app again the next time multi-factor authentication is required.`, dan `Are you sure you want to reset it?`
24. Verifikasi tombol dialog `[Cancel]` dan `[Reset]`
25. Klik `[Cancel]`
26. Verifikasi Badge tetap `Enrolled`

### TC-GS-USER-328: Reset Authenticator dikonfirmasi, status jadi Not enrolled yet

27. Kembali ke User List dengan klik Back
28. Klik Name `John Doe {runId}-058` di User List
29. Pasang intercept pada respons Reset Authenticator: tahan respons
30. Klik `Reset Authenticator` → `[Reset]`
31. Verifikasi tombol `[Reset]` dalam state loading
32. Verifikasi tombol `[Reset]` disabled
33. Lepas intercept respons Reset Authenticator sehingga respons diteruskan
34. Verifikasi toast sukses: "Success, authenticator has been reset for John Doe {runId}-058."
35. Verifikasi Badge `Enrolled` diganti teks muted `Not enrolled yet`
36. Verifikasi Button `Reset Authenticator` tidak tampil

### TC-GS-USER-334: Reset Authenticator oleh holder Update terhadap target Normal sukses

37. Logout dari akun Total Control, lalu login sebagai Bayu Saputra (Manage user and role Update-Only: R+U) `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.GS_UPDATE_PASSWORD`
38. Buka Global Settings > User > User List (sub-tab Login User)
39. Pilih 100 baris per halaman pada Pagination
40. Klik Name `Dewi Lestari {runId}-058` di User List
41. Klik `Reset Authenticator` → `[Reset]`
42. Verifikasi toast sukses: "Success, authenticator has been reset for Dewi Lestari {runId}-058."

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (42 langkah). Alasan: seluruh blok satu kelas (fungsional) dan satu layar (sub-section Authenticator di User Detail); tiap blok memakai user target sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pembukaan layar, buka Detail, dan pindah akun tidak dihitung sebagai alur uji.
- Urutan TC sumber diubah: screening dan guard (TC-GS-USER-325, 326, 332, 333) di awal; TC-GS-USER-327 dan 329 digabung pada satu pembukaan dialog Reset Authenticator `John Doe` (dialog dibuka satu kali, diasersi, lalu `[Cancel]`); aksi Reset berhasil (TC-GS-USER-328, 334) di akhir; TC-GS-USER-334 paling akhir karena membutuhkan ganti akun eksplisit.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): pembukaan layar, Back ke User List, pasang dan lepas intercept, "Tunggu aksi selesai", dan ganti akun ke Bayu Saputra.
- TC-GS-USER-331 diverifikasi di spec 159.
- Tooltip `"Default User cannot be modified."` dan `"Ask another admin to reset your authenticator."` ditulis persis seperti Expected TC, termasuk tanda kutip ganda.
- Temuan untuk QA:
  - TC-GS-USER-326 dan TC-GS-USER-334: Dewi Lestari belum enroll MFA di TC-GS-USER-326 tetapi Enrolled MFA di TC-GS-USER-334; Tabel Pre-setup tidak menyebut status MFA Dewi Lestari. Spec memakai Dewi Lestari Pre-setup (belum enroll) untuk TC-GS-USER-326 dan user seed `Dewi Lestari {runId}-058` (Enrolled) untuk TC-GS-USER-334.
  - TC-GS-USER-333: precondition "Akun aktor Enrolled MFA" tidak tercatat di Tabel Pre-setup untuk Siti Nurhaliza; disediakan tim FE.
  - TC-GS-USER-328: Expected a ("tombol loading dan disabled selama request") mengasersi state sementara tetapi precondition tidak menyebut respons ditahan; spec menahan respons lewat intercept.
  - TC-GS-USER-328: Post Condition (login berikutnya yang memicu MFA meminta enrollment ulang) tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-332 dan 333: tanda kutip ganda pada tooltip tidak jelas apakah bagian teks atau pembatas.
  - TC-GS-USER-334: Expected hanya menyebut toast; spec tidak menambah asersi badge setelah Reset.
