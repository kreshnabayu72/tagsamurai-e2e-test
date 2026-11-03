---
id: TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download
title: "Tab Storage: Screening Quota, Breakdown Used, Read-only, Filter Panel, Download, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-298
  - TC-AC-ACC-299
  - TC-AC-ACC-302
  - TC-AC-ACC-303
  - TC-AC-ACC-786
  - TC-AC-ACC-300
  - TC-AC-ACC-304
coverage:
  web: automated
---

# Tab Storage: Screening Quota, Breakdown Used, Read-only, Filter Panel, Download, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi" (Storage Total 100 GB, Used 40 GB = file/dokumen 25 GB + footprint Unmanaged/Disposed 15 GB). Seed Purchase History Storage (F6): Storage P-S1 (Qty 60 GB / CV Mitra Sejati / Andi Wijaya / 01 Jan 2026 08:00), P-S2 (25 GB / PT Distribusi Nusantara / Budi Santoso / 10 Apr 2026 13:00), P-S3 (15 GB / CV Mitra Sejati / Citra Dewi / 25 Sep 2026 09:00). C-09 "PT Baru Daftar" (tanpa subscription dan tanpa kuota). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: pembacaan berkas unduhan (nama berkas CSV dan XLSX) oleh browser; tidak memeriksa isi berkas.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-298: Screening Tab Storage

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Storage`
4. Verifikasi tab aktif `Storage`
5. Verifikasi Quota berkolom `Total (GB) | Used (GB) | Available (GB)` satu baris
6. Verifikasi sub-baris breakdown tampil di bawah Used
7. Verifikasi Purchase History Storage memiliki toolbar Search dengan placeholder "Search by source or action by...", Filter, dan Download
8. Verifikasi Purchase History Storage berkolom `Qty (GB) | Source | Action by | Date`
9. Verifikasi Pagination tampil di footer

### TC-AC-ACC-299: Storage: Used = file/dokumen + footprint Unmanaged/Disposed; Available = Total − Used

10. Lihat Quota Storage "PT Sejahtera Abadi"
11. Verifikasi Total 100 GB
12. Verifikasi Used 40 GB dengan dua sub-baris menjorok di bawah Used: "Files & Documents" `25 GB` dan "Unmanaged / Disposed Assets" `15 GB`
13. Verifikasi Available 60 GB

### TC-AC-ACC-302: Tab Storage read-only; top-up lewat License Allocation

14. Periksa Tab `Storage`
15. Verifikasi tidak ada aksi write pada Tab `Storage`

### TC-AC-ACC-303: Screening Filter Purchase History Storage: label, placeholder, dan urutan awal Date Newest First

16. Lihat urutan awal baris Purchase History Storage
17. Verifikasi urutan awal (Newest First): P-S3 (Qty 15), P-S2 (Qty 25), P-S1 (Qty 60)
18. Klik Filter pada toolbar Purchase History Storage
19. Verifikasi Qty: field range dengan placeholder "Min" dan "Max"
20. Verifikasi Source: dropdown multi-select searchable, placeholder "All sources"
21. Verifikasi Date: date range picker satu field, placeholder "Select date"
22. Verifikasi Action by: dropdown multi-select searchable, placeholder "All users"
23. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
24. Klik ulang icon Filter untuk menutup panel Filter

### TC-AC-ACC-786: Download Purchase History Storage: toolbar Download dan nama file untuk CSV dan XLSX

25. Lihat toolbar Section Purchase History Storage
26. Verifikasi toolbar Section Purchase History Storage memuat Search, Filter, dan Download
27. Klik Download pada toolbar Purchase History Storage
28. Verifikasi overlay memuat opsi "Download as CSV" dan "Download as XLSX"
29. Klik "Download as CSV"
30. Verifikasi tidak ada toast sukses
31. Verifikasi berkas `Purchase-Storage-PT Sejahtera Abadi.csv` terunduh
32. Klik Download pada toolbar Purchase History Storage lagi, lalu klik "Download as XLSX"
33. Verifikasi berkas `Purchase-Storage-PT Sejahtera Abadi.xlsx` terunduh

### TC-AC-ACC-300 dan TC-AC-ACC-304: Tab Storage Client tanpa subscription dan tanpa kuota

34. Kembali ke List lewat breadcrumb Client
35. Ganti isi Search dengan `PT Baru Daftar`, tekan Enter
36. Klik Company Name "PT Baru Daftar" untuk membuka Detail (Client tanpa subscription)
37. Verifikasi navigasi tab memuat Tab `Storage` (tab selalu tampil tanpa dipengaruhi plan, addon, atau subscription)
38. Klik Tab `Storage`
39. Verifikasi Quota Storage menampilkan Total (GB) 0, Used (GB) 0, Available (GB) 0
40. Verifikasi empty state kuota tidak tampil
41. Verifikasi Purchase History Storage menampilkan "No purchase history yet" dan "Storage quota purchase history will appear here."

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan satu tab pada satu role, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Klik ulang icon Filter untuk menutup panel (D-001) adalah langkah penghubung (S-03). TC-300 dan TC-304 memakai Client yang sama (PT Baru Daftar) sehingga satu pembukaan; Expected TC-300 "Tab Storage tampil" diasersi pada navigasi tab dan Expected TC-304 pada isi Tab `Storage`.
- Temuan untuk QA (S-15): TC-300 Expected "Tab Storage tampil; empty state bila tanpa kuota" bertentangan dengan TC-304 (Client yang sama "PT Baru Daftar": Quota Total/Used/Available 0 dan "empty state kuota tidak tampil", hanya Purchase History yang empty state); spec mengikuti TC-304 untuk Quota dan tidak mengasersi frasa bersyarat "empty state bila tanpa kuota". TC-302 Expected hanya "Tidak ada aksi write"; anchor positif adalah Quota yang tampil pada Verifikasi TC-299 di Tab yang sama. Post Condition seluruh TC `-`.
