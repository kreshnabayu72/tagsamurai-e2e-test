---
id: TC-GS-NLU-E2E-046-edit-validasi-email-sudah-dipakai
title: "Edit: validasi Email sudah dipakai"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-149
  - TC-GS-NLU-150
  - TC-GS-NLU-472
coverage:
  web: automated
---

# Edit: validasi Email sudah dipakai

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json` sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Login User Ahmad Fauzi (`ahmadfauzi@qwertysystem.net`), Non-Login User Budi Kurniawan (`budi.kurniawan@qwertysystem.net`), dan Login User Rina Putri (Activated, email pending `rinaputri.baru@qwertysystem.net`). Ketiga email hanya diketik di form target dan tidak pernah disimpan.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): satu Non-Login User target Edit Target 08 dengan First Name `Edit Target 08`, Last Name `{runId}-046`, Email `edittarget08+{runId}-046@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`, Active. Ketiga TC memakai satu target dan satu pembukaan Popup Edit karena tidak ada Save yang berhasil.
- Data uji: Email `ahmadfauzi@qwertysystem.net` (TC-GS-NLU-149), `budi.kurniawan@qwertysystem.net` (TC-GS-NLU-150), `rinaputri.baru@qwertysystem.net` (TC-GS-NLU-472); jeda sekitar 500 ms setelah mengetik (idiom pendek, di bawah 30 detik).
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target 08 {runId}-046`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 08 {runId}-046` > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-149: Validasi Email sudah dipakai Login User pada Popup Edit muncul langsung saat mengetik

3. Ketik Email `ahmadfauzi@qwertysystem.net` lalu tunggu sekitar 500 ms tanpa berpindah field
4. Verifikasi pesan inline `Email already exists` muncul tanpa menunggu kursor keluar field
5. Klik `[Save]`
6. Verifikasi Popup Edit tetap terbuka
7. Verifikasi tidak ada toast sukses

### TC-GS-NLU-150: Validasi Email sudah dipakai Non-Login User lain pada Popup Edit muncul langsung saat mengetik

8. Kosongkan isi Email
9. Ketik Email `budi.kurniawan@qwertysystem.net` lalu tunggu sekitar 500 ms tanpa berpindah field
10. Verifikasi pesan inline `Email already exists` muncul tanpa menunggu kursor keluar field
11. Klik `[Save]`
12. Verifikasi Popup Edit tetap terbuka
13. Verifikasi tidak ada toast sukses

### TC-GS-NLU-472: Validasi Email yang sedang pending konfirmasi di Login User pada Popup Edit muncul langsung saat mengetik

14. Kosongkan isi Email
15. Ketik Email `rinaputri.baru@qwertysystem.net` lalu tunggu sekitar 500 ms tanpa berpindah field
16. Verifikasi pesan inline `Email already exists` muncul tanpa menunggu kursor keluar field
17. Klik `[Save]`
18. Verifikasi Popup Edit tetap terbuka
19. Verifikasi tidak ada toast sukses
20. Klik `✕` pada Popup Edit Non-Login User
21. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
22. Klik `[Leave]`
23. Klik `⋯` pada baris `Edit Target 08 {runId}-046` > `Edit` sehingga Popup Edit Non-Login User terbuka
24. Verifikasi Email Edit Target 08 tetap `edittarget08+{runId}-046@qwertysystem.net` (tidak berubah pada ketiga TC)
25. Klik `✕` pada Popup Edit Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search Name bersuffix untuk menemukan baris target (Email bukan kolom Search), R-16); langkah 8 dan 14 (pembersih antar TC pada form yang sama dengan error inline identik, R-12); langkah 20 sampai 22 (menutup popup yang dirty secara deterministik, S-08); langkah 23 dan 25 (membuka ulang Popup Edit untuk mengamati Email tersimpan, lalu menutupnya tanpa perubahan sehingga tanpa dialog).
- Temuan untuk QA:
  - TC-GS-NLU-149, TC-GS-NLU-150, dan TC-GS-NLU-472 memakai target berbeda (Edit Target 08, 09, 32). Karena tidak ada Save yang berhasil, spec memakai satu target dan satu pembukaan popup.
  - Expected butir b ("Email ... tidak berubah") tidak menyebut cara mengamati; spec membuka ulang Popup Edit dan mengasersi isi field Email.
