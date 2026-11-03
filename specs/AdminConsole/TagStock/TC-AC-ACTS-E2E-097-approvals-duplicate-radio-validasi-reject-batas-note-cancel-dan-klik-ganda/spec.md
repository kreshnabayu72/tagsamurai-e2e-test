---
id: TC-AC-ACTS-E2E-097-approvals-duplicate-radio-validasi-reject-batas-note-cancel-dan-klik-ganda
title: "Approvals Duplicate: Radio Approve/Reject, Reject Tanpa Note (V-09), Batas 360 Karakter, Cancel Tanpa Commit, dan Klik Ganda Submit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-276
  - TC-AC-ACTS-279
  - TC-AC-ACTS-280
  - TC-AC-ACTS-283
  - TC-AC-ACTS-284
  - TC-AC-ACTS-294
coverage:
  web: automated
---

# Approvals Duplicate: Radio Approve/Reject, Reject Tanpa Note (V-09), Batas 360 Karakter, Cancel Tanpa Commit, dan Klik Ganda Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: Approvals > TAG Stock > Tab Active (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data Subject pending disiapkan seeding fixture BE (disediakan tim FE/BE): sedikitnya tiga Subject Register Duplicate pending dari requester Distributor, satu untuk tiap aksi yang memutuskan Subject (TC-AC-ACTS-283 Reject dan TC-AC-ACTS-294 Approve; TC lain tidak memutuskan Subject). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Approval Note uji: 360 karakter dan 361 karakter non-spasi (dibuat saat langkah dijalankan).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-276: Radio Approve/Reject netral dan [Submit] disabled sampai dipilih

1. Buka Approvals > TAG Stock > Tab Active
2. Klik `Review` pada Subject Register Duplicate pending pertama
3. Verifikasi radio Approve dan Reject tidak terpilih
4. Verifikasi `[Submit]` disabled
5. Pilih Approve
6. Verifikasi `[Submit]` aktif
7. Klik `[Cancel]`

### TC-AC-ACTS-279: Reject tanpa Approval Note ditolak dengan V-09

8. Klik `Review` pada Subject pending pertama
9. Pilih Reject
10. Biarkan Approval Note kosong, klik `[Submit]`
11. Verifikasi pesan "Approval Note must not be empty"
12. Verifikasi dialog tetap terbuka
13. Klik `[Cancel]`
14. Verifikasi Subject tetap pending di Tab Active

### TC-AC-ACTS-280: Reject dengan Approval Note hanya spasi dianggap kosong

15. Klik `Review` pada Subject pending pertama
16. Pilih Reject
17. Isi Approval Note dengan tiga spasi, klik `[Submit]`
18. Verifikasi pesan "Approval Note must not be empty" tetap muncul
19. Klik `[Cancel]`
20. Verifikasi tidak ada Subject berubah (Subject pending pertama tetap di Tab Active)

### TC-AC-ACTS-284: [Cancel] menutup Detail Approval tanpa commit

21. Klik `Review` pada Subject pending pertama
22. Pilih Approve
23. Klik `[Cancel]`
24. Verifikasi dialog tertutup
25. Verifikasi Subject tetap pending di Tab Active

### TC-AC-ACTS-283: Approval Note batas 360 karakter

26. Klik `Review` pada Subject pending kedua
27. Pilih Reject
28. Isi Approval Note 361 karakter non-spasi
29. Verifikasi error real-time "Max. 360 characters"
30. Verifikasi `[Submit]` diblok
31. Ubah Approval Note menjadi 360 karakter
32. Klik `[Submit]`
33. Verifikasi 360 karakter diterima dan Submit berhasil (toast "Success, duplicate TAG has been rejected.")

### TC-AC-ACTS-294: Klik ganda [Submit] approval diproses sekali dengan state Submitting

34. Klik `Review` pada Subject pending ketiga
35. Pilih Approve
36. Klik `[Submit]` dua kali cepat
37. Verifikasi `[Submit]` disabled saat proses
38. Buka Tab History
39. Verifikasi Subject itu tercatat Approved dengan satu TAG Code (satu TAG Code diterbitkan)

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (39 langkah); alasan: semua blok satu halaman dan satu dataset Subject pending (dialog Review Tab Active), dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-AC-ACTS-283 setelah TC-AC-ACTS-284 dan TC-AC-ACTS-294 terakhir karena keduanya memutuskan Subject (aksi yang mengubah data di akhir; S-10). Pada TC-AC-ACTS-283 urutan 361 karakter lalu 360 karakter menggantikan urutan TC (360 lalu 361) karena Submit berhasil menutup dialog sehingga 361 karakter tidak dapat diasersi sesudahnya.
- Langkah penghubung tanpa Verifikasi (S-03): `[Cancel]` menutup dialog Review sebelum TC berikutnya (S-09), dan buka Tab History pada TC-AC-ACTS-294 untuk mengamati TAG Code yang diterbitkan.
- Temuan untuk QA:
  - TC-AC-ACTS-283 menyebut "Submit berhasil" tanpa toast; spec memakai toast Reject Register Duplicate dari TC-AC-ACTS-281 ("Success, duplicate TAG has been rejected.").
  - TC-AC-ACTS-294 menyebut "S-22" dan "satu TAG Code diterbitkan" tanpa cara mengamati; spec membaca Tab History.
  - TC-AC-ACTS-279 menyebut "Subject tetap pending" tanpa cara mengamati setelah dialog tetap terbuka; spec menutup dialog lalu memeriksa Tab Active.
