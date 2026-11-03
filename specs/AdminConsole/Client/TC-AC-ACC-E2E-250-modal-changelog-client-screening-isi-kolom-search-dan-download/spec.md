---
id: TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download
title: "Modal Changelog: Client: Screening, Isi Kolom, Search per Kolom, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-339
  - TC-AC-ACC-341
  - TC-AC-ACC-342
  - TC-AC-ACC-354
  - TC-AC-ACC-722
  - TC-AC-ACC-729
  - TC-AC-ACC-970
coverage:
  web: automated
---

# Modal Changelog: Client: Screening, Isi Kolom, Search per Kolom, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): riwayat Changelog Client L-01 sampai L-09 dan riwayat Changelog Subscription SL-01 (Add Subscription, FAMS Professional, PT Sejahtera Abadi) :

| Id | Date | Action | Client Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| L-01 | 01 Jan 2026 08:00 | Create | PT Sejahtera Abadi | Company Name | — | PT Sejahtera Abadi | Andi Wijaya |
| L-02 | 15 Jun 2026 10:15 | Edit | PT Sejahtera Abadi | PIC Email | pic.old@example.com | pic.new@example.com | Andi Wijaya |
| L-03 | 20 Jun 2026 14:00 | Change Partner | PT Teknologi Maju | Partner | CV Mitra Lama | CV Mitra Baru | Budi Santoso |
| L-04 | 01 Jul 2026 09:00 | Suspend | PT Wahana Nusantara | Status | Active | Suspended | Citra Dewi |
| L-05 | 05 Jul 2026 11:30 | Unsuspend | PT Wahana Nusantara | Status | Suspended | Active | Citra Dewi |
| L-06 | 08 Jul 2026 00:05 | Auto-Archive | PT Karya Abadi | Status | Active | Archived | System |
| L-07 | 09 Jul 2026 10:00 | Auto-Reactivate | PT Bangkit Jaya | Status | Archived | Active | System |
| L-08 | 10 Jul 2026 16:45 | Resend Activation Email | PT Teknologi Maju | Email | — | admin@example.com | Andi Wijaya |
| L-09 | 12 Aug 2026 13:20 | Delete | PT Lama Tak Berbayar | Company Name | PT Lama Tak Berbayar | — | Budi Santoso |

- Parameter blok TC-AC-ACC-341 (langkah 24 sampai 27):

| Kolom | Kata kunci | Baris tampil | Baris tidak tampil |
|---|---|---|---|
| Action | resend | L-08 | L-01 |
| Client Name | wahana | L-04, L-05 | L-01 |
| Field | pic email | L-02 | L-04 |
| Old Value | pic.old@example.com | L-02 | L-01 |
| New Value | admin@example.com | L-08 | L-09 |
| Modified By | budi | L-03, L-09 | L-04 |

- Kemampuan teknis: penangkapan nama berkas unduhan di browser uji (disediakan tim FE). Changelog adalah audit trail permanen: baris seed dicari lewat Search atau Filter Date dan ukuran halaman 100 (S-14), total baris tidak diasersi sebagai angka absolut (S-12).
- General Settings: Date Format dan Time Format tidak diubah.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-339: Screening Modal Changelog: Client

1. Klik [Changelog] di toolbar List
2. Verifikasi Header: Title "Changelog: Client"
3. Verifikasi Toolbar: Search dengan placeholder "Search action, field, or value..."
4. Verifikasi Toolbar: `Filter` dan `Download` tampil
5. Verifikasi tabel memuat kolom `Date`, `Action`, `Client Name`, `Field`, `Old Value`, `New Value`, `Modified By`, `Column Visibility (⋯)`
6. Verifikasi urutan default Date terbaru
7. Verifikasi tabel read-only tanpa row action
8. Verifikasi Footer: Pagination dengan default 10 baris per halaman
9. Verifikasi opsi ukuran halaman 10, 25, 50, 100
10. Verifikasi modal berlebar 800 px, tinggi hug content maksimum 648 px, dan padding 24 px

### TC-AC-ACC-354: Nilai Action, Client Name teks biasa, Old/New kosong

11. Ubah ukuran halaman modal menjadi 100 baris, ketik Search "PT Lama Tak Berbayar", tekan Enter
12. Klik Filter dan buka dropdown Action
13. Verifikasi opsi Action memuat Create, Edit, Change Partner, Unsuspend, Suspend, Auto-Archive, Auto-Reactivate, Delete, Send Activation Email, Resend Activation Email, dan Retry Access Setup
14. Tutup dropdown dan panel Filter dengan klik ulang ikon Filter
15. Verifikasi sel Client Name baris L-09 berupa teks biasa (bukan link)
16. Verifikasi baris Delete (L-09): New Value `—`
17. Ganti isi Search dengan "PT Sejahtera Abadi" lalu tekan Enter
18. Verifikasi baris Create (L-01): Old Value `—`

