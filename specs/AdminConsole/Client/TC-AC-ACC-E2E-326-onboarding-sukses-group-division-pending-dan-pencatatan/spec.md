---
id: TC-AC-ACC-E2E-326-onboarding-sukses-group-division-pending-dan-pencatatan
title: "One-step Onboarding Berhasil: Group Mengikuti Distributor Induk, Division Terseed Tanpa Position, Start Date Masa Depan Pending, dan Pencatatan Changelog serta Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-510
  - TC-AC-ACC-513
  - TC-AC-ACC-514
  - TC-AC-ACC-515
coverage:
  web: automated
---

# One-step Onboarding Berhasil: Group Mengikuti Distributor Induk, Division Terseed Tanpa Position, Start Date Masa Depan Pending, dan Pencatatan Changelog serta Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Data Uji (tiap TC memakai Client baru yang dibuat spec dengan Company Name bersuffix; Email Default User bersuffix agar unik): Nilai tetap tiap baris Data Uji: PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia/DKI Jakarta/Jakarta Selatan`; Postal Code `12190`; Division `Finance`; Product `FAMS`; Plan `Professional`; Duration `1 year`.
  - TC-AC-ACC-510: Company Name `PT Onboarding Menteng {runId}-326`; Partner `CV Mitra Sejati`; Default User `Rudi Hartono`, Email `rudi.hartono+{runId}-326@qwertysystem.net`; Start Date hari ini.
  - TC-AC-ACC-513: Company Name `PT Onboarding Divisi {runId}-326`; Group `Cabang Menteng`; Default User `Rizky Pratama`, Email `rizky.pratama+{runId}-326@qwertysystem.net`; Start Date hari ini.
  - TC-AC-ACC-514: Company Name `PT Onboarding Tertunda {runId}-326`; Group `Cabang Menteng`; Default User `Siska Amelia`, Email `siska.amelia+{runId}-326@qwertysystem.net`; Start Date 7 hari setelah hari ini.
  - TC-AC-ACC-515: Company Name `PT Log Satu Langkah {runId}-326`; Group `Cabang Menteng`; Default User `Teguh Santoso`, Email `teguh.santoso+{runId}-326@qwertysystem.net`; Start Date hari ini.
- Hook `after` menghapus Client, subscription, dan Default User yang dibuat spec lewat Fixture BE (Client dengan subscription tidak dapat dihapus lewat UI).
- Kemampuan teknis: Fixture BE untuk menghapus data uji; membaca Changelog Client dan Activity Log. TC-AC-ACC-513 dan TC-AC-ACC-514 membuka Global Settings tenant Client (cara masuk konteks tenant Client disediakan tim FE). Tidak butuh intercept, klien HTTP, atau jam server.

## Test Steps

### Partner dipilih, Select Group tersembunyi (TC-AC-ACC-510)

1. Buka Admin Console > Client Subscription
2. Klik `[+ Subscription]`
3. Pilih Subscription Type `New`
4. Buka field Client dan pilih opsi `+ New Client`
5. Isi Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, dan Division pada form inline sesuai tabel Data Uji (Company Name `PT Onboarding Menteng {runId}-326`)
6. Pilih Partner `CV Mitra Sejati`
7. Lihat form inline
8. Verifikasi field Select Group tidak tampil
9. Isi Product, Plan, Duration, dan Start Date sesuai tabel Data Uji
10. Klik `[Submit]`
11. Verifikasi toast sukses `Success, client has been created.`
12. Buka Admin Console > Client, ketik Search `PT Onboarding Menteng {runId}-326`, tekan Enter
13. Verifikasi baris `PT Onboarding Menteng {runId}-326` di sub-tab Active: Managed By `CV Mitra Sejati`
14. Verifikasi Group `Area Jakarta`
15. Verifikasi FAMS `Active`

### Division terseed, Default User tertaut tanpa Position (TC-AC-ACC-513)

16. Buka Admin Console > Client Subscription
17. Klik `[+ Subscription]`
18. Pilih Subscription Type `New`
19. Buka field Client dan pilih opsi `+ New Client`
20. Isi Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, dan Division pada form inline sesuai tabel Data Uji (Company Name `PT Onboarding Divisi {runId}-326`)
21. Pilih Group `Cabang Menteng` pada tree Select Group
22. Isi Product, Plan, Duration, dan Start Date sesuai tabel Data Uji
23. Klik `[Submit]`
24. Verifikasi toast sukses `Success, client has been created.`
25. Buka Admin Console > Client, ketik Search `PT Onboarding Divisi {runId}-326`, tekan Enter, lalu buka Detail Client `PT Onboarding Divisi {runId}-326`
26. Verifikasi section Default User: Name `Rizky Pratama`
27. Verifikasi section Default User: Division `Finance`
28. Verifikasi section Default User: Position `—`
29. Buka Global Settings tenant Client > Division
30. Verifikasi Division `Finance` sebagai satu-satunya Division
31. Verifikasi kolom Code Division `Finance` terisi (tidak kosong)
32. Buka Global Settings tenant Client > Position
33. Verifikasi Position kosong (empty state)

