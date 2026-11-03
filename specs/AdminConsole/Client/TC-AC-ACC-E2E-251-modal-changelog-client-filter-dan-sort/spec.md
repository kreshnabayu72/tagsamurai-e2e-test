---
id: TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort
title: "Modal Changelog: Client: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-721
  - TC-AC-ACC-723
  - TC-AC-ACC-724
  - TC-AC-ACC-725
  - TC-AC-ACC-726
  - TC-AC-ACC-727
  - TC-AC-ACC-728
coverage:
  web: automated
---

# Modal Changelog: Client: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): riwayat Changelog Client L-01 sampai L-09 (Date, Action, Client Name, Field, Old Value, New Value, Modified By): L-01 01 Jan 2026 08:00 Create PT Sejahtera Abadi Company Name — / PT Sejahtera Abadi Andi Wijaya; L-02 15 Jun 2026 10:15 Edit PT Sejahtera Abadi PIC Email pic.old@example.com / pic.new@example.com Andi Wijaya; L-03 20 Jun 2026 14:00 Change Partner PT Teknologi Maju Partner CV Mitra Lama / CV Mitra Baru Budi Santoso; L-04 01 Jul 2026 09:00 Suspend PT Wahana Nusantara Status Active / Suspended Citra Dewi; L-05 05 Jul 2026 11:30 Unsuspend PT Wahana Nusantara Status Suspended / Active Citra Dewi; L-06 08 Jul 2026 00:05 Auto-Archive PT Karya Abadi Status Active / Archived System; L-07 09 Jul 2026 10:00 Auto-Reactivate PT Bangkit Jaya Status Archived / Active System; L-08 10 Jul 2026 16:45 Resend Activation Email PT Teknologi Maju Email — / admin@example.com Andi Wijaya; L-09 12 Aug 2026 13:20 Delete PT Lama Tak Berbayar Company Name PT Lama Tak Berbayar / — Budi Santoso.
- Parameter blok TC-AC-ACC-723 (langkah 13 sampai 16):

| Field Filter | Nilai | Baris tampil | Baris tidak tampil |
|---|---|---|---|
| Action | Suspend | L-04 | L-05 |
| Client Name | PT Teknologi Maju | L-03, L-08 | L-01 |
| Field | Status | L-04, L-05, L-06, L-07 | L-02 |
| Modified By | Budi Santoso | L-03, L-09 | L-04 |

- Parameter blok TC-AC-ACC-727 (urutan relatif; baris dalam kurung kurawal sama nilai dan urutan antar-barisnya tidak dinilai; descending urutan sebaliknya), langkah 36 sampai 42:

| Kolom | Ascending |
|---|---|
| Action | L-06, L-07, L-03, L-01, L-09, L-02, L-08, L-04, L-05 |
| Client Name | L-07, L-06, L-09, {L-01, L-02}, {L-03, L-08}, {L-04, L-05} |
| Field | {L-01, L-09}, L-08, L-03, L-02, {L-04, L-05, L-06, L-07} |
| Modified By (nama lengkap) | {L-01, L-02, L-08}, {L-03, L-09}, {L-04, L-05}, {L-06, L-07} |

- Kemampuan teknis: Changelog adalah audit trail permanen; baris seed dibatasi lewat Filter Date 01 Jan 2026 sampai 12 Aug 2026 dan ukuran halaman 100 pada blok sort (S-14); total baris tidak diasersi sebagai angka absolut (S-12).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-721: Screening Filter Panel Changelog: Client

1. Klik [Changelog] di toolbar List
2. Klik Filter pada toolbar modal
3. Verifikasi field Date (label "Date"): date range picker satu field dengan placeholder "Select date"
4. Verifikasi field Action: placeholder "All actions"
5. Verifikasi field Client Name: placeholder "All clients"
6. Verifikasi field berlabel "Field": placeholder "All fields"
7. Verifikasi field Modified By: placeholder "All users"
8. Verifikasi Old Value dan New Value tidak memiliki field filter
9. Verifikasi Footer panel: [Clear Field] di kiri dan [Apply] di kanan
10. Klik ulang ikon Filter untuk menutup panel

### TC-AC-ACC-723: Filter kolom Action, Client Name, Field, dan Modified By

11. Ubah ukuran halaman modal menjadi 100 baris
12. Klik Filter dan klik [Clear Field]
13. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-723" (langkah 13 sampai 16): pilih nilai pada field Filter sesuai baris tabel, lalu klik [Apply]
14. Verifikasi baris pada kolom "Baris tampil" tampil
15. Verifikasi baris pada kolom "Baris tidak tampil" tidak tampil
16. Klik Filter dan klik [Clear Field]
17. Klik [Apply]

### TC-AC-ACC-724: Filter kolom Date dengan rentang awal berbeda dari rentang akhir

18. Klik Filter, pilih rentang Date 01 Jul 2026 sampai 10 Jul 2026, lalu klik [Apply]
19. Verifikasi baris L-04, L-05, L-06, L-07, dan L-08 tampil (batas akhir 10 Jul 2026 inklusif)
20. Verifikasi baris L-01, L-02, L-03, dan L-09 tidak tampil
21. Klik Filter, klik [Clear Field], lalu klik [Apply]