### TC-AC-ACC-970: Modified By `System` dan format nama singkat

19. Ganti isi Search dengan "Auto" lalu tekan Enter
20. Verifikasi baris L-06 (Auto-Archive) dan L-07 (Auto-Reactivate) tampil dengan Modified By `System`
21. Ganti isi Search dengan "PT Sejahtera Abadi" lalu tekan Enter
22. Verifikasi baris L-01 (Create) dan L-02 (Edit) tampil dengan Modified By "Andi W"

### TC-AC-ACC-341: Search per kolom

23. Klik ikon ✕ pada input Search lalu tekan Enter
24. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-341" (langkah 24 sampai 27): ketik kata kunci pada kolom Search, tekan Enter
25. Verifikasi baris pada kolom "Baris tampil" tampil
26. Verifikasi baris pada kolom "Baris tidak tampil" tidak tampil
27. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-722: Search tidak mencakup kolom Date

28. Klik ikon Search, ketik teks sel Date baris L-02 persis seperti tampil (15 Jun 2026, pukul 10:15, format sesuai General Settings), lalu tekan Enter
29. Verifikasi empty state: Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
30. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-342: Download Changelog: Client

31. Klik Download pada toolbar modal
32. Verifikasi overlay memuat opsi "Download as CSV" dan "Download as XLSX"
33. Klik "Download as CSV"
34. Verifikasi tidak ada toast sukses
35. Verifikasi berkas `Changelog-Client.csv` terunduh
36. Klik Download lagi lalu klik "Download as XLSX"
37. Verifikasi tidak ada toast sukses
38. Verifikasi berkas `Changelog-Client.xlsx` terunduh

### TC-AC-ACC-729: Changelog: Client tidak memuat aksi Subscription

39. Klik ikon Search, ketik "Subscription", lalu tekan Enter
40. Verifikasi empty state: Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
41. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik "Auto" dan tekan Enter
42. Verifikasi baris L-06 (Auto-Archive) dan L-07 (Auto-Reactivate) tampil
43. Klik ikon ✕ pada input Search lalu tekan Enter
44. Klik Filter lalu buka dropdown Action dan baca opsi
45. Verifikasi opsi Action tidak memuat "Add Subscription" dan tidak memuat "Cancel Request"
46. Tutup dropdown dan panel Filter dengan klik ulang ikon Filter, lalu tutup modal
47. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Subscription, lalu klik [Changelog]
48. Ubah ukuran halaman modal menjadi 100 baris
49. Verifikasi baris SL-01 dengan Action "Add Subscription" tampil di Changelog: Subscription

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 11 dan 17 (Search untuk memperkecil baris audit trail ke baris seed, S-14), langkah 14 dan 46 (menutup panel Filter lewat klik ulang ikon Filter, D-001 `docs/spec-decisions.md`), langkah 23, 27, 30, 43 (mengosongkan Search), langkah 46 (menutup modal), langkah 47 (Search dan buka Detail Client).
- Urutan TC di spec berbeda dari urutan nomor TC (339, 354, 970, 341, 722, 342, 729) agar TC-AC-ACC-729 yang berpindah ke halaman Detail berada paling akhir; tiap TC dapat berjalan dari modal yang sama karena Search dikosongkan di antara TC.
- Langkah 24 sampai 27 diulang untuk 6 baris tabel parameter (24 langkah setelah ekspansi).
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (Modal Changelog: Client, baca-saja atas data seed) pada satu modal yang sama; tiap blok diawali Search yang dikosongkan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: Filter dan Sort Changelog: Client ada di spec 251; Setup Column ada di spec 256 sampai 260; empty state genuinely kosong di spec 261; SSE di spec 262; isolasi per viewer di spec 263, 264, dan 265.
- Temuan untuk QA:
  - TC-AC-ACC-354 Expected a ("Action memuat ...") tidak menyebut surface yang memuat daftar Action; spec memeriksa opsi dropdown Filter Action (langkah 12 dan 13).
  - TC-AC-ACC-722 langkah 2 mensyaratkan teks sel Date "persis seperti tampil" tanpa menyebut format tampilan; spec memakai nilai yang dibaca dari sel baris L-02.
  - TC-AC-ACC-339 Expected c menyebut dimensi modal (W800, tinggi hug content maks 648px, padding 24px) tanpa menyebut cara mengukur; spec mengasersi lebar, tinggi maksimum, dan padding dari gaya komputasi elemen modal.
  - TC-AC-ACC-341 langkah 2 mengubah ukuran halaman menjadi 100; pada audit trail permanen yang tumbuh (S-14) baris seed L-01 sampai L-09 hanya dijamin tampil lewat Search yang dipakai TC.
