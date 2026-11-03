---
id: TC-AC-ACC-E2E-261-modal-changelog-empty-state-genuinely-kosong-dan-hasil-search-kosong
title: "Tiga Modal Changelog: Empty State Genuinely Kosong dan Hasil Search Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-340
  - TC-AC-ACC-345
  - TC-AC-ACC-350
coverage:
  web: automated
---

# Tiga Modal Changelog: Empty State Genuinely Kosong dan Hasil Search Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite. Akun kedua (langkah ganti akun, hanya untuk TC-AC-ACC-340 butir a): Total Control pada tenant tanpa riwayat Changelog Client; akun dan tenant ini tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA), password `Spectra.env.AC_CLIENT_TC_EMPTY_TENANT_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" dengan riwayat Changelog Client (fixture L-01 sampai L-09), Changelog Subscription (SL-01 sampai SL-03), dan Changelog Asset Control (AL-01 sampai AL-03) untuk butir hasil Search kosong.
- Data Dinamis milik spec (dibuat lewat API seeding di hook `before`, dihapus di `after`): Client "PT Changelog Kosong {runId}-261" tanpa riwayat subscription dan tanpa riwayat Asset Control sehingga Changelog: Subscription dan Changelog: Asset Control miliknya genuinely kosong (TC memakai "PT Baru Daftar" Pre-setup C-09, yang dipakai juga untuk Delete di spec lain).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-345: Empty state Modal Changelog: Subscription

1. Ketik Search "PT Changelog Kosong {runId}-261" di List Client, tekan Enter, klik Company Name hasilnya, klik Tab Subscription, lalu klik [Changelog]
2. Verifikasi empty state genuinely kosong: Illustration dengan Title "No changelog yet" dan Description "Subscription changes and history will appear here."
3. Tutup modal, klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Subscription, lalu klik [Changelog]
4. Klik ikon Search, ketik "zzzz", lalu tekan Enter
5. Verifikasi empty state hasil Search kosong: Title "No results found" dan Description "Try adjusting your search or filter."
6. Klik ikon ✕ pada input Search lalu tekan Enter, lalu tutup modal

### TC-AC-ACC-350: Empty state Modal Changelog: Asset Control

7. Klik menu Client di sidebar, ketik Search "PT Changelog Kosong {runId}-261", tekan Enter, klik Company Name hasilnya, klik Tab Asset Control, lalu klik ikon Changelog
8. Verifikasi empty state genuinely kosong: Illustration dengan Title "No changelog yet" dan Description "Asset control activities and changes will appear here."
9. Tutup modal, klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Asset Control, lalu klik ikon Changelog
10. Klik ikon Search, ketik "zzzz", lalu tekan Enter
11. Verifikasi empty state hasil Search kosong: Title "No results found" dan Description "Try adjusting your search or filter."
12. Klik ikon ✕ pada input Search lalu tekan Enter, lalu tutup modal

### TC-AC-ACC-340: Empty state Modal Changelog: Client

13. Klik menu Client di sidebar, lalu klik [Changelog] di toolbar List
14. Klik ikon Search, ketik "zzzz", lalu tekan Enter
15. Verifikasi empty state hasil Search kosong: Title "No results found" dan Description "Try adjusting your search or filter."
16. Klik ikon ✕ pada input Search lalu tekan Enter, lalu tutup modal
17. Logout, lalu login sebagai Total Control pada tenant tanpa riwayat Changelog Client
18. Klik [Changelog] di toolbar List
19. Verifikasi empty state genuinely kosong: Illustration dengan Title "No changelog yet" dan Description "Activities and changes will appear here."

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): "Search dan buka Detail Client" pada langkah 1, 3, 7, 9 (hook suite hanya membuka List Client dan klik sidebar mereset Search), langkah 6, 12, 16 (mengosongkan Search dan menutup modal).
- Urutan butir di dalam TC-AC-ACC-340 dibalik (hasil Search kosong pada langkah 13 sampai 16 lebih dulu, genuinely kosong pada langkah 17 sampai 19 sesudah ganti akun) agar ganti akun berada di akhir spec; Expected tidak bergantung pada urutan. Urutan TC (345, 350, 340) berbeda dari urutan nomor TC dengan alasan yang sama.
- Temuan untuk QA:
  - TC-AC-ACC-340 butir a mensyaratkan "Tidak ada riwayat Changelog" pada seluruh Changelog: Client, yang tidak dapat dipertahankan di tenant bersama karena Changelog adalah audit trail permanen dan spec lain menambah baris; spec memakai tenant terpisah tanpa riwayat yang disediakan tim FE (akun dan tenant belum didefinisikan di Pre-setup).
  - TC-AC-ACC-345 dan 350 memuat dua kondisi (genuinely kosong dan "pada data yang ada") pada satu Client "PT Baru Daftar"; hasil Search kosong memerlukan data, sehingga spec memakai dua Client (Client milik spec untuk genuinely kosong, "PT Sejahtera Abadi" untuk Search kosong).