### TC-AC-ACC-725: Filter kolom Date dengan tanggal mulai sama dengan tanggal akhir

22. Klik Filter, pilih rentang Date 05 Jul 2026 sampai 05 Jul 2026, lalu klik [Apply]
23. Verifikasi baris L-05 (05 Jul 2026 pukul 11:30) tampil
24. Verifikasi baris L-04 (01 Jul 2026) dan L-06 (08 Jul 2026) tidak tampil
25. Klik Filter, klik [Clear Field], lalu klik [Apply]

### TC-AC-ACC-726: Sort kolom Date

26. Klik Filter, pilih rentang Date 01 Jan 2026 sampai 12 Aug 2026, lalu klik [Apply]
27. Verifikasi urutan awal (Newest First): L-09, L-08, L-07, L-06, L-05, L-04, L-03, L-02, L-01
28. Klik header kolom Date satu kali
29. Verifikasi ascending (Oldest First): L-01, L-02, L-03, L-04, L-05, L-06, L-07, L-08, L-09
30. Klik header kolom Date untuk kedua kali
31. Verifikasi descending (Newest First): L-09, L-08, L-07, L-06, L-05, L-04, L-03, L-02, L-01
32. Klik header kolom Date untuk ketiga kali
33. Verifikasi indikator sort Date nonaktif
34. Verifikasi urutan kembali ke default Newest First: L-09, L-08, L-07, L-06, L-05, L-04, L-03, L-02, L-01

### TC-AC-ACC-727: Sort kolom Action, Client Name, Field, dan Modified By

35. Verifikasi baris L-01 sampai L-09 tampil pada halaman 1 (Filter Date langkah 26 masih aktif)
36. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-727" (langkah 36 sampai 42): klik header kolom satu kali
37. Verifikasi urutan ascending sesuai tabel
38. Klik header kolom untuk kedua kali
39. Verifikasi urutan descending (urutan ascending dibalik)
40. Klik header kolom untuk ketiga kali
41. Verifikasi indikator sort kolom nonaktif
42. Verifikasi urutan kembali ke default Date Newest First

### TC-AC-ACC-728: Sort kolom Old Value dan New Value: nilai kosong di akhir saat ascending dan di awal saat descending

43. Verifikasi baris L-01 sampai L-09 seluruhnya tampil pada halaman 1 (ukuran halaman 100)
44. Klik header kolom Old Value satu kali
45. Verifikasi Old Value ascending: {L-04, L-06} (Active), L-07 (Archived), L-03 (CV Mitra Lama), L-02 (pic.old@example.com), L-09 (PT Lama Tak Berbayar), L-05 (Suspended), {L-01, L-08} (nilai kosong `—` di akhir)
46. Klik header kolom Old Value untuk kedua kali
47. Verifikasi Old Value descending: nilai kosong `—` di awal ({L-01, L-08}), L-05, L-09, L-02, L-03, L-07, {L-04, L-06}
48. Klik header kolom New Value satu kali
49. Verifikasi New Value ascending: {L-05, L-07} (Active), L-08 (admin@example.com), L-06 (Archived), L-03 (CV Mitra Baru), L-02 (pic.new@example.com), L-01 (PT Sejahtera Abadi), L-04 (Suspended), L-09 (nilai kosong `—` di akhir)
50. Klik header kolom New Value untuk kedua kali
51. Verifikasi New Value descending: nilai kosong `—` di awal (L-09), L-04, L-01, L-02, L-03, L-06, L-08, {L-05, L-07}

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-09): langkah 10 (menutup panel Filter lewat klik ulang ikon Filter, D-001 `docs/spec-decisions.md`); langkah 12, 16, 17, 21, 25 (membersihkan filter; `[Clear Field]` hanya mengosongkan draft sehingga [Apply] ikut diklik, D-003); langkah 26 (Filter Date 01 Jan 2026 sampai 12 Aug 2026 pada TC-AC-ACC-726 dan 727 sebagai pembatas baris seed pada audit trail yang tumbuh, S-14; filter yang sama dipakai TC-AC-ACC-728 di langkah 3 TC itu).
- Langkah 13 sampai 16 diulang untuk 4 baris tabel parameter (16 langkah setelah ekspansi) dan langkah 36 sampai 42 untuk 4 baris tabel parameter (28 langkah setelah ekspansi); tiap iterasi diawali [Clear Field] (D-003) atau klik header berikutnya.
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (Filter dan Sort Modal Changelog: Client) pada satu dataset seed baca-saja; filter dibersihkan atau dibatasi Date di tiap blok sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-726 dan 727 tidak mencantumkan Filter Date pembatas pada langkah sumber; pada audit trail permanen baris non-seed dapat masuk halaman teramati. Spec menambah Filter Date 01 Jan 2026 sampai 12 Aug 2026 mengikuti TC-AC-ACC-728 (langkah 26).
  - TC-AC-ACC-723 langkah 5 menyebut "opsi pengguna Budi Santoso" untuk Modified By tetapi Expected tabel memakai nama lengkap; spec memilih opsi "Budi Santoso".
