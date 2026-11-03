---
id: TC-AC-ACC-E2E-191-quota-detail-mengikuti-perubahan-fams-asset-tag-dan-storage
title: "Quota Detail Client Mengikuti Perubahan di FAMS: Used Asset dan TAG Bertambah, Footprint Storage Berkurang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-286
  - TC-AC-ACC-810
  - TC-AC-ACC-301
coverage:
  web: automated
---

# Quota Detail Client Mengikuti Perubahan di FAMS: Used Asset dan TAG Bertambah, Footprint Storage Berkurang

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dipulihkan pada TC, ditiru bersuffix): Client "PT Uji Top-up {runId}-191" di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE) dengan atribut C-DTL-5 (Tabel A3): Direct, Group Cabang Menteng, FAMS Active Professional; License Quota FAMS Asset 100/10/90 (Total/Used/Available), Concurrent User 10/2/8; TAG Quota RFID 20/5/15. Hook `after` menghapus aset dan TAG uji di tenant FAMS lalu Client lewat API.
- Data milik spec untuk TC-301 (kelas Dikonsumsi pada TC, ditiru bersuffix): Client "PT Footprint Uji {runId}-191" di-seed hook `before` lewat Fixture BE (atribut C-ISO-12: FAMS Active; Storage Total 50 GB / Used 20 GB (Files & Documents 10 GB + Unmanaged / Disposed Assets 10 GB) / Available 30 GB; aset Unmanaged "Forklift Uji" 10 GB di FAMS; Partner CV Mitra Sejati; Group Area Jakarta). Hook `after` menghapus sisa aset dan Client lewat API.
- Alasan data bersuffix: ketiga TC menambah atau menghapus aset/TAG di FAMS (aksi tulis) sehingga tidak memakai fixture Pre-setup bersama C-01, C-DTL-5, atau C-ISO-12 (S-06, S-12).
- Kemampuan teknis (kelas d, harness produk eksternal FAMS): mendaftarkan satu aset dan satu TAG baru di tenant FAMS Client uji; disediakan tim FE/BE tanpa endpoint karangan (S-13). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACC-810: Used Asset pada License Quota bertambah setelah FAMS mendaftarkan aset baru

1. Ketik Search `PT Uji Top-up {runId}-191`, tekan Enter
2. Klik Company Name "PT Uji Top-up {runId}-191" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat baris Asset pada License Quota
4. Verifikasi baris Asset menampilkan Total 100, Used 10, Available 90
5. Di FAMS tenant "PT Uji Top-up {runId}-191", daftarkan satu aset baru
6. Tunggu aksi selesai, lalu muat ulang Detail
7. Klik Tab `Subscription`, sub-tab `FAMS`, lalu lihat baris Asset pada License Quota
8. Verifikasi baris Asset menampilkan Total 100, Used 11, Available 89

### TC-AC-ACC-286: Used TAG di-sync dari FAMS/SAMS

9. Klik Tab `TAG`, lalu catat Used dan Available baris RFID pada tabel Quota
10. Di FAMS tenant "PT Uji Top-up {runId}-191", daftarkan satu TAG baru
11. Tunggu aksi selesai, lalu muat ulang Tab `TAG`
12. Verifikasi Used baris RFID bertambah sesuai hasil sinkronisasi terakhir dari nilai yang dicatat pada langkah 9
13. Verifikasi Available = Total − Used pada baris RFID

### TC-AC-ACC-301: Footprint Storage berkurang setelah aset Unmanaged/Disposed di-Delete

14. Kembali ke List lewat breadcrumb Client
15. Ganti isi Search dengan `PT Footprint Uji {runId}-191`, tekan Enter
16. Klik Company Name "PT Footprint Uji {runId}-191" untuk membuka Detail
17. Klik Tab `Storage`, lalu lihat baris Used dan sub-barisnya
18. Verifikasi baris Used menampilkan Used 20 GB dengan sub-baris "Files & Documents" 10 GB dan "Unmanaged / Disposed Assets" 10 GB
19. Di FAMS tenant "PT Footprint Uji {runId}-191", Delete aset Unmanaged "Forklift Uji"
20. Tunggu aksi selesai, lalu muat ulang Tab `Storage` dan lihat baris Used dan sub-barisnya
21. Verifikasi baris Used menampilkan Used 10 GB
22. Verifikasi sub-baris "Files & Documents" 10 GB dan "Unmanaged / Disposed Assets" 0 GB

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "catat Used dan Available" (TC-286) dan "Tunggu aksi selesai" adalah langkah penghubung (bagian 8b butir 8).
- Pembagian TC lintas spec: sinkronisasi Used lewat push dan rekonsiliasi harian saat push terlewat (TC-816) ada di spec lain; id TC masing-masing tetap satu spec.
- Temuan untuk QA (S-15): TC-301 meminta Delete aset Unmanaged di FAMS tanpa langkah rinci (Manual Only (b) lintas produk FAMS); spec mengikuti redaksi TC. TC-286 Precondition menyebut Detail "PT Sejahtera Abadi" (C-01) tanpa menyebut baris TAG; Expected "Used bertambah sesuai hasil sinkronisasi terakhir" tidak menyebut nilai pasti, sehingga spec membandingkan terhadap nilai yang dicatat sebelum aksi. TC-286 dan TC-810 menyebut tombol aksi di FAMS tanpa langkah rinci; spec mengikuti redaksi TC. Post Condition TC-810 (hapus aset uji sehingga Used kembali 10) dipenuhi hook `after` yang menghapus Client milik spec.
