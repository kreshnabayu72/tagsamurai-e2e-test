---
id: TC-AC-ACC-E2E-253-modal-changelog-subscription-filter-dan-sort
title: "Modal Changelog: Subscription: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-730
  - TC-AC-ACC-732
  - TC-AC-ACC-733
  - TC-AC-ACC-734
  - TC-AC-ACC-735
coverage:
  web: automated
---

# Modal Changelog: Subscription: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Subscription).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): riwayat Changelog Subscription SL-01 (01 Jan 2026 08:00, Action `Add Subscription`, Subscription `<nama produk FAMS> — Professional`, Field `Plan`, Old Value `—`, New Value `Professional`, Modified By Andi Wijaya); SL-02 (20 Jun 2026 14:00, `Edit`, `<nama produk FAMS> — Professional`, `Duration`, `1 year(s)`, `2 year(s)`, Budi Santoso); SL-03 (05 Jul 2026 09:00, `Cancel Request`, `<nama produk SAMS> — Growth`, `Status`, `Waiting for Approval`, `Canceled`, Citra Dewi).
- Parameter blok TC-AC-ACC-732 (langkah 12 sampai 15):

| Field Filter | Nilai | Baris tampil | Baris tidak tampil |
|---|---|---|---|
| Action | Edit | SL-02 | SL-01 |
| Subscription | opsi berakhiran "— Professional" | SL-01, SL-02 | SL-03 |
| Field | Plan | SL-01 | SL-02 |
| Modified By | Citra Dewi | SL-03 | SL-01 |

- Parameter blok TC-AC-ACC-735 (ascending; descending urutan sebaliknya; langkah 38 sampai 44):

| Kolom | Urutan ascending |
|---|---|
| Action | SL-01 (Add Subscription), SL-03 (Cancel Request), SL-02 (Edit) |
| Field | SL-02 (Duration), SL-01 (Plan), SL-03 (Status) |
| Old Value | SL-02 (1 year(s)), SL-03 (Waiting for Approval), SL-01 (nilai kosong `—` di akhir) |
| Modified By (nama lengkap) | SL-01 (Andi Wijaya), SL-02 (Budi Santoso), SL-03 (Citra Dewi) |

- Kemampuan teknis: Changelog adalah audit trail permanen; baris seed dibatasi lewat Filter Date 01 Jan 2026 sampai 05 Jul 2026 dan ukuran halaman 100 pada blok sort (S-14); total baris tidak diasersi sebagai angka absolut (S-12).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Subscription

### TC-AC-ACC-730: Screening Filter Panel Changelog: Subscription

2. Klik [Changelog], lalu klik Filter pada toolbar modal
3. Verifikasi field Date (label "Date"): date range picker satu field dengan placeholder "Select date"
4. Verifikasi field Action: placeholder "All actions"
5. Verifikasi field Subscription: placeholder "All subscriptions"
6. Verifikasi field berlabel "Field": placeholder "All fields"
7. Verifikasi field Modified By: placeholder "All users"
8. Verifikasi Old Value dan New Value tidak memiliki field filter
9. Verifikasi Footer panel: [Clear Field] di kiri dan [Apply] di kanan
10. Klik ulang ikon Filter untuk menutup panel

### TC-AC-ACC-732: Filter kolom Action, Subscription, Field, dan Modified By

11. Ubah ukuran halaman modal menjadi 100 baris
12. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-732" (langkah 12 sampai 15): klik Filter dan klik [Clear Field]
13. Pilih nilai pada field Filter sesuai baris tabel, lalu klik [Apply]
14. Verifikasi baris pada kolom "Baris tampil" tampil
15. Verifikasi baris pada kolom "Baris tidak tampil" tidak tampil
16. Klik Filter dan klik [Clear Field]
17. Klik [Apply]

### TC-AC-ACC-733: Filter kolom Date

18. Klik Filter, pilih rentang Date 01 Jun 2026 sampai 05 Jul 2026, lalu klik [Apply]
19. Verifikasi baris SL-02 (20 Jun 2026) dan SL-03 (05 Jul 2026) tampil (batas akhir inklusif)
20. Verifikasi baris SL-01 (01 Jan 2026) tidak tampil
21. Klik Filter, klik [Clear Field], lalu klik [Apply]

### TC-AC-ACC-734: Sort kolom Date

22. Klik Filter, pilih rentang Date 01 Jan 2026 sampai 05 Jul 2026, lalu klik [Apply]
23. Verifikasi urutan awal (Newest First): SL-03, SL-02, SL-01
24. Klik header kolom Date satu kali
25. Verifikasi ascending (Oldest First): SL-01, SL-02, SL-03
26. Klik header kolom Date untuk kedua kali
27. Verifikasi descending (Newest First): SL-03, SL-02, SL-01
28. Klik header kolom Date untuk ketiga kali
29. Verifikasi indikator sort Date nonaktif
30. Verifikasi urutan kembali ke default Newest First: SL-03, SL-02, SL-01

### TC-AC-ACC-735: Sort kolom Action, Field, Old Value, New Value, dan Modified By

31. Verifikasi baris SL-01, SL-02, dan SL-03 tampil pada halaman 1 (Filter Date langkah 22 masih aktif)
32. Klik header kolom New Value satu kali
33. Verifikasi New Value ascending: SL-02 (2 year(s)), SL-03 (Canceled), SL-01 (Professional)
34. Klik header kolom New Value untuk kedua kali
35. Klik header kolom New Value untuk ketiga kali
36. Verifikasi indikator sort New Value nonaktif
37. Verifikasi urutan kembali ke default Date Newest First
38. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-735" (langkah 38 sampai 44): klik header kolom satu kali
39. Verifikasi urutan ascending sesuai tabel
40. Klik header kolom untuk kedua kali
41. Verifikasi urutan descending (urutan ascending dibalik)
42. Klik header kolom untuk ketiga kali
43. Verifikasi indikator sort kolom nonaktif
44. Verifikasi urutan kembali ke default Date Newest First

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-09): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client); langkah 10 (menutup panel Filter lewat klik ulang ikon Filter, D-001 `docs/spec-decisions.md`); langkah 12, 16, 17, 21 (membersihkan filter; `[Clear Field]` hanya mengosongkan draft sehingga [Apply] ikut diklik, D-003); langkah 22 (Filter Date 01 Jan 2026 sampai 05 Jul 2026 sebagai pembatas baris seed pada audit trail yang tumbuh, S-14; TC-AC-ACC-734 dan 735 tidak mencantumkannya).
- Langkah 12 sampai 15 diulang untuk 4 baris tabel parameter (16 langkah setelah ekspansi) dan langkah 38 sampai 44 untuk 4 baris tabel parameter (28 langkah setelah ekspansi). New Value ditulis eksplisit (langkah 32 sampai 37) karena Expected TC-AC-ACC-735 butir d hanya menyebut urutan ascending.
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (Filter dan Sort Modal Changelog: Subscription) pada satu dataset seed baca-saja; filter dibersihkan atau dibatasi Date di tiap blok sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-735 Expected d tidak menyebut urutan New Value descending; klik kedua pada langkah 34 tidak diasersi.
  - TC-AC-ACC-734 dan 735 tidak mencantumkan Filter Date pembatas; spec menambahkannya (langkah 22).
  - TC-AC-ACC-735 butir c: Old Value descending menyebut SL-01 (nilai kosong) di awal; dicakup oleh balikan urutan ascending pada langkah 41.
