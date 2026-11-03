---
id: TC-AC-ACC-E2E-194-top-up-license-allocation-asset-dan-storage
title: "Top-up Asset License dan Storage dari License Allocation Tercermin di Detail Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-811
  - TC-AC-ACC-815
coverage:
  web: automated
---

# Top-up Asset License dan Storage dari License Allocation Tercermin di Detail Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data milik spec (kelas Dipulihkan pada TC, ditiru bersuffix): Client "PT Uji Top-up {runId}-194" di-seed hook `before` lewat Fixture BE (disediakan tim FE/BE) dengan atribut C-DTL-5 (Tabel A3): Direct, Group Cabang Menteng, FAMS Active Professional; License Quota FAMS Asset 100/10/90, Concurrent User 10/2/8; Purchase History License satu baris Professional / Fixed Asset / New / 12 months / Qty 100 / CV Mitra Sejati / Andi Wijaya; Storage Quota Total 50 GB, Used 10 GB (Files & Documents 10 GB, Unmanaged / Disposed Assets 0 GB), Available 40 GB; Purchase History Storage satu baris Qty (GB) 50. Top-up bersifat permanen sehingga hook `after` menghapus Client lewat API.
- Alasan data bersuffix: top-up mengubah kuota secara permanen sehingga tidak memakai fixture Pre-setup bersama C-DTL-5 (S-06, S-12).
- Kemampuan teknis: halaman Admin Console > License Allocation untuk melakukan top-up; akun Total Control. Suite berjalan serial (`parallel: false`).
- General Settings: Date Format dan Time Zone tenant uji tidak diubah (asersi tanggal mengikuti format General Settings).

## Test Steps

### TC-AC-ACC-811: Top-up Asset license menambah Total License Quota dan Purchase History tanpa mengubah kartu Subscription Details

1. Ketik Search `PT Uji Top-up {runId}-194`, tekan Enter
2. Klik Company Name "PT Uji Top-up {runId}-194" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`, lalu catat kartu Subscription Details (Subscription ID, Plan, Status badge, Start, End), baris Asset pada License Quota, dan tabel Purchase History License
4. Di Admin Console > License Allocation, lakukan top-up Asset license 50 ke Client "PT Uji Top-up {runId}-194"
5. Tunggu aksi selesai, lalu muat ulang Detail
6. Klik Tab `Subscription`, sub-tab `FAMS`
7. Verifikasi baris Asset pada License Quota menampilkan Total 150, Used 10, Available 140
8. Verifikasi Purchase History License memuat baris baru Purchase Type "Additional" Item "Fixed Asset" Qty 50 pada urutan paling atas
9. Verifikasi Purchase History License masih memuat baris Qty 100
10. Verifikasi Section "Subscription Details" tetap berisi satu kartu dengan Subscription ID, Plan, Status badge, Start, dan End yang sama seperti pada langkah 3

### TC-AC-ACC-815: Top-up Storage menambah Total Quota Storage dan Purchase History Storage

11. Klik Tab `Storage`, lalu lihat Quota dan tabel Purchase History Storage
12. Verifikasi Quota Storage menampilkan Total (GB) 50, Used (GB) 10, Available (GB) 40
13. Di Admin Console > License Allocation, lakukan top-up Type Storage 20 GB ke Client "PT Uji Top-up {runId}-194"
14. Tunggu aksi selesai, lalu muat ulang Detail
15. Klik Tab `Storage`, lalu lihat Quota dan tabel Purchase History Storage
16. Verifikasi Quota Storage menampilkan Total (GB) 70, Used (GB) 10, Available (GB) 60
17. Verifikasi sub-baris "Files & Documents" 10 GB dan "Unmanaged / Disposed Assets" 0 GB
18. Verifikasi Purchase History Storage memuat baris baru Qty (GB) 20 pada urutan paling atas
19. Verifikasi Purchase History Storage masih memuat baris Qty (GB) 50

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "catat kartu Subscription Details", "Tunggu aksi selesai", dan "muat ulang Detail" adalah langkah penghubung (S-03, bagian 8b butir 8). Aksi top-up pada Admin Console > License Allocation ditulis sesuai redaksi TC (langkah rinci modul License Allocation tidak ada di TC ini).
- Temuan untuk QA (S-15): kedua TC tidak menyebut kolom Date untuk urutan "paling atas" baris baru (diasumsikan sort default Date terbaru). Post Condition (reset fixture C-DTL-5) dipenuhi hook `after` karena Client milik spec dihapus.
