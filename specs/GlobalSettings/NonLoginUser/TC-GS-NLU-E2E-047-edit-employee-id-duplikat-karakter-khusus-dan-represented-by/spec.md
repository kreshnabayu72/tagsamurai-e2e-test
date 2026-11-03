---
id: TC-GS-NLU-E2E-047-edit-employee-id-duplikat-karakter-khusus-dan-represented-by
title: "Edit: Employee ID duplikat, karakter khusus, dan Represented By Inactive tersimpan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-151
  - TC-GS-NLU-152
  - TC-GS-NLU-153
  - TC-GS-NLU-481
  - TC-GS-NLU-495
coverage:
  web: automated
---

# Edit: Employee ID duplikat, karakter khusus, dan Represented By Inactive tersimpan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json`, nilai dirujuk sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Login User Ahmad Fauzi (Employee ID `EMP-0001`), Non-Login User Budi Kurniawan (Employee ID `FT-0231`), Non-Login User Rina Marlina (Employee ID `DR-0114`), dan Login User Jane Smith (Inactive). Ketiga Employee ID hanya dipakai sebagai nilai pembanding duplikat.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): Non-Login User Edit Target 10 (TC-GS-NLU-151, TC-GS-NLU-152, dan TC-GS-NLU-153 dalam satu pembukaan popup), Edit Target 33 (TC-GS-NLU-481), dan `Nonaktif Wakil {runId}-047` (TC-GS-NLU-495, Represented By Jane Smith yang Inactive, Position `Staff`, Email `nonaktifwakil+{runId}-047@qwertysystem.net`). Target Edit Target: First Name `Edit Target NN`, Last Name `{runId}-047`, Email `edittargetNN+{runId}-047@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`, Active. Mekanisme membuat Non-Login User dengan Represented By yang Inactive tidak disebut TC, PRD, atau LLD sehingga disediakan tim FE/BE.
- Data uji: Employee ID `EMP-0001`, `FT-0231`, `dr-0114` (existing `DR-0114`), `EMP/2026-002 #B-{runId}-047` (TC-GS-NLU-481 menulis `EMP/2026-002 #B`; suffix per run, S-12); Position `Driver`.
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target 10 {runId}-047`, tekan Enter
2. Klik `⋯` pada baris Edit Target 10 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-151: Validasi Employee ID sudah dipakai Login User pada Popup Edit

3. Ketik Employee ID `EMP-0001` lalu tunggu sekitar 500 ms
4. Verifikasi pesan inline `Employee ID already exists`

### TC-GS-NLU-152: Validasi Employee ID sudah dipakai Non-Login User lain pada Popup Edit

5. Kosongkan isi Employee ID
6. Ketik Employee ID `FT-0231` lalu tunggu sekitar 500 ms
7. Verifikasi pesan inline `Employee ID already exists`

### TC-GS-NLU-153: Employee ID yang hanya beda huruf besar kecil dianggap berbeda pada Popup Edit

8. Kosongkan isi Employee ID
9. Ketik Employee ID `dr-0114` lalu tunggu sekitar 500 ms
10. Verifikasi field Employee ID menampilkan `dr-0114`
11. Verifikasi tidak ada pesan `Employee ID already exists` (pembanding case-sensitive)
12. Klik `[Save]`
13. Verifikasi toast sukses `Success, non-login user has been updated.`

### TC-GS-NLU-481: Employee ID dengan karakter khusus diterima tanpa helper text pada Popup Edit

14. Ganti isi kotak search dengan `Edit Target 33 {runId}-047`, tekan Enter
15. Klik `⋯` pada baris Edit Target 33 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
16. Isi Employee ID `EMP/2026-002 #B-{runId}-047`
17. Verifikasi field Employee ID menampilkan `EMP/2026-002 #B-{runId}-047`
18. Verifikasi tidak ada pesan error karakter
19. Verifikasi tidak ada helper text di bawah field Employee ID
20. Klik `[Save]`
21. Verifikasi toast sukses `Success, non-login user has been updated.`
22. Buka Detail record tersebut
23. Verifikasi Detail menampilkan Employee ID `EMP/2026-002 #B-{runId}-047`
24. Kembali ke daftar Non-Login User lewat breadcrumb

### TC-GS-NLU-495: Edit tanpa mengubah Represented By tetap tersimpan saat Login User yang diwakili sudah Inactive

25. Ketik Search `Nonaktif Wakil {runId}-047`, tekan Enter
26. Klik `⋯` pada baris Nonaktif Wakil > `Edit` sehingga Popup Edit Non-Login User terbuka
27. Verifikasi badge Represented By menampilkan `Jane Smith` saat popup terbuka
28. Ubah Position menjadi `Driver` tanpa mengubah Represented By
29. Klik `[Save]`
30. Verifikasi toast sukses `Success, non-login user has been updated.`
31. Verifikasi Position baris Nonaktif Wakil tersimpan `Driver`
32. Verifikasi tidak ada pesan `Represented by must not be empty` maupun error Represented By
33. Verifikasi sel Represented By baris tetap `Jane S`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: validasi diblokir (TC-GS-NLU-151, TC-GS-NLU-152) lebih dulu dalam satu popup, lalu TC-GS-NLU-153 (Save sukses pada popup yang sama), TC-GS-NLU-481, dan TC-GS-NLU-495 (aksi sukses), sesuai S-10.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 14, dan 25 (Search Name bersuffix untuk menemukan baris target, R-16; Email bukan kolom Search List sehingga hanya menjadi data form); langkah 5 dan 8 (pembersih antar TC pada form yang sama dengan error inline identik, R-12); langkah 24 (kembali ke daftar setelah Detail).
- TC-GS-NLU-151, TC-GS-NLU-152, dan TC-GS-NLU-153 memakai Edit Target 10, 11, dan 12 pada TC; spec memakai Edit Target 10 untuk ketiganya.
- Employee ID TC-GS-NLU-481 `EMP/2026-002 #B` disimpan unik per run sebagai `EMP/2026-002 #B-{runId}-047` (S-12); karakter khusus tetap diuji. Employee ID `dr-0114` pada TC-GS-NLU-153 tetap literal karena yang diuji adalah perbedaan huruf besar kecil terhadap `DR-0114` Pre-setup; nilainya tersimpan di Edit Target 10 milik spec dan ikut terhapus oleh hook `after`.
- Temuan untuk QA:
  - TC-GS-NLU-151 dan TC-GS-NLU-152 tidak memberi Expected tentang `[Save]` (tidak ada klik Save); spec mengikuti TC dan tidak menambah asersi Save.
  - TC-GS-NLU-495 menyebut record `Nonaktif Wakil` dari Pre-setup, tetapi Save menulis Position; spec memakai data milik spec `Nonaktif Wakil {runId}-047` (S-06). Sel Represented By `Jane S` mengikuti singkatan `[First Name] [Last Initial]`.
