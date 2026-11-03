---
id: TC-AC-DS-E2E-178-state-tenant-register-ditolak-suspended-expired
title: "State Tenant: Register SKU oleh Distributor Suspended, Distributor Expired, dan Principal Expired Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-532
  - TC-AC-DS-536
  - TC-AC-DS-540
coverage:
  web: automated
---

# State Tenant: Register SKU oleh Distributor Suspended, Distributor Expired, dan Principal Expired Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Bahari Teknik, Suspended (Hendra Saputra, Modified By `Hendra S`): `totalControlDistSusp_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTSUSP_PASSWORD` (Pre-setup #18). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (di akhir iterasi sebelumnya): Total Control Distributor PT Kencana Daya, Expired (Maya Anggraini, Modified By `Maya A`): `totalControlDistExp_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTEXP_PASSWORD` (Pre-setup #19).
- Akun ganti akun (di akhir iterasi sebelumnya): Total Control Principal Kedaluwarsa, Expired: `totalControlPrincipalExp_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_PRIEXP_PASSWORD` (Pre-setup #20).
- Kemampuan baca (disediakan tim FE/BE): jumlah entri Changelog, System Log aktor, dan Activity Log tab User Action dicatat sebagai baseline sebelum aksi pemicu; audit trail permanen sehingga asersi memakai selisih terhadap baseline (S-12).
- State global: status entitas (Suspended, Expired) adalah state Pre-setup dan tidak diubah spec. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Pre-setup (hanya dibaca): pohon Category (#25), Device Name (#26), Brand Distributor (#28), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37).
- Data Dinamis (kode literal; tidak boleh tersimpan): `NEW-SUS-01`, `NEW-EXP-01`, `NEW-PEX-01`. Hook `after` memastikan tidak ada.
- Tabel "Entitas diuji" (parameter tiap iterasi):

  | TC | Akun | User aktor | SKU | Brand | Model/Type | Akun berikutnya |
  |---|---|---|---|---|---|---|
  | 532 | #18 Distributor Suspended | `totalControlDistSusp_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hendra Saputra`) | `NEW-SUS-01` | `Nordik` | `T-S1` | #19 (`totalControlDistExp`, `Spectra.env.AC_DS_DISTEXP_PASSWORD`) |
  | 536 | #19 Distributor Expired | `totalControlDistExp_automated_{namaCompany}@qwertysystem.net` (nama tampil `Maya Anggraini`) | `NEW-EXP-01` | `Nordik` | `T-S1` | #20 (`totalControlPrincipalExp`, `Spectra.env.AC_DS_PRIEXP_PASSWORD`) |

## Test Steps

### TC-AC-DS-532 dan TC-AC-DS-536: Register SKU oleh Distributor Suspended dan Distributor Expired ditolak dengan toast entitas tidak aktif

1. Untuk setiap baris tabel "Entitas diuji" pada Prerequisites, lakukan langkah 2 sampai 20 dengan urutan baris 532 lalu 536
2. Klik ikon Changelog, catat jumlah entri sebagai baseline N_CL, lalu tutup modal
3. Buka Settings > User, pilih user kolom "User aktor", buka Detail lalu tab System Log, catat jumlah entri sebagai baseline N_SL
4. Buka Activity Log lalu tab User Action, catat jumlah entri sebagai baseline N_AL
5. Buka halaman `Settings > Device > Device SKU`
6. Klik `[+ SKU]` lalu isi SKU kolom "SKU" (Asset TAG, Device Name `Asset TAG`, Brand kolom "Brand", Model/Type kolom "Model/Type", foto `foto-a.jpg`)
7. Klik `[Submit]`
8. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
9. Klik `[Clear Field]` lalu tutup popup dengan `[✕]`, lalu tutup toast
10. Buka tab browser baru dengan sesi aktor yang sama lalu buka halaman `Settings > Device > Device SKU`
11. Klik ikon Search, ketik kolom "SKU", tekan Enter
12. Verifikasi Search menampilkan "No results found" (tidak ada SKU baru)
13. Klik ikon Changelog
14. Verifikasi jumlah entri Changelog sama dengan baseline N_CL (tidak ada entri baru)
15. Buka Settings > User, pilih user kolom "User aktor", buka Detail lalu tab System Log
16. Verifikasi jumlah entri System Log sama dengan baseline N_SL (tidak ada entri baru)
17. Buka Activity Log lalu tab User Action
18. Verifikasi jumlah entri Activity Log tab User Action sama dengan baseline N_AL (tidak ada entri baru)
19. Verifikasi Read tetap berjalan: List dan Changelog tetap dapat dibuka
20. Tutup tab baru, Logout, lalu login sebagai akun kolom "Akun berikutnya" dan buka halaman `Settings > Device > Device SKU`

### TC-AC-DS-540: Register SKU oleh Principal Expired ditolak dengan toast entitas tidak aktif

21. Klik `[+ SKU]` lalu isi SKU `NEW-PEX-01` (Asset TAG, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-PE`, foto `foto-a.jpg`)
22. Klik `[Submit]`
23. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
24. Klik `[Clear Field]` lalu tutup popup dengan `[✕]`, lalu tutup toast
25. Buka tab browser baru dengan sesi aktor yang sama lalu buka halaman `Settings > Device > Device SKU`
26. Verifikasi List tetap dapat dibaca
27. Klik ikon Search, ketik `NEW-PEX-01`, tekan Enter
28. Verifikasi Search `NEW-PEX-01` menampilkan "No results found" (tidak ada SKU baru)

## Notes

- Perulangan per baris tabel Prerequisites dipakai karena alur tiap entitas identik (8b butir 7); langkah 2 sampai 20 diulang untuk baris 532 dan 536. Ganti akun ke baris berikutnya adalah langkah eksplisit di akhir iterasi (hook `after` memulihkan sesi ke akun default suite).
- Langkah penghubung tanpa `Verifikasi`: pencatatan baseline, `[Clear Field]` lalu `[✕]` (popup bersih sehingga tidak ada dialog `Unsaved Changes`), penutupan toast, dan pembukaan tab baru.
- Spec berada di atas sekitar 35 langkah pada hitungan ekspansi; alasan: semua blok satu kelas harness (h) dengan alur identik per entitas dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah pembacaan Changelog, System Log, dan Activity Log berpola (buka surface, bandingkan dengan baseline) dihitung sebagai blok baca-log.
- Temuan untuk QA:
  - Absence log (Changelog, System Log, Activity Log tidak memuat entri baru) diasersi di spec ini dengan baseline (S-05, `P-5` tidak dipakai karena spec ini kelas h, bukan spec absence kelas g); tidak ada spec absence yang memuat aksi TC ini, sehingga Expected TC tidak boleh hanya dirujuk. Butuh keputusan bila konvensi menghendaki pemindahan ke spec absence.
  - TC 540 tidak mengamati log; spec mengikuti TC. Tab baru pada TC 532, 536, dan 540 dipakai sesuai TC untuk membaca state dari sesi yang sama.
  - Entitas Pre-setup #18, #19, #20 (nama tampil, Model/Type `B-01`/`K-01`, SKU `EXP-PRI-01`) adalah data rancangan yang belum terverifikasi ada di environment.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
