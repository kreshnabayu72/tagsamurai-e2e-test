---
id: TC-AC-ACC-E2E-252-modal-changelog-subscription-screening-search-dan-download
title: "Modal Changelog: Subscription: Screening, Format Kolom Subscription, Search per Kolom, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-344
  - TC-AC-ACC-346
  - TC-AC-ACC-347
  - TC-AC-ACC-731
coverage:
  web: automated
---

# Modal Changelog: Subscription: Screening, Format Kolom Subscription, Search per Kolom, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Subscription).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): riwayat Changelog Subscription pada Client "PT Sejahtera Abadi": SL-01 (01 Jan 2026 08:00, Action `Add Subscription`, Subscription `<nama produk FAMS> — Professional`, Field `Plan`, Old Value `—`, New Value `Professional`, Modified By Andi Wijaya); SL-02 (20 Jun 2026 14:00, `Edit`, `<nama produk FAMS> — Professional`, `Duration`, `1 year(s)`, `2 year(s)`, Budi Santoso); SL-03 (05 Jul 2026 09:00, `Cancel Request`, `<nama produk SAMS> — Growth`, `Status`, `Waiting for Approval`, `Canceled`, Citra Dewi).
- Parameter blok TC-AC-ACC-346 (langkah 17 sampai 20):

| Kolom | Kata kunci | Baris tampil | Baris tidak tampil |
|---|---|---|---|
| Action | cancel | SL-03 | SL-01 |
| Subscription | professional | SL-01, SL-02 | SL-03 |
| Field | duration | SL-02 | SL-01 |
| Old Value | 1 year | SL-02 | SL-03 |
| New Value | 2 year | SL-02 | SL-01 |
| Modified By | citra | SL-03 | SL-01 |

- Kemampuan teknis: penangkapan nama berkas unduhan di browser uji (disediakan tim FE). Changelog adalah audit trail permanen: ukuran halaman 100 dan Search dipakai untuk baris seed (S-14); total baris tidak diasersi sebagai angka absolut (S-12).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Subscription

### TC-AC-ACC-344: Screening Modal Changelog: Subscription

2. Klik [Changelog]
3. Verifikasi Header: Title "Changelog: Subscription"
4. Verifikasi Toolbar: Search dengan placeholder "Search action, field, or value..."
5. Verifikasi Toolbar: `Filter` dan `Download` tampil
6. Verifikasi tabel memuat kolom `Date`, `Action`, `Subscription`, `Field`, `Old Value`, `New Value`, `Modified By`, `Column Visibility (⋯)`
7. Verifikasi urutan default Date terbaru
8. Verifikasi tabel read-only tanpa row action
9. Verifikasi Footer: Pagination dengan default 10 baris per halaman
10. Verifikasi opsi ukuran halaman 10, 25, 50, 100
11. Verifikasi modal berlebar 800 px dan tinggi hug content maksimum 648 px

### TC-AC-ACC-731: Kolom Subscription berformat Product — Plan

12. Ubah ukuran halaman modal menjadi 100 baris, ketik Search "Add Subscription", tekan Enter
13. Verifikasi sel Subscription baris SL-01 berpola "<nama produk> — Professional": nama produk subscription FAMS, spasi, em dash "—", spasi, Plan "Professional"
14. Verifikasi sel Subscription berupa teks biasa (bukan link)
15. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-346: Search per kolom

16. Klik ikon Search
17. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-346" (langkah 17 sampai 20): ketik kata kunci pada kolom Search, tekan Enter
18. Verifikasi baris pada kolom "Baris tampil" tampil
19. Verifikasi baris pada kolom "Baris tidak tampil" tidak tampil
20. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-347: Download Changelog: Subscription

21. Klik Download pada toolbar modal
22. Verifikasi overlay memuat opsi "Download as CSV" dan "Download as XLSX"
23. Klik "Download as CSV"
24. Verifikasi tidak ada toast sukses
25. Verifikasi berkas `Changelog-Subscription-PT Sejahtera Abadi.csv` terunduh
26. Klik Download lagi lalu klik "Download as XLSX"
27. Verifikasi tidak ada toast sukses
28. Verifikasi berkas `Changelog-Subscription-PT Sejahtera Abadi.xlsx` terunduh

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 12 (Search "Add Subscription" memperkecil baris audit trail ke baris seed SL-01, S-14), langkah 15 dan 20 (mengosongkan Search sebelum kata kunci berikutnya, S-09).
- Langkah 17 sampai 20 diulang untuk 6 baris tabel parameter (24 langkah setelah ekspansi). Urutan TC (344, 731, 346, 347) berbeda dari urutan nomor TC agar screening berada paling awal.
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (Modal Changelog: Subscription, baca-saja atas data seed) pada satu modal; Search dikosongkan di antara blok sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: Filter dan Sort Changelog: Subscription ada di spec 253; Setup Column di spec 256 sampai 260; empty state genuinely kosong di spec 261; SSE di spec 262.
- Temuan untuk QA:
  - TC-AC-ACC-344 mensyaratkan ">10 baris" riwayat Changelog sedangkan fixture SL-01 sampai SL-03 hanya tiga baris untuk "PT Sejahtera Abadi"; asersi pagination default 10 tetap diasersi sebagai elemen UI.
  - TC-AC-ACC-731 menulis nama produk sebagai "<nama produk>" tanpa nilai persis; spec mengasersi pola, bukan teks nama produk.
