---
id: TC-AC-DS-E2E-179-state-tenant-edit-ditolak-suspended-expired
title: "State Tenant: Edit SKU oleh Distributor Suspended dan Expired Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-533
  - TC-AC-DS-537
coverage:
  web: automated
---

# State Tenant: Edit SKU oleh Distributor Suspended dan Expired Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Bahari Teknik, Suspended (Hendra Saputra, Modified By `Hendra S`): `totalControlDistSusp_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTSUSP_PASSWORD` (Pre-setup #18). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (di akhir iterasi sebelumnya): Total Control Distributor PT Kencana Daya, Expired (Maya Anggraini, Modified By `Maya A`): `totalControlDistExp_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTEXP_PASSWORD` (Pre-setup #19).
- Kemampuan baca (disediakan tim FE/BE): jumlah entri Changelog, System Log aktor, dan Activity Log tab User Action dicatat sebagai baseline sebelum aksi pemicu; audit trail permanen sehingga asersi memakai selisih terhadap baseline (S-12).
- State global: status entitas (Suspended, Expired) adalah state Pre-setup dan tidak diubah spec. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Pre-setup (hanya dibaca): SKU inti dan seed (#29, #30), SKU lokal Distributor Suspended `BAH-LOC-01` (Model/Type `B-01`) dan Expired `KEN-LOC-01` (Model/Type `K-01`) (#18, #19).
- Data Dinamis: tidak ada; tidak ada perubahan yang boleh tersimpan.
- Tabel "Entitas diuji":

  | TC | Akun | User aktor | SKU | Model/Type tersimpan | Akun berikutnya |
  |---|---|---|---|---|---|
  | 533 | #18 Distributor Suspended | `totalControlDistSusp_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hendra Saputra`) | `BAH-LOC-01` | `B-01` | #19 (`totalControlDistExp`, `Spectra.env.AC_DS_DISTEXP_PASSWORD`) |
  | 537 | #19 Distributor Expired | `totalControlDistExp_automated_{namaCompany}@qwertysystem.net` (nama tampil `Maya Anggraini`) | `KEN-LOC-01` | `K-01` | #1 (`totalControlSku`, `Spectra.env.AC_DS_TC_PASSWORD`) |

## Test Steps

### TC-AC-DS-533 dan TC-AC-DS-537: Edit SKU oleh Distributor Suspended dan Distributor Expired ditolak dengan toast entitas tidak aktif

1. Untuk setiap baris tabel "Entitas diuji" pada Prerequisites, lakukan langkah 2 sampai 18 dengan urutan baris 533 lalu 537
2. Klik ikon Changelog, catat jumlah entri sebagai baseline N_CL, lalu tutup modal
3. Buka Settings > User, pilih user kolom "User aktor", buka Detail lalu tab System Log, catat jumlah entri sebagai baseline N_SL
4. Buka Activity Log lalu tab User Action, catat jumlah entri sebagai baseline N_AL
5. Buka halaman `Settings > Device > Device SKU`, ketik Search kolom "SKU", tekan Enter, klik ⋯ pada baris SKU lalu pilih `Edit`
6. Ubah Model/Type menjadi `H-S2`
7. Klik `[Save]`
8. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
9. Kembalikan Model/Type ke nilai kolom "Model/Type tersimpan", tutup popup dengan `[✕]`, lalu tutup toast
10. Buka tab browser baru dengan sesi aktor yang sama lalu buka halaman `Settings > Device > Device SKU`, ketik Search kolom "SKU", tekan Enter
11. Verifikasi badge Model/Type baris SKU tetap sama dengan kolom "Model/Type tersimpan"
12. Klik ikon Changelog
13. Verifikasi jumlah entri Changelog sama dengan baseline N_CL (tidak ada entri baru)
14. Buka Settings > User, pilih user kolom "User aktor", buka Detail lalu tab System Log
15. Verifikasi jumlah entri System Log sama dengan baseline N_SL (tidak ada entri baru)
16. Buka Activity Log lalu tab User Action
17. Verifikasi jumlah entri Activity Log tab User Action sama dengan baseline N_AL (tidak ada entri baru)
18. Tutup tab baru, Logout, lalu login sebagai akun kolom "Akun berikutnya" dan buka halaman `Settings > Device > Device SKU`

## Notes

- Perulangan per baris tabel Prerequisites dipakai karena alur tiap entitas identik (8b butir 7); langkah 2 sampai 18 diulang untuk baris 533 dan 537. Ganti akun ke baris berikutnya adalah langkah eksplisit di akhir iterasi (hook `after` memulihkan sesi ke akun default suite).
- Langkah penghubung tanpa `Verifikasi`: pencatatan baseline, Search untuk menemukan baris target (R-16), pengembalian field dirty ke nilai tersimpan sebelum menutup popup (S-09), dan pembukaan tab baru.
- Spec berada di atas sekitar 35 langkah pada hitungan ekspansi; alasan: semua blok satu kelas harness (h) dengan alur identik per entitas dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah pembacaan Changelog, System Log, dan Activity Log berpola (buka surface, bandingkan dengan baseline) dihitung sebagai blok baca-log.
- Temuan untuk QA:
  - Absence log (Changelog, System Log, Activity Log tidak memuat entri baru) diasersi di spec ini dengan baseline (S-05, `P-5` tidak dipakai karena spec ini kelas h, bukan spec absence kelas g); tidak ada spec absence yang memuat aksi TC ini, sehingga Expected TC tidak boleh hanya dirujuk. Butuh keputusan bila konvensi menghendaki pemindahan ke spec absence.
  - Entitas Pre-setup #18, #19, #20 (nama tampil, Model/Type `B-01`/`K-01`, SKU `EXP-PRI-01`) adalah data rancangan yang belum terverifikasi ada di environment.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
