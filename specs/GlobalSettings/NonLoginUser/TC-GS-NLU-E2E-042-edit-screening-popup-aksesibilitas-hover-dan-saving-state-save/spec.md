---
id: TC-GS-NLU-E2E-042-edit-screening-popup-aksesibilitas-hover-dan-saving-state-save
title: "Edit: screening Popup, aksesibilitas, hover dan Saving state Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-134
  - TC-GS-NLU-135
  - TC-GS-NLU-136
  - TC-GS-NLU-137
coverage:
  web: automated
---

# Edit: screening Popup, aksesibilitas, hover dan Saving state Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json` sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Non-Login User Budi Kurniawan (Field Technician, Operations, `FT-0231`, `budi.kurniawan@qwertysystem.net`, Represented By Ahmad Fauzi, foto, Active) dan Rina Marlina (Driver, Logistics, `DR-0114`, Temporary +30 hari, Represented By Dewi Anggraini). Popup Edit keduanya hanya dibuka dan ditutup tanpa Save sehingga data tidak berubah.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE): Non-Login User target Save (TC-GS-NLU-137) dengan First Name `Simpan Uji`, Last Name `{runId}-042`, Email `simpanuji+{runId}-042@qwertysystem.net`, Position `Staff`, Division `Operations`, Represented By `Ahmad Fauzi`, Active. TC-GS-NLU-137 memakai data milik spec, bukan Budi Kurniawan, karena Save menulis Position.
- Kemampuan teknis: hover elemen; membaca atribut `aria-required`, `aria-describedby` dan posisi fokus; membaca state hover dan Saving state tombol.
- Kemampuan teknis: respons permintaan simpan ditahan dan dilepas lewat `Spectra.intercept()` (TC-GS-NLU-137); intercept dilepas pada langkah terakhir.
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Klik `⋯` pada baris Budi Kurniawan > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-134: Screening Popup Edit Non-Login User dengan nilai terisi

3. Verifikasi header menampilkan Title `Edit Non-Login User` dan tombol close `✕`
4. Verifikasi avatar foto Budi tampil
5. Verifikasi First Name `Budi` dan Last Name `Kurniawan`
6. Verifikasi Position `Field Technician`, Division `Operations`, dan Employee ID `FT-0231`
7. Verifikasi Email `budi.kurniawan@qwertysystem.net`
8. Verifikasi helper text di bawah Email `Used to send the activation email if this person is later converted to a login user.`
9. Verifikasi Represented By berupa badge `Ahmad Fauzi` dengan ikon `✎`
10. Verifikasi checkbox `Set as Temporary User` tidak tercentang
11. Verifikasi bagian Custom Fields tampil
12. Verifikasi footer menampilkan tombol `[Clear Field]` dan `[Save]`
13. Verifikasi footer tanpa checkbox `Stay on this form after submitting`

### TC-GS-NLU-136: Accessibility Popup Edit Non-Login User: atribut field wajib dan focus trap

14. Verifikasi field wajib punya `aria-required="true"`
15. Tekan Tab berulang melewati `[Save]`
16. Verifikasi fokus tetap di dalam popup (focus trap)
17. Kosongkan First Name
18. Klik `[Save]`
19. Verifikasi First Name yang error punya `aria-describedby` ke pesan `First name must not be empty`
20. Klik `✕` pada Popup Edit Non-Login User
21. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
22. Klik `[Leave]`

### TC-GS-NLU-135: Popup Edit menampilkan Temporary User terisi untuk Temporary User aktif

23. Ganti isi kotak search dengan `Rina Marlina`, tekan Enter
24. Klik `⋯` pada baris Rina Marlina > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
25. Verifikasi checkbox `Set as Temporary User` tercentang
26. Verifikasi date picker `Temporary Until` tampil berisi tanggal Rina Marlina (+30 hari)
27. Klik `✕` pada Popup Edit Non-Login User

### TC-GS-NLU-137: Hover dan Saving state tombol Save pada Popup Edit

28. Ganti isi kotak search dengan `Simpan Uji {runId}-042`, tekan Enter
29. Klik `⋯` pada baris `Simpan Uji {runId}-042` > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
30. Ubah Position menjadi `Driver`
31. Hover `[Save]`
32. Verifikasi `[Save]` menampilkan state hover sesuai desain
33. Klik `[Save]` dengan respons permintaan simpan ditahan
34. Verifikasi `[Save]` masuk Saving state sampai respons diterima
35. Lepas tahanan respons

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: TC-GS-NLU-136 dijalankan sebelum TC-GS-NLU-135 supaya popup Budi Kurniawan dipakai TC-GS-NLU-134 dan TC-GS-NLU-136 tanpa pembukaan ulang; TC-GS-NLU-137 terakhir karena Save menulis data.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 23, dan 28 (Search Name bersuffix untuk menemukan baris target (Email bukan kolom Search), R-16); langkah 20 sampai 22 (menutup popup yang dirty secara deterministik, S-08) dan langkah 27 (menutup popup yang tidak berubah sehingga tanpa dialog); langkah 35 (melepas tahanan respons; hasil penyimpanan setelah dilepas tidak diasersi karena TC tidak memberi Expected).
- Spec berakhir dengan Position data milik spec yang tersimpan `Driver`; data itu dihapus hook `after`.
- Temuan untuk QA:
  - TC-GS-NLU-137 langkah 3 menyebut Budi Kurniawan sebagai target, tetapi Save menulis Position; spec memakai data milik spec `Simpan Uji` (S-06).
  - TC-GS-NLU-137 Expected butir a ("state hover sesuai desain") tidak menyebut tampilan hover; spec mengasersi state hover apa adanya dan tidak menentukan warna.
  - TC-GS-NLU-135 menyebut tanggal Rina Marlina "+30 hari" tanpa tanggal absolut; tanggal itu dihitung dari waktu seeding Pre-setup dan dibaca dari date picker.