### Start Date masa depan: term Pending (TC-AC-ACC-514)

34. Buka Admin Console > Client Subscription
35. Klik `[+ Subscription]`
36. Pilih Subscription Type `New`
37. Buka field Client dan pilih opsi `+ New Client`
38. Isi Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, dan Division pada form inline sesuai tabel Data Uji (Company Name `PT Onboarding Tertunda {runId}-326`)
39. Pilih Group `Cabang Menteng` pada tree Select Group
40. Isi Product, Plan, Duration, dan Start Date sesuai tabel Data Uji (Start Date 7 hari setelah hari ini)
41. Klik `[Submit]`
42. Verifikasi toast sukses `Success, client has been created.`
43. Buka Admin Console > Client, ketik Search `PT Onboarding Tertunda {runId}-326`, tekan Enter
44. Verifikasi baris `PT Onboarding Tertunda {runId}-326`: FAMS `Pending`
45. Buka Detail Client `PT Onboarding Tertunda {runId}-326`
46. Verifikasi section Default User: status `Not Yet Activated`
47. Verifikasi tombol `[Resend Activation Email]` tidak tampil
48. Buka Global Settings tenant Client > User dan lihat Default User
49. Verifikasi Default User belum memiliki App Access produk FAMS

### Pencatatan Changelog dan Activity Log (TC-AC-ACC-515)

50. Buka Admin Console > Client Subscription
51. Klik `[+ Subscription]`
52. Pilih Subscription Type `New`
53. Buka field Client dan pilih opsi `+ New Client`
54. Isi Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, dan Division pada form inline sesuai tabel Data Uji (Company Name `PT Log Satu Langkah {runId}-326`)
55. Pilih Group `Cabang Menteng` pada tree Select Group
56. Isi Product, Plan, Duration, dan Start Date sesuai tabel Data Uji
57. Klik `[Submit]`
58. Tunggu aksi selesai
59. Buka Admin Console > Client lalu klik `[Changelog]` di toolbar, ketik Search `PT Log Satu Langkah {runId}-326` di Search modal, tekan Enter
60. Verifikasi Changelog Client: Action `Create`, Client Name `PT Log Satu Langkah {runId}-326`, Field `Company Name`, Old Value `—`, New Value `PT Log Satu Langkah {runId}-326`, Modified By aktor
61. Buka Admin Console > Activity Log lalu cari baris Name `PT Log Satu Langkah {runId}-326`
62. Verifikasi Activity Log: baris Action `Create`, Object `Client`, Name `PT Log Satu Langkah {runId}-326`, Field `Company Name`, Old Value `—`, New Value `PT Log Satu Langkah {runId}-326`, Modified By aktor

## Notes

- Spec membuat empat Client lewat UI (tiap TC satu pembuatan); tidak ada aksi menghabisi data. Cleanup via Fixture BE di hook `after`.
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (pembuatan Client lewat form inline) dan data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah isi form diulang per blok mengikuti tabel Data Uji.
- Nama literal pada Expected TC (`PT Onboarding Menteng`, `PT Onboarding Divisi`, `PT Onboarding Tertunda`, `PT Log Satu Langkah`) diberi suffix `{runId}-326`; Default User Email diberi `+{runId}-326` agar unik (S-12).
- Langkah penghubung (S-03): `Tunggu aksi selesai` sebelum pindah surface (bagian 8b butir 8).
- Temuan untuk QA
  - TC-AC-ACC-510: Expected (c) `Group Area Jakarta` untuk Client yang dibuat Principal dengan Partner `CV Mitra Sejati` mengikuti Group Distributor induk (PT Distribusi Nusantara, Area Jakarta) sesuai Tabel A.
  - TC-AC-ACC-513 dan TC-AC-ACC-514: Langkah `Buka Global Settings tenant Client` tidak menyebut cara masuk ke tenant Client; Division `Finance` sebagai satu-satunya Division mengandalkan tenant baru tanpa Division sebelumnya.
  - TC-AC-ACC-515: Langkah 8 `Buka Admin Console > Client lalu klik Changelog` tanpa Search; spec menambah Search nama bersuffix sebagai langkah penghubung (S-12).
