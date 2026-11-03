---
id: TC-AC-DS-E2E-182-plan-tier-register-edit-delete-identik
title: "Plan Tier: Register, Edit, dan Delete Berperilaku Identik pada Starter, Growth, Professional, dan Enterprise"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-559
coverage:
  web: automated
---

# Plan Tier: Register, Edit, dan Delete Berperilaku Identik pada Starter, Growth, Professional, dan Enterprise

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada empat Principal uji ber-plan Starter, Growth, Professional, dan Enterprise (Pre-setup #41). Email dan env var password akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kredensial disediakan tim FE. Akun Starter login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun plan berikutnya login di akhir iterasi sebelumnya (ganti akun eksplisit). Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37), empat Principal uji per plan (#41).
- Data Dinamis (kode literal pada Tabel Data Uji Dinamis TC): SKU `PLAN-STR-01`, `PLAN-GRW-01`, `PLAN-PRO-01`, `PLAN-ENT-01` (Data Dinamis #38); dibuat lalu dihapus dalam iterasi masing-masing; hook `before` menghapus sisa kode itu bila ada dan hook `after` menghapusnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Tabel "Plan yang diuji":

  | Plan | SKU | Akun berikutnya |
  |---|---|---|
  | Starter | `PLAN-STR-01` | Total Control Principal ber-plan Growth |
  | Growth | `PLAN-GRW-01` | Total Control Principal ber-plan Professional |
  | Professional | `PLAN-PRO-01` | Total Control Principal ber-plan Enterprise |
  | Enterprise | `PLAN-ENT-01` | Total Control Principal default suite (`totalControlSku`, `Spectra.env.AC_DS_TC_PASSWORD`) |

## Test Steps

### TC-AC-DS-559: Register, Edit, dan Delete SKU berperilaku identik pada plan Starter, Growth, Professional, dan Enterprise

1. Untuk setiap baris tabel "Plan yang diuji" pada Prerequisites, lakukan langkah 2 sampai 13 dengan urutan Starter, Growth, Professional, Enterprise
2. Klik `[+ SKU]` lalu isi SKU kolom "SKU" (Asset TAG, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-PL`, foto `foto-a.jpg`)
3. Klik `[Submit]`
4. Verifikasi muncul toast sukses: "Success, device SKU has been registered." tanpa dialog upsell dan tanpa pembatasan fitur
5. Ketik Search kolom "SKU", tekan Enter, klik ⋯ pada baris SKU lalu pilih `Edit`
6. Ubah Model/Type menjadi `T-PL2`
7. Klik `[Save]`
8. Verifikasi muncul toast sukses: "Success, device SKU has been updated." tanpa dialog upsell dan tanpa pembatasan fitur
9. Klik ⋯ pada baris SKU lalu pilih `Delete`
10. Klik `[Delete]`
11. Verifikasi muncul toast sukses: "Success, device SKU has been deleted." tanpa dialog upsell dan tanpa pembatasan fitur
12. Verifikasi UI Register, Edit, dan Delete pada plan ini identik dengan plan lain
13. Klik `(←)` pada kotak Search, Logout, lalu login sebagai akun kolom "Akun berikutnya" dan buka halaman `Settings > Device > Device SKU`

## Notes

- Perulangan per baris tabel Prerequisites dipakai karena alur tiap plan identik (8b butir 7); langkah 2 sampai 13 diulang empat kali. Spec berada di atas sekitar 35 langkah pada hitungan ekspansi; alasan: seluruhnya satu kelas harness (h) dengan alur identik per plan dan berdiri sendiri.
- Langkah penghubung tanpa `Verifikasi`: Search kolom "SKU" (menemukan baris target, R-16), `(←)` pada Search, dan ganti akun ke plan berikutnya (hook `after` memulihkan sesi ke akun default suite).
- Expected TC 559 menulis tiga toast, tanpa dialog upsell, tanpa pembatasan fitur, dan UI identik dalam satu butir per plan; spec memecah per klausa: toast dan dua klausa "tanpa ..." digabung pada satu `Verifikasi` per toast sebagai satu elemen, dan klausa UI identik sebagai `Verifikasi` tersendiri.
- Temuan untuk QA:
  - S-15/S-11: Pre-setup #41 tidak memberi email dan env var untuk empat akun Total Control per plan; spec menulis "disediakan tim FE" tanpa mengarang nama.
  - Asersi "UI identik dengan plan lain" tidak punya pembanding operasional di TC; spec mengasersinya per iterasi tanpa pembanding tambahan.
  - Plan tier diubah oleh akun pelaku yang tidak disebut TC; spec memakai empat Principal uji yang sudah ber-plan, bukan mengubah plan.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
