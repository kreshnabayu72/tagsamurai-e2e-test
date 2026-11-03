---
id: TC-AC-ACC-E2E-255-modal-changelog-asset-control-filter-dan-sort
title: "Modal Changelog: Asset Control: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-736
  - TC-AC-ACC-737
  - TC-AC-ACC-738
  - TC-AC-ACC-739
  - TC-AC-ACC-740
coverage:
  web: automated
---

# Modal Changelog: Asset Control: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Asset Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): riwayat Changelog Asset Control AL-01 (10 Jan 2026 08:00, Action `Generate Enrollment QR`, Object `Enrollment Token`, Field `Status`, Old Value `—`, New Value `Active`, Modified By Andi Wijaya); AL-02 (02 Mar 2026 09:00, `Deactivate Station`, `Gerbang Lama`, `Status`, `Inactive`, `Deactivated`, Budi Santoso); AL-03 (12 Dec 2025 10:00, `Revoke Tablet`, `Tablet Lama`, `Status`, `Active`, `Revoked`, Citra Dewi).
- Parameter blok TC-AC-ACC-737 (langkah 11 sampai 14):

| Field Filter | Nilai | Baris tampil | Baris tidak tampil |
|---|---|---|---|
| Action | Revoke Tablet | AL-03 | AL-01 |
| Object | Gerbang Lama | AL-02 | AL-01 |
| Modified By | Andi Wijaya | AL-01 | AL-02 |

- Parameter blok TC-AC-ACC-740 (ascending; descending urutan sebaliknya; langkah 31 sampai 37):

| Kolom | Urutan ascending |
|---|---|
| Action | AL-02 (Deactivate Station), AL-01 (Generate Enrollment QR), AL-03 (Revoke Tablet) |
| Object | AL-01 (Enrollment Token), AL-02 (Gerbang Lama), AL-03 (Tablet Lama) |
| Old Value | AL-03 (Active), AL-02 (Inactive), AL-01 (nilai kosong `—` di akhir) |
| New Value | AL-01 (Active), AL-02 (Deactivated), AL-03 (Revoked) |
| Modified By (nama lengkap) | AL-01 (Andi Wijaya), AL-02 (Budi Santoso), AL-03 (Citra Dewi) |

- Kemampuan teknis: Changelog adalah audit trail permanen; baris seed dibatasi lewat Filter Date 12 Dec 2025 sampai 02 Mar 2026 dan ukuran halaman 100 pada blok sort (S-14); total baris tidak diasersi sebagai angka absolut (S-12).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control

### TC-AC-ACC-736: Screening Filter Panel Changelog: Asset Control

2. Klik ikon Changelog di Tab Asset Control, lalu klik Filter pada toolbar modal
3. Verifikasi field Date (label "Date"): date range picker satu field dengan placeholder "Select date"
4. Verifikasi field Action: placeholder "All actions"
5. Verifikasi field Object: placeholder "All objects"
6. Verifikasi field Modified By: placeholder "All users"
7. Verifikasi kolom Field, Old Value, dan New Value tidak memiliki field filter
8. Verifikasi Footer panel: [Clear Field] di kiri dan [Apply] di kanan
9. Klik ulang ikon Filter untuk menutup panel

### TC-AC-ACC-737: Filter kolom Action, Object, dan Modified By

10. Ubah ukuran halaman modal menjadi 100 baris
11. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-737" (langkah 11 sampai 14): klik Filter dan klik [Clear Field]
12. Pilih nilai pada field Filter sesuai baris tabel, lalu klik [Apply]
13. Verifikasi baris pada kolom "Baris tampil" tampil
14. Verifikasi baris pada kolom "Baris tidak tampil" tidak tampil
15. Klik Filter dan klik [Clear Field]
16. Klik [Apply]

### TC-AC-ACC-738: Filter kolom Date

17. Klik Filter, pilih rentang Date 01 Jan 2026 sampai 02 Mar 2026, lalu klik [Apply]
18. Verifikasi baris AL-01 (10 Jan 2026) dan AL-02 (02 Mar 2026) tampil (batas akhir inklusif)
19. Verifikasi baris AL-03 (12 Dec 2025) tidak tampil
20. Klik Filter, klik [Clear Field], lalu klik [Apply]

### TC-AC-ACC-739: Sort kolom Date

21. Klik Filter, pilih rentang Date 12 Dec 2025 sampai 02 Mar 2026, lalu klik [Apply]
22. Verifikasi urutan awal (Newest First): AL-02, AL-01, AL-03
23. Klik header kolom Date satu kali
24. Verifikasi ascending (Oldest First): AL-03, AL-01, AL-02
25. Klik header kolom Date untuk kedua kali
26. Verifikasi descending (Newest First): AL-02, AL-01, AL-03
27. Klik header kolom Date untuk ketiga kali
28. Verifikasi indikator sort Date nonaktif
29. Verifikasi urutan kembali ke default Newest First: AL-02, AL-01, AL-03

### TC-AC-ACC-740: Sort kolom Action, Object, Old Value, New Value, dan Modified By

30. Verifikasi baris AL-01, AL-02, dan AL-03 tampil pada halaman 1 (Filter Date langkah 21 masih aktif)
31. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-740" (langkah 31 sampai 37): klik header kolom satu kali
32. Verifikasi urutan ascending sesuai tabel
33. Klik header kolom untuk kedua kali
34. Verifikasi urutan descending (urutan ascending dibalik)
35. Klik header kolom untuk ketiga kali
36. Verifikasi indikator sort kolom nonaktif
37. Verifikasi urutan kembali ke default Date Newest First

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-09): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client); langkah 9 (menutup panel Filter lewat klik ulang ikon Filter, D-001 `docs/spec-decisions.md`); langkah 11, 15, 16, 20 (membersihkan filter; `[Clear Field]` hanya mengosongkan draft sehingga [Apply] ikut diklik, D-003); langkah 21 (Filter Date 12 Dec 2025 sampai 02 Mar 2026 sebagai pembatas baris seed pada audit trail yang tumbuh, S-14; TC-AC-ACC-739 dan 740 tidak mencantumkannya).
- Langkah 11 sampai 14 diulang untuk 3 baris tabel parameter (12 langkah setelah ekspansi) dan langkah 31 sampai 37 untuk 5 baris tabel parameter (35 langkah setelah ekspansi).
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (Filter dan Sort Modal Changelog: Asset Control) pada satu dataset seed baca-saja; filter dibersihkan atau dibatasi Date di tiap blok sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-739 dan 740 tidak mencantumkan Filter Date pembatas; spec menambahkannya (langkah 21).
  - TC-AC-ACC-740 butir c: Old Value descending menyebut AL-01 (nilai kosong) di awal; dicakup oleh balikan urutan ascending pada langkah 34.
