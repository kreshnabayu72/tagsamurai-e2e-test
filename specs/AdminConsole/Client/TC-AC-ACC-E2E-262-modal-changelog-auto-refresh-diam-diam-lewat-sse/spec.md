---
id: TC-AC-ACC-E2E-262-modal-changelog-auto-refresh-diam-diam-lewat-sse
title: "Tiga Modal Changelog: Auto-Refresh Diam-Diam lewat SSE saat Log Baru Masuk dari Sesi Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-343
  - TC-AC-ACC-348
  - TC-AC-ACC-353
coverage:
  web: automated
---

# Tiga Modal Changelog: Auto-Refresh Diam-Diam lewat SSE saat Log Baru Masuk dari Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor (pengamat modal Changelog): Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Pelaku kedua: sesi API aktor yang hanya memicu perubahan state (bukan sesi UI kedua, konvensi bagian 3 P-2 butir 2026-10-21 dan 2026-10-30); akun dan jenis aksi yang menghasilkan log baru di tiap modal tidak disebut TC dan disediakan tim FE (lihat Temuan untuk QA).
- Data Pre-setup (hanya dibaca oleh pengamat): Client C-01 "PT Sejahtera Abadi" (Tab Subscription dan Tab Asset Control) dengan riwayat Changelog lebih dari 10 baris (precondition TC).
- Tabel "Modal Changelog" (parameter blok; kolom `Cara buka` selalu dimulai dari menu Client di sidebar):

| Modal | Cara buka |
|---|---|
| Changelog: Client | Klik menu Client di sidebar, lalu klik [Changelog] di toolbar List |
| Changelog: Subscription | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Subscription, lalu klik [Changelog] |
| Changelog: Asset Control | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Asset Control, lalu klik ikon Changelog |

- Kemampuan teknis: pemicu aksi lewat sesi API aktor yang menghasilkan satu baris log baru pada surface modal (data unik bersuffix `{runId}-262`, disediakan tim FE); pembacaan total baris Pagination modal sebagai baseline (S-12; total tidak diasersi sebagai angka absolut).
- State global: aksi pemicu menambah baris audit trail permanen; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-343, TC-AC-ACC-348, dan TC-AC-ACC-353: Auto-refresh diam-diam lewat SSE (Client, Subscription, Asset Control)

1. Untuk setiap baris tabel "Modal Changelog" (langkah 1 sampai 8; TC-AC-ACC-343 untuk Changelog: Client, TC-AC-ACC-348 untuk Changelog: Subscription, TC-AC-ACC-353 untuk Changelog: Asset Control): buka modal sesuai kolom "Cara buka"
2. Catat halaman aktif tabel modal, posisi scroll tabel, dan total baris pada Pagination (baseline B)
3. Pelaku kedua (sesi API) menjalankan aksi yang menghasilkan satu baris log baru pada surface modal hingga baris log tersimpan
4. Verifikasi baris log baru masuk ke tabel modal tanpa memuat ulang halaman
5. Verifikasi baris baru ditempatkan in-place sesuai sort dan filter yang aktif
6. Verifikasi total baris pada Pagination = B + 1
7. Verifikasi halaman aktif dan posisi scroll tabel tidak berubah
8. Tutup modal Changelog

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): "Cara buka" tiap modal (menu Client di sidebar, Search dan buka Detail Client; hook suite hanya membuka List Client dan klik sidebar mereset Search), langkah 8 (menutup modal).
- Langkah 1 sampai 8 diulang 3 kali (24 langkah setelah ekspansi): iterasi 1 memetakan TC-AC-ACC-343, iterasi 2 TC-AC-ACC-348, iterasi 3 TC-AC-ACC-353. Ketiga TC identik kecuali surface; digabung sebagai satu blok berulang.
- Langkah 6 (selisih total Pagination terhadap baseline) adalah penanda baris baru yang ditambahkan (S-12); Expected TC hanya menyebut "entry baru masuk in-place sesuai sort/filter aktif tanpa mengganggu posisi scroll/halaman".
- Temuan untuk QA:
  - TC-AC-ACC-343, 348, dan 353 menyebut "Dari sesi lain lakukan aksi yang menghasilkan log baru" tanpa menyebut aksi, akun pelaku, dan durasi propagasi SSE; spec memakai sesi API pelaku kedua yang disediakan tim FE. Bila TC bermaksud sesi UI kedua sebagai objek asersi, TC perlu menyatakannya.
  - TC-AC-ACC-343, 348, 353 tidak menyebut sort/filter aktif yang harus diuji; spec memakai keadaan default modal.
