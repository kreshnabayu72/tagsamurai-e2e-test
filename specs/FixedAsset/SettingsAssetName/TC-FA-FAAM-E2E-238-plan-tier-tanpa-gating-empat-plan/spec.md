---
id: TC-FA-FAAM-E2E-238-plan-tier-tanpa-gating-empat-plan
title: "Plan Tier: Menu dan Aksi Create-Edit-Delete Tanpa Gating pada Starter, Growth, Professional, dan Enterprise"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-674
coverage:
  web: automated
---

# Plan Tier: Menu dan Aksi Create-Edit-Delete Tanpa Gating pada Starter, Growth, Professional, dan Enterprise

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor default (hook `before`): Total Control client utama `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Halaman dibuka hook `beforeEach` suite. Langkah 1 pada tiap iterasi tabel mengganti akun dan client secara eksplisit; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Tabel "Client yang diuji" (Pre-setup No. 16d: empat client dengan plan Starter, Growth, Professional, Enterprise, katalog Asset Name di bawah kuota paket; email Total Control tiap client tidak tertulis di Pre-setup TC dan disediakan tim FE; spec dijalankan untuk setiap baris):

  | Plan | Akun Total Control | Env | Asset Name | Code |
  |---|---|---|---|---|
  | Starter | disediakan tim FE | `Spectra.env.FA_TIER_STARTER_TC_PASSWORD` | `Tier Item Starter {runId}-238` | `TIER-674` |
  | Growth | disediakan tim FE | `Spectra.env.FA_TIER_GROWTH_TC_PASSWORD` | `Tier Item Growth {runId}-238` | `TIER-674` |
  | Professional | disediakan tim FE | `Spectra.env.FA_TIER_PRO_TC_PASSWORD` | `Tier Item Professional {runId}-238` | `TIER-674` |
  | Enterprise | disediakan tim FE | `Spectra.env.FA_TIER_ENT_TC_PASSWORD` | `Tier Item Enterprise {runId}-238` | `TIER-674` |

- Env var: `FA_TC_PASSWORD`, `FA_TIER_STARTER_TC_PASSWORD`, `FA_TIER_GROWTH_TC_PASSWORD`, `FA_TIER_PRO_TC_PASSWORD`, `FA_TIER_ENT_TC_PASSWORD` (nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo).
- Data Dinamis (dibuat lewat UI pada tiap iterasi, dihapus oleh TC itu sendiri): Asset Name pada tabel di atas dengan TAG Type `QR`. Field wajib lain: Category `IT Equipment`, Brand `Dell`, UoM `Unit`; TC tidak menyebut nilai ini (lihat Temuan untuk QA).
- Kemampuan teknis: empat client dengan plan berbeda (disediakan tim BE/FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus Asset Name bersuffix `-238` yang tersisa pada empat client lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-674: login sebagai Total Control pada tiap client dan berada di Fixed Asset.

## Test Steps

Untuk setiap baris tabel "Client yang diuji" (langkah 1 sampai 18):

1. Logout lalu login sebagai Total Control pada client plan baris tabel
2. Buka Fixed Asset > Settings > Asset Master
3. Verifikasi menu `Settings > Asset Master` tampil
4. Klik `[+ Asset Name]`
5. Isi Asset Name pada baris tabel dengan TAG Type `QR` dan field wajib lain
6. Klik `[Submit]`
7. Verifikasi toast `Success, asset name has been created.`
8. Verifikasi tidak ada dialog upsell
9. Ketik Search Asset Name pada baris tabel, tekan Enter
10. Klik `⋯` baris Asset Name pada baris tabel lalu `Edit`
11. Ubah Code menjadi `TIER-674`
12. Klik `[Save]`
13. Verifikasi toast `Success, asset name has been updated.`
14. Verifikasi tidak ada dialog upsell
15. Klik `⋯` baris Asset Name pada baris tabel lalu `Delete`
16. Klik `[Delete]`
17. Verifikasi toast `Success, asset name has been deleted.`
18. Verifikasi tidak ada dialog upsell

## Notes

- Langkah 1 sampai 18 diulang untuk baris Starter, Growth, Professional, lalu Enterprise (ekspansi 72 langkah). Di atas ~35 karena alasan berikut: TC-FA-FAAM-674 sendiri adalah satu TC dengan empat parameter plan dan langkah identik, satu kelas harness (kelas h, plan tier), dan memecahnya per plan melanggar aturan satu TC satu spec. Parameter tiap iterasi hanya akun, client, dan nama Asset Name, ada di tabel Prerequisites.
- Langkah penghubung tanpa `Verifikasi`: langkah 2 (navigasi), langkah 9 (Search untuk menemukan baris target), langkah 1 (ganti akun dan client eksplisit; S-07).
- Langkah 8, 14, 18 adalah asersi absence dengan anchor toast sukses hasil server yang sudah diasersi pada langkah 7, 13, 17 (bagian 8b butir 2).
- Temuan untuk QA:
  - Pre-setup No. 16d tidak memuat email akun Total Control untuk empat client tier.
  - TC-FA-FAAM-674 tidak menyebut field wajib selain TAG Type pada Create; spec memakai Category `IT Equipment`, Brand `Dell`, UoM `Unit`.
  - TC-FA-FAAM-674 tidak menyebut teks toast; spec memakai toast sukses Create, Edit, dan Delete yang dikonfirmasi pada TC lain (`Success, asset name has been created.`, `Success, asset name has been updated.`, `Success, asset name has been deleted.`).
  - TC-FA-FAAM-674 tidak menyebut teks atau bentuk "dialog upsell"; spec mengasersi tidak ada dialog upsell tanpa teks.
